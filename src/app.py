from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {
        "message": "Hello world"
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=80, host='0.0.0.0', reload=True)