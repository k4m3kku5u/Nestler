from datetime import datetime
from discord import Embed

def banEmbed():
    return Embed(
        title="Offense Report",
        color=0x000000,
        timestamp=datetime.utcnow(),
        type="rich"
    )

def kickEmbed():
    return Embed(
        title="Offense Report",
        color=0x000000,
        timestamp=datetime.utcnow(),
        type="rich"
    )

def pingEmbed():
    return Embed(
        title="Ping/Pong Procedure",
        description="Measures the latency of the active client.\n" + 
                    "────────────────────────\n" +
                    "client = Discord bot\n" +
                    "dapi = Discord API\n" +
                    "ms = Milliseconds\n" + 
                    "────────────────────────", 
        color=0x000000,
        timestamp=datetime.utcnow(),
        type="rich"
    )
