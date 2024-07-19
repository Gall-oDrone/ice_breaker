from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser

import os

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent 
from third_parties.linkedin import scrape_linkedin_profile


def ice_breaker_with(name: str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
    given the information {information} about a cryptocurrency financial news article I want you to create:
    1. A short summary
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    res = chain.invoke(input={"information": linkedin_data})
    print(res)

if __name__ == '__main__':
    load_dotenv()
    print("Ice Breaker Enter")
    name="Alfredo Lefranc Flores"
    ice_breaker_with(name=name)

    