from sqlalchemy import create_engine, desc
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from datetime import datetime
from models import UserScore
from flask_sqlalchemy import SQLAlchemy
from common import logger
import app
import configwork
import MySQLdb
import sqlalchemy


def get_db_config():
    # config = configwork.get_config()
    config = {'Database': {'host':'198.13.47.188', 'port':19762, 'username':'mrbluesky', 'password':'kang12!@'}}
    return config['Database']

def connect():
    # Get config
    db_config = get_db_config()
    host = db_config['host']
    port = int(db_config['port'])
    username = db_config['username']
    password = db_config['password']
    # Make session
    # engine = create_engine('mysql+mysqldb://%s:%s@%s:%d/score_system' % (username, password, host, port), convert_unicode=True)
    engine = create_engine('mysql+mysqldb://mrbluesky:kang12!@@198.13.47.188:19762/MINICOMMERCE', convert_unicode=True)
    Session = sessionmaker(autocommit=False, bind=engine)
    db_session = Session()
    return db_session

def get_user_score(db_session, session_id, user_name):
    # Get user score from db
    user_score = db_session.query(UserScore).filter(UserScore.session_id==session_id).one_or_none()
    # UserScore.query.filter_by(sessiod_id=session_id, user_name=user_name).first()
    if user_score is None:
        return None
    return user_score.as_dict()