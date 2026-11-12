from fastapi import FastAPI

app = FastAPI()

@app.get("/hw")
def hello_world():
    return {"Hello": "World"}

# if __name__ == "__main__";
#     app()
    