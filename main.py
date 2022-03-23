import telebot
import all_currencies as cur

bot = telebot.TeleBot('5259299071:AAFXeWvd1jUgFjnmEq9oLe3-CusnYfx1NLk')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Какие курсы валют есть:\n\n 🇺🇸 USD 🇺🇿 UZS 🇷🇺 RUB 🇺🇦 UAH 🇨🇳 CNY 🇰🇷 KRW 🇰🇿 KZT', parse_mode='html')

@bot.message_handler(content_types=['text'])
def dollar_to_sum(message):
    id_ = message.chat.id
    text = (message.text).split()
    num = float(text[0])
    currency = text[1]
    if currency == 'доллар' or currency == 'долларов' or currency == 'баксов' or currency == 'бакс':
        bot.send_message(id_,
                         f'🇺🇸{num} USD \n\n 🇺🇿{num * cur.dollartosum: .2f} UZS \n 🇷🇺{num * cur.dollartoruble: .2f} RUB \n 🇺🇦{num * cur.dollartohryvnia} UAH \n 🇨🇳{num * cur.dollartoyuan: .2f} CNY \n 🇰🇷{num * cur.dollartowon: .2f} KRW \n 🇰🇿{num * cur.dollartotenge: .2f} KZT')
    elif currency == "сум" or currency == "сумов" or currency == "sum" or currency == "som" or currency == "сом":
        dollar = num * cur.sumtodollar
        bot.send_message(id_,
                         f'🇺🇿{num} UZS \n\n 🇺🇸{dollar: .2f} USD \n 🇷🇺{dollar * cur.dollartoruble: .2f} RUB \n 🇺🇦{dollar * cur.dollartohryvnia: .2f} UAH \n 🇨🇳{dollar * cur.dollartoyuan: .2f} CNY \n 🇰🇷{dollar * cur.dollartowon: .2f} KRW \n 🇰🇿{dollar * cur.dollartotenge: .2f} KZT')
    elif currency == 'грн' or currency == 'гривня' or currency == 'гривен' or currency == 'гривны':
        hryvnia = num * cur.hryvniatodollar
        bot.send_message(id_,
                         f'🇺🇦{num} UAH \n\n 🇺🇸{hryvnia: .2f} USD \n 🇷🇺{hryvnia * cur.dollartoruble: .2f} RUB \n 🇺🇿{hryvnia * cur.dollartosum: .2f} UZS \n 🇨🇳{hryvnia * cur.dollartoyuan: .2f} CNY \n 🇰🇷{hryvnia * cur.dollartowon: .2f} KRW \n 🇰🇿{hryvnia * cur.dollartotenge: .2f} KZT')
    elif currency == 'рубль' or currency == 'рублей' or currency == 'руб' or currency == 'рубля' or currency == 'ruble':
        ruble = num * cur.rubletodollar
        bot.send_message(id_,
                         f'🇷🇺{num} RUB \n\n 🇺🇸{ruble: .2f} USD \n 🇺🇦{ruble * cur.dollartohryvnia: .2f} UAH \n 🇺🇿{ruble * cur.dollartosum: .2f} UZS \n 🇨🇳{ruble * cur.dollartoyuan: .2f} CNY \n 🇰🇷{ruble * cur.dollartowon: .2f} KRW \n 🇰🇿{ruble * cur.dollartotenge: .2f} KZT')
    elif currency == 'тенге' or currency == 'tenge':
        tenge = num * cur.tengetodollar
        bot.send_message(id_,
                         f'🇰🇿{num} KZT \n\n 🇺🇸{tenge: .2f} USD \n 🇺🇦{tenge * cur.dollartohryvnia: .2f} UAH \n 🇺🇿{tenge * cur.dollartosum: .2f} UZS \n 🇨🇳{tenge * cur.dollartoyuan: .2f} CNY \n 🇰🇷{tenge * cur.dollartowon: .2f} KRW \n 🇷🇺{tenge * cur.dollartoruble: .2f} RUB')
    elif currency == 'юань' or currency == 'юани' or currency == 'юаней' or currency == 'сny' or currency == 'yuan':
        yuan = num * cur.yuantodollar
        bot.send_message(id_,
                         f'🇨🇳{num} CNY \n\n 🇺🇸{yuan: .2f} USD \n 🇺🇦{yuan * cur.dollartohryvnia: .2f} UAH \n 🇺🇿{yuan * cur.dollartosum: .2f} UZS \n 🇰🇿{yuan * cur.dollartoyuan: .2f} KZT \n 🇰🇷{yuan * cur.dollartowon: .2f} KRW \n 🇷🇺{yuan * cur.dollartoruble: .2f} RUB')
    elif currency == 'вон' or currency == 'вона' or currency == 'won' or currency == 'krw':
        won = num * cur.wontodollar
        bot.send_message(id_,
                         f'🇰🇷{num} KRW \n\n 🇺🇸{won: .2f} USD \n 🇺🇦{won * cur.dollartohryvnia: .2f} UAH \n 🇺🇿{won * cur.dollartosum: .2f} UZS \n 🇰🇿{won * cur.dollartoyuan: .2f} KZT \n 🇨🇳{won * cur.dollartowon: .2f} CNY \n 🇷🇺{won * cur.dollartoruble: .2f} RUB')


bot.infinity_polling()
