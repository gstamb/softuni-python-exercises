import socket
from urllib.parse import urlparse

urls = ['http://google:443', "http://softuni.bg/", "http://softuni.bg:447/search?Query=pesho&Users=True#go"]


def get_protocol(scheme):
    if scheme in {'http', 'https'}:
        return {"Protocol": scheme}
    return None


def get_host_port(netloc, scheme):
    try:
        socket.gethostbyname(netloc.split()[0])
        if ":" not in netloc:
            default_port = 80 if scheme == "http" else 443
            netloc = f"{netloc}:{default_port}"
        host, port = netloc.split(":")
        return {"Host": host}, {"Port": port}
    except:
        return None, None


def get_url_path(path):
    url_path = "/"
    if path:
        url_path = path
    return {"Path": url_path}


def get_query(query):
    return {"Query": query}


def get_fragments(fragment):
    return {"Fragments": fragment}


def validate_url(url):
    components = urlparse(url)
    protocol = get_protocol(components.scheme)
    host, port = get_host_port(components.hostname, components.scheme)
    path = get_url_path(components.path)
    query = get_query(components.query)
    fragments = get_fragments(components.fragment)
    if protocol and host and path:
        return [protocol, host, port, path, query, fragments]


for url in urls:
    components = validate_url(url)
    if not components:
        print("Invalid URL")
        continue
    valid_components = [component for component in components if any(component.values())]

    for component in valid_components:
        for key, value in component.items():
            if value:
                print(f"{key}: {value}")
