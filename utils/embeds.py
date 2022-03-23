from discord import Embed

def banEmbed():
    return Embed(
        title="",
        description="",
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
