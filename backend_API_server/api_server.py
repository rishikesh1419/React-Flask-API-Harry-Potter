from config import mydb
from flask import Flask
from flask import jsonify, request
from flask_cors import CORS
from bson.json_util import dumps
from pymongo import MongoClient
from query_proc import parse_query
from random import randint

app = Flask(__name__)
cors = CORS(app)

"""
Get a random house
Returns: a random house with its id, name, mascot, head of house, house ghost, founder, school,
         list of members (id), list of values, list of colors
"""


@app.route("/sortinghat", methods=["GET"])
def sorting_hat():
    houses = ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]
    try:
        house = dumps(mydb.houses.find({"name": houses[randint(0, 3)]}))
        if len(house) > 0:
            return house
        else:
            return "", 404
    except:
        return "", 500


"""
Characters request route to get all characters and to search for characters by name
Valid uses: /characters (Get all characters), /characters?name=search_string (Search for a character)
Returns: character's _id, name, house and species
"""


@app.route("/characters", methods=["GET"])
def get_chars():
    try:
        params = parse_query(request.query_string)
        if params:
            characters = dumps(
                mydb.characters.find(
                    {"name": {"$regex": params["name"], "$options": "i"}},
                    {"name": 1, "house": 1, "species": 1},
                )
            )
            if len(characters) > 0:
                return characters
            else:
                return "", 404
        else:
            if mydb.characters.count_documents({}) > 0:
                return dumps(
                    mydb.characters.find({}, {"name": 1, "house": 1, "species": 1})
                )
            else:
                return jsonify([])
    except:
        return "", 500


"""
Get a character using _id
Returns: _id, name, role, wand, boggart, patronus, house, school, alias, animagus, blood status, species,
          if member of ministry of magic, order of phoenix, Dumbledore's army, death eaters (4 booleans)
"""


@app.route("/characters/<id>", methods=["GET"])
def get_char_details(id):
    try:
        characters = dumps(mydb.characters.find({"_id": id}))
        if len(characters) > 0:
            return characters
        else:
            return "", 404
    except:
        return "", 500


"""
Get house names with _id and their founders
"""


@app.route("/houses", methods=["GET"])
def get_houses():
    try:
        if mydb.houses.count_documents({}) > 0:
            return dumps(mydb.houses.find({}, {"name": 1, "founder": 1}))
        else:
            return jsonify([])
    except:
        return "", 500


"""
Get house details using name (Gryffindor, Slytherin, Ravenclaw, Hufflepuff)
Returns: _id, name, mascot, head of house, house ghost, founder, school,
         list of members (_id), list of values, list of colors
"""


@app.route("/houses/<name>", methods=["GET"])
def get_house_details(name):
    try:
        if mydb.houses.count_documents({}) > 0:
            return dumps(mydb.houses.find({"name": name}))
        else:
            return jsonify([])
    except:
        return "", 500


"""
Return all spells with details: _id, spell, type, effect
"""


@app.route("/spells", methods=["GET"])
def get_spells():
    try:
        if mydb.spells.count_documents({}) > 0:
            return dumps(mydb.spells.find())
        else:
            return jsonify([])
    except:
        return "", 500


if __name__ == "__main__":
    app.run(debug=True)
