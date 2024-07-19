from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser

import os

if __name__ == '__main__':
    load_dotenv()
    print("Hello LangChain!")
    information="""
    Bitcoin’s trajectory has been a hot topic in financial circles, and predictions about its end-of-year value are more diverse than ever. Roundtable anchor, Rob Nelson, recently delved into these forecasts with John Divine, Digital Asset OTC Trading at BlockFills, who remains steadfast in his bullish stance on bitcoin, projecting it to hit $150,000 by December 31st.

    Nelson opened the discussion by probing Divine on whether his crystal ball predictions had shifted. Divine confidently reiterated his forecast of bitcoin reaching $150,000. He highlighted various bullish indicators, including recent statements from Anthony Scaramucci of SkyBridge Capital and Standard Chartered’s optimistic outlook.

    Divine emphasized the significant impact of market dynamics, noting that traditional stocks are currently at all-time highs while bitcoin is lagging. He pointed out the systematic trading strategies that intertwine the performance of the S&P 500 and bitcoin, suggesting that bitcoin's lag could eventually lead to a significant surge once certain market conditions are met.

    He explained that bitcoin's path to $85,000 could be swift once it breaks past the $72,000 mark, potentially reaching $100,000 before the U.S. election. Divine attributed this potential rise to various market players, including miners, systematic traders, and speculators, who might drive bitcoin's price up in a high-activity environment.

    Divine concluded by stressing the lack of significant capital deployment during recent retracements, suggesting that the next wave of investments could propel bitcoin to new all-time highs. He remains unwavering in his prediction, anticipating a robust market response that could see bitcoin hit his projected target by year-end.
    """

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
    res = chain.invoke(input={"information": information})

    print(res)