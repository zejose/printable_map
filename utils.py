import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pdfkit

def map_to_png(map):
    '''
    Save a map as png file

    Returns: path of png file

    Arguments: map (folium.map)
    '''
    path = 'usermaps/html/current_map.html'
    tmpurl = 'file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=path)
    map.save(path)
    #Open a browser window...
    browser = webdriver.Chrome((ChromeDriverManager().install()))
    #..that displays the map...
    browser.get(tmpurl)
    #Grab the screenshot
    png_path = 'usermaps/png/map.png'
    browser.save_screenshot(png_path)
    #Close the browser
    browser.quit()
    return png_path


def map_to_html(map):
    '''
    Save a map as html file

    Returns: path of html file

    Arguments: map (folium.map)
    '''
    path = 'usermaps/html/current_map.html'
    map.save(path)
    return path


def map_to_pdf(html_path):
    pdf_path = 'usermaps/pdf/current_map.pdf'
    # create pdf
    pdfkit.from_file(html_path, pdf_path)
    return pdf_path