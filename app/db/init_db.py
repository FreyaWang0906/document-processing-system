from app.db.models import Base
from app.db.session import engine

# Create all tables in the database
def init_db():
    Base.metadata.create_all(bind=engine)

# Run this when script is executed directly
if __name__ == "__main__":
    init_db()