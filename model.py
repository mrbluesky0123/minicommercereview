from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

Base = declarative_base()

class Review(Base):
    __tablename__ = 'goods_review'
    
    goods_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    review_seq = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(String, primary_key=False)
    review_score = Column(Integer, primary_key=False)
    review_cmmnt = Column(String, primary_key=False)
    reg_dt = Column(DateTime, primary_key=False)
    regr_id = Column(String, primary_key=False)
    upd_dt = Column(DateTime, primary_key=False, nullable=True)
    updr_id = Column(String, primary_key=False, nullable=True)

    def __init__(self, goods_id, review_seq, user_id, review_score, review_cmmnt, reg_dt, regr_id, upd_dt, updr_id):
        self.goods_id = goods_id
        self.review_seq = review_seq
        self.user_id = user_id
        self.review_score = review_score
        self.review_cmmnt = review_cmmnt
        self.reg_dt = reg_dt
        self.regr_id = regr_id
        self.upd_dt = upd_dt
        self.updr_id = updr_id

    def __repr__(self):
        return 'goods_id: %d, review_seq: %d, user_id: %s, review_score: %d, review_cmmnt: %s, reg_dt: %s, regr_id: %s, upd_dt: %s, updr_id: %s'\
                   % (self.goods_id, self.review_seq, self.user_id, self.review_score, self.review_cmmnt, self.reg_dt, self.regr_id, self.upd_dt, self.updr_id)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}