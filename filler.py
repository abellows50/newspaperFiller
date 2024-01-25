import sys
import os

articleFileName = sys.argv[1]
articleText = ""
template = ""
with open("template.html", 'r') as f:
    template = f.read()
with open(f"{articleFileName}.txt", 'r') as f:
    articleText = f.read()
with open(f"{articleFileName}.html", 'w') as f:
    f.write(template.replace("{{article}}", articleText))