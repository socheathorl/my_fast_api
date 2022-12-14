from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from server.routes import router as NoteRouter

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
  return RedirectResponse("/docs")
  # return {
  #   "message": "Welcome to my note application, use the /docs route to proceed"
  # }


app.include_router(NoteRouter, prefix="/note")