import os
from langchain.tools import tool
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, Tool
from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper

load_dotenv()

@tool
def web_search(query: str) -> str:
    """
    Perform a web search using Serper.
    """
    search_tool = GoogleSerperAPIWrapper()
    return search_tool.run(query)

language_model = ChatGroq(model="llama-3.1-70b-versatile", temperature=0.7, max_tokens=2000)

analysis_prompt = PromptTemplate(
    input_variables=["input_data"],
    template="""
    You are an expert in market research and industry analysis.

    Based on the following company data:
    {input_data}

    Perform these tasks:
    1. Identify and describe the industry or industries, including recent trends.
    2. Segment the company into focus areas with examples.
    3. Highlight the company’s key offerings, strategic focus areas, and vision.
    4. Include financial or market performance metrics if available.

    Provide a detailed and structured summary.
    """
)

tools = [
    Tool(
        name="SearchTool",
        func=web_search,
        description="Retrieve web-based company and industry information."
    )
]

analysis_agent = initialize_agent(tools, language_model, verbose=True)

def generate_company_analysis(input_query):
    search_results = analysis_agent.invoke({"input": input_query})
    summary_chain = analysis_prompt | language_model
    detailed_summary = summary_chain.invoke({"input_data": search_results})
    with open("CompanyAnalysis.md", "w", encoding="utf-8") as file:
        file.write("# Company Analysis\n")
        file.write(detailed_summary.content)
    return detailed_summary.content
