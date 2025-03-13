from .db import do_address_query


def make_response(input: str) -> dict:
    res = do_address_query(input)
    return dict(text=res)
