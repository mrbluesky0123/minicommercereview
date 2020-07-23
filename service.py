
import dbwork
import app



def get_goods_review(goods_id):
    # Log request
    print('Received request: ' + str(goods_id)) 
    db_session = dbwork.connect()
    reviews = dbwork.get_user_reviews(db_session, goods_id);
    
    dbwork.close(db_session)
    # Make response
    
    return reviews