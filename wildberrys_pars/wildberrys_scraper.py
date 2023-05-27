import json
import aiohttp


url = (
    'https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&'
    'curr=rub&dest=-1257786&page={}&query={}&regions=80,115,38,4,64,'
    '83,33,68,70,69,30,86,75,40,1,66,110,22,31,48,71,114&resultset='
    'catalog&sort=popular&spp=0&suppressSpellcheck=false'
)

headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/58.0.3029.110 Safari/537.3'
    ),
}


async def find_product_position(session: aiohttp.ClientSession,
                                item_name: str, item_art: int) -> str:

    page = 1
    while True:
        try:
            async with session.get(url.format(page, item_name),
                                   headers=headers) as response:
                data = await response.text()
                data = json.loads(data)

            for position,  product in enumerate(data['data']['products']):
                if product['id'] == item_art:
                    return (f"Страница {page}, место {position+1}, "
                            f"название - {product['name']}")

        except KeyError:
            return f'Артикул {item_art} по запросу "{item_name}" не найден'
        page += 1


async def get_product_position(item_name: str, item_art: int) -> str:

    async with aiohttp.ClientSession() as session:
        return await find_product_position(session, item_name, item_art)
