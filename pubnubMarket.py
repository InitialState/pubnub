## www.pubnub.com - PubNub Real-time push service in the cloud.
# coding=utf8

## PubNub Real-time Push APIs and Notifications Framework
## Copyright (c) 2010 Stephen Blum
## http://www.pubnub.com/


import sys
## Import the Pubnub library
from Pubnub import Pubnub
## Import the Initial State Library
from ISStreamer.Streamer import Streamer

## Default publish key to 'demo' if no key given
publish_key = len(sys.argv) > 1 and sys.argv[1] or 'demo'
## Set subscribe key equal to the Market Orders Demo key
subscribe_key = 'sub-c-4377ab04-f100-11e3-bffd-02ee2ddab7fe'
## Default secret key to 'demo' if no key given
secret_key = len(sys.argv) > 3 and sys.argv[3] or 'demo'

## -----------------------------------------------------------------------
## Initiate Pubnub State
## -----------------------------------------------------------------------
pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,
                secret_key=secret_key)

channel = 'pubnub-market-orders'

## -----------------------------------------------------------------------
## Initiate Initial State Streamer
## -----------------------------------------------------------------------
streamer = Streamer(bucket_name="PubNub Market Orders", access_key="Your_Access_Key")


# Asynchronous usage
def callback(message, channel):
	## Stream bid price, trade type and order quantity
    streamer.log(str(message['symbol']) + " :moneybag:Bid Price (USD)",'%.4f' % message['bid_price'])
    streamer.log(str(message['symbol'])+" :bar_chart:Trade Type",str(message['trade_type']))
    streamer.log(str(message['symbol'])+" :hash:Order Quantity",str(message['order_quantity']))


def error(message):
    print("ERROR : " + str(message))


def connect(message):
    print("CONNECTED")


def reconnect(message):
    print("RECONNECTED")


def disconnect(message):
    print("DISCONNECTED")


## Subscribe to the Market Orders Demo channel
pubnub.subscribe(channels=channel, callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)

## Sleep 10 seconds between read/sends
import time
while True:
    time.sleep(10)
