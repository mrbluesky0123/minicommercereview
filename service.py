
import dbwork
import app
import re

def get_goods_review_service(goods_id):
    # Log request
    print('Received request: ' + str(goods_id)) 
    db_session = dbwork.connect()
    reviews = dbwork.get_user_reviews(db_session, goods_id);
    print(type(reviews[0]))
    dbwork.close(db_session)
    
    # Make response to camel case
    new_list = []
    for review in reviews:
        camel_cased_review = snake_to_camel(review)
        new_list.append(camel_cased_review)
    
    return new_list

def post_goods_review_service(request):
    case_converted_request = camel_to_snake(request)
    print(case_converted_request)
    db_session = dbwork.connect()
    result = dbwork.post_goods_review(db_session, case_converted_request)
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

def camel_to_snake(dict)
    keys = dict.keys()
    new_dict = {}
    for camel_cased_key in keys:
        snake_cased_key = camel_cased_key[0].lower() + re.sub(r'(?!^)[A-Z]', lambda x: '_' + x.group(0).lower(), camel_cased_key[1:])
        new_dict[snake_cased_key] = dict[camel_cased_key]

    return new_dict