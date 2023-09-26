from fastapi import FastAPI
from fastapi.params import Body

from .spell.models import SpellCorrection
from .spell.clean_text import clean_stopwords

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/inputs")
def create_input(payload: str = Body(...)):
    output = SpellCorrection()
    method_corrected_spelling= output.correct_spelling(payload)
    method_spell_checker= output.spell_checker(payload)
    method_fix_spelling= output.fix_spelling(payload)
    return{
        "methode 1": method_corrected_spelling, 
        "methode 2": method_spell_checker,
        "methode 3": method_fix_spelling,
        "methode 1 key words": clean_stopwords(method_corrected_spelling), 
        "methode 2 key words": clean_stopwords(method_spell_checker),
        "methode 3 key words": clean_stopwords(method_fix_spelling),
        }
