from sqlalchemy import create_engine, desc
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from datetime import datetime
from model import Review
from flask_sqlalchemy import SQLAlchemy
import app
# import MySQLdb
import sqlalchemy
import json

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

def get_user_reviews(db_session, goods_id):
    # Get user score from db
    user_reviews = db_session.query(Review).filter(Review.goods_id==goods_id).all()
    # UserScore.query.filter_by(sessiod_id=session_id, user_name=user_name).first()
    # print(type(user_reviews[0]))
    user_reviews_list = []

    if user_reviews is None:
        return None
    else:
        for review in user_reviews:
            review_json = review.as_dict()
            user_reviews_list.append(review_json)

    return user_reviews_list


def close(db_session):
    # Close session
    db_session.close()