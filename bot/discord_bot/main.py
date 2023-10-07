import asyncio

from bot.clients.rabbit import RabbitWorker
from bot.discord_bot import conf
from bot.discord_bot.discord_factory import discord_factory
from loguru import logger


async def main():
    discord_client = discord_factory(conf.ENV)
    logger.info(f"{conf.RABBIT_HOST = }")
    logger.info(f"{conf.RABBIT_PORT = }")
    logger.info(f"{conf.RABBIT_USER = }")
    logger.info(f"{conf.RABBIT_PASSWORD = }")
    rabbit = RabbitWorker(
        conf.RABBIT_HOST,
        conf.RABBIT_PORT,
        conf.RABBIT_USER,
        conf.RABBIT_PASSWORD,
        discord_client,
        asyncio.get_event_loop(),
    )

    await asyncio.gather(
        rabbit.consume(),
        discord_client.start(conf.DISCORD_TOKEN),
    )


if __name__ == "__main__":
    asyncio.run(main())
