import os


class Config:
    """Global config object."""

    def __init__(self) -> None:
        self.mongo = self._MongoMeta()


    class _MongoMeta:
        """Mongo connection configuration."""

        def __init__(self) -> None:
            self._host = os.getenv("MONGO_HOST", "localhost")  # type: ignore
            self._port = int(os.getenv("MONGO_PORT", 27017))  # type: ignore
            self._username: str = os.getenv("MONGO_USERNAME", "")  # type: ignore
            self._password: str = os.getenv("MONGO_PASSWORD", "")  # type: ignore
            self.db: str = os.getenv("MONGO_DATABASE", "hosting_base")  # type: ignore
            self.coll = os.getenv("MONGO_COLL", "hosting_items")

            uri = "mongodb://"
            if self._username and self._password:
                uri += f"{self._username}:{self._password}@{self._host}:{self._port}/{self.db}"
            else:
                uri += f"{self._host}:{self._port}/{self.db}"
            uri += "?authSource=admin"
            self.uri = os.getenv("MONGO_URI", uri)


def get_config() -> Config:
    """Get Config instance."""
    return Config()