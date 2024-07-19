#!/usr/bin/env python
from typing import List
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from langchain_community.chat_models import ChatOllama
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import MessagesPlaceholder

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


# 1. Create prompt template
system_template = "You are my helpful assistant. Answer all questions to the best of your ability,"
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            system_template,
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

# 2. Create model

from langchain_huggingface import HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
     model_id="Trelis/Mistral-7B-Instruct-v0.2-function-calling-v3",
     task="text-generation",
     pipeline_kwargs=dict(
         max_new_tokens=512,
         do_sample=False,
         repetition_penalty=1.03
     ),
 )

HUGGINGFACEHUB_API_TOKEN = "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"
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

from langchain_huggingface import ChatHuggingFace

model = ChatHuggingFace(llm=llm)

chain = prompt | model
chain_with_msg_history = RunnableWithMessageHistory(chain, get_session_history,
                                                    input_messages_key="input",
    history_messages_key="history")

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = chain_with_msg_history | parser


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)