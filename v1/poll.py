import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
import sqlite3
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

# API_TOKEN = '6481378248:AAGkYAhaI1sixVXUBvoxj5a3p_5uWMxDt0w'
API_TOKEN = '6603890448:AAG1tIrvcZr9VAjEbv7mRRBNYFEGbztVYzQ'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

channel_link = "@basmala_bilim"

# admin = 1152912629
admin = 6036909801

admin_qosh = {
    'school': -1,
    'status': False
    
}
admin_ayr = {
    'school': -1,
    'status': False
    
}
admin_text = {
    'school': -1,
    'status': False
    
}

def is_admin(id):
    return admin == id



# 1532 : {
#         "status" : 0,
#     }

user = {
    
}

def create_inline_button(m):
    if isinstance(m, list):
        inline_keyboard = types.InlineKeyboardMarkup()
        for item in m:
            inline_button = types.InlineKeyboardButton(item['text'], callback_data=item['callback_data'] )
            inline_keyboard.add(inline_button)

        return inline_keyboard
    else:
        
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton(m['text'], callback_data=m['callback_data'])
        inline_keyboard.add(inline_button)
        return inline_keyboard

like = {
    
}

school_list =[
    '1-maktab',
    '3-maktab',
    '4-maktab',
    '5-maktab',
    '6-maktab',
    '7-maktab',
    '8-maktab',
    '9-maktab',
    '10-maktab',
    '11-maktab',
    '12-maktab',
    '13-maktab',
    '14-maktab',
    '15-maktab',
    '16-maktab',
    '17-maktab',
    '18-maktab',
    '19-maktab',
    '20-maktab',
    '21-maktab',
    '22-maktab',
    '23-maktab',
    '24-maktab',
    '25-maktab',
    '26-maktab',
    '27-maktab',
    '28-maktab',
    '29-maktab',
    '30-maktab',
    '21-maktab',
    '32-maktab',
    '34-maktab',
    '36-maktab',
    '37-maktab',
    '38-maktab',
    '40-maktab',
    '41-maktab',
    '43-maktab',
    '44-maktab',
    '45-maktab',
    '46-maktab','47-maktab','50-maktab','51-maktab','66-maktab','67-maktab','74-maktab','75-maktab','76-maktab','85-maktab','88-maktab','1-DIMI','40-INT',]

# def get_school_inline_button():
#     inline_keyboard = types.InlineKeyboardMarkup()
#     for item in school_list:
#         if school_list.index(item) != 0 and school_list.index(item) % 3 == 0:
#             inline_keyboard.add(m)
#             m = []
            
#         inline_button = types.InlineKeyboardButton(text=item, callback_data=item )
#         # inline_keyboard.add(inline_button)
#         try:
#             m.append(inline_button)
#         except:
#             m = []
#             m.append(inline_button)
            
#     return inline_keyboard

def get_school_inline_button(school_list):
    # Bir qator (row) uchun 3 ta tugma
    buttons_per_row = 3

    # Keyboard yaratish
    keyboard = InlineKeyboardMarkup()

    # school_list ro'yxatini 3 ta elementga bo'lib olib, InlineKeyboardButton qo'shamiz
    for i in range(0, len(school_list), buttons_per_row):
        row_buttons = school_list[i:i+buttons_per_row]  # 3 ta element olib olamiz
        buttons = [InlineKeyboardButton(text=school, callback_data=school) for school in row_buttons]
        keyboard.row(*buttons)

    return keyboard
def get_statis():
    # text = ""
    # for key, value in like.items():
    #     text+=f"{school_list[key]} => {value}-ta ovoz yig`di\n" 
    # return text
    conn = sqlite3.connect("likelist.db")
    cursor = conn.cursor()

    # Barcha ma'lumotlarni o'qish
    cursor.execute("SELECT school, count FROM like")
    results = cursor.fetchall()

    # Ma'lumotlarni string ko'rinishida yig'ish
    school_count_text = []
    for result in results:
        school, count = result
        school_count_text.append(f"{school_list[school]} => {count} ta ovoz yig`di\n")

    # Ma'lumotlar bazasini yopish
    conn.close()

    # Ma'lumotlarni qaytarish
    return "".join(school_count_text)

def add_user_to_list(number):
    # Ma'lumotlar bazasiga ulanish
    conn = sqlite3.connect("likelist.db")
    cursor = conn.cursor()

    # Yangi foydalanuvchini jadvalga qo'shish
    cursor.execute("INSERT INTO user_list (number) VALUES (?)", (number,))
    conn.commit()

    # Ma'lumotlar bazasini yopish
    conn.close()

