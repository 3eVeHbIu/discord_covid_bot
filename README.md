# Бот для Discord выводящий статистику вируса COVID19 #

## Содержание ##

* [Создание discord бота](#creature)
* [Функционал](#function)
* [Зависимости](#addictions)
* [Настройка](#settings)


<h2 id='creature'> Создание бота в Discord </h2>

Для создания бота перейдите по [ссылке](https://discordapp.com/developers/applications). Далее необходимо нажать на **New Application**, и указать имя нашего приложения.

![/images/1.png](https://raw.githubusercontent.com/sergo2048/discord_covid_bot/master/images/create.png)

Создав приложение, необходимо создать самого *бота*. Для этого переходим в раздел **bot**, указываем имя бота, а также, ниже, выбираем его *права*.

![/images/1.png](https://raw.githubusercontent.com/sergo2048/discord_covid_bot/master/images/bot_creation.png)

По сути бот готов. Копируем его **TOKEN** и сохраняем в отдельный файл (у меня это *settings.py* ~~тут показывать не буду~~). Потом мы будем импортировать этот *токен* в основную программу для подключения.

Теперь осталось добавить бота на наш канал. Для этого переходим на вкладку OAuth2, ставим галочку, где bot, а также выбираем его возможности (это, кстати, очень важно).

> **НЕ ДАВАЙТЕ БОТУ БОЛЬШЕ ПРАВ ЧЕМ ТРЕБУЕТ ЕГО ФУНКЦИОНАЛ**

![/images/1.png](https://raw.githubusercontent.com/sergo2048/discord_covid_bot/master/images/add.png)
![/images/1.png](https://raw.githubusercontent.com/sergo2048/discord_covid_bot/master/images/permission.png)

После всего этого просто копируем сгенерированную ссылку, переходим по ней и выбираем канал, на который мы хоти добавить бота.

![/images/1.png](https://raw.githubusercontent.com/sergo2048/discord_covid_bot/master/images/conected.png)

Если вы все сделали правильно, то бот должен был присоединиться к каналу.

<h2 id='function'> Функционал </h2>

На данный момент бот поддерживает 5 основных команд:

* $hello - здоровается с пользователем отправившим команду.
* $info - выводит в чат информацию о своих возможностях.
* $world - выводит информацию o covid19 по миру.
* $russia - выводит информацию o covid19 по России.
* $country+<Название страны> - выводит информацию o covid19 по указанной вами стране.

Зная это, вы спокойно сможете использовать моего бота.

![/images/1.png](https://raw.githubusercontent.com/sergo2048/discord_covid_bot/master/images/small.png)

<h2 id='addictions'> Зависимости</h2>

В данном боте используются Python версии 3.6. а так же его сторонние модули. Поэтому для его корректной работы их необходимо установить.

1. discord.py 1.3.3 - это основной инструмен при работе с Discord  
Прочитать об этом модуле больше можно [тут](https://pypi.org/project/discord.py/) или [тут](https://discordpy.readthedocs.io/en/latest/)  
Для его установки необходимо выполнить:

```python
pip3 install discord.py
```

2. covid-data-api - этот модуль отвечает за получение статистики по Covid19.  
Прочитать про него можно [тут](https://pypi.org/project/covid-data-api/).

```python
pip3 install covid-data-api
```

Так же в данном проекте используются стандартные модули, такие как:

* xml
* datetime

<h2 id='settings'> Настройка </h2>

Также для того что бы бот нормально работал, необходимо создать файл **settings.py**, в котором нужно указать примерно следующие:

```python
# Токен бота из дискорда
BOT_TOKEN = ''

# Информация в чат что умеет бот
INFO = ''' Привет :innocent:, я создан что бы следить за ситуацией с covid-19 :microbe: в мире не выходя из твоего любимого discord.
Что бы узнать о ситуации в мире напиши $world :earth_asia:,
Что бы узнать о ситуации в России матушке напиши $Russia :flag_ru:,
Что бы узнать про другую страну напиши $country+<Название страны> :rainbow_flag:,

Ничего не бойся :kissing_closed_eyes:   ,  следи за гигиеной :bathtub:,  почаще мой руки :shield:,  не выходи на улицу без веского повода :mask:,  в discord ты в безопасности:+1:.
'''
```

Теперь если вы проделали все что написано выше, бот должен работать. Запустить его можно командой в терминале:

```python
pyhon3 main.py
```
