from auth.models.user import Base
from sqlalchemy import create_engine
from auth.config import config


def setup_database():
    engine = create_engine(config.DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")


if __name__ == "__main__":
    setup_database()

