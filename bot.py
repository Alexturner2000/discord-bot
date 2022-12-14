import discord
import responses

server_ip = 'localhost'


async def send_message(message, client_message, is_private):
    """Handles the message event."""
    try:
        response = responses.handle_response(client_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA1MTYyODkwMzI5NjQyMTk2OA.GFswDL.DlOBjMkG-9isw83AgT7DayaqhwbmzoNl8upS9U'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} sent a message in {channel}: {user_message}")

        if user_message == "!server":
            embed_me = discord.Embed(title=f"Minecraft Server : {server_ip}", url="http://sampleip:8123/",
                                     description="Vanilla minecraft 1.19.2 server, with dynamap plugin", color=0xFF5733)
            embed_me.set_thumbnail(url="https://imgur.com/SZMq61g.png")
            await message.channel.send(embed=embed_me)

    client.run(TOKEN)
