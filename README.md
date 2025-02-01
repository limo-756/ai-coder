# AI Coder

An intelligent coding assistant that can generate code and execute system commands, with built-in safety features and extensible architecture.

## Prerequisites

- Python 3.10.6
- pyenv (for Python version management)
- pip (Python package manager)

## Project Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-coder
   ```

2. **Set up Python environment**
   ```bash
   # install pyenv
   brew update
   brew install pyenv
   # Setup shell env based on shell env - https://github.com/pyenv/pyenv
   
   # Set local Python version using pyenv
   pyenv install 3.10.6
   pyenv shell 3.10.6
   
   # Create virtual environment
   # for more details on pyenv virtualenvs visit - https://github.com/pyenv/pyenv-virtualenv
   brew install pyenv-virtualenv
   pyenv virtualenv 3.10.6 ai-coder
   
   
   # Activate virtual environment
   # On MacOS:
   exec "$SHELL"
   pyenv activate ai-coder
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
