import logging
import os

from infinopy import InfinoClient
from langchain import LLMChain, OpenAI
from langchain.agents import ZeroShotAgent, AgentExecutor
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from langchain.callbacks import InfinoCallbackHandler
from dotenv import load_dotenv

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)


from Tools import tools_collection
from src.Visualisation.create_metric import create_metrics

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
LLM = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
_LLM = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo-0613")

client = InfinoClient()
infino_handler = InfinoCallbackHandler(model_id="test_openai", model_version="0.1", verbose=False)


def create_agent():
    tool_list = [
        Tool.from_function(
            name="Small talk",
            func=tools_collection.small_talk,
            description="useful for when user is doing conversation about things that are not important, often between people who do not know each other well.",
            return_direct=True,
        )
        # Tool(
        #     name="Set vacations",
        #     func=tools_collection.small_talk,
        #     description="useful for when user wants to set vacations or holidays",
        # )
    ]
    prefix = """Answer the following questions as best you can, but speaking as JARVIS from ironman. You have access to the following tools:"""
    suffix = """Begin! Remember to speak as JARVIS from ironman when giving your final answer.
    Chat History: {chat_history}
    Question: {input}
    {agent_scratchpad}"""

    prompt = ZeroShotAgent.create_prompt(
        tool_list, prefix=prefix, suffix=suffix, input_variables=["input", "agent_scratchpad", "chat_history"]
    )

    print("************", prompt)

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    llm_chain = LLMChain(llm=LLM, prompt=prompt)
    tool_names = [tool.name for tool in tool_list]
    agent = ZeroShotAgent(llm_chain=llm_chain, allowed_tools=tool_names)
    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent, tools=tool_list, verbose=True, memory=memory
    )
    return agent_executor
    # agent = initialize_agent(tools=tool_list, llm=LLM, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    # print("*******", agent.run(user_message))


def message_handler(data_obj):
    user_msg = data_obj.message
    agent = create_agent()
    response = agent.run(user_msg, callbacks=[infino_handler])
    create_metrics(client)
    return response
