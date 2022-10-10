import telebot
from telebot import types
import os


bot = telebot.TeleBot('5695529219:AAF1Lalc_XKY6zlEY4G-jalvLZWOnt5o6PM')


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Привет.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,
                     "Решил порыбачить, но не знаешь с чего начать? Напиши 'да' или 'нет'")

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        markup = types.InlineKeyboardMarkup()
        markup1 = types.InlineKeyboardMarkup()
        markup2 = types.InlineKeyboardMarkup()
        markup3 = types.InlineKeyboardMarkup()
        markup4 = types.InlineKeyboardMarkup()
        markup5 = types.InlineKeyboardMarkup()
        markup6 = types.InlineKeyboardMarkup()
        markup7 = types.InlineKeyboardMarkup()
        markup8 = types.InlineKeyboardMarkup()
        markup9 = types.InlineKeyboardMarkup()
        markup10 = types.InlineKeyboardMarkup()
        markup11 = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text='январь', callback_data='choice_1')
        item2 = types.InlineKeyboardButton(text='февраль', callback_data='choice_2')
        item3 = types.InlineKeyboardButton(text='март', callback_data='choice_3')
        item4 = types.InlineKeyboardButton(text='апрель', callback_data='choice_4')
        item5 = types.InlineKeyboardButton(text='май', callback_data='choice_5')
        item6 = types.InlineKeyboardButton(text='июнь', callback_data='choice_6')
        item7 = types.InlineKeyboardButton(text='июль', callback_data='choice_7')
        item8 = types.InlineKeyboardButton(text='август', callback_data='choice_8')
        item9 = types.InlineKeyboardButton(text='сентябрь', callback_data='choice_9')
        item10 = types.InlineKeyboardButton(text='октябрь', callback_data='choice_10')
        item11 = types.InlineKeyboardButton(text='ноябрь', callback_data='choice_11')
        item12 = types.InlineKeyboardButton(text='декабрь', callback_data='choice_12')
        item13 = types.InlineKeyboardButton(text='ШАГ 1', callback_data='choice_13')
        item14 = types.InlineKeyboardButton(text='ШАГ 2', callback_data='choice_14')
        item15 = types.InlineKeyboardButton(text='ШАГ 3', callback_data='choice_15')
        item16 = types.InlineKeyboardButton(text='ШАГ 4', callback_data='choice_16')
        item17 = types.InlineKeyboardButton(text='ШАГ 5', callback_data='choice_17')
        item18 = types.InlineKeyboardButton(text='ШАГ 6', callback_data='choice_18')
        item19 = types.InlineKeyboardButton(text='ШАГ 7', callback_data='choice_19')
        item20 = types.InlineKeyboardButton(text='ШАГ 8', callback_data='choice_20')
        item21 = types.InlineKeyboardButton(text='ШАГ 9', callback_data='choice_21')
        item22 = types.InlineKeyboardButton(text='ШАГ 10', callback_data='choice_22')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        markup1.add(item13)
        markup2.add(item14)
        markup3.add(item15)
        markup4.add(item16)
        markup5.add(item17)
        markup6.add(item18)
        markup7.add(item19)
        markup8.add(item20)
        markup9.add(item21)
        markup10.add(item22)
        if message.text == "да":
            bot.send_message(message.chat.id,
                             "Отлично! Я помогу тебе! Выбери месяц, в котором ты собираешься рыбачить",
                             reply_markup=markup)
        elif message.text == "нет":
            bot.send_message(message.chat.id,
                             "Извини, я помогаю рыболовам-новичкам. Напиши '/start', чтобы начать с начала или нам придется попрощаться.")
        elif message.text == "далее":
            bot.send_message(message.chat.id,
                             "Ну, что? Можно поздравить с первой пойманной рыбой? (Напиши один из ответов: 'пока нет', 'ура')")
        elif message.text == "пока нет":
                bot.send_message(message.chat.id, "Не огорчайся. Новичкам сложнее добиться успеха. Ты гарантированно прочувствуешь азарт добычи, продолжив трудиться. Кстати, не отчаивайся, если первый улов не впечатлит тебя размером. Через это проходил каждый рыбак. Удачи в дальнейшем и хорошего клёва!!! ПОКА!...")
                bot.send_sticker(message.chat.id, open('Пока.webp', 'rb'))
        elif message.text == "ура":
                bot.send_sticker(message.chat.id, open('Поздравляю.webp', 'rb'))
                bot.send_message(message.chat.id, "ПОЗДРАВЛЯЮ!!! Теперь ты настоящий рыбак! Не отчаивайся, если первый улов не впечатлит тебя размером. Через это проходил каждый рыбак. Удачи в дальнейшем и хорошего клева!!!")
        elif message.text == "продолжить":
            bot.send_message(message.chat.id,
                             "Шагай по кнопкам и ты узнаешь, как легко и просто поймать свою первую рыбу.",
                             reply_markup=markup1)
        else:
                sti_1 = open('Не_понимаю.webp', 'rb')
                bot.send_sticker(message.chat.id, sti_1)
                bot.send_message(message.chat.id,
                                 "Я помогаю рыболовам-новичкам. Напиши '/start', чтобы начать с начала или нам придется попрощаться.") \

        @ bot.callback_query_handler(func=lambda call: True)
        def callback(call):
            if call.message:
                if call.data == 'choice_1' or call.data == 'choice_2' or call.data == 'choice_12':
                    bot.send_message(call.message.chat.id,
                                     "Ты выбрал не самое лучшее время для новичка. Дождись весеннего тепла и возвращайся сюда! Если интересует зимняя (подледная) рыбалка, переходи по ссылке: https://lovlyavsem.ru/zimnyaya-rybalka")
                if call.data == 'choice_13':
                    bot.send_message(call.message.chat.id,
                                     "УДИЛИЩЕ. Для первых шагов рекомендую длину 4 м. Лучше выбирать не слишком дорогое телескопическое маховое удилище – простое в управлении и достаточно уловистое на первых порах. Простейшая оснастка таких удилищ легко дается даже ребенку, а транспортировка и хранение не вызовут проблем из-за складной конструкции.",
                                     reply_markup=markup2)
                if call.data == 'choice_14':
                    bot.send_message(call.message.chat.id,
                                     "СНАСТЬ. Для того, чтобы собрать снасть самостоятельно, вам понадобится леска диаметром 0,14-0,25 мм, поплавок 2-4 г, набор грузил, крючки 12-14 размера. Как вариант - готовая оснастка, которая полностью собрана, огружена и готова к ловле. Все это можно найти в ближайшем специализированном магазине.",
                                     reply_markup=markup3)
                if call.data == 'choice_15':
                    bot.send_message(call.message.chat.id,
                                     "ПРИМАНКА. Можно пробовать ловить на опарыша, красного червя, тесто, кукурузу – какая-нибудь рыба по-любому клюнет.",
                                     reply_markup=markup4)
                if call.data == 'choice_16':
                    bot.send_message(call.message.chat.id,
                                     "ВОДОЕМ. Для первых шагов в рыбалке подойдет любой водоем с небольшим течение или вовсе без него, с удобным подходом к берегу. Это может быть ближайший к твоему дому пруд. Поверь, там есть рыба!",
                                     reply_markup=markup5)
                if call.data == 'choice_17':
                    bot.send_message(call.message.chat.id,
                                     "ОСНАСТКА. Чтобы оснастить нашу удочку, возможно, придется попотеть. Верю, у тебя все получится. Держи несколько полезных зарисовок: ")
                    bot.send_photo(message.chat.id, open('крючки.jpg', 'rb'))
                    bot.send_photo(message.chat.id, open('петля.jpg', 'rb'))
                    bot.send_photo(message.chat.id, open('оснастка удилища.jpg', 'rb'))
                    bot.send_message(message.chat.id,
                                     "Примерно так должна выглядеть твоя снасть. Ну, что... Идем дальше!",
                                     reply_markup=markup6)
                if call.data == 'choice_18':
                    bot.send_message(call.message.chat.id,
                                     "НАЖИВКА. Насаживай выбранную наживку правильно, аккуратно продевая крючок, чтобы не повредить руки. Теперь нужно выставить глубину поплавка и сделать заброс. Передвигая поплавок вверх-вниз по леске. Забрасывая его в место лова, нужно добиться чтобы крючок с наживкой лежал на дне, а поплавок стоял в воде вертикально, погруженный по антенну - так называют продолжение тела поплавка в виде более тонкого стержня из разных материалов. Возможно придется добавить или убавить грузики-дробинки с лески.",
                                     reply_markup=markup7)
                if call.data == 'choice_19':
                    bot.send_message(call.message.chat.id,
                                     "СНАСТЬ ГОТОВА! Забрасывай наживку, аккуратно придерживая крючок свободной рукой. Плавно, но быстро подними удилище кончиком вверх, одновременно отпуская крючок и подавая снасть вперед. Такой заброс позволит очень точно положить поплавок в заданное место.",
                                     reply_markup=markup8)
                if call.data == 'choice_20':
                    bot.send_message(call.message.chat.id,
                                     "ПОКЛЕВКА. Ее придется подождать – это нормально. Наслаждайся природой, ее звуками и атмосферой рыбалки.")
                    bot.send_audio(message.chat.id, os.system('audio.mp3'))
                    bot.send_message(call.message.chat.id,
                                     "Не торопись отчаиваться. Рано или поздно поклевка обязательно произойдет. Обычно, если в течение 10-15 минут ничего не происходит, крючок с приманкой перезабрасывают в другое место. Контролируй наживку. Она всегда должна находиться на крючке.",
                                     reply_markup=markup9)
                if call.data == 'choice_21':
                    bot.send_message(call.message.chat.id,
                                     "РЕАКЦИЯ. От тебя потребуются максимум наблюдения и усидчивости в ожидании подходящего для подсечки момента. Когда он настанет? Это сможешь понять только ты. Реакция на поклевку не должна быть слишком резкой. Рыбалка не терпит суеты. Время выбора подсечки – один из увлекательнейших аспектов рыбалки, то что делает ее такой волнующей.",
                                     reply_markup=markup10)
                if call.data == 'choice_22':
                    bot.send_message(call.message.chat.id,
                                     "ПОДСЕЧКА. Дождался поклевки – подсекай (создай ситуацию, при которой поплавок будет двигаться в сторону, противоположную направлению взмаха удилища). В данном случае усилие быстрее предастся крючку, который сильнее вцепится рыбе в губу. Это должно быть хлесткое короткое движение, резкое, но мягкое. Силу и амплитуду подсечки ты выработаешь со временем. Здесь этому я тебя вряд ли научу... Для дальнейшего общения напиши 'далее'.")
                elif call.data == 'choice_3' or 'choice_4' or 'choice_5' or 'choice_6' or 'choice_7' or 'choice_8' or 'choice_9' or 'choice_10' or call.data == 'choice_11':
                    bot.send_message(call.message.chat.id,
                                     "Здорово! Напиши 'продолжить', если не передумал насчет рыбалки.")



bot.polling(none_stop=True, interval=0)