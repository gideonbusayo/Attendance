from flask import Flask, redirect, render_template, request

# # Intriducing Binance TradeBot for MANA USDT pair

# import websocket, json, pprint, talib, numpy
# # from config import *
# from binance.client import Client
# from binance.enums import *

# gunicorn_logger = logging.getLogger('gunicorn.error')
# app.logger.handlers = gunicorn_logger.handlers
# app.logger.setLevel(gunicorn_logger.level)

# API_KEY = ''
# API_SECRET = ''


# SOCKET = "wss://stream.binance.com:9443/ws/manausdt@kline_1m"

# RSI_PERIOD = 14
# RSI_OVERBOUGHT = 70
# RSI_OVERSOLD = 30
# TRADE_SYMBOL = 'MANAUSDT'
# TRADE_QUANTITY = 500

# closes = []
# in_position = False

# client = Client(API_KEY, API_SECRET)

# def order(side, quantity, symbol,order_type=ORDER_TYPE_MARKET):
#     try:
#         print("sending order")
#         order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
#         print(order)
#     except Exception as e:
#         print("an exception ocurred - {}".format(e))
#         return False

#     return True

# attendances = []
# attendanced = []
   
# def on_open(ws):
#     print('opened connection')

# def on_close(ws):
#     print('closed connection')

# def on_message(ws, message):
#     global closes, in_position
    

#     app.logger.info('received message')
#     print('received message')
#     json_message = json.loads(message)
#     pprint.pprint(json_message)

#     candle = json_message['k']

#     is_candle_closed = candle['x']
#     close = candle['c']

#     if is_candle_closed:
#         print("candle closed at {}".format(close))
#         closes.append(float(close))
#         print("closes")
#         print(closes)

#         if len(closes) > RSI_PERIOD:
#             np_closes = numpy.array(closes)
#             rsi = talib.RSI(np_closes, RSI_PERIOD)
#             print("all rsis calculated so far")
#             app.logger.info(rsi)
            
#             print(rsi)
#             last_rsi = rsi[-1]
#             print("the current rsi is {}".format(last_rsi))

#             if last_rsi > RSI_OVERBOUGHT:
#                 if in_position:
#                     print("Overbought! Sell! Sell! Sell!")
#                     # put binance sell logic here
#                     order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
#                     attendances.append(close)
#                     if order_succeeded:
#                         in_position = False
#                 else:
#                     print("It is overbought, but we don't own any. Nothing to do.")
            
#             if last_rsi < RSI_OVERSOLD:
#                 if in_position:
#                     print("It is oversold, but you already own it, nothing to do.")
#                 else:
#                     print("Oversold! Buy! Buy! Buy!")
#                     # put binance buy order logic here
#                     order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
#                     attendanced.append(close)
#                     if order_succeeded:
#                         in_position = True

                
# ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
# ws.run_forever()


# # Front ENd section



app = Flask(__name__)

@app.route("/")
def attendance():
    #l = [attendances, attendanced]
    l = "Welcome"
    return render_template ("tasks.html", l=l)

