import os
import subprocess
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent
from langchain.tools import tool
from dotenv import load_dotenv
from Agent2 import extract_use_cases

load_dotenv()

def kaggle_search(term: str) -> str:
    try:
        result = subprocess.run(
            ["kaggle", "datasets", "list", "-s", term],
            stdout=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return str(e)

@tool
def kaggle_dataset_search(query: str) -> str:
    """
    Search for datasets on Kaggle based on the given use case.
    """
    return kaggle_search(query)

resource_model = ChatGroq(model="llama-3.1-70b-versatile", temperature=0.7, max_tokens=1500)

resource_prompt = PromptTemplate(
    input_variables=["use_cases"],
    template="""
    Analyze the following use cases:
    {use_cases}

    1. Identify ML-related use cases needing datasets.
    2. For each use case, find datasets on Kaggle, providing their names, links, and relevance.
    3. Provide a structured summary.
    """
)

resource_tools = [kaggle_dataset_search]

resource_agent = initialize_agent(tools=resource_tools, llm=resource_model, prompt=resource_prompt, verbose=True)

def collect_resources(company_input):
    use_case_list = extract_use_cases(company_input)
    dataset_results = resource_agent.invoke({"input": use_case_list})
    with open("ResourceCollection.md", "w", encoding="utf-8") as file:
        file.write("# Resource Collection\n")
        file.write(dataset_results['output'])
    return dataset_results['output']

# collect_resources("Flipkart")