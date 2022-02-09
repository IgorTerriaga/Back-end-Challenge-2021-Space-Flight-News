from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql+psycopg2://zyhfesfxpfxvbz:6318d82135697351e26637859cc30126bd6937367c892daad9fc008ac6af06ba@ec2-34-205-46-149.compute-1.amazonaws.com:5432/d7b7etm394h0d",
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
