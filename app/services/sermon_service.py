#!/usr/bin/python3
# app/services/sermon_service.py

from app.database.models import BookSeriesSermon, ScriptureSermon, TopicSermon
from app import db

def create_sermon(name, verse_text, preached_by, audio, category):
    """Create and add a new sermon to the specified category."""
    sermon = None

    if category == "Book Series":
        sermon = BookSeriesSermon(name=name, verse_text=verse_text, preached_by=preached_by, audio=audio)
    elif category == "By Scripture":
        sermon = ScriptureSermon(name=name, verse_text=verse_text, preached_by=preached_by, audio=audio)
    elif category == "By Topic":
        sermon = TopicSermon(name=name, verse_text=verse_text, preached_by=preached_by, audio=audio)

    if sermon:
        db.session.add(sermon)
        db.session.commit()
        return sermon
    else:
        return None

def get_sermons_by_category(category):
    """Retrieve all sermons from a specified category."""
    if category == "Book Series":
        return BookSeriesSermon.query.all()
    elif category == "By Scripture":
        return ScriptureSermon.query.all()
    elif category == "By Topic":
        return TopicSermon.query.all()

def get_sermon_by_name_and_category(name, category):
    """Retrieve a sermon by its name and category."""
    if category == "Book Series":
        return BookSeriesSermon.query.filter_by(name=name).first()
    elif category == "By Scripture":
        return ScriptureSermon.query.filter_by(name=name).first()
    elif category == "By Topic":
        return TopicSermon.query.filter_by(name=name).first()

def update_sermon(sermon, name, verse_text, preached_by, audio):
    """Update the attributes of a sermon."""
    if sermon:
        sermon.name = name
        sermon.verse_text = verse_text
        sermon.preached_by = preached_by
        sermon.audio = audio
        db.session.commit()
        return sermon
    else:
        return None

def delete_sermon(sermon):
    """Delete a sermon from the database."""
    if sermon:
        db.session.delete(sermon)
        db.session.commit()
        return True
    else:
        return False
