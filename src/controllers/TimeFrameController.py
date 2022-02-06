from flask import Blueprint
from flask_restx import Namespace, Resource, fields
from ..module.timeframe_search import get_all_timeframe

timeframe_controller_api = Namespace('timeframe', 'Get timeframe list' )

@timeframe_controller_api.route("")
class TimeFrameController(Resource):

    @timeframe_controller_api.response(200, 'List of timeframes', fields.List(fields.String))
    def get(self):
        return get_all_timeframe()
        