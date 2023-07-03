from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from typing import Optional, Type


class VacationApplication():
    name = "leave_vacation_handler"
    description = "useful for when you need to apply for leaves or vacation in a company"

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:

        return ""
