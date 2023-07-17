import re

text = input()
body_pattern =r"((?<=<body).*?(?=</body>))"
body = re.findall(body_pattern, text)


title_pattern =r"((?<=<title).*?(?=</title>))"
title_results = re.findall(title_pattern, text)

pattern_excess_tags = r'<[^>]+>|\\n|>'

cleaned_text = re.sub(pattern_excess_tags, '', body[0])
cleaned_title = re.sub(pattern_excess_tags, '', title_results[0])
content= cleaned_text.strip()
title= cleaned_title.strip()

print(f"Title: {title}")
print(f"Content: {content}")