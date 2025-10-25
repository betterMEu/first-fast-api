from pydantic import (
    PostgresDsn,
    computed_field,
)
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    datasource_scheme: str = ""
    datasource_host: str = ""
    datasource_port: int = 3306
    datasource_username: str = ""
    datasource_password: str = ""
    datasource_database: str = ""

    @computed_field  # type: ignore[prop-decorator]
    @property
    def datasource_url(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme=self.datasource_scheme,
            username=self.datasource_username,
            password=self.datasource_password,
            host=self.datasource_host,
            port=self.datasource_port,
            path=self.datasource_database,
        )


settings = Settings()
