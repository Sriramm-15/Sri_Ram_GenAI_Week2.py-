import requests
import csv

API_KEY = "ba35f62793f20a784f52ba33ccb1dfd1" 

def fetch_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            print("City not found")
            return None
        return data
    except:
        print("Network error.")
        return None

def analyze_weather(data):
    temp = data['main']['temp']
    wind = data['wind']['speed']
    humidity = data['main']['humidity']

    if temp <= 10:
        summary = "Cold"
    elif temp <= 24:
        summary = "Mild"
    else:
        summary = "Hot"

    if wind > 10:
        summary += " | High wind alert!"
    if humidity > 80:
        summary += " | Humid conditions!"

    return summary

def log_weather(city):
    data = fetch_weather(city)
    if data:
        summary = analyze_weather(data)

        with open("weather_log.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([city, data['main']['temp'], summary])

        print(f"Weather saved for {city}: {summary}")
    else:
        print("Failed to log weather.")

city = input("Enter city name: ")
log_weather(city)
