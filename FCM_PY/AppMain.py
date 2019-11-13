import os
from flask import Flask, request, jsonify
from flask_restful import reqparse, Api, abort, Resource
from pyfcm import FCMNotification

app = Flask(__name__)
parser = reqparse.RequestParser()
#API_KEY = "AAAAQY_TBCs:APA91bFUJAY07IJfPlj9Sn3u2FeczHWbBqnaN-sEWJVX9iTDaNQ9t2dbjNzWekb_m4uALn1C4B9DnTyuHF65D1yogw3VkOSwxiO5LnM83BP-i_YOiSQl_83L3WLbWDcc5hVc5dAdSk7a"
proxy_dict = {
          "http"  : "http://127.0.0.1",
          "https" : "http://127.0.0.1",
        }
        #, proxy_dict=proxy_dict
#registration_id = "dtTU9t-FzDM:APA91bGRUe2AGQF2P4MkaPcUTzvLDjjmzMK2refmirOYFTC9Es-_5bZ6wsnffZE-HegQb1Xy1KY9kEQ_AHyUSfwRClLBDx_5efmKTrr8-VEb6lBPCqLGnVcxlsvuPAsfreImNW90BIHl" 
@app.route('/fcm',methods=['POST'])
def firebase():
    parser.add_argument('server_key',type=str)
    parser.add_argument('fcm_token',type=str)
    parser.add_argument('title',type=str)
    parser.add_argument('body',type=str)
    args = parser.parse_args()
    try:
        API_KEY = format(args['server_key'])
        registration_id = format(args['fcm_token'])
        message_title = format(args['title'])
        message_body = format(args['body'])
        
        push_service = FCMNotification(api_key = API_KEY)
        #result = push_service.notify_single_device(registration_id=registration_id, message_body=message_body, message_title=message_title)
        dict1 = {
        "title":message_title,
        "body":message_body,
    }
        result = push_service.notify_single_device(registration_id=registration_id, data_message=dict1)
        return jsonify(dict1)
        print(result)
    except Exception as e:
        return jsonify({"error": f"An Error Occured:{e}"})
    

@app.route('/gcm',methods=['POST'])
def gcm():

    parser.add_argument('title',type=str)
    parser.add_argument('body',type=str)
    args = parser.parse_args()
    message_title = format(args['title'])
    message_body = format(args['body'])
    dict1 = {
        "title":message_title,
        "body":message_body,
    }
    return jsonify(dict1)    

if __name__ == "__main__":
    app.run()