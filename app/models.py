from sqlalchemy import Column, String, Integer

from database import Base

ignore_missing_imports = True

class Recipes(Base):
    __tablename__ = 'Recipes'
    id = Column(Integer, primary_key=True, index=True)
    recipe_name = Column(String, index=True)
    ingredients = Column(String, index=True)
    time_to_cooking = Column(Integer, index=True)
    description = Column(String, index=True)
    views = Column(Integer, index=True, default=0)
