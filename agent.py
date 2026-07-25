from planner import Planner

from executor import Executor

from document import DocumentGenerator


class Agent:

    def __init__(self):
        self.planner=Planner()
        self.executor=Executor()
        self.doc=DocumentGenerator()
    def run(self, request):
        tasks=self.planner.create_plan(request)  
        content=self.executor.execute(
            request,
            tasks
        )  

        file=self.doc.save(content)

        return {
            "success":True,

            "tasks":tasks,

            "summary": "Completed Successfully",

            "output_file":file
        }
    
