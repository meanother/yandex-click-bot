from clickbot import DefaultDriver, TorDriver, log
import time
import traceback


kw_temp = [
    'банкротство юридических лиц обнинск',
    'банкротство граждан',
]

test = [
    'банкротство юридических лиц обнинск',
]

kw = [
    'банкротство юридических лиц',
    'банкротство юридических лиц калужская область',
    'банкротство юридических лиц обнинск',
    'банкротство юридических лиц Боровск',
    'банкротство юридических лиц Наро-Фоминск',
    'банкротство юридических лиц Малоярославец',

    'банкротство граждан',
    'банкротство граждан обнинск',
    'банкротство граждан Наро-Фоминск',
    'банкротство граждан Боровск',
    'банкротство граждан калужская область',
    'банкротство граждан Малоярославец',
    'банкротство граждан Балабаново',
    'банкротство граждан Ермолино',

    'Законное списание долгов',
    'Законное списание долгов Обнинск',
    'Законное списание долгов Наро-Фоминск',
    'Законное списание долгов Боровск',
    'Законное списание долгов Ермолино',
    'Законное списание долгов калужская область',
    'Законное списание долгов Малоярославец',
    'Законное списание долгов Балабаново',

    'Списать долги',
    'Списать долги Обнинск',
    'Списать долги Ермолино',
    'Списать долги Боровск',
    'Списать долги Наро-Фоминск',
    'Списать долги Балабаново',
    'Списать долги Малоярославец',
    'Списать долги калужская облсть',

    'Как списать долги',
    'Как списать долги обнинск',
    'Как списать долги Наро-Фоминск',
    'Как списать долги Боровск',
    'Как списать долги Балабаново',
    'Как списать долги Ермолино',
    'Как списать долги Малоярославец',
    'Как списать долги калужская область',

    'Банкротство физических лиц минусы',
    'Справка по банкротству физических лиц',

]

while True:
    try:
        prepare = DefaultDriver(kw)
        prepare.init()
        prepare.x()
        data = prepare.take_promotion_urls()
        prepare.close()

        tor = TorDriver(kw)
        tor.init()
        for url in data:
            tor.start(url)
        tor.close()
        time.sleep(35)
    except Exception as e:
        # tor.close()
        log.error(str(e) + traceback.format_exc())
