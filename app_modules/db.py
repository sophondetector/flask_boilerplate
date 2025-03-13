from sqlalchemy import create_engine, text


class _DB_CONFIG:
    USER = "wade"
    HOST = "localhost"
    DB = "old"


_engine = sync_engine = create_engine(
    f"postgresql+psycopg://{_DB_CONFIG.USER}@{_DB_CONFIG.HOST}/{_DB_CONFIG.DB}"
)


# def get_cxn():
#     global _cxn
#     return _cxn


if __name__ == '__main__':
    with _engine.connect() as conn:
        result = conn.execute(text("select * from addresses limit 5"))
        print(result.all())
