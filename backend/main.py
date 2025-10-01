from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings

app = FastAPI(
    # set title and description
    title="Choose Your Own Adventure Game API",
    description="api to generate cool stories",
    version="0.1.0",    # if we are in prod, we can update this everytime we make a change
    docs_url="/docs",
    redoc_url="/redoc",     # all the fastapi api's come with documentation which we can view from the website
)

# adding middleware
# have our api be used from a different origin
# origin = domain/ url the services is running on
# frontend runs on localhost:x, but backend may run on localhost:y
# since backend has builtin securities it won't allow it to communicate with anything that's not on the same port/ origin
# by adding CORS, we enable certain origins/urls to interact with our backend

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],    # GET, POST, PUT
    allow_headers=["*"],    # additional info
)

if __name__ == "__main__":  # only run if we are in main.py file (not imported)
    import uvicorn
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
        # uvicorn - webserver - allows to run the fastapi application - because it can' run unless it's connected to a server
        