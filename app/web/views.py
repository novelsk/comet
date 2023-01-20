from fastapi import FastAPI, responses
from tortoise.exceptions import IntegrityError
from .models import City
from .settings import api_key  # get key on: https://openweathermap.org/
import requests


def setup_views(app: FastAPI):
    @app.post("/weather/{city}")
    async def add_city(city: str) -> responses.JSONResponse:
        print(city)
        response = requests.get(f'https://openweathermap.org/data/2.5/find?q={city}&appid={api_key}')
        result = response.json()
        if result['cod'] == '200':
            context = {
                'added': [],
                'exist': []
            }
            for city in result['list']:
                try:
                    temp = await City.create(name=city['name'], remote_id=city['id'])
                    context['added'].append(temp.name)
                except IntegrityError:
                    context['exist'].append(city['name'])

            return responses.JSONResponse(status_code=201, content=context)
        return responses.JSONResponse(status_code=result['cod'], content=result)
