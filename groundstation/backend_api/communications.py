from flask import request
from flask import Blueprint
from flask_restful import Resource, Api
import datetime
import json

from groundstation.backend_api.models import Communications
from groundstation import db
from groundstation.backend_api.utils import create_context, dynamic_filters_communications

communications_blueprint = Blueprint('communications', __name__)
api = Api(communications_blueprint)

class Communication(Resource):

    @create_context
    def get(self, message_id):
        #given some id, fetch a message from the communications table

        response_object = {
            'status': 'fail',
            'message': 'message does not exist'
        }

        #get a single message via it's ID
        message = Communications.filter_by(id=message_id).first() #should only be one

        if not message: #query of Communications returned nothing
            return response_object, 404
        else: # there is a message in Communications with message_id
            response_object = {
                'status': 'success',
                'data': message.to_json()
            }

            return response_object, 200

class CommunicationList(Resource):
    @create_context
    def post(self, local_data=None):

        #JSON object expected
        # dict {
        # command : string of the form "COMMAND_NAME ARG1 ARG2 ... ARGN"
        # sender : string
        # receiver : string
        # }

        response_object = {
            'status': 'fail',
            'message': 'Invalid payload'
        }

        if not local_data:
            post_data = request.get_json()
        else:
            post_data = json.loads(local_data)
        post_data.update({'timestamp': datetime.datetime.now(datetime.timezone.utc)})


        #TODO: assertion checks for proper data types

        # message should look like:
        # dict {
        # command : string of the form "COMMAND_NAME ARG1 ARG2 ... ARGN" or a string with a response from the satellite
        # timestamp : autogenerated time for when function was called
        # sender : string
        # receiver : string
        # }
        message = Communications(**post_data)
        db.session.add(message)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': f'message {message.message} was sent!',
            'data': message.to_json()
        }

        return response_object, 201

    @create_context
    def get(self, local_data=None):

        # handle if this get is a local call or not
        # local_data will be a dictionary
        if not local_data:
            args = dynamic_filters_communications(request.args)
        else:
            args = dynamic_filters_communications(local_data)

        response_object = {
            'status': 'fail',
            'message': 'no available messages'
        }

        # order by ascending [min_id, min_id + 1, ..., max_id]
        message_list = Communications.query.filter(*args).order_by(Communications.id)

        if not message_list: # no messages for receiver
            response_object.update({'data':[]})
            return response_object, 200
        else: #message_list has multiple objects
            response_object = {
                'status': 'success',
                'data': {
                    'messages': [message.to_json() for message in message_list]
                }
            }
            return response_object, 200

api.add_resource(CommunicationList, '/api/communications')
api.add_resource(Communication, '/api/communications/<message_id>')
