from fastapi.testclient import TestClient
import pytest
from app.main import app, create_input

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Check Spelling"}



@pytest.mark.parametrize("payload, corrected_outputs", [
    ("i ned to go bu grocry at wammart", {
        "methode 1": "i need to go by grocry at wammart",
        "methode 2": "i ned to go bu grocery at mammary",
        "methode 3": "I need to go buy Grocery at Walmart.",
        "methode 1 key words": "need go grocry wammart",
        "methode 2 key words": "ned go bu grocery mammary",
        "methode 3 key words": "I need go buy Grocery Walmart."
        }),
    ("leroymerin", {
        "methode 1": "leroymerin",
        "methode 2": "leroymerin",
        "methode 3": "Leroy Merlin",
        "methode 1 key words": "leroymerin",
        "methode 2 key words": "leroymerin",
        "methode 3 key words": "Leroy Merlin"
        }),
    ("in the wst of the continent lives th trib of red-wolf,\
      one of the strongst in the rigion",{
        "methode 1": "the trib of red wolf one of the strongest in the region",
        "methode 2": "in the wet of the continent lives the trip of red-wolf, one of the strongest in the region",
        "methode 3": "In the west of the continent lives the tribe of Red-Wolves, one of the strongest in the region.",
        "methode 1 key words": "trib red wolf one strongest region",
        "methode 2 key words": "wet continent lives trip red-wolf, one strongest region",
        "methode 3 key words": "In west continent lives tribe Red-Wolves, one strongest region."
        })

])
def test_create_input(payload, corrected_outputs):
    response = create_input(payload)
    assert response == corrected_outputs