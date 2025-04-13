
import time
import requests
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart


TOKEN = "7727672285:AAFwr3Ia1tUpQo79DEs2eCBzchOD75xTIjQ"
users_id = ["1397940161", "677261123", "810252597"]
bot = Bot(token=TOKEN)
dp = Dispatcher()

url1 = "https://www.fiit.stuba.sk/prijimacky/bakalari/skuska.html?page_id=5763"
url2 = "https://studuj.fiit.sk/page/prijimacky?fbclid=PAZXh0bgNhZW0CMTEAAaY9pyX4UrNVwOkaYOdtG9bv_q8FpVoJqQt32WsBaqD7LN-F6CAzx6ezRUs_aem_9zTP-QxULAqoDWvbj8AQsQ"


@dp.message(CommandStart())
async def begind():
    while True:
        original_html1 = requests.get(url1)
        html_code1 = original_html1.text
        original_html2 = requests.get(url2)
        html_code2 = original_html2.text

        time.sleep(900)

        new_original_html1 = requests.get(url1)
        new_html_code1 = new_original_html1.text
        new_original_html2 = requests.get(url2)
        new_html_code2 = new_original_html2.text


        for user_id in users_id:
            if len(html_code1) != len(new_html_code1):
                await bot.send_message(user_id, text=f"Мб шото помінялось на сайті: {url1}. {len(html_code1), len(new_html_code1)}")

            elif len(html_code2) != len(new_html_code2):
                await bot.send_message(user_id, text=f"Мб шото помінялось на сайті: {url2}. {len(html_code2), len(new_html_code2)}")

            else:
                continue
if __name__ == '__main__':
    asyncio.run(begind())