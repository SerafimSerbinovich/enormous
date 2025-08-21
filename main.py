import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from core.bot.bot import dp, bot
from core.web import routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await asyncio.create_task(dp.start_polling(bot))
    yield
    # shutdown
    await bot.session.close()

app = FastAPI(lifespan=lifespan)
app.include_router(routers.router)
uvicorn.run(app)
