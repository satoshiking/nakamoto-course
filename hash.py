from hashlib import md5


def md125(s: str) -> str:  # use this hash function to generate a collision
    return md5(s.encode()).hexdigest()[:8]


def generate_md125_collisions() -> (str, str):
    dp = {}
    key = 'nakamoto'
    num = 0
    while dp.get(md125(key), None) is None:
        dp[md125(key)] = key
        num += 1
        key += str(num)
    return (key, md125(key))


generate_md125_collisions()