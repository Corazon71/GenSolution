import os
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from Agent1 import generate_company_analysis
from Agent2 import analyze_market
from Agent3 import collect_resources

load_dotenv()

markdown_model = ChatGroq(model="llama-3.1-70b-versatile", temperature=0.7, max_tokens=3000)

report_prompt = PromptTemplate(
    input_variables=["company_summary", "market_analysis", "resources"],
    template="""
    Create a structured Markdown report summarizing:
    1. Market Research:
    {company_summary}

    2. Use Cases:
    {market_analysis}

    3. Dataset Resources:
    {resources}
    """
)

def generate_report(summary, market, resources):
    report_data = {"company_summary": summary, "market_analysis": market, "resources": resources}
    markdown_report = report_prompt | markdown_model
    final_output = markdown_report.invoke(report_data)
    with open("FinalReport.md", "w") as file:
        file.write(final_output.content)
    return final_output

summary = generate_company_analysis("ExampleCompany")
market_analysis = analyze_market("ExampleCompany")
resources = collect_resources("ExampleCompany")
final = generate_report(summary, market_analysis, resources)
