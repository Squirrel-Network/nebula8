from pyowm import OWM
from config import Config
from core.utilities.message import message
from languages.getLang import languages

def sendWeatherMessage(update,context,city,mintemp,maxtemp,humidity,icon):
    languages(update,context)
    stringMessage = languages.weather_message.format(city,mintemp,maxtemp,humidity,icon)
    msg = message(update,context,stringMessage)
    return msg

def init(update, context):
    text = update.message.text[8:].strip().capitalize()
    if text != "":
        owm = OWM(Config.OPENWEATHER_API)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(text)
        w = observation.weather
        temp = w.temperature('celsius')
        mintemp = temp['temp_min']
        maxtemp = temp['temp_max']
        humidity = w.humidity
        status = w.detailed_status
        print(status)
        if status == 'clear sky':
            sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'{} ☀️'.format(status))
        elif status == 'broken clouds':
            sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'{} ⛈'.format(status))
        elif status == 'scattered clouds':
            sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'{} 🌤'.format(status))
        elif status == 'few clouds':
            sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'{} 🌦'.format(status))
        elif status == 'overcast clouds':
            sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'{} ☁️'.format(status))
        elif status == 'light rain':
            sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'{} 🌧'.format(status))
        elif status == 'moderate rain':
            sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'{} 🌧'.format(status))
        elif status == 'rain':
            sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'{} 🌧'.format(status))
        elif status == 'smoke':
            sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'{} 🌫'.format(status))
        elif status == 'mist':
            sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,'{} 🌫'.format(status))
        else:
            sendWeatherMessage(update,context,text,mintemp,maxtemp,humidity,status)
    else:
        message(update,context, text="You need to type a search criteria!\nHow to use the command: <code>/weather text</code>")