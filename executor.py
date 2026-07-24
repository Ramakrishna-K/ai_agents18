


from tools import ToolBox
from llm import ask_llm
from prompts import CONTENT_PROMPT
from utils import self_check


class Executor:

    def __init__(self):
        self.toolbox = ToolBox()

    def execute(self, request, tasks):

        completed = []

        for task in tasks:
            result = self.toolbox.execute(task)
            completed.append(result)

        prompt = CONTENT_PROMPT.format(
            request=request,
            tasks=completed
        )

        content = ask_llm(prompt)

        content = self_check(content)

        return content