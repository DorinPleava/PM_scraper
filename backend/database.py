import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os as _os
import urllib as _urllib


# DATABASE_URL = "sqlite:///./database.db"

# engine = _sql.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = _declarative.declarative_base()

db_server = _os.environ.get('db_server', 'localhost')
db_port = _urllib.parse.quote_plus(str(_os.environ.get('db_port', '5432')))
db_name = _os.environ.get('db_name', 'pm_scraper')
db_username = _urllib.parse.quote_plus(str(_os.environ.get('db_username', 'postgres')))
db_password = _urllib.parse.quote_plus(str(_os.environ.get('db_password', 'secret')))
ssl_mode = _urllib.parse.quote_plus(str(_os.environ.get('ssl_mode','prefer')))

DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, db_server, db_port, db_name, ssl_mode)

engine = _sql.create_engine(
    #DATABASE_URL, connect_args={"check_same_thread": False}
    DATABASE_URL, pool_size=3, max_overflow=0
)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
# metadata = _sql.MetaData()

# # metadata.create_all(bind=engine)
# metadata.create_all(engine)

# -----------------------NEW-------------------------

# db_server = _os.environ.get('db_server', 'localhost')
# db_port = _urllib.parse.quote_plus(str(_os.environ.get('db_port', '5432')))
# db_name = _os.environ.get('db_name', 'pm_scraper')
# db_username = _urllib.parse.quote_plus(str(_os.environ.get('db_username', 'postgres')))
# db_password = _urllib.parse.quote_plus(str(_os.environ.get('db_password', 'secret')))
# ssl_mode = _urllib.parse.quote_plus(str(_os.environ.get('ssl_mode','prefer')))

# DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, db_server, db_port, db_name, ssl_mode)

# database = _db.Database(DATABASE_URL)

# metadata = _sql.MetaData()

# engine = _sql.create_engine(
#     #DATABASE_URL, connect_args={"check_same_thread": False}
#     DATABASE_URL, pool_size=3, max_overflow=0
# )
# metadata.create_all(engine)
