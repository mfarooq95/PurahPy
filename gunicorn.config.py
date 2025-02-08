bind = "0.0.0.0:$PORT"
workers = 4
threads = 2
timeout = 30
accesslog = "-"
errorlog = "-"
loglevel = "info"
worker_class = "gevent"