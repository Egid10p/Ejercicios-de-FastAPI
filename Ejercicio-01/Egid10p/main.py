from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/sumar")
async def sumar(number_1: int = 0, number_2: int = 0):
    return {"resultado": number_1 + number_2}

@app.get("/restar")
async def sumar(number_1: int = 0, number_2: int = 0):
    return {"resultado": number_1 - number_2}
    
@app.get("/multiplicar")
async def sumar(number_1: int = 0, number_2: int = 0):
    return {"resultado": number_1 * number_2}

@app.get("/dividir")
async def sumar(number_1: int = 0, number_2: int = 0):
    return {"resultado": number_1 / number_2}
