# CRM Lead Automation Bot 🚀

This professional Python-based automation tool was developed to streamline lead management by synchronizing data from Excel spreadsheets directly into the Habilis CRM via Webhook integration. It eliminates manual data entry, significantly reducing human error and processing time.

📂 Project Structure
The repository is organized following clean code principles and modular architecture:

## Plaintext

```text
automatic-discharge-B2crm/
├── data/               # Local storage for Excel files (ignored by git)
│   └── Leads.xlsx      # Input data file
├── src/                # Source code directory
│   └── index.py        # Main execution logic
├── .env                # Private environment variables (Credentials)
├── .gitignore          # Rules to prevent sensitive data leaks
├── requirements.txt    # Project dependencies and libraries
└── README.md           # Project documentation
```

## 🛠️ Key Features

Data Normalization: Automatically formats Excel headers and lead information to ensure API compatibility.

Secure Configuration: Utilizes environment variables (.env) to protect sensitive Webhook URLs and API endpoints.

Resilience & Error Handling: Built with the requests library, featuring connection timeouts and detailed console feedback for debugging.

Smart Directory Resolution: Implements dynamic path handling to ensure the script runs correctly regardless of the execution environment.

🧰 Tech Stack
Language: Python 3.x.

Data Handling: Pandas & OpenPyXL.

API Integration: Requests.

Environment Management: Python-Dotenv.

🚀 How to Run

1. Clone the repository
   Bash
   git clone https://github.com/Rodolpholn/automatic-discharge-B2crm.git
2. Install Dependencies
   Use the requirements.txt file to set up your environment:

Bash
python -m pip install -r requirements.txt 3. Setup Environment Variables
Create a file named .env in the root directory and add your CRM Webhook URL:

Fragmento do código
WEBHOOK_URL=https://your-crm-link.com/webhook 4. Prepare your Data
Ensure your Leads.xlsx file is inside the data/ folder with the following columns: ID, NOME, and CELULAR.

5. Execute
   Run the script from the root of the project:

Bash
python src/index.py
📈 Professional Context
This project highlights my proficiency in Python automation and API integrations. It solves a real-world business challenge by automating the flow between marketing spreadsheets and sales CRM systems, demonstrating a focus on efficiency and data security.

```

```
