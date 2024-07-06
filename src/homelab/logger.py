import logging
import os
import sys

log_level = os.getenv("HOMELAB__LOG_LEVEL", "INFO")
log_format = os.getenv("HOMELAB__LOG_FORMAT", "%(asctime)s %(levelname)-8s %(threadName)-15s %(name)s:%(lineno)-3s %(message)s")
log = logging.getLogger("homelab")
log.setLevel(log_level)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(log_level)
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
log.addHandler(handler)
