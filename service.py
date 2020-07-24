
import dbwork
import app

def get_goods_review_service(goods_id):
    # Log request
    print('Received request: ' + str(goods_id)) 
    db_session = dbwork.connect()
    reviews = dbwork.get_user_reviews(db_session, goods_id);
    print(type(reviews[0]))
    dbwork.close(db_session)
    # Make response
    
    return snake_to_camel(reviews)

def post_goods_review_service(request):
    db_session = dbwork.connect()
    result = dbwork.post_goods_review(db_session, request)
    dbwork.close(db_session)
    
    return snake_to_camel(result)

def snake_to_camel(dict):
    keys = dict.keys()
    new_dict = {}
    for snake_cased_key in keys:
        # Convert into camel
        components = snake_cased_key.split('_')
        camel_cased_key = components[0] + ''.join(x.title() for x in components[1:])
        # Set new value to camel cased key
        new_dict[camel_cased_key] = dict[snake_cased_key]
    
    return new_dict