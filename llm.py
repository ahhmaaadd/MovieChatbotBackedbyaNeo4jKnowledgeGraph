import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import httpx
from dotenv import load_dotenv
import os


# Create the LLM
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def update_base_url(request: httpx.Request) -> None:
    if request.url.path == "/chat/completions":
        request.url = request.url.copy_with(path="/v1/chat")
    elif request.url.path == "/embeddings":
        request.url = request.url.copy_with(path="/v1/openai/ada-002/embeddings")


# Initialize HTTP client with event hook to update the base URL
http_client = httpx.Client(
    event_hooks={"request": [update_base_url]}
)

llm = ChatOpenAI(
                base_url="https://aalto-openai-apigw.azure-api.net",
                api_key=openai_api_key,
                default_headers={
                    "Ocp-Apim-Subscription-Key": openai_api_key,
                },
                http_client=http_client
            )


# Create the Embedding model
embeddings = OpenAIEmbeddings(
    base_url="https://aalto-openai-apigw.azure-api.net",
    api_key=openai_api_key,
    default_headers={
        "Ocp-Apim-Subscription-Key": openai_api_key,
    },
    http_client=http_client
)
