from loguru import logger

logger.remove()

logger.add(sink="history.log", level="INFO", rotation="1 MB")
