from utils import require_var


class Dynmap:
    storage: dict

    def __init__(self, **args) -> None:
        self.storage = args

    def from_env(cls, **kwargs):
        db_name = kwargs.pop("DB_NAME", "dynmap")
        host = kwargs.pop("HOST", "localhost")
        password = kwargs.pop("DB_PASSWORD", require_var())
        port = kwargs.pop("PORT", "3306")
        db_type = kwargs.pop("DB_TYPE", "mysql")
        user = kwargs.pop("DB_USER", "dynmap")

        return cls(
            database=db_name,
            hostname=host,
            password=password,
            port=port,
            type=db_type,
            userid=user,
        )
