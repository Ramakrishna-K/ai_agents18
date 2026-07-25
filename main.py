
# from fastapi import FastAPI
# from schemas import *
# from agent import Agent
# import uvicorn

# app = FastAPI()

# agent = Agent()


# @app.get("/")
# def root():
#     return {"message": "Hello AI Agent is Running"}


# @app.post("/agent")
# def run(req: AgentRequest):
#     result = agent.run(req.request)
#     return result

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)


from fastapi import FastAPI
from fastapi.responses import FileResponse
from schemas import *
from agent import Agent
import uvicorn

app = FastAPI()
agent = Agent()


@app.get("/")
def root():
    return {"message": "Hello AI Agent is Running"}


@app.post("/agent")
def run(req: AgentRequest):
    result = agent.run(req.request)
    return result


@app.get("/download")
def download():
    return FileResponse(
        "output/res.docx",
        filename="res.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
