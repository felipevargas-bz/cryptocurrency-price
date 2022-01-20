import websocket
import json
import time
import requests
from logging import getLogger

log = getLogger(__name__)
class Binance_websocket():

    def __init__(self,symbol):

        self.symbol = symbol.lower() # Convertir a minúsculas
        self.wss_url = "wss://stream.binance.com/stream?streams="

    def on_open(self,ws):
        print("on_open")# conexión exitosa

        data = {
            "method": "SUBSCRIBE",
            "params":
                [
                    "{}@kline_1m".format(self.symbol)
                ],
            "id": 1
        }
        ws.send(json.dumps(data)) # Enviar en formato json


    def on_close(self,ws):
        print("on_close") # conexión cerrada


    def on_error(self,ws, error):
        print("on_error") # error de conexión
        print(error) # devolver mensaje de error


    def on_message(self,ws, msg):
        msg = json.loads(msg)  # msg devuelve la cadena que se convertirá en formato json

        dict = {}
        if "data"in msg:
            dict = msg["data"]["k"]
            dict["name"] = dict.pop("s")
            log.info(f'Working properly, cryptocurrency name {dict["name"]}')

        if 'ping' in msg:
            ws.send(json.dumps({"pong": msg["ping"]})) # Recibir el ping enviado por la plataforma, devolver pong, de lo contrario se desconectará

        url = "http://docker_coin_1:8085/api/coin/"
        response = requests.post(url, json=dict) # Enviar los datos al servidor
        print(response)
        time.sleep(3) # Esperar 3 segundo

    def run(self):

        ws = websocket.WebSocketApp(self.wss_url,
                                    on_open=self.on_open,
                                    on_close=self.on_close,
                                    on_message=self.on_message,
                                    on_error=self.on_error)

        ws.run_forever(ping_interval=60)  # Enviar un paquete de latidos cada 15 segundos


ws  = Binance_websocket("BTCUSDT")
ws.run()
