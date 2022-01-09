from flask import Flask
from .module.market_search import get_all_markets
from .module.timeframe_search import get_all_timeframe
from .module.stock_search import get_stock
from .module.quote_loader import load_quote
from .module.excepiton import ArgsException
from flask_restx import Api, Resource, fields
from .controllers import quote
from .controllers import stock
from .controllers import models

app = Flask(__name__)
api: Api = Api(app, version='2.0', title='Sample API',
               description='A sample API')

stockModel = api.model('stock', models.stock)
quoteModel = api.model('quote', models.quote)
errorModel = api.model('error', models.fieldError)


@api.route('/timeframe')
class TimeframeController(Resource):

    @api.response(200, 'List of timeframes', fields.List(fields.String))
    def get(self):
        return get_all_timeframe()


@api.route('/market')
class MarketController(Resource):

    @api.response(200, 'List of markets', fields.List(fields.String))
    def get(self):
        return get_all_markets()


@api.route('/stock')
class StockController(Resource):

    @api.response(200, 'List of stocks', [stockModel])
    @api.response(400, "Wrong query parameters", [errorModel])
    @api.expect(stock.parser)
    def get(self):
        try:
            args = stock.verify_args(**stock.parser.parse_args())
        except ArgsException as ex:
            return ex.to_output(), 400
        df = get_stock(**args)
        return df.to_dict(orient="records")


@api.route('/quote')
class QuoteController(Resource):
    
    @api.response(200, 'List of quotes', [quoteModel])
    @api.response(400, "Wrong query parameters", [errorModel])
    @api.expect(quote.parser)
    def get(self):
        try:
            args = quote.verify_args(**quote.parser.parse_args())
        except ArgsException as ex:
            return ex.to_output(), 400
        df = load_quote(**args)
        return df.to_dict(orient="records")


if __name__ == "__main__":
    app.run()
