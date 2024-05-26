from sqlalchemy import Column, Integer, String, DateTime
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    email = Column(String(200), unique=True, index=True)
    hashed_password = Column(String(100))
    created_at = Column(DateTime())
