from typing import Annotated
from langchain_core.tools import tool
from scraping.db.documents import ArticleDocument
from tooling.http_handler import HttpHandler


@tool
def get_medium_article(link: Annotated[str, "The link of the Medium article"],) -> str:
    """Get a medium article from the given link"""
    filter_options = {"link": link}
    article = ArticleDocument.get(**filter_options)
    return article.content['Content']


endpoint = "http://localhost:8080"
api_client = HttpHandler(endpoint)
@tool
def get_goals():
    get_response = api_client.get("/api/goals")
    if get_response:
        print("GET response:", get_response.json())
    return get_response.json()



@tool
def create_goals(goal, description):
    post_data = {'goal': 'Learn Python', 'deadline': '2024-12-31'}
    post_response = api_client.post("/api/goals", json=post_data)
    if post_response:
        print("POST response:", post_response.json())
    print(post_response.json())

