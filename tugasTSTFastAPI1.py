from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def hello() -> dict:
    return { "message": "Tugas 1 TST : Nasywaa Anggun Athiefah 18222021"} 