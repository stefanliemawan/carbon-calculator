import shortuuid
import hashlib
import os

# salt = os.urandom(32)

def generate_id(tablename, index):
    match tablename:
        case "item_emissions":
            prefix = "iem"
        case "users":
            prefix = "usr"
        case "user_emissions":
            prefix = "uem"

    uid = shortuuid.uuid()

    id = f"{prefix}-{uid}{index}"

    return id

def hash_password(password):
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), 100000)
    print(key)
    return key