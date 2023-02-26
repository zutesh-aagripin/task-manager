from sqlalchemy import Table, Column, Integer, String, DateTime, sql, ForeignKey

from db import metadata

task = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(120), nullable=False, unique=True),
    Column("created_at", DateTime(timezone=True), server_default=sql.func.now()),
    Column("user_id", ForeignKey("users.id"))
)
