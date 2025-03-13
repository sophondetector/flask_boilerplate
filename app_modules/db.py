from sqlalchemy import create_engine, text


class _DB_CONFIG:
    USER = "wade"
    HOST = "localhost"
    DB = "old"


_engine = sync_engine = create_engine(
    f"postgresql+psycopg://{_DB_CONFIG.USER}@{_DB_CONFIG.HOST}/{_DB_CONFIG.DB}"
)


def do_address_query(input: str) -> list[str]:
    query = f'''
    select address from addresses
    where address like \'%{input}%\';
    '''

    with _engine.connect() as conn:
        result = conn.execute(text(query))
        rows = result.all()
        res = [ite[0] for ite in rows]

    return res


if __name__ == '__main__':
    res = do_address_query('New')
    for ite in res:
        print(ite)

    # with _engine.connect() as conn:
    #     result = conn.execute(text("select * from addresses limit 5"))
    #     print(result.all())
