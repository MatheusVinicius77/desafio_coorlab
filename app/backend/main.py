from fastapi import FastAPI
from controller import router as item_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(item_router)


if __name__ == "__main__":

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)