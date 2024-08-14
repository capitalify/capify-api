from motor.motor_asyncio import AsyncIOMotorClient
from src.config import settings

client = AsyncIOMotorClient(settings.mongodb_settings.url.get_secret_value())
db = client.get_database("db")