def ovoz_qosh(school, count):
    # if like.get(a):
    #     like[a] += b
    # else:
    #     like[a] = b
    conn = sqlite3.connect("likelist.db")
    cursor = conn.cursor()

    # Ma'lumotlarni o'qish
    cursor.execute("SELECT school, count FROM like WHERE school=?", (school,))
    result = cursor.fetchone()

    if result is not None:
        # Ma'lumot mavjud, uning count'ini yangilash
        existing_count = result[1]
        new_count = existing_count + count
        cursor.execute("UPDATE like SET count=? WHERE school=?", (new_count, school))
    else:
        # Ma'lumot mavjud emas, yangi ma'lumotni qo'shish
        cursor.execute("INSERT INTO like (school, count) VALUES (?, ?)", (school, count))

    conn.commit()

    # Ma'lumotlar bazasini yopish
    conn.close()    

def check_user_in_list(number):
    # Ma'lumotlar bazasiga ulanish
    conn = sqlite3.connect("likelist.db")
    cursor = conn.cursor()

    # Foydalanuvchi raqamini jadvalda qidirish
    cursor.execute("SELECT EXISTS (SELECT 1 FROM user_list WHERE number=?)", (number,))
    result = cursor.fetchone()

    # Ma'lumotlar bazasini yopish
    conn.close()

    # Natijani tekshirish va qaytarish
    return  result and result[0]
    #     return True
    # else:
    #     return False

def get_all_user_numbers():
    # Ma'lumotlar bazasiga ulanish
    conn = sqlite3.connect("likelist.db")
    cursor = conn.cursor()

    # Barcha "number" larni o'qish
    cursor.execute("SELECT number FROM user_list")
    results = cursor.fetchall()

    # Ma'lumotlar bazasini yopish
    conn.close()

    # "number" larni listga qo'shish
    user_numbers = [result[0] for result in results]
    
    return user_numbers

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    print(message)
    # user.append(message.from_user.id)
    await message.answer("Assalomu aleykum")
    global channel_link
    user_id = message.from_user.id
    member = await bot.get_chat_member(channel_link, user_id)
    if member.status in ["member", "administrator", "creator"]:
        if is_admin(user_id):
            button = types.KeyboardButton("Statistika")
            send_message = types.KeyboardButton("Xabar jo`natish")
            ovoz_qoshish = types.KeyboardButton("Ovoz qo`shish")
            ovoz_ayrish = types.KeyboardButton("Ovoz ayrish")
            # change_admin = types.KeyboardButton("Adminlikga bo")
            
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button, send_message)
            keyboard.add(ovoz_qoshish, ovoz_ayrish)
            await message.answer("Xush kelibsiz!", reply_markup = keyboard)
        else:
            if check_user_in_list(user_id):
                button = types.KeyboardButton("Statistika")
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button)
                await message.answer("Siz ovoz berish jarayonida qatnashgansiz", reply_markup=keyboard)
            else:
                inline_button = get_school_inline_button(school_list)
                await message.answer("Quyidagi maktablardan biriga ovoz bering", reply_markup = inline_button)
    else:
        inline_button = types.InlineKeyboardMarkup()
        
        channel = f"https://t.me/{channel_link[1:]}"  # Removing '@' from the username
        channel_button = types.InlineKeyboardButton(text="Kanalga azo bo`lish", url=channel)
        tasdiqlash = types.InlineKeyboardButton(text = "Tasdiqlash", callback_data = "tasdiqlash")
        inline_button.add(channel_button)
        inline_button.add(tasdiqlash)
        

        await message.answer("Botimizdan foydalanish uchun telegram kanalimizga obuna bo`lishingiz kerak", reply_markup = inline_button)


@dp.callback_query_handler(lambda c: c.data == "tasdiqlash")
async def process_hello_button(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Kanalimizga azo bo`lganiz uchun tashakkur")
    global channel_link
    user_id = callback_query.from_user.id
    member = await bot.get_chat_member(channel_link, user_id)
    if member.status in ["member", "administrator", "creator"]:
        if is_admin(user_id):
            button = types.KeyboardButton("Statistika")
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button)
            await callback_query.message.answer("Xush kelibsiz!", reply_markup = keyboard)
        else:
            if check_user_in_list(user_id):
                button = types.KeyboardButton("Statistika")
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button)
                await callback_query.message.answer("Siz ovoz berish jarayonida qatnashgansiz", reply_markup=keyboard)
            else:
                inline_button = get_school_inline_button(school_list)
                await callback_query.message.answer("Quyidagi maktablardan biriga ovoz bering", reply_markup = inline_button)
    else:
        inline_button = types.InlineKeyboardMarkup()
        
        channel = f"https://t.me/{channel_link[1:]}"  # Removing '@' from the username
        channel_button = types.InlineKeyboardButton(text="Kanalga azo bo`lish", url=channel)
        tasdiqlash = types.InlineKeyboardButton(text = "Tasdiqlash", callback_data = "tasdiqlash")
        inline_button.add(channel_button)
        inline_button.add(tasdiqlash)
        

        await callback_query.message.answer("Botimizdan foydalanish uchun telegram kanalimizga obuna bo`lishingiz kerak", reply_markup = inline_button)



@dp.callback_query_handler(lambda c: c.message.text == "Quyidagi maktablardan biriga ovoz bering")
async def process_hello_button(callback_query: types.CallbackQuery):
    member = await bot.get_chat_member(channel_link, callback_query.from_user.id)
    if member.status in ["member", "administrator", "creator"]:
        if check_user_in_list(callback_query.from_user.id):
            await callback_query.message.answer("Siz ovoz berish jarayonida qatnashgansiz")
        else:  
            add_user_to_list(callback_query.from_user.id)
            ovoz_qosh(school_list.index(callback_query.data), 1)
            button = types.KeyboardButton("Statistika")
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button)
            await callback_query.message.answer(f"Tabriklayman {callback_query.data}ga muvaffaqiyatli ovoz berdingiz", reply_markup = keyboard)
    else:
        inline_button = types.InlineKeyboardMarkup()
        
        channel = f"https://t.me/{channel_link[1:]}"  # Removing '@' from the username
        channel_button = types.InlineKeyboardButton(text="Kanalga azo bo`lish", url=channel)
        tasdiqlash = types.InlineKeyboardButton(text = "Tasdiqlash", callback_data = "tasdiqlash")
        inline_button.add(channel_button)
        inline_button.add(tasdiqlash)

        await callback_query.message.answer("Botimizdan foydalanish uchun telegram kanalimizga obuna bo`lishingiz kerak", reply_markup = inline_button)

