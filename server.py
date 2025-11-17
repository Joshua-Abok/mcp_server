# creating an MCP server in the python-mcp client
# the script defines MCP server for a weather service
from mcp.server.fastmcp import FastMCP

# create an MCP server instance
mcp = FastMCP("Weather Service")


# define a handler for the "get_weather" command
@mcp.tool()
def get_weather(location: str) -> str:
    '''Fetches weather information for a given location.'''
    # In a real implementation, this would fetch data from a weather API.
    weather_reports = {
        "New York": "Sunny, 25°C",
        "London": "Cloudy, 18°C",
        "Tokyo": "Rainy, 22°C",
    }
    return weather_reports.get(location, "Location not found")

@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    '''Resource to get weather information for a given location.'''
    return get_weather(location)

@mcp.prompt()
def weather_prompt(location: str) -> str:
    '''Prompt to get weather information for a given location.'''
    return f"The current weather in {location} is: {get_weather(location)}"


# Run the server 
if __name__ == "__main__":
    mcp.run(transport="sse", port=3001)