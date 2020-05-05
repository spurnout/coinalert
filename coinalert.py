from bittrex import Bittrex
from twilio.rest import Client
import time

# twilio account info
account = "[twilio SID]"
token = "[token]"
client = Client(account, token)


#bittrex api key and secret
api = Bittrex("[api key]", "[api secret]")

def get_coin_value():
    while True:
        print api.get_marketsummary('BTC-XVG')
        response = api.get_marketsummary('BTC-XVG')
        #making last global below is probably useless since i moved the test_and_text into this function, might still want to separate in the future and keep last as a global variable though
        global last
        last = response['result'][0]['Last']
        print last
        # test to see if the price of BTC-SC has risen above 0.00000975
        if last >= 4.39e-06:
            print("XVG has hit target of 439, make your move! Coin value at: " + str(last))
            message = client.messages.create(to="+18186531589", from_="+18189753284",
                                    body="XVG has hit target, make your move!")
            message = client.messages.create(to="+18183902130", from_="+18189753284",
                                    body="XVG has hit target, make your move!")
            time.sleep(285)
        else:
            print("XVG has not hit target and is still at: " + str(last))
            #message = client.messages.create(to="+18186531589", from_="+18189753284",
            #                            body="Price equal to or lower than 0.00001000")
        time.sleep(15)

# test to see if the price of BTC-XLM has risen above 0.000010000

get_coin_value()
