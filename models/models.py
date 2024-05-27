import os
from datetime import datetime

from dotenv import load_dotenv
from sqlalchemy import String, func, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

POSTGRES_PASSWORD = os.getenv('POSTGRES_DB_PASSWORD')
POSTGRES_USER = os.getenv('POSTGRES_DB_USER')
POSTGRES_DB = os.getenv('POSTGRES_DB_USER')
POSTGRES_HOST = os.getenv('POSTGRES_DB_HOST')
POSTGRES_PORT = int(os.getenv('POSTGRES_DB_PORT'))

load_dotenv()

db_url: str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
engine = create_engine(url=db_url, echo=True)
Session = sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    email: Mapped[str] = mapped_column(unique=True)
    role: Mapped[str] = mapped_column(default='management')
    age: Mapped[int] = mapped_column(nullable=True)
    salary: Mapped[float] = mapped_column(nullable=True)
    job_title: Mapped[bool] = mapped_column(nullable=True)
    date_promotion: Mapped[datetime] = mapped_column(nullable=True)
    password: Mapped[str]
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())
    is_active: Mapped[bool] = mapped_column(default=False)
    is_enabled: Mapped[bool] = mapped_column(default=False)
    is_admin: Mapped[bool] = mapped_column(default=False)

# Base.metadata.create_all(bind=engine)