from os import path
from typing import Optional

from tinydb import TinyDB, Query
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder as js_enc

from valids import *


CUR_DIR = path.abspath(path.dirname(__file__))
DB_PATH = path.join(CUR_DIR, 'db.json')


DB = TinyDB(DB_PATH)
Forms = DB.table('forms')

app = FastAPI()

guess_type = make_guess_type(is_date, is_phone, is_email, is_text)


@app.post("/get_form")
async def get_form(req: Request):
    form = await req.form()

    form = { k: guess_type(v) for k, v in form.items() }

    form_names = [form.get('name') for form in Forms.search(Query().fragment(form))]
    
    return JSONResponse(content=js_enc(form_names if len(form_names) else form))
