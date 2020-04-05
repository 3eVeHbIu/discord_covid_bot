from settings import BOT_TOKEN, INFO
from covid.api import CovId19Data
from country import table
import discord


def get_text(stats, text):
    return '''На дату {0}, {1}:
{2[confirmed]} заразившихся:sneezing_face:,
{2[recovered]} выздоровевших:sweat_smile:,
{2[deaths]} умерших.:skull_crossbones:
Последние обновление информации производилось в {3}'''.format(stats['last_updated'][:10], text, stats, stats['last_updated'][10:])


class MyClient(discord.Client):
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(client))
        # Выводит в консоль сообщение при удачном присоединении и готовности работать,

    async def on_message(self, message: discord.Message):

        if message.content.startswith('$hello'):
            await message.channel.send('Hello {0.author.name}!'.format(message), tts=True)

        elif message.content.startswith('$help') or message.content.startswith('$info'):
            await message.channel.send(INFO)
            # Выводи в чат информацию по работе с ботом

        elif message.content.startswith('шо там в мире?') or message.content.startswith('$world'):
            api = CovId19Data(force=False)
            res = api.get_stats()
            await message.channel.send(get_text(res, 'во всем мире'))
            # Выводи в чат статистику по миру

        elif message.content.startswith('Как там родина моя?') or message.content.startswith('$russia'):
            api = CovId19Data(force=False)
            res = api.filter_by_country('Russia')
            await message.channel.send(get_text(res, 'в России'))
            # Выводи в чат статистику по России

        elif message.content.startswith('$country'):
            api = CovId19Data(force=False)
            country = message.content[9:].lower()
            available = api.show_available_countries()
            flag = True
            for collection in table:
                if country in map(lambda i: i.lower(), collection):
                    for item in collection:
                        if item in available:
                            res = api.filter_by_country(item)
                            flag = False
                            await message.channel.send(get_text(res, 'в стране - {}'.format(collection[0])))
                            break
                    break
            if flag:
                await message.channel.send('К сожалению такой страны нет в базе данных')
            # Выводит статистику страны указанной после команды $country

    async def on_disconect(self):
        print('I\'m all')


client = MyClient()
client.run(BOT_TOKEN)
