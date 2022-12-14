"""
Rest API for logic module

"""

import discord
import json
import requests

server_ip = 'localhost'


# MORE info located http://{server_ip}:4567/swagger#/'

# test
req_url_ping = f"http://{server_ip}:4567/v1/ping"
# name, version, onlinePlayers, health: uptime
req_url_server = f"http://{server_ip}:4567/v1/server"
# time, storm, thundering, difficulty, seed
req_url_worlds = f"http://{server_ip}:4567/v1/worlds"
# nothing
req_url_scoreboard = f"http://{server_ip}:4567/v1/scoreboard"
# displayName, location, health, hunger
req_url_players = f"http://{server_ip}:4567/v1/players"
# name
req_url_plugins = f"http://{server_ip}:4567/v1/plugins"


selector = req_url_server
get = requests.get(selector)

json_obj = json.dumps(get.json(), indent=4)

# print name value from json_obj
print(json_obj[0])
