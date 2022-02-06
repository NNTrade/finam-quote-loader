from flask import Blueprint, Flask
from flask_restx import Namespace,Api, Resource, fields
from flask_restx import reqparse
from ..module.excepiton import ArgsException
from ..module.timeframe_search import get_all_timeframe

timeframe_controller = Blueprint('TimeFrame controller', __name__)
timeframe_controller_api = Namespace('TimeFrame controller', 'Get timeframe list' )

@timeframe_controller_api.route('/timeframe')
class TimeFrameController(Resource):

    @timeframe_controller_api.response(200, 'List of timeframes', fields.List(fields.String))
    def get(self):
        return get_all_timeframe()
        