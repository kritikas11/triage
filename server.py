from fastmcp import FastMCP

mcp = FastMCP("incident-toy-server")

@mcp.tool()
def get_dummy_status(service_name: str) -> dict:
    """Returns a fake health status for a given service name."""
    return {
        "service": service_name,
        "status":"healthy",
        "latency_ms": 42
    }

if __name__ == "__main__":
    mcp.run()