from fastapi import FastAPI
import uvicorn
from web import routers


def main():
    app = FastAPI()
    app.include_router(routers.router)
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
     main()
