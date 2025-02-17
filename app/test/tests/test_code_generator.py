import pytest
from src.code_generator import CodeGenerator


@pytest.fixture
def code_generator():
    return CodeGenerator(model="llama3.1:8b", base_url="http://localhost:11434")


def test_generate_code(code_generator):
    prompt = "Create a function that calculates the factorial of a number"

    code = code_generator.generate_code(prompt)
    assert code is not None
    # The exact response might vary with different models
    assert "def" in code and "return" in code


def test_validate_generated_code(code_generator):
    # Test valid code
    valid_code = """
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    """
    assert code_generator.validate_generated_code(valid_code) is True

    # Test invalid code
    invalid_code = """
def factorial(n)
    return n
    """
    assert code_generator.validate_generated_code(invalid_code) is False

    # Test unsafe code
    unsafe_code = """
import os
os.system('rm -rf /')
    """
    assert code_generator.validate_generated_code(unsafe_code) is False