from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.base import Base

if TYPE_CHECKING:
    from src.db.models.match import Match
    from src.db.models.player import Player


class Elo(Base):
    __tablename__ = "elos"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    match_id: Mapped[str] = mapped_column(ForeignKey("matches.id"))
    player_id: Mapped[UUID] = mapped_column(ForeignKey("players.id"))
    elo: Mapped[int] = mapped_column(Integer())

    player: Mapped["Player"] = relationship(back_populates="elos")
    match: Mapped["Match"] = relationship(back_populates="elos")

    def __str__(self) -> str:
        return f"<Elo {str(self.id)}>"

    def __repr__(self) -> str:
        return f"<Elo {str(self.id)}>"
