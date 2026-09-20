import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"

)
BOT_TOKEN = '8212759248:AAHmgxD6tmUUxBHg1gL7FJ-6ZzKb0hiVY2o'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
LINKS = {
    "schedule": "https://etu.ru/ru/studentam/raspisanie-zanyatiy",
    "lk": "https://edu.etu.ru",
    "library": "https://library.etu.ru",
    "mail": "https://mail.etu.ru",
    "news": "https://etu.ru/ru/novosti",
    "moodle": "https://vec.etu.ru/login/index.php",
    "leti_tech":"https://open.etu.ru"

}

# Текст главного меню (то, что отдаём на /start)
HELP_TEXT = (
    "🏠 <b>Главное меню</b>\n\n"
    "/schedule — 📅 Расписание\n"
    "/lk — 🎓 Личный кабинет\n"
    "/library — 📚 Библиотека\n"
    "/mail — 📧 Почта\n"
    "/news — 📢 Новости\n"
    "/moodle — 📖 Moodle\n"
    "/leti_tech — 🎓 LETIteach\n"
    "/help — ❓ Помощь\n"
    "/about — ℹ️ О боте"
)

@dp.message(CommandStart(deep_link=True, magic=F.args == "schedule"))
async def start_schedule(message: Message):
    await message.answer(f"📅 Расписание: {LINKS['schedule']}")

# ---------- Хэндлеры ----------

@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(HELP_TEXT, parse_mode="HTML")

@dp.message(Command("moodle"))
async def cmd_moodle(message: Message) -> None:
    await message.answer(f"📖 Moodle: {LINKS['moodle']}")

@dp.message(Command("leti_tech"))
async def cmd_leti_tech(message: Message) -> None:
    await message.answer(f"🎓 LETIteach: {LINKS['leti_tech']}")

@dp.message(Command("schedule"))
async def cmd_schedule(message: Message) -> None:
    await message.answer(f"📅 Расписание: {LINKS['schedule']}")


@dp.message(Command("lk"))
async def cmd_lk(message: Message) -> None:
    await message.answer(f"🎓 Личный кабинет: {LINKS['lk']}")


@dp.message(Command("library"))
async def cmd_library(message: Message) -> None:
    await message.answer(f"📚 Библиотека: {LINKS['library']}")


@dp.message(Command("mail"))
async def cmd_mail(message: Message) -> None:
    await message.answer(f"📧 Почта: {LINKS['mail']}")


@dp.message(Command("news"))
async def cmd_news(message: Message) -> None:
    await message.answer(f"📢 Новости: {LINKS['news']}")


@dp.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer("Тебе не нужна помощь, ты машина 🤖")


@dp.message(Command("about"))
async def cmd_about(message: Message) -> None:
    await message.answer("Это крутой бот для быстрого доступа к сайтам ЛЭТИ 🎓")


# Эхо-хэндлер — ОБЯЗАТЕЛЬНО последним!
@dp.message(F.text)
async def echo_handler(message: Message) -> None:
    await message.answer(f"Ошибка ввода, сообщение: {message.text} не обработано")


# ---------- Точка входа ----------
async def main() -> None:
    print("Starting bot...")
    try:
        await dp.start_polling(
        bot,
        polling_timeout=30,
        relax=0.1,
        timeout=30,
        backoff=1,
        skip_updates=False,
        )
    except KeyboardInterrupt:
        print("Bot stopped by user")
    except Exception as e:
        print(f"Bot crashed: {type(e).__name__}: {e}")
    finally:
        await bot.session.close()
        print("Bot session stopped")


if __name__ == "__main__":
    asyncio.run(main())

