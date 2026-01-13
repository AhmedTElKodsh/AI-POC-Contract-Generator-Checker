"""RAG Pipeline for proposal content generation."""

import time
from datetime import datetime
from typing import Any, Optional
from uuid import uuid4

from src.knowledge_base.manager import KnowledgeBaseManager
from src.models.enums import Language, SectionType
from src.models.generation import (
    BOQItem,
    GeneratedSection,
    GenerationResult,
    ProjectParameters,
)
from src.models.search import SearchResult


# Section generation prompts
SECTION_PROMPTS = {
    SectionType.EXECUTIVE_SUMMARY: """Generate an executive summary for a {project_type} project.
Project: {project_name}
Client: {client}
Location: {location}
Scope: {scope_description}

Based on the following reference content:
{context}

Write a professional executive summary in {language}.""",

    SectionType.SCOPE_OF_WORK: """Generate a detailed scope of work for a {project_type} project.
Project: {project_name}
Deliverables: {deliverables}

Based on the following reference content:
{context}

Write a comprehensive scope of work in {language}.""",

    SectionType.METHODOLOGY: """Generate a methodology section for a {project_type} project.
Project: {project_name}
Scope: {scope_description}

Based on the following reference content:
{context}

Write a detailed methodology in {language}.""",

    SectionType.TIMELINE: """Generate a project timeline for a {project_type} project.
Project: {project_name}
Duration: {duration_months} months
Deliverables: {deliverables}

Based on the following reference content:
{context}

Write a realistic timeline with milestones in {language}.""",

    SectionType.TECHNICAL_APPROACH: """Generate a technical approach section for a {project_type} project.
Project: {project_name}
Scope: {scope_description}

Based on the following reference content:
{context}

Write a detailed technical approach in {language}.""",
}


