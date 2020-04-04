from settings import BOT_TOKEN, INFO
from covid.api import CovId19Data
import discord


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
            text = '''На дату {0}, во всем мире:
{1[confirmed]} заразившихся:sneezing_face:,
{1[recovered]} выздоровевших:sweat_smile:,
{1[deaths]} умерших.:skull_crossbones:'''.format(res['last_updated'][:10], res)
            await message.channel.send(text)
            # Выводи в чат статистику по миру

        elif message.content.startswith('Как там родина моя?') or message.content.startswith('$Russia'):
            api = CovId19Data(force=False)
            res = api.filter_by_country('Russia')
            text = '''На дату {0}, в Россие:
{1[confirmed]} заразившихся:sneezing_face:,
{1[recovered]} выздоровевших:sweat_smile:,
{1[deaths]} умерших.:skull_crossbones:'''.format(res['last_updated'][:10], res)
            await message.channel.send(text)
            # Выводи в чат статистику по России

        elif message.content.startswith('$country+'):
            api = CovId19Data(force=False)
            country = message[message.index('+') + 1:]
            try:
                res = api.filter_by_country()
            # Выводит статистику страны указанной после команды $country

    async def on_disconect(self):
        print('I\'m all')


client = MyClient()
client.run(BOT_TOKEN)
