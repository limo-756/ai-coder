from typing import Optional
import json
import requests
from loguru import logger


class CodeGenerator:
    """Handles code generation using Ollama."""

    def __init__(self, model: str = "codellama", base_url: str = "http://localhost:11434"):
        """Initialize the code generator.

        Args:
            model: The Ollama model to use for code generation
            base_url: Ollama API base URL
        """
        self.model = model
        self.base_url = base_url
        self._setup_prompt_template()

    def _setup_prompt_template(self):
        """Set up the prompt template for code generation."""
        self.prompt_template = """
        You are a Python code generator. Generate clean, efficient, and safe Python code based on the user's request.
        Only provide the code without any explanation. The code should be complete and ready to run.

        User Request: {user_prompt}
        """

    def generate_code(self, prompt: str) -> Optional[str]:
        """Generate Python code based on the user prompt.

        Args:
            prompt: User's code generation request

        Returns:
            Generated Python code or None if generation fails
        """
        try:
            formatted_prompt = self.prompt_template.format(user_prompt=prompt)

            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": formatted_prompt,
                    "stream": False,
                    "temperature": 0.2,
                }
            )

            if response.status_code == 200:
                response_json = response.json()
                return response_json['response'].strip()
            else:
                logger.error(f"Ollama API request failed with status {response.status_code}")
                return None

        except Exception as e:
            logger.error(f"Code generation failed: {str(e)}")
            return None

    def validate_generated_code(self, code: str) -> bool:
        """Basic validation of generated code.

        Args:
            code: Generated Python code

        Returns:
            True if code passes basic validation, False otherwise
        """
        try:
            # Basic syntax check
            compile(code, '<string>', 'exec')

            # Add basic security checks
            forbidden_terms = ['os.system', 'subprocess', 'eval', 'exec']
            if any(term in code for term in forbidden_terms):
                logger.warning("Generated code contains potentially unsafe operations")
                return False

            return True

        except SyntaxError:
            logger.error("Generated code has syntax errors")
            return False
        except Exception as e:
            logger.error(f"Code validation failed: {str(e)}")
            return False