from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UrlMapping(Base):
    __tablename__ = "url_mappings"

    slug = Column(String, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
