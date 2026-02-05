# TODO: Implement user routes
#
# router = APIRouter(prefix="/users", tags=["users"])
#
# @router.get("/me", response_model=UserRead)
# async def get_current_user_profile(current_user: User = Depends(get_current_active_user)):
#     return current_user
#
# @router.patch("/me", response_model=UserRead)
# async def update_current_user(
#     user_update: UserUpdate,
#     current_user: User = Depends(get_current_active_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     # Update user fields, save to DB
#     pass
