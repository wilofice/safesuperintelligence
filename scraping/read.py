from pprint import pprint

from db.documents import ArticleDocument

data = ArticleDocument.get()

s = data.content['Content']

import re

s = ' '.join(s.split())
print(s)
print("-------")
#for item in data:
#pprint(item)
#print("-------")
