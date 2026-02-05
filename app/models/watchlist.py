# TODO: Implement Watchlist and WatchlistItem models
#
# Table: watchlists
# Columns:
# - id: UUID (primary key)
# - user_id: UUID (foreign key to users.id, ON DELETE CASCADE)
# - name: String(100)
# - created_at: DateTime
#
# Relationships:
# - user: many-to-one with User
# - items: one-to-many with WatchlistItem
#
# ---
#
# Table: watchlist_items
# Columns:
# - id: UUID (primary key)
# - watchlist_id: UUID (foreign key to watchlists.id, ON DELETE CASCADE)
# - symbol: String(10)
# - added_at: DateTime
#
# Constraints:
# - UniqueConstraint on (watchlist_id, symbol)
#
# Relationships:
# - watchlist: many-to-one with Watchlist
