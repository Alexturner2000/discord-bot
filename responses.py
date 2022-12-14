import json
import requests
import discord

server_ip = 'localhost'

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


def handle_response(message) -> str:
    """Handles the response to a user message."""

    if message == "/start":
        selector = req_url_server
        get = requests.get(selector)
        json_obj = json.dumps(get.json(), indent=4)
        return str(json_obj)
