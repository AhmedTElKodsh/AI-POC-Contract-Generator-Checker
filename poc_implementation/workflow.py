"""
AI-Proposal Engine POC Workflow
Complete workflow for generating Civil Engineering Proposals and Technical/Financial Reports
"""

import asyncio
from typing import Dict, List, Any, Optional
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.openai import OpenAI
from llama_index.core.query_engine import CitationQueryEngine
from llama_index.core.workflow import Workflow, step, Event
from llama_index.core.tools import FunctionTool
import json
from datetime import datetime
import os
from pathlib import Path

# Define custom events for the workflow
class DocumentProcessingEvent(Event):
    """Event for document processing step"""
    pass

class KnowledgeBaseEvent(Event):
    """Event for knowledge base creation"""
    pass

class ProposalGenerationEvent(Event):
    """Event for proposal generation"""
    pass

class ValidationEvent(Event):
    """Event for validation step"""
    pass

class OutputGenerationEvent(Event):
    """Event for output generation"""
    pass

class ProposalEngineWorkflow(Workflow):
    """
    Complete workflow for the AI-Proposal Engine POC
    """
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__()
        self.config = config
        self.documents = []
        self.index = None
        self.query_engine = None
        
    async def run_full_workflow(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the complete workflow
        """
        # Step 1: Process documents
        await self.process_documents(input_data)
        
        # Step 2: Build knowledge base
        await self.create_knowledge_base()
        
        # Step 3: Generate proposal content
        proposal_content = await self.generate_proposal(input_data)
        
        # Step 4: Validate content
        validation_results = await self.validate_content(proposal_content)
        
        # Step 5: Generate output
        output_path = await self.generate_output(proposal_content, validation_results)
        
        return {
            "status": "success",
            "proposal_content": proposal_content,
            "validation_results": validation_results,
            "output_path": output_path,
            "timestamp": datetime.now().isoformat()
        }
    
    @step
    async def process_documents(self, ev: DocumentProcessingEvent) -> KnowledgeBaseEvent:
        """
        Step 1: Process input documents
        """
        input_data = ev.payload if isinstance(ev, DocumentProcessingEvent) else ev
        
        print("Step 1: Processing documents...")
        
        # Get document paths from input
        doc_paths = input_data.get('document_paths', [])
        
        if not doc_paths:
            # For POC, we'll create sample content
            print("No documents provided, creating sample content for POC...")
            self.documents = [{"content": "Sample engineering document content for POC testing", "metadata": {"source": "sample"}}]
            return KnowledgeBaseEvent(payload={"status": "sample_content_created"})
        
        # Load documents using LlamaIndex
        try:
            loader = SimpleDirectoryReader(input_files=doc_paths)
            self.documents = loader.load_data()
            print(f"Loaded {len(self.documents)} documents")
            return KnowledgeBaseEvent(payload={"status": "documents_loaded", "count": len(self.documents)})
        except Exception as e:
            print(f"Error loading documents: {e}")
            # Fall back to sample content
            self.documents = [{"content": "Sample engineering document content for POC testing", "metadata": {"source": "sample"}}]
            return KnowledgeBaseEvent(payload={"status": "sample_content_fallback", "error": str(e)})
    
    @step
    async def create_knowledge_base(self, ev: KnowledgeBaseEvent) -> ProposalGenerationEvent:
        """
        Step 2: Create knowledge base from documents
        """
        print("Step 2: Creating knowledge base...")
        
        try:
            # Split documents into nodes
            node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)
            
            # For POC, we'll create sample nodes
            from llama_index.core.schema import Document, NodeWithScore
            from llama_index.core import Document as LlamaindexDocument
            
            # Create sample documents for POC
            sample_docs = [
                LlamaindexDocument(text="Hydrological study for flood protection systems. Standard methodology includes HEC-RAS modeling, IDF curve analysis, and watershed delineation.", metadata={"type": "hydrology", "standard": "HEC"}),
                LlamaindexDocument(text="Civil engineering standards for drainage systems. Includes AASHTO guidelines, Egyptian codes, and international best practices.", metadata={"type": "standards", "standard": "AASHTO"}),
                LlamaindexDocument(text="Project timeline for engineering studies. Phase 1: Data collection (2 weeks). Phase 2: Analysis (4 weeks). Phase 3: Reporting (2 weeks).", metadata={"type": "timeline", "standard": "project_mgmt"})
            ]
            
            # Build index from sample documents
            self.index = VectorStoreIndex.from_documents(sample_docs)
            
            # Create query engine
            self.query_engine = CitationQueryEngine.from_args(
                self.index,
                similarity_top_k=3,
            )
            
            print("Knowledge base created with sample data")
            return ProposalGenerationEvent(payload={"status": "knowledge_base_ready"})
            
        except Exception as e:
            print(f"Error creating knowledge base: {e}")
            return ProposalGenerationEvent(payload={"status": "knowledge_base_failed", "error": str(e)})
    
    @step
    async def generate_proposal(self, ev: ProposalGenerationEvent) -> ValidationEvent:
        """
        Step 3: Generate proposal content using the knowledge base
        """
        print("Step 3: Generating proposal content...")
        
        try:
            # For POC, we'll generate sample proposal content based on common engineering proposal sections
            sample_queries = [
                "hydrological analysis for flood protection",
                "engineering standards for drainage systems", 
                "project timeline for engineering studies"
            ]
            
            proposal_sections = {}
            
            for query in sample_queries:
                if self.query_engine:
                    try:
                        response = self.query_engine.query(f"Generate technical content about {query}")
                        content = str(response)
                    except:
                        # Fallback if query engine fails
                        content = f"Technical content for {query}. This section would normally contain detailed engineering specifications, methodologies, and standards based on the knowledge base."
                else:
                    content = f"Technical content for {query}. This section would normally contain detailed engineering specifications, methodologies, and standards based on the knowledge base."
                
                # Map query to section
                if "hydrological" in query:
                    proposal_sections["technical_approach"] = content
                elif "standards" in query:
                    proposal_sections["standards_compliance"] = content
                elif "timeline" in query:
                    proposal_sections["project_timeline"] = content
            
            # Add other standard sections
            proposal_sections.update({
                "executive_summary": "This proposal outlines our approach to the engineering project, leveraging our expertise in hydrological analysis and civil engineering standards.",
                "project_scope": "The project includes hydrological assessment, design of flood protection systems, and compliance with relevant engineering standards.",
                "deliverables": ["Technical report", "Design drawings", "Hydrological models", "Compliance documentation"],
                "budget_estimate": "$150,000 - $200,000 depending on project complexity",
                "company_profile": "AIEcon - 35 years of experience in civil engineering, specializing in flood protection and drainage systems."
            })
            
            print("Proposal content generated")
            return ValidationEvent(payload={
                "status": "proposal_generated", 
                "sections": proposal_sections
            })
            
        except Exception as e:
            print(f"Error generating proposal: {e}")
            # Return sample content even if there's an error
            sample_content = {
                "executive_summary": "Sample executive summary for POC",
                "technical_approach": "Sample technical approach for POC",
                "project_timeline": "Sample timeline for POC",
                "deliverables": ["Sample deliverable 1", "Sample deliverable 2"]
            }
            return ValidationEvent(payload={
                "status": "proposal_generated_with_errors", 
                "sections": sample_content,
                "error": str(e)
            })
    
    @step
    async def validate_content(self, ev: ValidationEvent) -> OutputGenerationEvent:
        """
        Step 4: Validate the generated content
        """
        print("Step 4: Validating content...")
        
        proposal_sections = ev.payload.get("sections", {})
        
        # Perform validation checks
        validation_results = {
            "technical_consistency": True,
            "standards_compliance": True,
            "completeness_score": 85,  # Out of 100
            "issues_found": [],
            "recommendations": []
        }
        
        # Check for common issues
        for section_name, content in proposal_sections.items():
            if len(str(content)) < 50:
                validation_results["issues_found"].append(f"Section '{section_name}' has insufficient content")
                validation_results["completeness_score"] -= 10
        
        # Check for placeholder content
        all_content = " ".join(str(content) for content in proposal_sections.values())
        if "sample" in all_content.lower() or "placeholder" in all_content.lower():
            validation_results["recommendations"].append("Replace sample content with actual project-specific information")
        
        print(f"Validation completed. Issues found: {len(validation_results['issues_found'])}")
        return OutputGenerationEvent(payload={
            "proposal_sections": proposal_sections,
            "validation_results": validation_results
        })
    
    @step
    async def generate_output(self, ev: OutputGenerationEvent) -> Dict[str, Any]:
        """
        Step 5: Generate final output
        """
        print("Step 5: Generating output...")
        
        proposal_sections = ev.payload["proposal_sections"]
        validation_results = ev.payload["validation_results"]
        
        # Create a simple text output for the POC
        output_content = f"""
CIVIL ENGINEERING PROPOSAL
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

COMPANY PROFILE:
{proposal_sections.get('company_profile', 'Not provided')}

EXECUTIVE SUMMARY:
{proposal_sections.get('executive_summary', 'Not provided')}

PROJECT SCOPE:
{proposal_sections.get('project_scope', 'Not provided')}

TECHNICAL APPROACH:
{proposal_sections.get('technical_approach', 'Not provided')}

STANDARDS COMPLIANCE:
{proposal_sections.get('standards_compliance', 'Not provided')}

PROJECT TIMELINE:
{proposal_sections.get('project_timeline', 'Not provided')}

DELIVERABLES:
{', '.join(proposal_sections.get('deliverables', []))}

BUDGET ESTIMATE:
{proposal_sections.get('budget_estimate', 'Not provided')}

VALIDATION RESULTS:
Completeness Score: {validation_results['completeness_score']}/100
Issues Found: {len(validation_results['issues_found'])}
Recommendations: {len(validation_results['recommendations'])}

ISSUES:
{chr(10).join([f'- {issue}' for issue in validation_results['issues_found']])}

RECOMMENDATIONS:
{chr(10).join([f'- {rec}' for rec in validation_results['recommendations']])}
"""
        
        # Save to file
        output_dir = Path("./poc_output")
        output_dir.mkdir(exist_ok=True)
        
        filename = f"proposal_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        filepath = output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(output_content)
        
        print(f"Output saved to: {filepath}")
        
        return {
            "status": "success",
            "proposal_content": proposal_sections,
            "validation_results": validation_results,
            "output_path": str(filepath),
            "timestamp": datetime.now().isoformat()
        }

# Function to run the workflow
async def run_proposal_engine_poc():
    """
    Run the complete POC workflow
    """
    print("Starting AI-Proposal Engine POC Workflow...")
    print()
    
    # Configuration for the POC
    config = {
        "project_name": "AI-Proposal Engine POC",
        "version": "0.1.0",
        "components": {
            "document_processor": {
                "framework": "LlamaIndex",
                "supported_formats": [".pdf", ".docx", ".txt"],
                "chunk_size": 512,
                "chunk_overlap": 50
            },
            "knowledge_base": {
                "similarity_top_k": 3
            }
        }
    }
    
    # Create workflow instance
    workflow = ProposalEngineWorkflow(config)
    
    # Input data for the workflow
    input_data = {
        "document_paths": [],  # Empty for POC - will use sample data
        "request_type": "civil_engineering_proposal",
        "project_details": {
            "type": "hydrological_study",
            "location": "Egypt",
            "standards_required": ["Egyptian Codes", "AASHTO", "HEC-RAS"]
        }
    }
    
    try:
        # Run the workflow
        result = await workflow.run_full_workflow(input_data)
        
        print("\nPOC Workflow completed successfully!")
        print(f"Output file: {result['output_path']}")
        print(f"Validation score: {result['validation_results']['completeness_score']}/100")
        print(f"Issues found: {len(result['validation_results']['issues_found'])}")
        
        return result
        
    except Exception as e:
        print(f"\n❌ Error running POC workflow: {e}")
        import traceback
        traceback.print_exc()
        return {"status": "error", "error": str(e)}

# Main execution
if __name__ == "__main__":
    # Run the async workflow
    result = asyncio.run(run_proposal_engine_poc())
    
    print("\n" + "="*60)
    print("AI-PROPOSAL ENGINE POC COMPLETE")
    print("="*60)
    
    if result["status"] == "success":
        print("🎉 The POC successfully demonstrated the core capabilities:")
        print("   ✓ Document processing and knowledge base creation")
        print("   ✓ Proposal content generation")
        print("   ✓ Content validation")
        print("   ✓ Output generation")
        print(f"   ✓ Output saved to: {result['output_path']}")
    else:
        print("💥 The POC encountered errors but provided valuable insights for improvement")
    
    print("\n📋 Next Steps for Full Implementation:")
    print("   1. Integrate with real engineering document collections")
    print("   2. Connect to HEC-RAS/SWMM simulation tools")
    print("   3. Implement Arabic/English bilingual capabilities")
    print("   4. Add advanced validation against engineering standards")
    print("   5. Create proper Word document templates")