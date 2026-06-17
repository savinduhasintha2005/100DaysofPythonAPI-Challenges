from fastapi import FastAPI
from enum import Enum

app = FastAPI(
    title = "Temperature Convertor API",
    description="Convert Celsius, Fahrenheit, and Kelvin temperatures",
    version="1.0"
)

@app.get("/")
def home():
    return {"message" : "Welcome to Temperature Convertor API"}


@app.get("/convert")
def convert_temperature(
        temperature : float,
        from_unit : str,
        to_unit : str,
):

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        result = temperature

    elif from_unit == "celsius":
        if to_unit == "fahrenheit":
            result = (temperature * 9/5) + 32
        elif to_unit == "kelvin":
            result = (temperature + 273.15)
        else:
            return {"message" : "Invalid target unit"}

    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            result = (temperature - 32) * 5/9
        elif to_unit == "kelvin":
            result = (temperature - 32) * 5/9 + 273.15
        else:
            return {"message" : "Invalid target unit"}

    elif from_unit == "kelvin":
        if to_unit == "celsius":
            result = (temperature - 273.15)
        elif to_unit == "fahrenheit":
            result = (temperature - 273.15) * 9/5 + 32
        else:
            return {"message" : "Invalid target unit"}

    else:
        return {"message" : "Invalid source unit"}

    return {
        "input_temperature": temperature,
        "from_unit": from_unit,
        "to_unit": to_unit,
        "converted_temperature": round(result, 2)
    }










