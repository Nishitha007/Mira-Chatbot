# Author: Dhaval Patel. Codebasics YouTube Channel

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse


app = FastAPI()


@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if intent == " track.order - Context:ongoing - tracking":
        return JSONResponse(content={
            "fulfillmentText": f"Received == {intent}== in the backend"

        )}