# Project Guide for AI Travel Planner

## Project Overview
- **Description**: The AI Travel Planner is designed to assist users with travel planning using AI technologies.
- **Key Technologies**: Python, FastAPI, Streamlit, various Langchain libraries.
- **High-Level Architecture**: The application uses a modular architecture with separate directories for utilities, logging, and exception handling.

## Getting Started
- **Prerequisites**: 
  - Python 3.x
  - pip for installing dependencies
- **Installation Instructions**: 
  - Clone the repository.
  - Run `pip install -r requirements.txt` to install required packages.
- **Basic Usage Examples**: 
  - Run the application with `python main.py` to start using the travel planner.
- **Running Tests**: 
  - Tests should be included in the future; currently, run the main application to test basic functionality.

## Project Structure
- **Overview**:
  - `agent/`: Contains the core AI workflow.
  - `exception/`: Handles exceptions throughout the application.
  - `logger/`: Responsible for logging application events.
  - `utils/`: Contains utility functions for various operations.
  - `prompt_library/`: Contains prompts for the AI.
  - `tools/`: Provides various tools for different functionalities.
- **Key Files**:
  - `app.py`: Main application definition.
  - `main.py`: Entry point of the application.
  - `requirements.txt`: Lists project dependencies.
  - `setup.py`: Script for package setup and installation.

## Development Workflow
- **Coding Standards**: Follow PEP 8 for Python code style.
- **Testing Approach**: Testing frameworks to be defined; currently, manual testing is advised.
- **Build and Deployment Process**: Deployment guidelines to be established.
- **Contribution Guidelines**: Contributions welcome; follow the code style and submit pull requests.

## Key Concepts
- **Domain-Specific Terminology**: Features such as "prompts" and "tools" refer to specific functionalities of the AI Travel Planner.
- **Core Abstractions**: AI workflows and utility functions are abstracted for reusable components.
- **Design Patterns Used**: Modular design pattern to separate concerns.

## Common Tasks
- **Step-by-Step Guides**: 
  - How to add a new tool: create a new file in the `tools/` directory and implement the necessary functions.
- **Examples**: 
  - To use the calculator tool, import it from `tools/calculator_tool.py` and call the desired functions.

## Troubleshooting
- **Common Issues**: 
  - Ensure all dependencies are installed; check the `requirements.txt` file.
- **Debugging Tips**: 
  - Use print statements or logging to trace execution and identify issues.

## References
- **Documentation Links**: 
  - [Langchain Documentation](https://docs.langchain.com/)
  - [FastAPI Documentation](https://fastapi.tiangolo.com/)
  - [Streamlit Documentation](https://docs.streamlit.io/)