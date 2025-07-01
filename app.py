from firstapi import FirstAPI

app = FirstAPI()

@app.get("/")
def read_root():
    return {"message": "Hello DevOps World!"}
