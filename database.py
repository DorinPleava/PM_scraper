import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os as _os
import urllib as _urllib

db_server = _os.environ.get('db_server', 'localhost')
db_port = _urllib.parse.quote_plus(str(_os.environ.get('db_port', '5432')))
db_name = _os.environ.get('db_name', 'pm_scraper')
db_username = _urllib.parse.quote_plus(str(_os.environ.get('db_username', 'postgres')))
db_password = _urllib.parse.quote_plus(str(_os.environ.get('db_password', 'secret')))
ssl_mode = _urllib.parse.quote_plus(str(_os.environ.get('ssl_mode','prefer')))

DATABASE_URL = "sqlite:///./database.db?check_same_thread=False"
# DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, db_server, db_port, db_name, ssl_mode)

engine = _sql.create_engine(
    # azure setting ?
    # DATABASE_URL, echo=True

    # local setting
    DATABASE_URL #, check_same_thread=False,

    # DATABASE_URL, pool_size=3, max_overflow=0
)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()

print('connection is ok')
print(engine.table_names())