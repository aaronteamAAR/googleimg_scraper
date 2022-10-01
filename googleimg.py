from email.mime import image
import enum
from tabnanny import verbose
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from datetime import datetime as dt
from PIL import Image
import time
import os


PATH ="C:/Users/USER/Downloads/chromedriver_win32/chromedriver.exe"
    
wd = webdriver.Chrome(executable_path=PATH)


# Get images and list them from google 
def get_images(wd, delay, max_images, url):
    def scroll_down(wd):
        wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(delay)
    url = url
    wd.get(url)
    
    image_url = set()
    skips = 0
    
    
    
    
    
    
    
    
    
    while len(image_url) + skips < max_images:
        scroll_down(wd)
        thumdnails = wd.find_elements(By.CLASS_NAME, 'Q4LuWd')



        for img in thumdnails[len(image_url) + skips:max_images]:
            try:
               img.click()
               time.sleep(delay) 
            except:
                continue
            
            images = wd.find_elements(By.CLASS_NAME, 'n3VNCb')
            for image in images:
                if image.get_attribute('src') in image_url:
                    max_images += 1
                    skips += 1
                    break
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_url.add(image.get_attribute('src'))
                    
    
    return image_url


# save images 

def download_images(down_path, url, file_name, image_type='PNG', verbose=True):
    try:
        time = dt.now()
        current_time = time.strftime('%H:%M:%S')
        image_content = requests.get(url).content
        img_file = io.BytesIO(image_content)
        image = Image.open(img_file)
        file_path = down_path + file_name
        
        
        with open(file_path, 'wb') as file:
            image.save(file, image_type)
            
            if verbose == True:
                print(f'The image:{file_path}  download 100% at {current_time}')
    except Exception as e:
        print(f'unable to download image due to: \n: {str(e)}')
        
        
if __name__ == "__main__":
     
    google_urls = ['https://www.google.com/search?q=elon+musk+images&tbm=isch&ved=2ahUKEwjPjo2fxL_6AhVG0IUKHZf_AN0Q2-cCegQIABAA&oq=elon&gs_lcp=CgNpbWcQARgAMgQIABBDMgcIABCxAxBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMggIABCABBCxAzIICAAQgAQQsQM6BwgjEOoCECc6BQgAEIAEOggIABCxAxCDAToLCAAQgAQQsQMQgwFQm74BWJ7DAWDazgFoAHAAeACAAeIWiAH4HpIBCTItMy4xLjktMZgBAKABAaoBC2d3cy13aXotaW1nsAEKwAEB&sclient=img&ei=03U4Y4_ZIcaglwSX_4PoDQ&bih=749&biw=1600#imgrc=pnFzWnBrTlTqFM']
        
    label = ['Elon musk']   
    
    if len(google_urls) != len(label):
        raise ValueError('Not a match')
          
          
    player_path = './elon'
    
    for ibl in label:
        if not os.path.exists(player_path + ibl):
            print(f'making folder: {str(ibl)}')
            os.makedirs(player_path + ibl)
            
            
            
    for url_current, ibl in zip(google_urls, label):
        urls = get_images(wd, 0, 10, url_current)
        
        
        for i, url in enumerate(urls):
            download_images(down_path=f'/elon/elonmusk/{ibl}/',
            url = url,
            file_name=str(i+1)+ '.jpg',
            verbose= True
            )
            
    wd.quit()

