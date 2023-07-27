from fastapi import FastAPI, Request
from fastapi.responses import FileResponse 
import logging

app = FastAPI()


# Logging 설정
logging.basicConfig(level=logging.INFO)



@app.get("/soochan")
async def root(request:Request):
    logging.info("Hello World")
    return FileResponse('mypage.html')

@app.get("/kaist.jpg")
async def root(request:Request):
    logging.info("Hello World")
    return FileResponse('kaist.jpg')