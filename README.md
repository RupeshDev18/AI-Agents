# AI Agents Project

This project is designed to automate the end-to-end workflow of sourcing, managing, and executing coding projects using specialized AI agents. Each agent is responsible for a specific task, such as project discovery, agreement drafting, marketing outreach, and more.

## Project Structure

The project is organized into modular folders for scalability and maintainability. Here’s an overview of the folder structure:
```css
ai-agents-project/
├── agents/                     # Folder for all AI agents
 │   ├── project_discovery/      # Project Discovery Agent
 │   ├── client_agreement/       # Client-Agreement Agent
 │   ├── marketing_outreach/     # Marketing & Outreach Agent
 │   └── utils/                  # Shared utilities across agents
├── templates/                  # Folder for agreement templates
├── data/                       # Folder for data storage
├── tests/                      # Unit and integration tests
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── main.py                     # Entry point for the entire project
```
## Agents Overview

### 1. Project Discovery Agent

- **Purpose**: Fetches and filters coding projects from platforms like Upwork, Freelancer, etc.
- **Key Features**:
  - Web scraping/API integration for project data.
  - NLP-based filtering to match projects with required skills.
  - Ranking algorithm to prioritize high-relevance projects.
- **How to Run**:
  ```bash
  python agents/project_discovery/main.py
  ```

### 2. Client-Agreement Agent

- **Purpose**: Automates the drafting and signing of contracts, NDAs, and scope-of-work documents.
- **Key Features**:

  - Template-based agreement generation.
  - Dynamic clause generation using GPT-4.
  - Integration with DocuSign for e-signatures.
- **How to Run**:

  ```bash
  python agents/client_agreement/main.py
  ```

  ### 3. Marketing & Outreach Agent
- **Purpose**: Automates client outreach and follow-ups via email and LinkedIn.
- **Key Features**:

  - Personalized email generation.
  - LinkedIn scraping for client contact information.
  - Automated follow-up reminders.
- **How to Run**:

  ```bash
  python agents/marketing_outreach/main.py
  ```

  ## Getting Started

  ### Prerequisites
- Python 3.8 or higher.
- Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

  ### Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/RupeshDev18/AI-Agents.git](https://github.com/RupeshDev18/AI-Agents.git)
   cd ai-agents-project
   ```
2. Set up environment variables:

   - Create a `.env` file in the root directory.
   - Add your API keys and credentials (e.g., OpenAI, DocuSign, AWS):

     ```
     OPENAI_API_KEY=your_openai_key
     DOCUSIGN_ACCESS_TOKEN=your_docusign_token
     AWS_ACCESS_KEY_ID=your_aws_key
     AWS_SECRET_ACCESS_KEY=your_aws_secret
     ```

     ### Running the Project

- To run all agents sequentially:

  ```bash
  python main.py
  ```
- To run a specific agent:

  ```bash
  python agents/<agent_name>/main.py
  ```

  ---

  ## Configuration
- **API Keys**: Store all API keys and sensitive information in the `.env` file.
- **Templates**: Add or modify agreement templates in the `templates/` folder.
- **Databases**: SQLite databases are stored in the `data/` folder.---## Testing
- Run unit and integration tests:

  ```bash
  python -m pytest tests/
  ```

  ## Contributing

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:

   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.
6. ## License

   This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
7. ## Contact

   For questions or feedback, reach out to:

- Rupesh yadav - ry993494787[@gmail.com](mailto: ry993494787@gmail.com "gmail")
- **Project Repository** - [GitHub]([https://github.com/RupeshDev18/AI-Agents.git](https://github.com/RupeshDev18/AI-Agents.git)))
