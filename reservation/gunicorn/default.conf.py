# Gunicorn configuration file

# Defaults
bind = ["0.0.0.0:8000"]
backlog = 2048
daemon = False
max_requests = 200
errorlog = "-"
loglevel = "warning"
timeout = 180
workers = 8
