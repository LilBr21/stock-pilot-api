# TODO: Implement watchlist routes
#
# router = APIRouter(prefix="/watchlists", tags=["watchlists"])
#
# @router.get("/", response_model=list[WatchlistRead])
# async def list_watchlists(
#     current_user: User = Depends(get_current_active_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     # Get all watchlists for current user
#     pass
#
# @router.post("/", response_model=WatchlistRead, status_code=201)
# async def create_watchlist(
#     watchlist_create: WatchlistCreate,
#     current_user: User = Depends(get_current_active_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     # Create new watchlist for current user
#     pass
#
# @router.get("/{watchlist_id}", response_model=WatchlistRead)
# async def get_watchlist(
#     watchlist_id: UUID,
#     current_user: User = Depends(get_current_active_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     # Get watchlist by ID (verify ownership)
#     pass
#
# @router.delete("/{watchlist_id}", status_code=204)
# async def delete_watchlist(
#     watchlist_id: UUID,
#     current_user: User = Depends(get_current_active_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     # Delete watchlist (verify ownership)
#     pass
#
# @router.post("/{watchlist_id}/items", response_model=WatchlistItemRead, status_code=201)
# async def add_watchlist_item(
#     watchlist_id: UUID,
#     item_create: WatchlistItemCreate,
#     current_user: User = Depends(get_current_active_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     # Add stock symbol to watchlist
#     pass
#
# @router.delete("/{watchlist_id}/items/{symbol}", status_code=204)
# async def remove_watchlist_item(
#     watchlist_id: UUID,
#     symbol: str,
#     current_user: User = Depends(get_current_active_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     # Remove stock from watchlist
#     pass
