import json
from wsgiref.simple_server import make_server
from urllib import parse


def application(environ, start_response):

    d = parse.parse_qs(environ['QUERY_STRING'])
    print(d)

    species = d.get("species", [''])[0]
    print(species)

    dic = {"Cyberman": "John Lumic",
           "Dalek": "Davros",
           "Judoon": " Shadow Proclamation Convention 15 Enforcer",
           "Human": "Leonardo da Vinci",
           "Ood": "Klineman Halpen",
           "Silence": "Tasha Lem",
           "Slitheen": "Coca - Cola salesman",
           "Sontaran": "General Staal",
           "Time Lord": "Rassilon",
           "Weeping Angel": "The Division Representative",
           "Zygon": "Broton"}

    ans = dic.get(species)
    resp_dict = {
        'credentials': 'Unknown'
    }
    if ans is not None:
        resp_dict['credentials'] = ans

    response_body = json.dumps(resp_dict)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body.encode('utf-8')]


if __name__ == "__main__":
    httpd = make_server(
        'localhost',
        8888,
        application
    )

    while True:
        httpd.handle_request()

