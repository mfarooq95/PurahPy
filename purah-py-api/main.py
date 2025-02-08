import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from supabase import create_client, Client

load_dotenv('.env')

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
app = Flask(__name__)
db = SQLAlchemy()
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMT_POOL_SIZE'] = 10
app.config['SQLALCHEMY_POOL_RECYCLE'] = 1800
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30

supabase = create_client(supabase_url = SUPABASE_URL, supabase_key = SUPABASE_KEY)

#Create API resources and methods
class OneHandedWeapons(Resource):
    def get(self):
        response = supabase.table("one-handed-weapons").select("*").execute()
        data = response.data
        return data

class OneHandedWeapon(Resource):
    def get(self, weapon_name):
        response = supabase.table("one-handed-weapons").select("*").eq("Name", weapon_name).limit(1).single().execute()
        if response:
            data = response.data
            return data
        else:
            return {"message": "Item not found"}, 404

class TwoHandedWeapons(Resource):
    def get(self):
        response = supabase.table("two-handed-weapons").select("*").execute()
        data = response.data
        return data

class TwoHandedWeapon(Resource):
    def get(self, weapon_name):
        response = supabase.table("two-handed-weapons").select("*").eq("Name", weapon_name).limit(1).single().execute()
        if response:
            data = response.data
            return data
        else:
            return {"message": "Item not found"}, 404

class Shields(Resource):
    def get(self):
        response = supabase.table("shields").select("*").execute()
        data = response.data
        return data

class Shield(Resource):
    def get(self, shield_name):
        response = supabase.table("shields").select("*").eq("Name", shield_name).limit(1).single().execute()
        if response:
            data = response.data
            return data
        else:
            return {"message": "Item not found"}, 404

class Spears(Resource):
    def get(self):
        response = supabase.table("spears").select("*").execute()
        data = response.data
        return data

class Spear(Resource):
    def get(self, spear_name):
        response = supabase.table("spears").select("*").eq("Name", spear_name).limit(1).single().execute()
        if response:
            data = response.data
            return data
        else:
            return {"message": "Item not found"}, 404

class Bows(Resource):
    def get(self):
        response = supabase.table("bows-weapons").select("*").execute()
        data = response.data
        return data

class Bow(Resource):
    def get(self, bow_name):
        response = supabase.table("bows-weapons").select("*").eq("Name", bow_name).limit(1).single().execute()
        data = response.data
        return data
        
class Monsters(Resource):
    def get(self):
        response = supabase.table("monsters").select("*").execute()
        data = response.data
        return data

class Monster(Resource):
    def get(self, monster_name):
        response = supabase.table("monsters").select("*").eq("Name", monster_name).limit(1).single().execute()
        data = response.data
        return data

# Create routes & endpoints
api.add_resource(OneHandedWeapons, '/weapons/onehandedweapons')
api.add_resource(OneHandedWeapon, '/weapons/onehandedweapons/<string:weapon_name>')
api.add_resource(TwoHandedWeapons, '/weapons/twohandedweapons')
api.add_resource(TwoHandedWeapon, '/weapons/twohandedweapons/<string:weapon_name>')
api.add_resource(Shields, '/shields')
api.add_resource(Shield, '/shields/<string:shield_name>')
api.add_resource(Spears, '/weapons/spears')
api.add_resource(Spear, '/weapons/spears/<string:spear_name>')
api.add_resource(Bows, '/weapons/bows')
api.add_resource(Bow, '/weapons/bows/<string:bow_name>')
api.add_resource(Monsters, '/monsters')
api.add_resource(Monster, '/monsters/<string:monster_name>')






if '__main__' == __name__:
    app.run(host = "0.0.0.0", port =int(os.environ.get("PORT", 5000)))