class RAGPipeline:
    """
    RAG-based content generation pipeline.

    Retrieves relevant context from the knowledge base and
    generates proposal sections using LLM.
    """

    def __init__(
        self,
        knowledge_base: Optional[KnowledgeBaseManager] = None,
        llm_provider: str = "openai",
        model_name: Optional[str] = None,
        api_key: Optional[str] = None,
    ):
        """
        Initialize the RAG pipeline.

        Args:
            knowledge_base: Knowledge base manager instance
            llm_provider: LLM provider (openai, anthropic)
            model_name: Model name to use
            api_key: API key for LLM provider
        """
        self.knowledge_base = knowledge_base or KnowledgeBaseManager()
        self.llm_provider = llm_provider
        self.model_name = model_name
        self.api_key = api_key

        self._llm_client = None
        self._initialize_llm()

    def _initialize_llm(self):
        """Initialize LLM client."""
        if self.llm_provider == "openai":
            try:
                import openai
                if self.api_key:
                    self._llm_client = openai.OpenAI(api_key=self.api_key)
                else:
                    self._llm_client = openai.OpenAI()
                self.model_name = self.model_name or "gpt-4o-mini"
            except Exception:
                pass

        elif self.llm_provider == "anthropic":
            try:
                import anthropic
                if self.api_key:
                    self._llm_client = anthropic.Anthropic(api_key=self.api_key)
                else:
                    self._llm_client = anthropic.Anthropic()
                self.model_name = self.model_name or "claude-3-haiku-20240307"
            except Exception:
                pass

    def retrieve_context(
        self,
        query: str,
        project_type: Optional[str] = None,
        top_k: int = 5,
    ) -> list[SearchResult]:
        """
        Retrieve relevant context from knowledge base.

        Args:
            query: Search query
            project_type: Filter by project type
            top_k: Number of results to retrieve

        Returns:
            List of relevant search results
        """
        filters = {}
        if project_type:
            filters["project_type"] = project_type

        return self.knowledge_base.search(
            query=query,
            top_k=top_k,
            filters=filters if filters else None,
        )

    def generate_section(
        self,
        section_type: SectionType,
        parameters: ProjectParameters,
        context_limit: int = 5,
    ) -> GeneratedSection:
        """
        Generate a single proposal section.

        Args:
            section_type: Type of section to generate
            parameters: Project parameters
            context_limit: Max context chunks to use

        Returns:
            GeneratedSection with content
        """
        start_time = time.time()

        # Build query from parameters
        query = f"{parameters.project_type.value} {parameters.scope_description}"

        # Retrieve context
        context_results = self.retrieve_context(
            query=query,
            project_type=parameters.project_type.value,
            top_k=context_limit,
        )

        # Format context for prompt
        context_text = self._format_context(context_results)

        # Get prompt template
        prompt_template = SECTION_PROMPTS.get(
            section_type,
            "Generate content for {section_type} section based on: {context}",
        )

        # Build prompt
        language_name = "Arabic" if parameters.language == Language.ARABIC else "English"
        prompt = prompt_template.format(
            project_type=parameters.project_type.value,
            project_name=parameters.project_name,
            client=parameters.client,
            location=parameters.location,
            scope_description=parameters.scope_description,
            deliverables=", ".join(parameters.deliverables),
            duration_months=parameters.duration_months,
            context=context_text,
            language=language_name,
            section_type=section_type.value,
        )

        # Generate content
        content, tokens_used = self._generate_with_llm(prompt, parameters.language)

        # Calculate confidence based on context availability
        confidence = min(len(context_results) / context_limit, 1.0)

        return GeneratedSection(
            section_type=section_type,
            title=self._get_section_title(section_type, parameters.language),
            content=content,
            citations=[r.document_id for r in context_results],
            confidence_score=confidence,
            tokens_used=tokens_used,
        )


    def generate_full_proposal(
        self,
        parameters: ProjectParameters,
        sections: Optional[list[SectionType]] = None,
    ) -> GenerationResult:
        """
        Generate multiple sections for a complete proposal.

        Args:
            parameters: Project parameters
            sections: Sections to generate (default: all standard sections)

        Returns:
            GenerationResult with all generated sections
        """
        start_time = time.time()

        # Default sections if not specified
        if not sections:
            sections = parameters.include_sections or [
                SectionType.EXECUTIVE_SUMMARY,
                SectionType.SCOPE_OF_WORK,
                SectionType.METHODOLOGY,
                SectionType.TECHNICAL_APPROACH,
                SectionType.TIMELINE,
                SectionType.DELIVERABLES,
            ]

        generated_sections = []
        total_tokens = 0

        for section_type in sections:
            section = self.generate_section(section_type, parameters)
            generated_sections.append(section)
            total_tokens += section.tokens_used

        generation_time = time.time() - start_time

        return GenerationResult(
            job_id=str(uuid4()),
            project_parameters=parameters,
            generated_sections=generated_sections,
            boq_items=[],  # BOQ generated separately
            total_cost=0.0,
            total_tokens=total_tokens,
            generation_time_seconds=generation_time,
            created_at=datetime.utcnow(),
        )

    def _format_context(self, results: list[SearchResult]) -> str:
        """Format search results as context text."""
        if not results:
            return "No relevant historical content found."

        context_parts = []
        for i, result in enumerate(results, 1):
            context_parts.append(f"[Reference {i}]\n{result.content}\n")

        return "\n".join(context_parts)

    def _generate_with_llm(
        self, prompt: str, language: Language
    ) -> tuple[str, int]:
        """Generate content using LLM."""
        if self._llm_client is None:
            # Fallback: return placeholder
            return self._generate_fallback(prompt, language), 0

        try:
            if self.llm_provider == "openai":
                return self._generate_openai(prompt, language)
            elif self.llm_provider == "anthropic":
                return self._generate_anthropic(prompt, language)
            else:
                return self._generate_fallback(prompt, language), 0
        except Exception as e:
            return f"[Generation error: {str(e)}]", 0

    def _generate_openai(self, prompt: str, language: Language) -> tuple[str, int]:
        """Generate using OpenAI API."""
        system_prompt = self._get_system_prompt(language)

        response = self._llm_client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=2000,
        )

        content = response.choices[0].message.content
        tokens = response.usage.total_tokens if response.usage else 0

        return content, tokens

    def _generate_anthropic(self, prompt: str, language: Language) -> tuple[str, int]:
        """Generate using Anthropic API."""
        system_prompt = self._get_system_prompt(language)

        response = self._llm_client.messages.create(
            model=self.model_name,
            max_tokens=2000,
            system=system_prompt,
            messages=[{"role": "user", "content": prompt}],
        )

        content = response.content[0].text
        tokens = response.usage.input_tokens + response.usage.output_tokens

        return content, tokens

    def _generate_fallback(self, prompt: str, language: Language) -> str:
        """Fallback generation when LLM is unavailable."""
        if language == Language.ARABIC:
            return "[محتوى تجريبي - يرجى تكوين مزود LLM لإنشاء محتوى حقيقي]"
        return "[Placeholder content - Please configure LLM provider for actual generation]"

    def _get_system_prompt(self, language: Language) -> str:
        """Get system prompt for LLM."""
        if language == Language.ARABIC:
            return """أنت مهندس استشاري خبير في إعداد العروض الفنية والتقارير الهندسية.
اكتب بأسلوب مهني وتقني باللغة العربية الفصحى.
استخدم المصطلحات الهندسية الصحيحة."""

        return """You are an expert consulting engineer specializing in technical proposals and engineering reports.
Write in a professional, technical style.
Use correct engineering terminology and maintain consistency throughout."""

    def _get_section_title(self, section_type: SectionType, language: Language) -> str:
        """Get localized section title."""
        titles = {
            SectionType.EXECUTIVE_SUMMARY: ("Executive Summary", "الملخص التنفيذي"),
            SectionType.SCOPE_OF_WORK: ("Scope of Work", "نطاق العمل"),
            SectionType.METHODOLOGY: ("Methodology", "المنهجية"),
            SectionType.TECHNICAL_APPROACH: ("Technical Approach", "النهج الفني"),
            SectionType.TIMELINE: ("Project Timeline", "الجدول الزمني"),
            SectionType.TEAM_COMPOSITION: ("Team Composition", "فريق العمل"),
            SectionType.DELIVERABLES: ("Deliverables", "المخرجات"),
            SectionType.COST_ESTIMATE: ("Cost Estimate", "تقدير التكلفة"),
            SectionType.BOQ: ("Bill of Quantities", "جدول الكميات"),
        }

        en_title, ar_title = titles.get(section_type, (section_type.value, section_type.value))
        return ar_title if language == Language.ARABIC else en_title

    def generate_boq(
        self,
        parameters: ProjectParameters,
        scope_items: Optional[list[str]] = None,
    ) -> list[BOQItem]:
        """
        Generate Bill of Quantities from scope items.

        Args:
            parameters: Project parameters
            scope_items: Specific scope items (uses deliverables if not provided)

        Returns:
            List of BOQItem objects
        """
        items = scope_items or parameters.deliverables

        # Retrieve historical cost data
        cost_context = self.retrieve_context(
            query=f"cost estimate BOQ {parameters.project_type.value}",
            project_type=parameters.project_type.value,
            top_k=3,
        )

        boq_items = []
        for i, item in enumerate(items, 1):
            # Generate BOQ item (simplified - would use LLM in production)
            boq_item = BOQItem(
                item_number=f"{i}.0",
                description=item,
                unit="LS",  # Lump Sum as default
                quantity=1.0,
                unit_rate=0.0,  # To be filled by cost estimation
                total=0.0,
                notes=None,
            )
            boq_items.append(boq_item)

        return boq_items
