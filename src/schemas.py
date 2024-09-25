from typing import Optional

from pydantic import BaseModel



class BaseRecipeShort(BaseModel):
    ingredients: str
    description: str

class BaseRecipeLong(BaseModel):
    recipe_name: str
    time_to_cooking: int
    views: int


class RecipeIn(BaseRecipeLong, BaseRecipeShort):
    views = 0

class RecipeOutShort(BaseRecipeShort):

    class Config:
        orm_mode = True

class RecipeOutLong(BaseRecipeLong):

    class Config:
        orm_mode = True
