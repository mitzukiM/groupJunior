from http.client import responses
from lib2to3.fixes.fix_input import context

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
router = APIRouter()

templates = Jinja2Templates(directory='templates')


@router.get('/')
async def index(request : Request):
    context = {'request':request}
    response = templates.TemplateResponse('index.html',context=context)
    return response

