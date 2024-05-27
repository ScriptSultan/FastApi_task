import uvicorn
from fastapi import FastAPI

from REST.req_user import users

app = FastAPI()
app.include_router(users)

if __name__ == '__main__':
    try:
        uvicorn.run(f"{__name__}:app", port=8000)
    except KeyboardInterrupt:
        pass

