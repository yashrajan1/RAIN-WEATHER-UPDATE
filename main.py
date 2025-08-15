from email.mime.text import MIMEText
import os
import requests
import smtplib

MY_EMAIL = "yraj42912@gmail.com"
PASSWORD = os.environ.get("PASSWORD")
msg_content = "Subject:Warning! Today there will be rain a lot!\n\nRemember to bring umbrella ☔!"


api_key = os.environ.get("API_KEY")
endpoint_hourly = "https://pro.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat":21.145800,
    "lon":79.088158,
    "appid":api_key
}

response = requests.get(endpoint_hourly,params=weather_params)
weather_data = response.json()
weather_slice = weather_data["list"][:7]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"] #stores weather id
    if int(condition_code) < 700:#if weather id is less than it shows rain
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        msg= MIMEText(msg_content,_charset="utf-8")
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=msg.as_string())





