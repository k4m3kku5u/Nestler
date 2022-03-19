from discord import Embed

def banEmbed(title: str, desc: str, clr: hex, time: int) -> Embed:
    return Embed(
        title = title,
        description = desc,
        color = clr,
        timestamp = time
    )

def kickEmbed(title: str, desc: str, clr: hex, time: int) -> Embed:
    return Embed(
        title = title,
        description = desc,
        color = clr,
        timestamp = time
    )

def pingEmbed(title: str, desc: str, clr: hex, time: int) -> Embed:
    return Embed(
        title = title,
        description = desc,
        color = clr,
        timestamp = time
    )
