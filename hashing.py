from passlib.context import CryptContext

pwt_context = CryptContext(schemes=["bcrypt"],
                           deprecated="auto")


class Hash():
    def bcrypt(password: str):
        return pwt_context.hash(password)

    def verify(plain_password, hashed_password):
        return pwt_context.verify(hashed_password, plain_password)

