import uvicorn

if __name__ == "__main__":
    uvicorn.run("example.main:app", host="0.0.0.0", port=8000, debug=True)
