import pytest
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
        
def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_encrypt_and_decrypt(client):
    message = "test"
    key =3
    response = client.post("/", data ={
        "message": message,
        "key": key,
        "action" : "encrypt",
        "use_polish": "off"
    })
    assert response.status_code == 200
    text = response.get_data(as_text=True)
    soup = BeautifulSoup(text, "html.parser")
    textarea = soup.find("textarea", {"name": "result"})
    assert textarea is not None
    assert textarea.text.strip() == "xhwx"
    response2 = client.post("/", data ={
        "message": "xhwx",
        "key": key,
        "action" : "decrypt",
        "use_polish": "off"
    })
    assert response2.status_code == 200
    text2 = response2.get_data(as_text=True)
    soup2 = BeautifulSoup(text2, "html.parser")
    textarea2 = soup2.find("textarea", {"name": "result"})
    assert textarea2 is not None
    assert textarea2.text.strip() == "test"