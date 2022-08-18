from os import getenv
from os.path import join, dirname, abspath
from dotenv import load_dotenv

basedir = abspath(dirname(__name__))
load_dotenv(join(basedir, '.env'))

MONGO_KEY = str(getenv('MONGO_KEY'))
DATABASE_NAME = str(getenv('DATABASE_NAME'))
DATASOURCE = str(getenv("DATASOURCE"))
DATA_ENDPOINT = str(getenv("DATA_ENDPOINT"))
