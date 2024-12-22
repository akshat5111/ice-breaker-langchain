import os
import sys
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.schema.output_parser import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
# from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'agents')))
from linkedin_lookup_agent import lookup as linkedin_lookup_agent


def ice_break_with(name:str):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
    Given the Linkedin information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables = ["information"], template = summary_template)

    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-pro")

    chain = summary_prompt_template | llm | StrOutputParser()
    # linkedin_data = scrape_linkedin_profile('https://www.linkedin.com/in/akshat-phadtare-7a3235218', True)
    res = chain.invoke(input={"information":linkedin_data})
    return res

if __name__ == '__main__':
    load_dotenv()
    print('Hello Langchain')
    result = ice_break_with(name="Akshat Phadtare")
    print(result)