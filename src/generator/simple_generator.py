from docxtpl import DocxTemplate
from src.models.generation import ProposalContext
import os

class SimpleGenerator:
    """
    A Template-Based Document Generator.
    
    This class represents the 'Render' phase of the architecture.
    It takes the fully enriched ProposalContext state object and maps it 
    onto a Jinja2-enabled Word Document (.docx).

    Library Used: docxtpl (http://docxtpl.readthedocs.io/)
    """

    def __init__(self, template_path: str = "templates/poc_template.docx"):
        """
        Args:
            template_path (str): Path to the .docx template file.
        """
        self.template_path = template_path

    def generate(self, context: ProposalContext, output_path: str) -> str:
        """
        Generates the final proposal document.

        Process:
        1. Loads the .docx template.
        2. Converts ProposalContext to a dictionary (context.dict()).
        3. Formats specific fields (like dates) for display.
        4. Renders the template with the dictionary data.
        5. Saves the result to output_path.

        Args:
            context (ProposalContext): The data to render.
            output_path (str): Where to save the generated file.

        Returns:
            str: The path to the generated file.
        """
        if not os.path.exists(self.template_path):
            raise FileNotFoundError(f"Template not found: {self.template_path}")

        doc = DocxTemplate(self.template_path)

        # context.dict() creates a dictionary representation of our Pydantic model.
        # This dictionary is exactly what Jinja2 needs to fill the {{ placeholders }}.
        render_data = context.dict()
        
        # Formatting: Date objects need to be strings for the template
        render_data['date'] = context.date.strftime("%Y-%m-%d")

        # Render the tags in the document
        doc.render(render_data)
        
        # Save to disk
        doc.save(output_path)
        
        return output_path