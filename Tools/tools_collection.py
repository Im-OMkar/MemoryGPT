import os
from langchain import OpenAI
from langchain.chains import create_tagging_chain
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
LLM = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
_LLM = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo-0613")


def small_talk(msg_user):
    prompt = f"""
    Carry out the small talk done by the user
    user's message : {msg_user}
    """
    answer = LLM(prompt)
    return answer


def for_vacation(question):
    schema = {
        "properties": {
            "startDate": {"type": "string"},
            "endDate": {"type": "string"},
        }
    }
    prompt = f"""
    Start with telling the employee what kind of function you do.
    And you will require the following fields to set leave vacation or free time:
    required_fields: startdate, enddate

    master's message : {question}
    """
    chain = create_tagging_chain(schema, _LLM)
    print("*********", chain.llm_kwargs)
    print("&&&&&&&&&", chain.run(prompt))
