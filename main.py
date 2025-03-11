from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import RedirectResponse

import string
import random

from requests import Session

from database import SessionLocal, engine, get_db
from models import Base, UrlMapping

Base.metadata.create_all(bind=engine)

app = FastAPI()


def generate_slug(length=6):
    """Generate a random short slug of given length."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.post("/shorten")
async def shorten_url(request: Request, db: Session = Depends(get_db)):
    """
    Expects JSON: {"url": "https://some-long-url.com"}
    Returns JSON: {"short_url": "http://localhost:8000/<slug>"}
    """
    data = await request.json()
    original_url = data.get("url")

    if not original_url:
        raise HTTPException(status_code=400, detail="Missing 'url' in request body")

    # Generate a random slug
    slug = generate_slug()
    while db.query(UrlMapping).filter(UrlMapping.slug == slug).first() is not None:
        slug = generate_slug()


    # Store the mapping
    url_record = UrlMapping(slug=slug, original_url=original_url)
    db.add(url_record)
    db.commit()
    db.refresh(url_record)

    # Construct the short link (assuming we run locally on port 8000)
    short_url = f"http://localhost:8000/{slug}"
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
