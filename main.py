import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command

# Импортируем наши клавиатуры
from buttons import (
    get_main_keyboard, 
    get_contact_keyboard, 
    get_inline_keyboard,
    get_category_keyboard
)

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Токен бота (лучше хранить в .env или config.py)
BOT_TOKEN = "7710478380:AAHviSn0y1Jg8tdEeKGg5DLxhKZT24w7TZ8"

# Создаем экземпляры бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Список категорий для примера
CATEGORIES = ["Электроника", "Одежда", "Книги", "Спорт", "Дом", "Детям"]

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    await message.answer(
        "👋 Добро пожаловать!\nВыберите действие:",
        reply_markup=get_main_keyboard()  # Используем клавиатуру из buttons.py
    )

@dp.message(F.text == "📋 Каталог")
async def show_catalog(message: types.Message):
    """Показываем категории товаров"""
    await message.answer(
        "Выберите категорию:",
        reply_markup=get_category_keyboard(CATEGORIES)  # Динамическая клавиатура
    )

@dp.message(F.text == "🛒 Корзина")
async def show_cart(message: types.Message):
    """Показываем корзину с inline-кнопками"""
    await message.answer(
        "🛒 Ваша корзина пуста\n\n"
        "Хотите посмотреть каталог?",
        reply_markup=get_inline_keyboard()  # Inline клавиатура
    )

@dp.message(F.text == "📞 Контакты")
async def show_contacts(message: types.Message):
    """Показываем контакты с возможностью отправить свой номер"""
    await message.answer(
        "📞 Наши контакты:\n"
        "Телефон: +7 (999) 123-45-67\n"
        "Email: info@example.com\n\n"
        "Или оставьте свой номер, и мы перезвоним:",
        reply_markup=get_contact_keyboard()  # Клавиатура с кнопкой отправки контакта
    )

@dp.message(F.text == "ℹ️ О нас")
async def about_us(message: types.Message):
    """Информация о компании"""
    await message.answer(
        "ℹ️ О нас:\n"
        "Мы - лучший магазин в мире!\n"
        "Работаем с 2023 года",
        reply_markup=get_main_keyboard()
    )

@dp.message(F.text == "↩️ Назад")
async def go_back(message: types.Message):
    """Возврат в главное меню"""
    await message.answer(
        "Главное меню:",
        reply_markup=get_main_keyboard()
    )

# Обработчики для inline-кнопок (callback_data)
@dp.callback_query(F.data == "confirm")
async def confirm_action(callback: types.CallbackQuery):
    await callback.message.answer("✅ Действие подтверждено!")
    await callback.answer()  # Закрываем "часики" на кнопке

@dp.callback_query(F.data == "cancel")
async def cancel_action(callback: types.CallbackQuery):
    await callback.message.answer("❌ Действие отменено")
    await callback.answer()

@dp.callback_query(F.data == "back")
async def back_action(callback: types.CallbackQuery):
    await callback.message.answer("Возврат в меню", reply_markup=get_main_keyboard())
    await callback.answer()

# Обработчик для категорий (динамические кнопки)
@dp.message(F.text.in_(CATEGORIES))
async def show_category_products(message: types.Message):
    """Показываем товары выбранной категории"""
    category = message.text
    await message.answer(
        f"Товары в категории '{category}':\n\n"
        f"Здесь будут товары категории {category}",
        reply_markup=get_main_keyboard()  # Возвращаем в главное меню
    )

# Обработчик для контакта
@dp.message(F.contact)
async def handle_contact(message: types.Message):
    """Обрабатываем полученный контакт"""
    contact = message.contact
    await message.answer(
        f"✅ Спасибо, {contact.first_name}!\n"
        f"Мы свяжемся с вами по номеру {contact.phone_number}",
        reply_markup=get_main_keyboard()
    )

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
