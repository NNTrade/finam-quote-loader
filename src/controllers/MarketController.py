from flask_restx import Namespace, Resource, fields
from ..module.market_search import get_all_markets

market_controller_api = Namespace('market','Get market list')

@market_controller_api.route("")
class MarketController(Resource):

    @market_controller_api.response(200, 'List of markets', fields.List(fields.String))
    def get(self):
        return get_all_markets()
        