@dp.message_handler(lambda m: m.text == "Statistika")
async def statustika(message: types.Message):
    a = get_statis()    
    if a:
        await message.answer(a)
    else:
        await message.answer("Hozircha hechkim ovoz yig`madi")
        
@dp.message_handler(lambda m: m.text == "Xabar jo`natish" and is_admin(m.from_user.id))
async def statustika(message: types.Message):
    admin_text['status'] = True
    await message.answer("Yubormoqchi bo`lgan matningizni yuboring")

@dp.message_handler(lambda m: admin_text['status'] and is_admin(m.from_user.id))
async def statustika(message: types.Message):
    for user1 in get_all_user_numbers():
        if user1 != admin:
            await bot.send_message(chat_id = user1, text = message.text)
    await message.answer("Xabar muvaffaqiyatli hammaga yuborildi")
    admin_text['status'] = False
@dp.message_handler(lambda m: m.text == "Ovoz qo`shish" and is_admin(m.from_user.id))
async def statustika(message: types.Message):
    await message.answer("Ovoz qo`shmoqchi bo`lgan maktabingizni tanlang", reply_markup = get_school_inline_button(school_list))


@dp.message_handler(lambda m: admin_qosh['status'] and is_admin(m.from_user.id))
async def statustika(message: types.Message):
    try:
        ovoz_qosh(admin_qosh['school'], int(message.text))
        await message.answer(f"Muvaffaqiyatli ravishda {school_list[admin_qosh['school']]}ga {message.text} ta ovoz qo`shildi")
        admin_qosh['status'] = False
    except:
        await message.answer("Faqat raqamni o`zini yuboring iltimos")

@dp.message_handler(lambda m: m.text == "Ovoz ayrish" and is_admin(m.from_user.id))
async def statustika(message: types.Message):
    await message.answer("Ovoz ayrmoqchi bo`lgan maktabingizni tanlang", reply_markup = get_school_inline_button(school_list))


@dp.message_handler(lambda m: admin_ayr['status'] and is_admin(m.from_user.id))
async def statustika(message: types.Message):
    try:
        n = int(message.text)
        n = (-1) * n
        ovoz_qosh(admin_ayr['school'], n )
        await message.answer(f"Muvaffaqiyatli ravishda {school_list[admin_qosh['school']]}dan {message.text} ta ovoz ayrildi")
        admin_ayr['status'] = False
    except:
        await message.answer("Faqat raqamni o`zini yuboring iltimos")


@dp.callback_query_handler(lambda c: c.message.text == "Ovoz ayrmoqchi bo`lgan maktabingizni tanlang")
async def process_hello_button(callback_query: types.CallbackQuery):
    admin_ayr['status'] = True
    admin_ayr['school'] = school_list.index(callback_query.data)
    await callback_query.message.answer("Nechta ovoz ayrmoqchisiz yozib yuboring")
    

@dp.callback_query_handler(lambda c: c.message.text == "Ovoz qo`shmoqchi bo`lgan maktabingizni tanlang")
async def process_hello_button(callback_query: types.CallbackQuery):
    admin_qosh['status'] = True
    admin_qosh['school'] = school_list.index(callback_query.data)
    await callback_query.message.answer("Nechta ovoz qo`shmoqchiligizni yozib yuboring")
    



            # send_message = types.KeyboardButton("Xabar jo`natish")
            # ovoz_qoshish = types.KeyboardButton("Ovoz qo`shish")
            # ovoz_ayrish = types.KeyboardButton("Ovoz ayrish")
            
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=False)
