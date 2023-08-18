def register_paths():
    valid_urls = {}

    while True:
        instruction = input()
        if instruction == "END":
            break
        url = instruction[:instruction.rindex("/")]
        req_type = instruction[instruction.rindex("/") + 1:]
        if url not in valid_urls:
            valid_urls[url] = []
        valid_urls[url].append(req_type)

    return valid_urls


def make_request(request):
    if request['path'] in urls and request['method'] in urls[request['path']]:
        status = "OK"
    else:
        status = "Not Found"
    return f"HTTP/1.1 404 {status}\n" \
           f"Content-Length: {len(status)}\n" \
           f"Content-Type: text/plain\n" \
           f"\n" \
           f"{status}"


def receive_request():
    request = input()
    request_type, path, details = request.split()
    return {
        'method': request_type.lower(),
        'path': path
    }


urls = register_paths()
request = receive_request()
print(make_request(request))
