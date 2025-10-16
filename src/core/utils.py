from datetime import datetime, timezone

def get_current_utc_time() -> str:
    """Return current UTC time in ISO 8601 format with 'Z' suffix."""
    return datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace("+00:00", "Z")
