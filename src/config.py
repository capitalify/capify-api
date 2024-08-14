import os
import yaml
from pathlib import Path
from pydantic import BaseModel, Field, SecretStr


class MongoDBSettings(BaseModel):
    url: SecretStr = Field(
        ...,
        examples=["mongodb://username:password@localhost:27017/db?authSource=admin"],
    )


class Settings(BaseModel):
    mongodb_settings: MongoDBSettings = Field(..., description="MongoDB settings")

    @classmethod
    def from_yaml(cls, path: Path) -> "Settings":
        with open(path, encoding="utf-8") as f:
            yaml_config = yaml.safe_load(f)

        return cls.model_validate(yaml_config, strict=False)


settings_path = os.getenv("SETTINGS_PATH", "settings.yaml")
settings: Settings = Settings.from_yaml(settings_path)

__all__ = ["settings"]
