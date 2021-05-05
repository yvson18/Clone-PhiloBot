from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from imageGenerator import geraImg

app = FastAPI()

@app.get("/img/{frase}")
def get_imgs_philo(frase:str):
    return StreamingResponse(geraImg(frase), media_type="image/jpg")