import requests

def get_weather(city):
    api_key = "e746f8c5a82dfsafg45621sfd621a1555269051ba958b7343"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather_info = {
            "city": data["name"],
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
        return weather_info
    else:
        return None

def main():
    city = input("Enter city name: ")
    weather_info = get_weather(city)
    
    if weather_info:
        print(f"Weather in {weather_info['city']}:")
        print(f"Description: {weather_info['description']}")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind Speed: {weather_info['wind_speed']} m/s")
    else:
        print("Failed to retrieve weather information. Please try again.")

if __name__ == "__main__":
    main()
