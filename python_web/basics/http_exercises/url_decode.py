from urllib import parse

urls_raw = ["http://www.google.bg/search?q=C%23",
            "https://mysite.com/show?n%40m3=p3%24h0",
            "http://url-decoder.com/i%23de%25?id=23"]

expected_parsed_urls = [
    "http://www.google.bg/search?q=C#",
    "https://mysite.com/show?n@m3=p3$h0",
    "http://url-decoder.com/i#de%?id=23"
]
for index, url in enumerate(urls_raw):
    actual = parse.unquote(url)
    expected = expected_parsed_urls[index]
    print(f"{expected} {actual} {actual == expected}")
