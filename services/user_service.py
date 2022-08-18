from fastapi import APIRouter, Response, status, HTTPException
from models import User, ShowUser, UserNotFoundError
from models.error_model import DatabaseError
from models.user_model import CreateUserRequestBody
from repositories.user_repo import create_user, query_user


user_router = APIRouter(tags=["users"])

# get user data
@user_router.get("/{uid}", response_model=ShowUser,
                 responses={
                     200: {
                         "model": ShowUser
                     },
                     404: {
                         "model": UserNotFoundError,
                         "description": "User Not Found Error"
                     },
                     520: {
                         "model": DatabaseError,
                         "description": "Database Connection Error"
                     }
                 })
async def get_user(uid: str):
    result = query_user(uid)
    if 200 in result:
        return result[200]
    else:
        error_key = list(result.keys())[0]
        raise HTTPException(status_code=error_key, detail=result[error_key])


# post user data
@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShowUser, 
                            responses={
                                201: {
                                    "model": ShowUser,
                                    "description": "User Was Created"
                                },
                                520: {
                                    'model': DatabaseError,
                                    'description': 'Database Connection Error'
                                }
                            })
async def add_user(user: CreateUserRequestBody):
    result = create_user(user)
    if 201 in result:
        return result[201][0]
    else:
        error_key = list(result.keys())[0]
        raise HTTPException(status_code=error_key, detail=result[error_key])