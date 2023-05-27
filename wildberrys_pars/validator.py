import json
import aiohttp

url = (
    "https://card.wb.ru/cards/detail?appType=1&curr=rub&dest=-1257786&"
    "regions=80,115,38,4,64,83,33,68,70,69,30,86,75,40,1,66,110,22,31,"
    "48,71,114&spp=0&nm={}"
    )


async def is_valid_article(item_art: str) -> bool:

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url.format(int(item_art))) as response:
                data = await response.text()
                data = json.loads(data)
                return bool(data["data"]["products"])
    except ValueError:
        return False
