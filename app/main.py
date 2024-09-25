from typing import List, Any, Sequence
from fastapi import FastAPI, HTTPException
from sqlalchemy.future import select

import models
import schemas
from database import engine, session

app = FastAPI()



@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.post('/recipes', response_model=schemas.RecipeOutShort)
async def books_1(book: schemas.RecipeIn) -> models.Recipes:
    new_book = models.Recipes(**book.dict())
    async with session.begin():
        session.add(new_book)
    return new_book


@app.get('/recipes/{recipe_id}', response_model=schemas.RecipeOutShort)
@app.get('/recipes', response_model=List[schemas.RecipeOutLong])
async def books(recipe_id=None) -> Sequence[Any]:
    if recipe_id:
        async with session.begin():
            data = await session.execute(select(models.Recipes).where(models.Recipes.id == recipe_id))
        res = data.scalar()
        if res:
            async with session.begin():
                res.views += 1
                await session.commit()
            return res
        else:
            raise HTTPException(status_code=404, detail="not found")
    async with session.begin():
        res = await session.execute(select(models.Recipes).order_by(models.Recipes.views.desc(), models.Recipes.time_to_cooking))
    return res.scalars().all()


