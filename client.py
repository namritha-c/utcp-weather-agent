# client.py
import asyncio
from utcp.utcp_client import UtcpClient
from utcp_http.http_call_template import HttpCallTemplate

async def main():
    # Create a UTCP client with configuration
    client = await UtcpClient.create(config={
        "manual_call_templates": [
            {
                "name": "weather_service",
                "call_template_type": "http",
                "http_method": "GET",
                "url": "http://localhost:8000/utcp"
            }
        ]
    })

    # Tools are automatically registered from the manual call templates
    # Call a tool by its namespaced name: {manual_name}.{tool_name}
    result = await client.call_tool(
        "weather_service.get_weather", 
        tool_args={"location": "San Francisco"}
    )
    print(f"Weather: {result['temperature']}°C, {result['conditions']}")

if __name__ == "__main__":
    asyncio.run(main())