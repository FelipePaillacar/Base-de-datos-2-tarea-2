import os

from litestar.contrib.sqlalchemy.plugins import (
    SQLAlchemyPlugin,
    SQLAlchemySyncConfig,
    SyncSessionConfig,
)

db_config = SQLAlchemySyncConfig(
    connection_string=os.environ["DATABASE_URL"],
    session_config=SyncSessionConfig(expire_on_commit=False),
)
sqlalchemy_config = SQLAlchemyPlugin(config=db_config)
