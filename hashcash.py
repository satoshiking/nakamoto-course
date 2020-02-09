from hashlib import sha256


def binary_leading_0s(hex_str: str):
    binary_representation = bin(int(hex_str, 16))[2:].zfill(256)
    return len(binary_representation) - len(binary_representation.lstrip('0'))

def is_valid(token: str, date: str, email: str, difficulty: int) -> bool:
    version = '1'
    to_validate = version + ':' + date[:6] + ':' + email + ':' + token.split(':')[-1][:16]
    digest = sha256(to_validate.encode()).hexdigest()
    return binary_leading_0s(digest) >= difficulty

def mint(date: str, email: str, difficulty: int) -> str:
    version = '1'
    prefix = version + ':' + date[:6] + ':' + email + ':'
    nonce = int('0000000000000000', 16)
    token = prefix + str(nonce)
    while not is_valid(token, date[:6], email, difficulty):
        nonce += 1
        token = prefix + str(nonce)
    return token
