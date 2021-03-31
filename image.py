from bs4 import BeautifulSoup
import requests
import os

def imagedown(url,folder):
    try:
      os.mkdir(os.path.join(os.getcwd(), folder))  
    except:
        pass
    os.chdir(os.path.join(os.getcwd(),folder))
    r=requests.get(url).text
    soup=BeautifulSoup(r,"html.parser")
    images=soup.find_all("img")
    for image in images:
        link=image["src"]
        name=image["alt"]
        im=requests.get(link)
        with open(name.replace("/","-").replace("*","")+".jpg", "wb") as f:
            
            f.write(im.content)
            print("writing:",name)
                
imagedown("https://www.airbnb.com/s/Ljubljana--Slovenia/homes?room_types%5B%5D=Entire%20home%2Fapt&min_beds=4&min_bedrooms=2&source=structured_search_input_header&tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&search_type=autocomplete_click&query=Ljubljana%2C%20Slovenia&place_id=ChIJ0YaYlvUxZUcRIOw_ghz4AAQ&checkin=2021-11-01&checkout=2021-11-04", "ktm")

