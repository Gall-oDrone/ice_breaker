from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser

import os

from ice_breaker.third_parties.linkedin import scrape_linkedin_profile

if __name__ == '__main__':
    load_dotenv()
    print("Hello LangChain!")
    
    summary_template = """
    given the information {information} about a cryptocurrency financial news article I want you to create:
    1. A short summary
    2. Extract the sentiment of the cryptocurrency financial news article. Assign a value of positive, negatie or neutral.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    #llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    llm = ChatOllama(model="llama3")
    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url = "https://gist.githubusercontent.com/Gall-oDrone/e9c0853d6b7d9e46ce4c7ab0c9ba022f/raw/2903594cd8868da7dc8a08abbd5e0ba9e2afc5a8/del-gal.json")
    res = chain.invoke(input={"information": linkedin_data})

    print(res)