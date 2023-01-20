from tortoise import Tortoise


async def init(settings):
    await Tortoise.init(config=settings.TORTOISE_ORM)
    await Tortoise.generate_schemas()
