import logging

from .settings import settings
from .database.accessor import init

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def setup():
    await init(settings)
    LOGGER.info('Application core is configured')
