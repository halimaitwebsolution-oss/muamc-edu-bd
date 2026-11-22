# gunicorn.conf.py
import multiprocessing

# 2 workers with 4 threads each — good for Render's free tier (512MB RAM)
# Increase workers to 4 on paid plans
workers = 2
threads = 4
worker_class = "gthread"
timeout = 120          # Render health check timeout is 90s; give margin
keepalive = 5
max_requests = 1000    # Recycle workers to prevent memory bloat
max_requests_jitter = 100
preload_app = True     # Load app once, share across workers (faster cold start)
accesslog = "-"
errorlog = "-"
loglevel = "info"
