from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

import string
import random

from requests import Session

from database import SessionLocal, engine, get_db
from models import Base, UrlMapping

Base.metadata.create_all(bind=engine)

app = FastAPI()

class URL(BaseModel):
    url: str

def generate_slug(length=6):
    """Generate a random short slug of given length."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.post("/shorten")
async def shorten_url(url: URL, db: Session = Depends(get_db)):
    original_url = url.url
    slug = generate_slug()

    while db.query(UrlMapping).filter(UrlMapping.slug == slug).first():
        slug = generate_slug()

    url_record = UrlMapping(slug=slug, original_url=original_url)
    db.add(url_record)
    db.commit()

    short_url = f"http://127.0.0.1:8000/{slug}"
    return {"short_url": short_url}

@app.get("/{slug}")
async def redirect_slug(slug: str, db: Session = Depends(get_db)):
    """
    When user visits /{slug}, redirect them to the original URL if it exists.
    """
    url_record = db.query(UrlMapping).filter(UrlMapping.slug == slug).first()
    if not url_record:
        raise HTTPException(status_code=404, detail="Slug not found")

    return RedirectResponse(url=url_record.original_url)
