from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    disabled: bool | None = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded",
        email="john@example.com",
        full_name="John Doe",
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    return User(
        username=token + "fakedecoded",
        email="john@example.com",
        full_name="John Doe",
    )


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
