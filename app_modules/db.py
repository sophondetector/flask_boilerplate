from sqlalchemy import create_engine

USERNAME = "wade"
HOSTNAME = "localhost"
DBNAME = "old"

_cxn = sync_engine = create_engine(
    f"postgresql+psycopg://{USERNAME}@{HOSTNAME}/{DBNAME}"
).connect()


def get_cxn():
    return _cxn
