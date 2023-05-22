from pydantic import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    postgres_user: str
    postgres_password: str
    postgres_db_name: str
    mail_username: str
    mail_password: str
    mail_from: str
    mail_port: int
    mail_server: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings_django = Settings()