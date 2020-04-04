import discord
from settings import BOT_TOKEN, INFO


class MyClient(discord.Client):
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(client))

        '''
            Выводит в консоль сообщение при удачном присоединении и готовности работать,
        '''

    async def on_message(self, message: discord.Message):

        if message.content.startswith('$hello'):
            await message.channel.send('Hello {0.author.name}!'.format(message), tts=True)

        elif message.content.startswith('$help') or message.content.startswith('$info'):
            await message.channel.send(INFO)

            # Выводи в чат информацтю по работе с ботом

        elif message.content.startswith('шо_там в мире?') or message.content.startswith('$world'):
            pass
            # Выводи в чат статистику по миру

        elif message.content.startswith('Как там родиная моя?') or message.content.startswith('$Russia'):
            pass
            # Выводи в чат статистику по России

        elif message.content.startswith('$country'):
            pass
            # Выводит статистику страны указанной после команды $country

    async def on_disconect(self):
        pass
        '''
            Прощается с чатом, и предупреждает от здоровье.
        '''


client = MyClient()
client.run(BOT_TOKEN)
