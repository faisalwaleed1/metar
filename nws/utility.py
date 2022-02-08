import imp
import math
import re


class Utility:
    """
    This class provides nws report related utility functions 
    """
    @classmethod
    def extract_temperature(cls, temperature):
        """
        Takes in temperature, extract info and return in new format. 
        """
        current_temp, dew_point = temperature.split("/")
        celsius = (
            int(current_temp[1:]) * -1
            if current_temp[0] == "M"
            else int(current_temp[1:])
        )
        fahrenheit = int((celsius * 1.8) + 32)
        return f"{celsius} C ({fahrenheit}F)"

    @classmethod
    def extract_wind(cls, wind):
        """
        Takes in wind, extract info and return with new format.
        """
        degree = wind[0:3]
        direction_val = int((float(degree) / 22.5) + 0.5)
        direction = [
            "N",
            "NNE",
            "NE",
            "ENE",
            "E",
            "ESE",
            "SE",
            "SSE",
            "S",
            "SSW",
            "SW",
            "WSW",
            "W",
            "WNW",
            "NW",
            "NNW",
        ]
        knots = int(int(wind[6:8])) if "G" in wind else int(int(wind[3:5]))
        return f"{direction[direction_val % 16]} at {math.ceil(knots * 1.151)} mph ({knots} knots)"

    @classmethod
    def string_to_json(cls, data):
        """
        Takes in report data, return required dict.
        """
        weather_records = data.replace("\n", " ").rstrip().split(" ")
        temperature = list(
            filter(re.compile("^M{0,1}[\d]+\/M{0,1}[\d]+$").match, weather_records[1:])
        )[0]

        wind = [record for record in weather_records[1:] if "KT" in record][0]
        return {
            "data": {
                "last_observation": f"{weather_records[0]} at {weather_records[1]} GMT",
                "station": weather_records[2],
                "temperature": cls.extract_temperature(temperature),
                "wind": cls.extract_wind(wind),
            }
        }
