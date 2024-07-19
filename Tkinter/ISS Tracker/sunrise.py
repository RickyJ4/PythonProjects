import requests
import datetime as dt
import smtplib

my_email = "laurencemagenga12@gmail.com"
password = "ypaslpvzngmegivt"

my_lat = 49.283764
my_long = -122.793205


def is_dark():
    parameters ={
        "lat": my_lat,
        "lng":my_long,
        "formatted": 0,
        }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = dt.datetime.now().hour

    if(now >=sunset or now <= sunrise):
        return True
    return False

def iss_location_near_me():
    response = requests.get(url= "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if(my_lat-5 <= iss_latitude <= my_lat + 5 or my_long -5 <= iss_longitude <= my_long + 5):
        return True
    return False

if (is_dark() == True and iss_location_near_me() == True):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password=password)
        connection.sendmail(
        from_addr= my_email,
        to_addrs= "RictorJunior8@gmail.com",
        msg= f"Subject : ISS is near by check outsife\n\n The ISS is Flying right above you take a look and see"
        )



