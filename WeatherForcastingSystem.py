


import tkinter as tk
from PIL import Image, ImageTk
import requests





root=tk.Tk()
root.title("My Weather Informer")
root.geometry("600x500")

def format_response(weather):
    try:
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str='City:%s\nCondition:%s\nTemperature:%s'%(city,condition,temp)
    except:
        final_str='There was problem retrieving that info'
    return final_str

    
def get_weather(city):
    weather_key='ace1a3a458961a7c2efb534f97d385a3'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city}
    response=requests.get(url,params)
    #print(response.json())
    weather=response.json()
   

    result['text']=format_response(response.json())
    

img=Image.open("./WeatherBackground.jpg")
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)
bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title=title=tk.Label(bg_lbl,text="You Can Found Weather Of Cities",fg='red',font=('times new roman',16,'bold'))
heading_title.place(x=80,y=18)
frame_one=tk.Frame(bg_lbl,bg="#42c2f4")
frame_one.place(x=80,y=50,width=450,height=50)

txt_box=tk.Entry(frame_one,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0)
btn=tk.Button(frame_one,text='Press Me',fg='blue',font=('times new roman',16,'bold'),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)

frame_two=tk.Frame(bg_lbl,bg="#42c2f4")
frame_two.place(x=80,y=130,width=450,height=300)

result=tk.Label(frame_two,font=40,bg='white',justify='left')
result.place(relwidth=1,relheight=1)

root.mainloop()





#key : ace1a3a458961a7c2efb534f97d385a3
#API : api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}







