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
## Set subscribe key equal to the State Capital Weather Demo key
subscribe_key = 'sub-c-b1cadece-f0fa-11e3-928e-02ee2ddab7fe'
## Default secret key to 'demo' if no key given
secret_key = len(sys.argv) > 3 and sys.argv[3] or 'demo'

## -----------------------------------------------------------------------
## Initiate Pubnub State
## -----------------------------------------------------------------------
pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,
                secret_key=secret_key)

channel = 'pubnub-weather'

## -----------------------------------------------------------------------
## Initiate Initial State Streamer
## -----------------------------------------------------------------------
streamer = Streamer(bucket_name="PubNub Weather", access_key="Your_Access_Key")


# Asynchronous usage
def callback(message, channel):
	## Set the emoji icon based on weather condition
    icon = weather_icon(message['weather'])
    if icon == None:
    	icon = ":white_sun_rain_cloud:"
    ## Stream city temperature and weather conditions
    streamer.log(str(message['location'])+" Temperature (F)",str(message['temp_fahrenheit']))
    streamer.log(str(message['location'])+" Weather Conditions",str(icon) + " " + str(message['weather']))


def error(message):
    print("ERROR : " + str(message))


def connect(message):
    print("CONNECTED")


def reconnect(message):
    print("RECONNECTED")


def disconnect(message):
    print("DISCONNECTED")

## Key for weather condition -> emoji icon
def weather_icon(weather_conditions):
	icon = {
		"Clear"            : ":sun_with_face:",
		"Cloudy"           : ":cloud:",
		"Snow"         : ":snowflake:",
		"Fog"              : ":foggy:",
		"Hazy"             : ":foggy:",
		"Mostly Cloudy"     : ":cloud:",
		"Mostly Sunny"      : ":sun_with_face:",
		"Partly Cloudy"     : ":partly_sunny:",
		"Overcast"     : ":partly_sunny:",
		"Partly Sunny"      : ":partly_sunny:",
		"Scattered Clouds" : ":cloud:",
		"Sleet"            : ":sweat_drops: :snowflake:",
		"Rain"             : ":umbrella:",
		"Light Rain"       : ":cloud_rain:",
		"Snow"             : ":snowflake:",
		"Light Snow"             : ":snowflake:",
		"Light Freezing Rain" : ":cloud_snow:",
		"Ice Pellets"      : ":cloud_snow:",
		"Sunny"            : ":sun_with_face:",
		"Heavy Thunderstorms and Rain"          : ":thunder_cloud_rain:",
		"Thunderstorm"     : ":cloud_lightning:",
	}
	return icon.get(weather_conditions)

## Subscribe to the State Capital Weather Demo channel
pubnub.subscribe(channels=channel, callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)

## Sleep 10 seconds between read/sends
import time
while True:
    time.sleep(10)
