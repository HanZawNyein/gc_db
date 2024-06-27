from typing import Optional

from sqlalchemy import create_engine, String
from sqlalchemy.orm import Mapped, mapped_column

from base import Base

engine = create_engine("sqlite://", echo=True)
if __name__ == '__main__':
    class User(Base):
        __tablename__ = 'user'

        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(30))
        fullname: Mapped[Optional[str]]
        username: Mapped[str] = mapped_column(String(30))

    Base.metadata.create_all(engine)
