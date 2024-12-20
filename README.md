____

# GenSolution - Multi-Agent AI System

## Overview
**GenSolution** is a multi-agent AI system designed to automate market research, use case generation, resource collection, and comprehensive reporting. It leverages LangChain, Generative AI models, and external tools like Kaggle to generate actionable insights for companies.

This system follows a linear architecture:
1. **Agent 1**: Conducts market research and industry analysis.
2. **Agent 2**: Identifies industry trends, challenges, and proposes use cases.
3. **Agent 3**: Searches for datasets relevant to the use cases.
4. **Agent 4**: Compiles a structured Markdown report summarizing all outputs.

---

## Features
- Automated **market research** with Serper API.
- Intelligent **use case generation** based on industry analysis.
- Precise **dataset recommendations** from Kaggle.
- Comprehensive **Markdown reporting**.

---

## Installation
Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/corazon71/GenSolution.git
   cd GenSolution
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Kaggle CLI** (if not already installed):
   - Follow the [Kaggle API Documentation](https://www.kaggle.com/docs/api) to set up your Kaggle API credentials.

---

## Environment Variables
The project requires the following environment variables, which should be stored in a `.env` file at the root of the project:

| Variable              | Description                              |
|-----------------------|------------------------------------------|
| `SERPER_API_KEY`      | API key for [Serper](https://serper.dev) for web searches. |
| `OPENAI_API_KEY`      | API key for OpenAI models (via ChatGroq). |
| `KAGGLE_USERNAME`     | Username for Kaggle API.                |
| `KAGGLE_KEY`          | API key for Kaggle API.                 |

### Example `.env` File:
```
SERPER_API_KEY=your_serper_api_key
OPENAI_API_KEY=your_openai_api_key
KAGGLE_USERNAME=your_kaggle_username
KAGGLE_KEY=your_kaggle_api_key
```

---

## Usage
### Running the Agents
1. **Generate Market Research**:
   Run Agent 1 to perform market research and generate an analysis:
   ```python
   from Agent1 import generate_company_analysis
   summary = generate_company_analysis("Flipkart")
   ```

2. **Analyze Trends and Use Cases**:
   Run Agent 2 to identify trends, challenges, and propose use cases:
   ```python
   from Agent2 import analyze_market
   market_analysis = analyze_market("Flipkart")
   ```

3. **Search for Datasets**:
   Run Agent 3 to collect relevant datasets:
   ```python
   from Agent3 import collect_resources
   resources = collect_resources("Flipkart")
   ```

4. **Generate Final Report**:
   Run Agent 4 to create a comprehensive Markdown report:
   ```python
   from Agent4 import generate_report
   final_report = generate_report(summary, market_analysis, resources)
   ```

### Output
- The final outputs are stored as Markdown files:
  - `CompanyAnalysis.md`
  - `MarketAnalysis.md`
  - `ResourceCollection.md`
  - `FinalReport.md`

---

## Repository Structure
```
GenSolution/
├── Agent1.py               # Market research and industry analysis
├── Agent2.py               # Industry trends, challenges, and use cases
├── Agent3.py               # Dataset recommendations
├── Agent4.py               # Final report generation
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not included in the repo)
└── README.md               # Project documentation
```

---

## Example
Here’s an example of a final report generated by the system:

```markdown
# Final Project Report: AI and ML Applications for Flipkart

## Market Research
Flipkart operates in the e-commerce and retail industries, focusing on personalized product recommendations, supply chain optimization, and customer service. The company has experienced significant growth, with a strong emphasis on AI-driven solutions.

## Use Cases
1. **AI-driven Quality Control in Manufacturing**
   - Improve defect detection using computer vision and ML.

2. **LLM-based Technical Support Systems**
   - Automate customer support using chatbots powered by LLMs.

3. **ML-driven Supply Chain Optimization**
   - Enhance supply chain management through predictive analytics.

## Dataset Resources
1. [Consumer Behavior Dataset](https://www.kaggle.com/zeesolver/consumer-behavior-and-shopping-habits-dataset)
   - Relevance: Useful for analyzing customer purchasing patterns.

2. [Online Retail Transaction Data](https://www.kaggle.com/thedevastator/online-retail-transaction-data)
   - Relevance: Historical sales data for demand forecasting.

```

---