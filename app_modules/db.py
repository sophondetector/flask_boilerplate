from sqlalchemy import create_engine, text

USERNAME = "wade"
HOSTNAME = "localhost"
DBNAME = "old"

_engine = sync_engine = create_engine(
    f"postgresql+psycopg://{USERNAME}@{HOSTNAME}/{DBNAME}"
)


# def get_cxn():
#     global _cxn
#     return _cxn


if __name__ == '__main__':
    with _engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())
