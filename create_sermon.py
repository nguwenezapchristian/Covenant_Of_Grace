from app import app, db
from app.database.models import BookSeriesSermon, ScriptureSermon, TopicSermon

def create_sermon(name, verse_text, preached_by, audio, category):
    """Create a new sermon and add it to the database."""
    with app.app_context():
        # Determine which model to use based on the category
        if category == "Book Series":
            SermonModel = BookSeriesSermon
        elif category == "By Scripture":
            SermonModel = ScriptureSermon
        elif category == "By Topic":
            SermonModel = TopicSermon
        else:
            # Handle unknown category
            raise ValueError(f"Invalid category: {category}")

        # Create a new sermon object
        sermon = SermonModel(name=name, verse_text=verse_text, preached_by=preached_by, audio=audio)

        # Add the sermon to the database session
        db.session.add(sermon)

        # Commit the transaction to save the sermon to the database
        db.session.commit()

if __name__ == "__main__":
    # Example usage of create_sermon function
    create_sermon("Kristo wabambwe", "Verse Text", "Christian", "audio/audio.mp3", "Book Series")
