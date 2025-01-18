from pprint import pprint

from db.documents import ArticleDocument


data = ArticleDocument.get()

for item in data:
    pprint(item)
    print("-------")