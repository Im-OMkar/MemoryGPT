from flask import Flask
from langchain import PromptTemplate, OpenAI
from langchain.agents import ZeroShotAgent, AgentExecutor
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.tools import Tool

from src.Tools import tools_collection
from src.utils import logger

app = Flask(__name__)
app.route("/")


@app.route("/")
def run():
    return "hello"


if __name__ == "__main__":
    logger.log("Running flask server")
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
