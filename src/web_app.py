from flask import Flask
from flask_restx import Api
from .controllers.TimeFrameController import timeframe_controller_api
from .controllers.MarketController import market_controller_api
from .controllers.StockController import stock_controller_api
from .controllers.QuoteController import quote_controller_api


app = Flask(__name__)
api: Api = Api(app, version='2.0', title='Correlation calculator service',
               description='Service load stock data from Finam')

#app.register_blueprint(timeframe_controller)
api.add_namespace(timeframe_controller_api)

#app.register_blueprint(market_controller)
api.add_namespace(market_controller_api)

#app.register_blueprint(stock_controller)
api.add_namespace(stock_controller_api)

#app.register_blueprint(quote_controller)
api.add_namespace(quote_controller_api)

if __name__ == "__main__":
    app.run()