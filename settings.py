from os import getenv
from os.path import join, dirname, abspath
from dotenv import load_dotenv

basedir = abspath(dirname(__name__))
load_dotenv(join(basedir, '.env'))

MONGO_URI = str(getenv('MONGO_URI'))
DATABASE_NAME = str(getenv('DATABASE_NAME'))
