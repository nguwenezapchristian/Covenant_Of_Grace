#!/usr/bin/python3
# app/database/models.py
from app import db

# Defining SQLAlchemy models

# Base class for common columns
class BaseSermon(db.Model):
    """Base Sermon model with common attributes"""
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    verse_text = db.Column(db.Text)
    preached_by = db.Column(db.String(255))
    audio = db.Column(db.String(255), nullable=False)

# Sermon model for Book Series category
class BookSeriesSermon(BaseSermon):
    """Model for sermons in the Book Series category"""
    __tablename__ = 'book_series_sermon'
    category = "Book Series"

# Sermon model for Scripture category
class ScriptureSermon(BaseSermon):
    """Model for sermons in the Scripture category"""
    __tablename__ = 'scripture_sermon'
    category = "By Scripture"

# Sermon model for Topic category
class TopicSermon(BaseSermon):
    """Model for sermons in the Topic category"""
    __tablename__ = 'topic_sermon'
    category = "By Topic"
