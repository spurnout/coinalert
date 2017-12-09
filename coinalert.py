import json
from bittrex import Bittrex
from twilio.rest import Client

account = "xxxxxxxxxx"
token = "xxxxxxxxxxxx"
client = Client(account, token)

api = Bittrex("xxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxx")

"""
print api.get_balance('XLM')
{'success': True, 
 'message': '',
 'result': {'Currency': 'XLM', 'Balance': 0.0, 'Available': 0.0, 
            'Pending': 0.0, 'CryptoAddress': None}
}
"""

print api.get_marketsummary('BTC-XLM')
response = api.get_marketsummary('BTC-XLM')
last = response['result'][0]['Last']
print last

# test to see if the price of BTC-XLM has risen above 0.000010000

if last >= 1.00e-05:
    print "great!"
    message = client.messages.create(to="+11234567890", from_="+11234567890",
                                 body="Price equal to or higher than 0.00001000")
else:
    print "bah!"
    message = client.messages.create(to="+11234567890", from_="+11234567890",
                                 body="Price equal to or lower than 0.00001000")
