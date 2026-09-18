from fastmcp import FastMCP

mcp = FastMCP("incident-toy-server")

@mcp.tool()
def get_dummy_status(service_name: str) -> dict:
    """Returns a fake health status for a given service name."""
    return {
        "service": service_name,
        "status": "healthy",
        "latency_ms": 42
    }

@mcp.tool()
def query_metrics(service_name: str, metric_name: str, time_range_minutes: int = 15) -> dict:
    """
    Query time-series metrics for a service (e.g. latency, error_rate, cpu_usage)
    over a recent time window. Returns current value, baseline, and whether it's anomalous.
    """
    return {
        "service": service_name,
        "metric": metric_name,
        "time_range_minutes": time_range_minutes,
        "current_value": 87.3,
        "baseline_value": 42.1,
        "is_anomalous": True
    }

@mcp.tool()
def search_logs(service_name: str, keyword: str, limit: int = 10) -> dict:
    """
    Search recent logs for a service, filtered by a keyword (e.g. 'timeout', 'error', '500').
    Returns matching log entries, most recent first, up to `limit` results.
    """
    fake_logs = [
        {"timestamp": "2026-09-19T10:15:22Z", "level": "ERROR", "message": f"Connection {keyword} while calling downstream auth service"},
        {"timestamp": "2026-09-19T10:14:58Z", "level": "ERROR", "message": f"Request {keyword} after 30000ms"},
        {"timestamp": "2026-09-19T10:14:40Z", "level": "WARN", "message": f"Retrying after {keyword} on attempt 2"},
    ]
    return {
        "service": service_name,
        "keyword": keyword,
        "limit": limit,
        "matches": fake_logs[:limit]
    }

@mcp.tool()
def get_deploy_history(service_name: str, limit: int = 5) -> dict:
    """
    Return recent deployment history for a service — version, timestamp, and who deployed it.
    Useful for correlating an incident's start time with a recent deploy.
    """
    fake_deploys = [
        {"version": "v2.4.1", "deployed_at": "2026-09-19T10:12:00Z", "deployed_by": "kritika"},
        {"version": "v2.4.0", "deployed_at": "2026-09-18T16:30:00Z", "deployed_by": "ci-bot"},
        {"version": "v2.3.9", "deployed_at": "2026-09-17T09:05:00Z", "deployed_by": "ci-bot"},
    ]
    return {
        "service": service_name,
        "limit": limit,
        "deploys": fake_deploys[:limit]
    }

@mcp.tool()
def get_service_health(service_name: str) -> dict:
    """
    Return an overall health snapshot for a service — status, uptime, and current error rate.
    Use this as a quick first check before digging into metrics or logs.
    """
    return {
        "service": service_name,
        "status": "degraded",
        "uptime_percent": 99.2,
        "error_rate_percent": 4.7
    }

if __name__ == "__main__":
    mcp.run()