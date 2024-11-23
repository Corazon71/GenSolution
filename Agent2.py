from Agent1 import generate_company_analysis
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

language_model = ChatGroq(model="llama-3.1-70b-versatile")

trends_prompt = PromptTemplate(
    input_variables=["analysis_output"],
    template="""
    You are a market analyst and AI expert.

    Based on this research summary:
    {analysis_output}

    Your tasks:
    1. Identify key industry trends and standards.
    2. Highlight major challenges like competition, technological limitations, or regulatory constraints.
    3. Propose 3-5 use cases where AI/ML can improve processes, enhance customer satisfaction, or boost efficiency.

    Provide a structured response.
    """
)

def analyze_market(company_input):
    company_analysis = generate_company_analysis(company_input)
    analysis_response = language_model.predict(trends_prompt.format(analysis_output=company_analysis))
    with open("MarketAnalysis.md", "w", encoding="utf-8") as file:
        file.write("# Market Analysis\n")
        file.write(analysis_response)
    return analysis_response

def extract_use_cases(company_input):
    market_text = analyze_market(company_input)
    extraction_prompt = PromptTemplate(
        input_variables=["market_content"],
        template="""
        Extract use cases from the following text:
        {market_content}
        List them as clear, concise bullet points.
        """
    )
    use_case_response = extraction_prompt | language_model
    return use_case_response.invoke({'market_content': market_text})
