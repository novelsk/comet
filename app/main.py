from fastapi import FastAPI
from core import setup
from web.views import setup_views

app = FastAPI()
app.on_event('startup')(setup)
setup_views(app)
