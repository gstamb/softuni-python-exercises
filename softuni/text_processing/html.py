title = input()
content = input()

html = ""

html += f"<h1>\n\t{title}\n</h1>\n"
html += f"<article>\n\t{content}\n</article>\n"

while True:
    comment = input()
    if comment == "end of comments":
        break
    html += f"<div>\n\t{comment}\n</div>\n"

print(html)
