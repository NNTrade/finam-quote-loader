from flask import Flask, request
from .module.market_search import get_all_markets
from .module.timeframe_search import get_all_timeframe
from .module.stock_search import get_stock, parse_args as stock_parse_args
from .module.quote_loader import parse_args as quote_parse_args, load_quote
from .module.excepiton import ArgsException
import json

app = Flask(__name__)
          
@app.route("/timeframe")
def timeframe():
    return ";".join(get_all_timeframe())

@app.route('/markets')
def market():
    return ";".join(get_all_markets())

@app.route('/stock')
def stock():
    try:
        args = stock_parse_args(request.args)
    except ArgsException as ex:
        return ex.to_output(), 400
    df = get_stock(**args)   
    return str(json.loads(df.to_json(orient="records")))

@app.route('/quote')
def quote():
    try:
        args = quote_parse_args(request.args)
    except ArgsException as ex:
        return ex.to_output(), 400
    df = load_quote(**args)
    return str(json.loads(df.to_json(orient="records")))
    
@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(use_reloader=True, debug=False)