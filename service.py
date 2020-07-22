import rediscache
import configwork
import dbwork
from common import logger
import app
import uuid
import braodcasting



def get_goods_review(request):
    # Log request
    print('Received request: ' + str(request)) 
    db_session = dbwork.connect()
    reviews = db_session.get_user_score(goods_id);
    
    # If it is failed to send result...
    if send_result is False:
        logger.error('Failed to send result to redis.')
        logger.error('Need to be implemented.')
        response['response_code'] = '2201'
        response['response_msg'] = 'Fail to insert result'
        return response
    
    dbwork.close(db_session)
    # Make response
    response['response_code'] = '0000'
    response['response_msg'] = 'Success!'
    return response