FILENAME = '/home/wade/Downloads/wordlist.txt'
with open(FILENAME, 'r') as fh:
    WORDLIST = fh.read().splitlines()


def prefix_query(prefix: str, n=10) -> list[str]:
    counter = 0
    res = []
    for word in WORDLIST:
        if word.startswith(prefix):
            res.append(word)
            counter += 1
            if counter == n:
                return res

    return res


def make_response(input: str) -> dict:
    res = prefix_query(input)
    return dict(text=res)
