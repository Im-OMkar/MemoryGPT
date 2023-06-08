from langchain import LLMChain, OpenAI
from langchain.agents import ZeroShotAgent, AgentExecutor
from langchain.tools import Tool
from src.Tools import tools_collection


def create_agent():
    tool_list = [
        Tool(
            name="Small talk",
            func=tools_collection.small_talk,
            description="useful for when user is doing small talk",
        )
    ]
    prefix = """Answer the following questions as best you can, but speaking as JARVIS from ironman also wait for your master's response. You have access to the\
                following tools:"""
    suffix = """Begin! Remember to speak as JARVIS from ironman and treat user as your master when giving your final answer.

    Question: {input}
    {agent_scratchpad}"""

    prompt = ZeroShotAgent.create_prompt(
        tool_list, prefix=prefix, suffix=suffix, input_variables=["input", "agent_scratchpad"]
    )

    llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
    tool_names = [tool.name for tool in tool_list]
    agent = ZeroShotAgent(llm_chain=llm_chain, allowed_tools=tool_names, verbose=True)
    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent, tools=tool_list, verbose=True
    )
    return agent_executor


def message_handler(msg_user):
    agent = create_agent()
    response = agent.run(msg_user)
    print(response)


message_handler("hello")




