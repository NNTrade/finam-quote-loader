from finam import Market

def get_all_markets():
    return [e.name for e in Market]