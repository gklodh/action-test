# gunicorn.conf.py — production settings
# Usage:  gunicorn -c deploy/gunicorn.conf.py app:app
bind = "0.0.0.0:8000"        # listen on all interfaces, port 8000
workers = 4                  # 2 × CPU cores + 1 is a good rule of thumb
worker_class = "sync"
timeout = 120
accesslog = "-"
errorlog = "-"
loglevel = "info"
