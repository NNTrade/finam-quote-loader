import logging
from flask import Blueprint
from flask_restx import Namespace,Resource, fields
from flask_restx import reqparse
from ..module.excepiton import ArgsException
from finam.const import Market
from ..module.stock_search import get_stock
from . import models

stock_controller = Blueprint('Stock controller', __name__)
stock_controller_api = Namespace('Stock controller','Get stock list in market')

parser = reqparse.RequestParser()
parser.add_argument('market', type=str, help='market name', location='args')
parser.add_argument('code', type=str, help='stock code', location='args')

stock = {"id" : fields.Integer, "code": fields.String, "name":fields.String, "market":fields.String}
stockModel = stock_controller_api.model('stock', stock)
errorModel = stock_controller_api.model('error', models.fieldError)

@stock_controller_api.route('/stock')
class StockController(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.logger = logging.getLogger("StockController")
        
    def verify_args(self, **args):
        market = args['market']
        code = args['code']
        args = {}
        
        ex = ArgsException()
        if market is not None:
            try:
                args["market"] = Market[market]  
            except Exception:
                ex.dic["tf"] = "Cannot parse tf (Timeframe) value"
            
        if code is not None:
            args["code"] = code
            
        if len(args) == 0:
            ex.dic["-"] = "Request must have market or code as query parameter"
        
        if len(ex.dic) > 0:
            raise ex

        return args

    @stock_controller_api.response(200, 'Id of task', [stockModel])
    @stock_controller_api.response(400, "Wrong query parameters", [errorModel])
    @stock_controller_api.response(500, "Service error")
    @stock_controller_api.expect(parser)
    def get(self):
        try:
            args = self.verify_args(**parser.parse_args())
        except ArgsException as ex:
            return ex.to_output(), 400
        
        try:
            df = get_stock(**args)
            return df.to_dict(orient="records")
        except Exception as ex:
            self.logger.exception("Unexpected exception")
            return "Get service error", 500