# STORE UTILITY FUNCTIONS HERE

from passlib.context import CryptContext

# Create a password context for hashing passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Password hashing function
def hash(password: str):
    return pwd_context.hash(password)

# Password verification function
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)