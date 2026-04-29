from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


def hash_password(password: str):
    return ph.hash(password)

def verify_hash(hashed: str, password: str):
    try:
        return ph.verify(hash=hashed, password=password)
    except VerifyMismatchError:
        return False