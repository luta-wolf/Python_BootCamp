from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
import http

list_of_species = {
    'Cyberman': 'John Lumic',
    'Dalek': 'Davros',
    'Judoon': 'Shadow Proclamation Convention 15 Enforcer',
    'Human': 'Leonardo da Vinci',
    'Ood': 'Klineman Halpen',
    'Silence': 'Tasha Lem',
    'Slitheen': 'Coca-Cola salesman',
    'Sontaran': 'General Staal',
    'Time Lord': 'Rassilon',
    'Weeping Angel': 'The Division Representative',
    'Zygon': 'Broton',
    'Unknown': 'Unknown'
}


def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    species = ''.join(d.get('species', ['Unknown']))
    name = ''.join(list_of_species.get(species, ["Unknown"]))

    if not species:
        status = '400 Bad Request'
        response_body = b"Error: No species provided"
    else:
        status = '200 OK' if name != "Unknown" else '404 Not Found'
        response_body = bytes(f"credentials:{name}\n", 'UTF-8')

    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]


def main():
    httpd = make_server('localhost', 8888, application)
    httpd.serve_forever()


if __name__ == "__main__":
    main()