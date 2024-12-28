from sqlalchemy import Column, Integer, String, Boolean
from backend.core.database import Base


class ThemeEntity(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(512), nullable=True)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<ThemeEntity id={self.id} title={self.title}>"
