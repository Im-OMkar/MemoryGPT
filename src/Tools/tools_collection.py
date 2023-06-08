import os
from langchain import OpenAI
from dotenv import load_dotenv

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
LLM = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)


def small_talk(msg_user):
    prompt = f"""
    Start with greeting your master. Then ask if there is something to be shared\
    master's message : {msg_user}
    """
    answer = LLM(prompt)
    print("**************",answer)
    return answer
