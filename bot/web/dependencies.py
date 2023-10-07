from bot import conf
from bot.clients.rabbit import RabbitClient
from loguru import logger


async def get_rabbit() -> RabbitClient:
    logger.info(f"{conf.RABBIT_HOST = }")
    logger.info(f"{conf.RABBIT_PORT = }")
    logger.info(f"{conf.RABBIT_USER = }")
    logger.info(f"{conf.RABBIT_PASSWORD = }")
    return RabbitClient(conf.RABBIT_HOST, conf.RABBIT_PORT, conf.RABBIT_USER, conf.RABBIT_PASSWORD)
