import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
# import pdfkit
import img2pdf


def map_to_png(map):
    '''
    Save a map as png file

    Returns: path of png file

    Parameter: map (folium.map)
    '''
    # html map path
    path = f'usermaps/html/{map.location[0]}_{map.location[1]}.html'
    
    # map url
    tmpurl = f'file://{os.getcwd()}/{path}'
    map.save(path)

    # Config the Headless Chrome
    chrome_options = webdriver.ChromeOptions()
    # set binary location for heroku build pack
    chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    
    # Open headless browser...
    # set exec_path for heroku build pack
    browser = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
    
    # get page
    browser.get(tmpurl)
    
    # wait to load page
    time.sleep(1)
    
    # Grab the screenshot
    png_path = f'usermaps/png/{map.location[0]}_{map.location[1]}.png'
    browser.save_screenshot(png_path)
    
    # Close the browser
    browser.quit()
    return png_path


def map_to_pdf(map):
    '''
    Save a map as pdf file

    Returns: path of pdf file

    Parameter: map (folium.map)
    '''
    png_path = map_to_png(map)
    pdf_path = f'usermaps/pdf/{map.location[0]}_{map.location[1]}.pdf'
            
    # opening image 
    image = Image.open(png_path) 

    # remove alpha channel
    image.convert('RGB').save(png_path)
    
    # converting into chunks using img2pdf 
    pdf_bytes = img2pdf.convert(image.filename) 
    
    # opening or creating pdf file 
    file = open(pdf_path, "wb") 
    
    # writing pdf files with chunks 
    file.write(pdf_bytes) 
    
    # closing image file 
    image.close() 
    
    # closing pdf file 
    file.close() 
    
    return pdf_path

def map_to_html(map):
    '''
    Save a map as html file

    Returns: path of html file

    Parameter: map (folium.map)
    '''
    path = 'usermaps/html/current_map.html'
    
    map.save(path)

    return path
