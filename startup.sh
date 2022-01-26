# gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

uvicorn main:app --reload
