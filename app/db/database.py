from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


engine = create_engine(settings.DATABASE_URL)

localSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)
