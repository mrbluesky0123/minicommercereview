
import dbwork
import app

def get_goods_review_service(goods_id):
    # Log request
    print('Received request: ' + str(goods_id)) 
    db_session = dbwork.connect()
    reviews = dbwork.get_user_reviews(db_session, goods_id);
    
    dbwork.close(db_session)
    # Make response
    
    return reviews

def post_goods_review_service(request):
    db_session = dbwork.connect()
    result = dbwork.post_goods_review(db_session, request)
    dbwork.close(db_session)
    
    return result