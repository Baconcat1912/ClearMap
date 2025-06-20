from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/echo/")
async def echo(request: Request):
    # Get the request data (JSON, form-data, etc.)
    data = await request.json() if request.headers.get("content-type") == "application/json" else None

    # Log the request details (for debugging)
    print(f"Received request: {data}")

    # Respond with the received data + success status
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "received_data": data,
            "message": "API request was successful!"
        }
    )




