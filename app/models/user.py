# TODO: Implement User model
#
# Table: users
# Columns:
# - id: UUID (primary key, default uuid4)
# - email: String(255), unique, indexed
# - hashed_password: String(255)
# - full_name: String(100), nullable
# - is_active: Boolean, default True
# - created_at: DateTime, server_default=func.now()
# - updated_at: DateTime, server_default=func.now(), onupdate=func.now()
#
# Relationships:
# - watchlists: one-to-many with Watchlist
#
# Hints:
# from sqlalchemy import String, Boolean, DateTime, func
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import Mapped, mapped_column, relationship
