from fastapi import FastAPI, HTTPException
import secrets
import string

app = FastAPI(
    title="Password Generator API",
    version="1.0"
)

def generate_password(length, uppercase, lowercase, digits, symbols):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    return ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

@app.get("/")
def home():
    return {"message": "Password Generator API"}

@app.get("/generate")
def generate(
        length: int = 12,
        uppercase: bool = True,
        lowercase: bool = True,
        digits: bool = True,
        symbols: bool = False):

    if length < 4 or length > 100:
        raise HTTPException(
            status_code=400,
            detail="Length must be between 4 and 100"
        )

    if not any([uppercase, lowercase, digits, symbols]):
        raise HTTPException(
            status_code=400,
            detail="Enable at least one character type"
        )

    password = generate_password(
        length,
        uppercase,
        lowercase,
        digits,
        symbols
    )

    return {
        "password": password,
        "length": length
    }