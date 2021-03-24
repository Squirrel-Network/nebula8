from pyowm import OWM
from pyowm.commons import exceptions
from config import Config
from core import decorators
from core.utilities.message import message
from languages.getLang import languages

def sendWeatherMessage(update,context,city,mintemp,maxtemp,humidity,icon):
    languages(update,context)
    stringMessage = languages.weather_message.format(city,mintemp,maxtemp,humidity,icon)
    msg = message(update,context,stringMessage)
    return msg

@decorators.delete.init
def init(update, context):
    text = update.message.text[8:].strip().capitalize()
    if text != "":
        try:
            owm = OWM(Config.OPENWEATHER_API)
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(text)
            w = observation.weather
            temp = w.temperature('celsius')
            mintemp = temp['temp_min']
            maxtemp = temp['temp_max']
            humidity = w.humidity
            status = w.status
            print(status)
            if status == 'Clear':
                sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'☀️')
            elif status == 'Clouds':
                sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'☁️')
            elif status == 'Rain':
                sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'🌧')
            elif status == 'Drizzle':
                sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'🌧')
            elif status == 'Mist':
                sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'🌫')
            else:
                sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,status)
        except exceptions.NotFoundError:
            message(update,context, text="The city you searched for does not exist!")
    else:
        message(update,context, text="You need to type a search criteria!\nHow to use the command: <code>/weather text</code>")