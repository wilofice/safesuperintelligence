from typing import Any

import loghelper
# from aws_lambda_powertools.utilities.typing import LambdaContext

import lib
from medium import MediumCrawler
from db.documents import UserDocument
from dispatcher import CrawlerDispatcher
from scraping.loghelper import LogHelper

logger = LogHelper()

_dispatcher = CrawlerDispatcher()
_dispatcher.register("medium", MediumCrawler)


def handler(event, context) -> dict[str, Any]:
    first_name, last_name = lib.user_to_names(event.get("user"))

    user = UserDocument.get_or_create(first_name=first_name, last_name=last_name)

    link = event.get("link")
    crawler = _dispatcher.get_crawler(link)

    try:
        crawler.extract(link=link, user=user)

        return {"statusCode": 200, "body": "Link processed successfully"}
    except Exception as e:
        return {"statusCode": 500, "body": f"An error occurred: {str(e)}"}


if __name__ == "__main__":
    event = {
        "user": "Genereux Alahassa",
        "link": "https://medium.com/ai-in-plain-english/claude-3-5-sonnet-why-it-is-better-than-chatgpt-7709d7cbc237",
    }
    handler(event, None)