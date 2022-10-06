import persona_fake
from fastapi import FastAPI, Request

#Run with: uvicorn main:app --reload

app = FastAPI()

@app.get("/fake-personal-data")
async def create_item(req: Request):

    init_person = persona_fake.Persona()
    fake_person = init_person.get_fake_person()
    print(fake_person)
    return fake_person












