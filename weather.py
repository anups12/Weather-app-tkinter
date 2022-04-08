    
from distutils import text_file
import tkinter as tk
from urllib import response
import requests
from PIL import Image, ImageTk

# key  = 89fe105f74428941d0a8571fef9d5eef
# Link = https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def response_weather(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        feels_like = weather['main']['feels_like']
        clouds = weather['clouds']['all']
        temp_min = weather['main']['temp_min']
        temp_max = weather['main']['temp_max']
        humidity = weather['main']['humidity']
        str_result = 'City : %s\nCondition : %s\nTemp :%s °C\nFeels-Like:%s ° C\nClouds : %s\nMinimum-Temp : %s °C\nMaximum-Temp :%s °C\nHumidity : %s\n'%(city,condition,temp,clouds,feels_like,temp_min,temp_max,humidity)
    except:
        str_result = "There is some error while fetching your result \n Please Try again with different keyword"
    return str_result

def get_weather(city):
    apid ='89fe105f74428941d0a8571fef9d5eef'
    url ='https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':apid, 'q':city, 'units':'metric'}
    response= requests.get(url, params)
    weather = response.json()

    lbl_txt1['text'] = response_weather(weather)



root = tk.Tk()
root.title("Weather App")
root.geometry("600x500")
root.configure(bg="lime")

img = Image.open('h.jpg')
img.resize((600,500), Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width=600, height=500)

lbl_txt = tk.Label(bg_lbl,text="Search the city ", font=('Arial', 30, 'bold','underline'), fg='black',bg='#FFD93A' )
lbl_txt.place(x=150,y=30)

frame_first = tk.Frame(bg_lbl,bg="lightpink", bd=5)
frame_first.place(x=50, y=100, width=500, height=50)

txt_field = tk.Entry(frame_first, font=('Arial', 25), width=18)
txt_field.grid(row=0, column=0, sticky='w')

button_search = tk.Button(frame_first, text="Search City ",font=('Arial', 15, 'bold'), fg="black", bg='blue', command=lambda: get_weather(txt_field.get()))
button_search.grid(row=0, column=1, padx=20)

frame_second = tk.Frame(bg_lbl,bg="#cccccc", bd=5, border=10, borderwidth=10 )
frame_second.place(x=50, y=180, width=500, height=250)

lbl_txt3 = tk.Label(frame_second ,text="Search Results ", font=('Arial', 15, 'bold','underline'), fg='green',bg='#cccccc')
lbl_txt3.place(relheight=.1, relwidth=1,relx=0,rely=0.02)

lbl_txt1 = tk.Label(frame_second,bg='#cccccc', justify='left', anchor='nw' )
lbl_txt1.place(relheight=.9, relwidth=1,relx=0,rely=0.2 )



root.mainloop()