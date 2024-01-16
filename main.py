import requests
from geopy.geocoders import Nominatim

def get_weather(api_key, city_name):
    # Konum bilgisini al
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city_name)
    
    if not location:
        print(f"{city_name} konumu bulunamadı.")
        return
    
    # Hava durumu API'sine sorgu yap
    api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            weather_data = response.json()
            print(f"{city_name} Hava Durumu:")
            print("Sıcaklık:", weather_data['main']['temp'], "°C")
            print("Durum:", weather_data['weather'][0]['description'])
        else:
            print("API sorgusu başarısız oldu. Hata kodu:", response.status_code)

    except requests.exceptions.ConnectionError as e:
        print("Bağlantı hatası:", e)

# OpenWeatherMap API anahtarınızı buraya ekleyin
api_key = "YOUR_OPENWEATHERMAP_API_KEY"

# Hava durumu bilgilerini almak istediğiniz şehir adını buraya ekleyin
city_name = "Istanbul"

get_weather(api_key, city_name)
