# app.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/utcp")
def utcp_discovery():
    return {
        "manual_version": "1.0.0",
        "utcp_version": "1.0.1",
        "tools": [
            {
                "name": "get_weather",
                "description": "Get current weather for a location",
                "inputs": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string", "description": "City name"}
                    },
                    "required": ["location"],
                },
                "outputs": {
                    "type": "object",
                    "properties": {
                        "temperature": {"type": "number"},
                        "conditions": {"type": "string"},
                    },
                },
                "tool_call_template": {
                    "call_template_type": "http",
                    "url": "http://127.0.0.1:8000/api/weather",
                    "http_method": "GET",
                },
            }
        ],
    }


# Implement the actual weather API endpoint
@app.get("/api/weather")
def get_weather(location: str):
    # In a real app, you'd fetch actual weather data
    return {"temperature": 22.5, "conditions": "Sunny"}
