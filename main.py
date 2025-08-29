import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from core.bot.bot import dp, bot
from core.web import routers
from core.database.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    create_tables()  # Create database tables
    await asyncio.create_task(dp.start_polling(bot))
    yield
    # shutdown
    await bot.session.close()

app = FastAPI(lifespan=lifespan)
app.include_router(routers.router)
uvicorn.run(app)
