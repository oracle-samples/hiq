from fastapi import FastAPI, Request
import time
from opentelemetry import trace
from opentelemetry.instrumentation.wsgi import collect_request_attributes
from opentelemetry.propagate import extract
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)


trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer_provider().get_tracer(__name__)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(ConsoleSpanExporter())
)

app = FastAPI()
import time
'''
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
'''

@app.get("/async")
async def root():
    #import pudb; pu.db
    time.sleep(2)
    return {"message": "async"}

@app.get("/sync")
def root():
    import pudb; pu.db
    time.sleep(2)
    return {"message": "sync"}

if __name__ == "__main__":
    import uvicorn
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    
    FastAPIInstrumentor.instrument_app(app, tracer_provider=trace.get_tracer_provider())
    
    uvicorn.run(app, host="0.0.0.0", port=8082)
