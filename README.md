# 🌐 Operation HelpSphere: Global Support Unleashed

## Mission Brief
Your mission, Agent, should you choose to accept it, is as follows:

You are tasked with developing a multilingual customer service AI assistant. This cutting-edge assistant must harness the power of Large Language Models (LLMs) to comprehend and respond to customer queries seamlessly.

The objective? To infiltrate the world of customer service and revolutionize the user experience for our fictional e-commerce front, TechStyle Global. This operation involves handling inquiries related to their diverse array of products, the details of which are hidden in the confidential product_catalog.txt file.

This mission demands precision, creativity, and linguistic dexterity. Should you succeed, you will arm TechStyle Global with the ultimate tool to dominate the global marketplace.

Good luck, Agent. The clock is ticking. 🕒

## Core Objectives
- Create a customer service bot using open-source LLMs
- Handle queries in multiple languages
- Implement a user interface for interaction
- Process common customer service scenarios

## Assignment Levels

### Level 1: The Initiate
**Requirements:**
- Use HuggingFace for LLM interaction
- Support 2 languages (English + 1 other)
- Basic text input/output interface
- Handle common customer queries:
  - What is the name of the company?
  - What types of products do they sell?

**Technical Stack:**
- Python
- HuggingFace/OpenAi/Athropic

### Level 2: The Specialist
**Requirements:**
- Implement conversation memory
- Simple Web-based UI
- Basic RAG implementation using text files provided (no vector db involved)
- Handle more complex customer queries using the txt files
  - Product specific queries
  - Shipping queries

**Technical Stack:**
- All Initiate tools plus:
- LangChain/LlamaIndex/Gradio chat interface

### Level 3: The Operative
**Requirements:**
- RAG implementation using vector databases
- Deploy to huggingface spaces

**Technical Stack:**
- All Specialist tools plus:
- Basic document storage
- Text similarity search
- Huggingface spaces

## Evaluation Criteria
- Response quality
- Code readability
- Interface usability
- Documentation quality

## Submission Guidelines
1. Fork the repository
2. Create folder in `submissions/[your-name]` (please follow the example in the submissions folder)
3. Include:
   - Source code
   - Requirements file
   - Setup instructions
   - Brief documentation

## Getting Started

Follow these steps to set up the project locally:

### 1. Fork the Repository
To work on your own copy of this project:
1. Navigate to the GitHub repository for this project.  
2. Click the **Fork** button in the top-right corner of the repository page.  
3. This will create a copy of the repository under your GitHub account.

---

### 2. Clone the Repository
After forking the repository:
1. Open a terminal on your local machine.  
2. Clone your forked repository by running:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   ```
3. Navigate to the project directory:
    ```bash
    cd <repository-name>
    ```

### 3. Create a virtual environment
Setup a virtual environment to isolate project dependancies
1. Run the following command in the terminal to create a virtual environment
    ```bash
    python3 -m venv .venv
    ```
2. Activate the virtual environment
  - On a mac/linux:
    ```bash
    source .venv/bin/activate
    ```
  - On a windows:
    ```
    .venv\Scripts\activate
    ```
3. Verify the virtual environment is active (the shell prompt should show (.venv))

### 4. Install dependancies
Install the required libraries for the project
1. Run the following command in the terminal to isntall dependancies from the requirements.txt file:
    ```bash
    pip install -r requirements.txt
    ```
Once the setup is complete, you can proceed with building your project


## Resources
- HuggingFace documentation: https://huggingface.co/docs/transformers/index
- Gradio documentation: https://www.gradio.app/docs
- LangChain documentation: https://python.langchain.com/docs/introduction/
- Huggingface Spaces documentation: https://huggingface.co/docs/hub/en/index#spaces