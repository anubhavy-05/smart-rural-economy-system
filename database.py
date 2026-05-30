from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Database ka naam aur location (SQLite use kar rahe hain)
SQLALCHEMY_DATABASE_URL = "sqlite:///./rural_economy.db"

# 2. Engine ban banana (Yeh actual database se connect karta hai)
# 'check_same_thread': False sirf SQLite ke liye zaroori hota hai FastAPI mein,
# taaki multiple requests ek sath data read/write kar sakein.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. SessionLocal banana (Yeh database ke sath ek temporary "session" ya baatcheet start karta hai)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base class banana (Hamari saari database tables is Base class ko inherit karengi)
Base = declarative_base()