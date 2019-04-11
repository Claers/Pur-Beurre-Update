bind = "flokami.ovh:8001"
log_file = "logs/gunicorn_logs.txt"

# Environment variables
raw_env = [
    "PRODUCTION=true",
]
