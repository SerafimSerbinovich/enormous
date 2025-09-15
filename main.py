import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from core.bot.bot import dp, bot
from core.web import llm_routers, user_routers
from core.database.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    await asyncio.create_task(dp.start_polling(bot))
    yield
    await bot.session.close()

def main():
    app = FastAPI(lifespan=lifespan)
    app.include_router(routers.router)
    app.include_router(user_router.router)
    uvicorn.run(app)

if __name__ == "__main__":
    main()
