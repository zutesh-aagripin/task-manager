from sqlalchemy import Table, Column, Integer, String

from db import metadata

user = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(200)),
    Column("last_name", String(200)),
    Column("username", String(120), unique=True),
    Column("password", String(255))
)
