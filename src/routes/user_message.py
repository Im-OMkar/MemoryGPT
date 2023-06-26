from flask import Blueprint, jsonify, request, Flask

import json
from collections import namedtuple

route_gpt = Blueprint('route_gpt', __name__)
controller_gpt = Blueprint('controller_gpt', __name__)

from src.controller.gpt_controller import *


@controller_gpt.route('/memory/', methods=['POST'])
def message():
    data_obj = json.loads(json.dumps(request.json), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    answer = message_handler(data_obj)
    print("******", answer)
    return answer
