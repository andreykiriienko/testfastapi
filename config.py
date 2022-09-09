import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# DB_USERNAME = os.getenv('DB_USERNAME')
# DB_PASSWORD = os.getenv('DB_PASSWORD')
# DB_HOST = os.getenv('DB_HOST')
# DB_NAME = os.getenv('DB_NAME')


DB_USERNAME = 'pbbot_testfastapi'
DB_PASSWORD = '7^bk39FZi;'
DB_NAME = 'pbbot_testfastapi'
DB_HOST = 'pbbot.mysql.tools'
DB_PORT = ''

engine = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}', encoding='utf8')
Base = declarative_base()
