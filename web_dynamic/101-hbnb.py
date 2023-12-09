#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """Close the current SQLAlchemy Session"""
    storage.close()


@app.route('/101-hbnb/', strict_slashes=False)
def hbnb():
    """HBNB is dynamic"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_cnt = []

    for state in states:
        st_cnt.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_cnt,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """This is the main function"""
    app.run(host='0.0.0.0', port=5001)
