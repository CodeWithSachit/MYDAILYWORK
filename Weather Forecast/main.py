import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  


API_KEY = "120c1c0cca5e467cba9141315241510"  
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather_data(location):
    """Fetch weather data from WeatherAPI."""
    query_url = f"{BASE_URL}?key={API_KEY}&q={location}"
    response = requests.get(query_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather():
    """Display the weather data in the Tkinter window."""
    location = location_entry.get() 
    data = get_weather_data(location)
    
    if data:
        location_name = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        temp_celsius = data['current']['temp_c']
        humidity = data['current']['humidity']
        weather_desc = data['current']['condition']['text']
        wind_kph = data['current']['wind_kph']
        
        
        result_label.config(text=(
            f"Weather in {location_name}, {region}, {country}:\n"
            f"Temperature: {temp_celsius}°C\n"
            f"Humidity: {humidity}%\n"
            f"Condition: {weather_desc}\n"
            f"Wind Speed: {wind_kph} km/h"
        ))
    else:
        messagebox.showerror("Error", "City/ZIP not found or API error.")

def refresh():
    """Clear the weather data and reset input fields for a new search."""
    location_entry.delete(0, tk.END)
    result_label.config(text="")

def exit_application():
    """Exit the application."""
    window.quit()


window = tk.Tk()
window.title("Weather Forecast Application")
window.geometry("400x550")
window.config(bg="lightblue")


window.iconbitmap("weather.ico")  


cloud_img = Image.open("weather.jpg")  
cloud_img = cloud_img.resize((300, 200))  
cloud_img_tk = ImageTk.PhotoImage(cloud_img)

image_label = tk.Label(window, image=cloud_img_tk, bg="lightblue")
image_label.pack(pady=10)


location_label = tk.Label(window, text="Enter city name or ZIP code:", bg="lightblue", font=("Arial", 12))
location_label.pack(pady=10)

location_entry = tk.Entry(window, width=30, font=("Arial", 12))
location_entry.pack(pady=5)


fetch_button = tk.Button(window, text="Get Weather", command=display_weather, font=("Arial", 12))
fetch_button.pack(pady=10)


refresh_button = tk.Button(window, text="Refresh", command=refresh, font=("Arial", 12))
refresh_button.pack(pady=5)


result_label = tk.Label(window, text="", bg="lightblue", font=("Arial", 12), justify="left")
result_label.pack(pady=10)


exit_button = tk.Button(window, text="Exit", command=exit_application, font=("Arial", 12), bg="red", fg="white")
exit_button.pack(pady=10)


window.mainloop()
