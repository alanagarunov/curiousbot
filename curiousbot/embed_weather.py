import pyowm


def thechecker(request, unit, loc):
    owm = pyowm.OWM("<token>")
    if request == "search":
        obs = owm.weather_at_place(loc)
        w = obs.get_weather()  # initalize our api
        if unit == "c":
            units = "celsius"
            unitss = "°C"
        elif unit == "f":
            units = "fahrenheit"
            unitss = "°F"

        # await client.say("Local time: " + str(w.get_reference_time(timeformat='iso')) + "\n")
        # the follow functions use the api functions to pull information based on what was passed from our command
        temps = w.get_temperature(unit=units)
        pressure = w.get_pressure()
        actualtemp = temps["temp"]
        maxtemp = temps["temp_max"]
        mintemp = temps["temp_min"]
        pressure = pressure["press"]
        sky = w.get_status()
        print(sky)
        if sky == "Clouds":
            condition = "☁️"
        elif sky == "Clear":
            condition = "☀️ "
        elif sky == "Rain":
            condition = "🌧️"
        elif sky == "Snow":
            condition = "🌨️"
        # sends back to main to be sent as a message on discord
        theinfo = [
            str(maxtemp),
            str(mintemp),
            str(actualtemp),
            str(pressure),
            unitss,
            condition,
        ]
        return theinfo


# TODO: implement other functions of the pyOWM api
"""     
elif request == '3day':
    fc = owm.three_hours_forecast(loc)
    #f = fc.get_forecast()
    rain = str(fc.when_rain())
    sun = str(fc.when_sun())
    cloud = str(fc.when_clouds())
    fog = str(fc.when_fog())
    snow = str(fc.when.snow())
    await client.say("Will rain? " + rain + "\n"
                    "Will snow? " + snow)
 """
