import requests


def test_species_name():
    url = "http://localhost:8888/?species=Time%20Lord"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.content == b"credentials:Rassilon\n"


def test_multiple_params():
    url = "http://localhost:8888/?species=Dalek&foo=bar"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.content == b"credentials:Davros\n"


if __name__ == "__main__":
    test_species_name()
    test_multiple_params()