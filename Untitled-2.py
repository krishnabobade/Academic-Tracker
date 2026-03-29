def show_menu():
    print("\n*************************************")
    print("WEATHER INFORMATION SYSTEM")
    print("*************************************")
    print("A. View Weather by City")
    print("B. View All Available Cities")
    print("C. Get Weather Safety Tips")
    print("D. Exit")
    print("***************************************")

weather_data = {
 "mumbai": {
        "temp": "32°C",
        "condition": "Hot ☀️",
        "wind speed": "28 km/h."
    },
    "delhi": {
        "temp": "23°C",
        "condition": "Warm ☁️",
        "wind speed": "24 km/h."

    },
    "pune": {
        "temp": "18°C",
        "condition": "Pleasant ☁️",
        "wind speed": "20 km/h."

    },
    "bangalore": {
        "temp": "30°C",
        "condition": "Hot ☀️",
        "wind speed": "26 km/h."
    
    },
    "amritsar": {
        "temp": "6°C",
        "condition": "cool 🧥",
        "wind speed": "9 km/h."

    },
    "chandigarh": {
        "temp": "18°C",
        "condition": "Pleasant ☁️",
        "wind speed": "20 km/h."
    
    },
    "shillong": {
        "temp": "9°C",
        "condition": "Cool 🧥",
        "wind speed": "12 km/h."
    }
}

def view_weather_by_city():
    city = input("\nEnter city name: ").lower()

    if city in weather_data:
        data = weather_data[city]
        print("\n'''''''''''''''''''''''''''''''''''")
        print("City:", city.capitalize())
        print("Temperature:", data["temp"])
        print("Condition:", data["condition"])
        print("wind speed:", data["wind speed"])
        print("'''''''''''''''''''''''''''''''''''''")
    else:
        print("\nSorry, weather data for this city is not available.")
        print("Please choose from the available cities.")

def view_all_cities():
    print("\nAvailable Cities:")
    print("\n'''''''''''''''''''''''''''''''''''")
    for city in weather_data:
        print("-", city.capitalize())
    print("\n'''''''''''''''''''''''''''''''''''")

def weather_tips():
    print("\nGeneral Weather Safety Tips:")
    print("\n'''''''''''''''''''''''''''''''''''")
    print("• Drink plenty of water in hot weather.")
    print("• Carry an umbrella during rainy conditions.")
    print("• Wear warm clothes in cold climates.")
    print("• Avoid outdoor activities during extreme heat.")
    print("\n'''''''''''''''''''''''''''''''''''")

while True:
    show_menu()
    choice = input("Enter your choice (A-D): ")

    if choice == "A":
        view_weather_by_city()
    elif choice == "B":
        view_all_cities()
    elif choice == "C":
        weather_tips()
    elif choice == "D":
        print("\nThank you for using the Weather Information System.")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 4.")