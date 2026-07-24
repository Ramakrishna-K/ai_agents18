

import json

from prompts import SYSTEM_PROMPT
from llm import ask_llm

class Planner:

    def create_plan(self, request):

        prompt = SYSTEM_PROMPT + "\n\nUser Request:\n" + request

        result = ask_llm(prompt)

        # print("LLM OUTPUT:")
        # print(result)

        data = json.loads(result)

        return data["tasks"]