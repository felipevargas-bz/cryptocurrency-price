import websocket
import json
import time
import requests


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

        # if 'data' in msg: # Debido a que la primera línea no son datos, excluya la impresión sin datos

        #     #conversión de marca de tiempo
        #     tupTime = time.localtime(msg['data']['E']/1000)
        #     otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
        #     msg['data']['E']=otherStyleTime


        # print(msg)



        if 'ping' in msg:
            ws.send(json.dumps({"pong": msg["ping"]})) # Recibir el ping enviado por la plataforma, devolver pong, de lo contrario se desconectará

        url = "http://docker_coin_1:8085/api/coin/"
        response = requests.post(url, json=json.dumps(msg["data"])) # Enviar los datos al servidor
        print(response)


    def run(self):

        ws = websocket.WebSocketApp(self.wss_url,
                                    on_open=self.on_open,
                                    on_close=self.on_close,
                                    on_message=self.on_message,
                                    on_error=self.on_error)

        ws.run_forever(ping_interval=60)  # Enviar un paquete de latidos cada 15 segundos




ws  = Binance_websocket("ETHUSDT")
ws.run()
