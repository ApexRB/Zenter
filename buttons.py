from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# ===== Простые Reply-кнопки (обычная клавиатура) =====
def get_main_keyboard():
    """Главная клавиатура с основными кнопками"""
    buttons = [
        [KeyboardButton(text="📋 Каталог"), KeyboardButton(text="🛒 Корзина")],
        [KeyboardButton(text="ℹ️ О нас"), KeyboardButton(text="📞 Контакты")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,  # Автоматически подгонять размер
        input_field_placeholder="Выберите действие"
    )

def get_contact_keyboard():
    """Клавиатура для отправки контакта"""
    buttons = [
        [KeyboardButton(text="📱 Отправить номер", request_contact=True)],
        [KeyboardButton(text="↩️ Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# ===== Inline-кнопки (кнопки под сообщением) =====
def get_inline_keyboard():
    """Inline клавиатура с ссылками и callback-кнопками"""
    builder = InlineKeyboardBuilder()
    
    # Кнопка с ссылкой
    builder.row(InlineKeyboardButton(
        text="🔗 Перейти на сайт",
        url="https://example.com"
    ))
    
    # Кнопки с callback_data (для обработки в хендлерах)
    builder.row(
        InlineKeyboardButton(text="✅ Подтвердить", callback_data="confirm"),
        InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")
    )
    
    # Кнопка "Назад" отдельно
    builder.row(InlineKeyboardButton(text="↩️ Назад", callback_data="back"))
    
    return builder.as_markup()

# ===== Клавиатуры с динамическим созданием =====
def get_category_keyboard(categories: list):
    """Создает клавиатуру с категориями из списка"""
    builder = ReplyKeyboardBuilder()
    for category in categories:
        builder.button(text=category)
    
    # Добавляем кнопку "Назад" и располагаем по 2 кнопки в ряд
    builder.button(text="↩️ Назад")
    builder.adjust(2)  # По 2 кнопки в ряд
    
    return builder.as_markup(resize_keyboard=True)
