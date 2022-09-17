import tkinter as tk
import requests
import time
import json

with open('credentials.json') as f:
    data = json.load(f)

api_key = data['api_key']


def get_weather(canvas):
    city = textfield.get()
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]["main"]
    temp = int(json_data["main"]["temp"] - 273.15)
    min_temp = int(json_data["main"]["temp_min"] - 273.15)
    max_temp = int(json_data["main"]["temp_max"] - 273.15)
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data["sys"]["sunrise"] + 3600))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data["sys"]["sunset"] + 3600))

    final_info = f"{condition}\n{str(temp)}°C"
    final_data = f"\nMax Temp: {str(max_temp)}°C\nMin Temp: {str(min_temp)}°C\nPressure: {str(pressure)}bar\nHumidity: {str(humidity)}%\nWind Speed: {str(wind)}\nSunrise: {sunrise}\nSunset: {sunset}"
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("1200x1000")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font=t, justify="center")
textfield.pack(pady=20)
textfield.focus()
textfield.bind("<Return>", get_weather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()