from fastapi import FastAPI, Request
import time


app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    import pudb; pu.db
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/async")
async def root():
    return {"message": "Hello World"}

@app.get("/sync")
def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8082)
