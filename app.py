from flask import Flask, render_template, url_for, redirect, request, session, send_file
from forms import NavigationForm
from folium import Map, CircleMarker, TileLayer
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup as BS
from utils import map_to_png, map_to_html, map_to_pdf

app = Flask(__name__)
app.config['SECRET_KEY'] = '$uper_$ecret_K€Y'

geolocator = Nominatim(user_agent="specify_your_app_name_here")

@app.route('/', methods=['GET', 'POST'])
def home():
    # Search bar & Button
    form = NavigationForm()
    # submit form
    if form.validate_on_submit():
        # get lat & long of input address
        # ADD ERROR HANDLING for non valid addresses !
        location = geolocator.geocode(form.search.data)
        coords = (location.latitude, location.longitude)
        zoom = int(form.zoom.data)
        map_style = form.map_style.data
        print('\n\nMAP STYLE: ', map_style)
    else:
        # default coords
        coords = (45.5236, -122.6750)
        # default zoom
        zoom = 12
        map_style = 'stamenterrain'
    # create map
    map = Map(location=coords, prefer_canvas=True, zoom_start=zoom)

    TileLayer(map_style).add_to(map)

    # add marker for current search result
    CircleMarker(location=coords, radius=12, fill_color='coral', color='red', fill_opacity=0.8).add_to(map)
    soup = BS(map._repr_html_(), features='html.parser')
    context = {
        'form': form,
        'html_map': soup
    }
    # add coords to session
    session['coords'] = coords
    session['zoom'] = zoom
    # render page
    return render_template('index.html', **context)

@app.route('/save_png', methods=['GET', 'POST'])
def save_png():
    # get coords from session
    coords = session.get('coords', None)
    zoom = session.get('zoom', None)
    # create map
    # FIX FIXED ZOOM BUG
    map = Map(location=coords, prefer_canvas=True, zoom_start=zoom)
    # save map as png and return path
    path = map_to_png(map)
    # show image of map
    return send_file(path)

@app.route('/save_pdf', methods=['GET', 'POST'])
def save_pdf():
    # get coords from session
    coords = session.get('coords', None)
    zoom = session.get('zoom', None)
    # create map
    # FIX FIXED ZOOM BUG
    map = Map(location=coords, prefer_canvas=True, zoom_start=zoom)
    # create html map and store path
    html_map = map_to_html(map)
    pdf_path = map_to_pdf(html_map)
    return send_file(pdf_path, None)


if __name__ == "__main__":
    app.run(debug=True)