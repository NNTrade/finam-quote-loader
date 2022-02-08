import logging
from tkinter.messagebox import NO
from flask import Blueprint
from flask_restx import Namespace, Resource, fields
from flask_restx import reqparse
from ..module.stock_search import by_code
from ..module.excepiton import ArgsException
from finam.const import Market
from . import models
from ..module.quote_loader import load_quote
from finam.exception import FinamObjectNotFoundError
import datetime
from finam import Timeframe

quote_controller_api = Namespace('quote', 'Get quotes')

parser = reqparse.RequestParser()
parser.add_argument('idx', type=str, help='stock index', location='args')
parser.add_argument('market', type=str, help='market name', location='args')
parser.add_argument('code', type=str, help='stock code', location='args')
parser.add_argument(
    'from', type=str, help='date from (format: YYYY-MM-DD)', location='args')
parser.add_argument(
    'till', type=str, help='date till (format: YYYY-MM-DD)', location='args')
parser.add_argument('tf', type=str, help='timeframe', location='args')

quote = {"DateTime": fields.DateTime("iso8601"), "Open": fields.Float, "High": fields.Float,
         "Low": fields.Float, "Close": fields.Float, "Volume": fields.Float}
quoteModel = quote_controller_api.model('quote', quote)
errorModel = quote_controller_api.model('error', models.fieldError)

@quote_controller_api.route("")
class QuoteController(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.logger = logging.getLogger("QuoteController")

    @staticmethod
    def verify_args(**args):
        stock = args['code']
        market = args['market']
        date_from = args['from']
        date_till = args['till']
        timeframe = args['tf']
        idx = int(args["idx"]) if args["idx"] is not None else None
            
        if (stock is None and idx is None) or \
                date_from is None or \
                date_till is None or \
                timeframe is None or \
                market is None:
            ex = ArgsException()
            
            if stock is None and idx is None:
                ex.dic["code"] = "Code Or Idx must be filled"
            if market is None:
                ex.dic["market"] = "Market must be filled"
            if date_from is None:
                ex.dic["from"] = "From must be filled"
            if date_till is None:
                ex.dic["till"] = "Till must be filled"
            if timeframe is None:
                ex.dic["tf"] = "Tf (Timeframe) must be filled"
            raise ex

        ex = ArgsException()
        try:
            market_enum = Market[market]
        except Exception:
            ex.dic["market"] = "Cannot parse market value"

        try:
            tf_enum = Timeframe[timeframe]
        except Exception:
            ex.dic["tf"] = "Cannot parse tf (Timeframe) value"

        format = '%Y-%m-%d'

        try:
            dt = datetime.datetime.strptime(date_from, format)
            dt_from = dt.date()
        except Exception:
            ex.dic["from"] = "Cannot parse from date value"

        try:
            dt = datetime.datetime.strptime(date_till, format)
            dt_till = dt.date()
        except Exception:
            ex.dic["till"] = "Cannot parse till date value"

        try:
            if stock is not None:
                stock_idx, market = by_code(stock, market_enum)
                if idx is not None and stock_idx != idx:
                        ex.dic["code"] = "Code Idx != Idx"
            else:
                stock_idx = int(idx)
                market = market_enum
            
        except FinamObjectNotFoundError:
            ex.dic["code"] = "Cannot find record for code"
        except Exception:
            ex.dic["code"] = "Found more than 1 variant"

        if len(ex.dic) > 0:
            raise ex

        return stock_idx, market, dt_from, dt_till, tf_enum

    @quote_controller_api.response(200, 'List of quotes', [quoteModel])
    @quote_controller_api.response(400, "Wrong query parameters", [errorModel])
    @quote_controller_api.response(500, "Service error")
    @quote_controller_api.expect(parser)
    def get(self):
        try:
            stock_idx, market, dt_from, dt_till, tf_enum = QuoteController.verify_args(
                **parser.parse_args())
        except ArgsException as ex:
            return ex.to_output(), 400
        try:
            df = load_quote(stock_idx=stock_idx, market=market,
                            start_date=dt_from, end_date=dt_till, timeframe=tf_enum)
            return df.to_dict(orient="records")
        except Exception as ex:
            self.logger.exception("Unexpected exception")
            return "Get service error", 500
