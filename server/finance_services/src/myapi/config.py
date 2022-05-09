import os
from urllib.parse import quote


def get_mysql_uri():
    host = os.environ.get(
        "DB_HOST", "bootcamp-db.cjpzthi8cj90.ap-southeast-1.rds.amazonaws.com:3306"
    )
    password = os.environ.get("DB_PASSWORD", "Bootcamp2022@Grab")
    user = os.environ.get("DB_USER", "demo")
    db_name = os.environ.get("DB_NAME", "finance_demo")
    return "mysql+pymysql://{user}:{pw}@{host}/{db}".format(
        host=host, db=db_name, user=user, pw=quote(password)
    )


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5000 if host == "localhost" else 80
    return f"http://{host}:{port}"
