import json
from bittrex import Bittrex
from twilio.rest import Client
import time, threading

# twilio account info
account = "xxxxxxxxxxx"
token = "xxxxxxxxxxxxxxxxxx"
client = Client(account, token)

#bittrex api key and secret
api = Bittrex("xxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxx")

""" # more example for me than anything
print api.get_balance('XLM')
{'success': True, 
 'message': '',
 'result': {'Currency': 'XLM', 'Balance': 0.0, 'Available': 0.0, 
            'Pending': 0.0, 'CryptoAddress': None}
}
"""

def get_coin_value():
    while True:
        print api.get_marketsummary('BTC-XLM')
        response = api.get_marketsummary('BTC-XLM')
        #making last global below is probably useless since i moved the test_and_text into this function, might still want to separate in the future and keep last as a global variable though
        global last
        last = response['result'][0]['Last']
        print last
        # test to see if the price of BTC-XLM has risen above 0.00000975
        if last >= 9.75e-06:
            print "great!"
            message = client.messages.create(to="+18181234567", from_="+18181234567",
                                    body="Price equal to or higher than 0.00000975")
            message = client.messages.create(to="+18181234567", from_="+18181234567",
                                    body="Price equal to or higher than 0.00000975")
            time.sleep(270)
        else:
            print "bah!"
            #message = client.messages.create(to="+18186531589", from_="+18189753284",
            #                            body="Price equal to or lower than 0.00001000")
        time.sleep(30)

# test to see if the price of BTC-XLM has risen above 0.000010000

def test_and_text():
    if last >= 9.75e-06:
        print "great!"
        message = client.messages.create(to="+18181234567", from_="+18181234567",
                                    body="Price equal to or higher than 0.00000975")
        message = client.messages.create(to="+18181234567", from_="+18181234567",
                                    body="Price equal to or higher than 0.00000975")
    else:
        print "bah!"
        #message = client.messages.create(to="+18186531589", from_="+18189753284",
        #                            body="Price equal to or lower than 0.00001000")
                                    
get_coin_value()
test_and_text()

