from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def verify_password(plain_password, hahsed_password):
    return pwd_context.verify(plain_password, hahsed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

hash = get_password_hash("junaid")
asd = get_password_hash("junaid")

print("hashed", hash)
print("asd", asd)

print("verify_password", verify_password("junaid",hash))
print("verify_password", verify_password("1junaid",hash))