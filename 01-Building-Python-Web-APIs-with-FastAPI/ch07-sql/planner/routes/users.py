from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.users import User, UserSignIn, TokenResponse

from database.connection import get_session

user_router = APIRouter(
    tags=["User"],
)

hash_password = HashPassword()


@user_router.post("/signup")
async def sign_user_up(new_user: User, session=Depends(get_session)) -> dict:
    print('new_user=',new_user)
    user_exist = session.get(User, new_user.email)

    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already."
        )
    hashed_password = hash_password.create_hash(new_user.password)
    new_user.password = hashed_password
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {
        "message": "User created successfully"
    }


@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: UserSignIn, session=Depends(get_session)) -> dict:
# async def sign_user_in(user: OAuth2PasswordRequestForm = Depends(), session=Depends(get_session)) -> dict:
    print('signin_user=',user)
    user_exist = session.get(User, user.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist."
        )
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed."
    )
