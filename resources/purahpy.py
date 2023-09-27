from flask import Response, request
from database.models import OneHandedWeapons
from flask_restful import Resource

class OneHandedWeaponsApi(Resource):
    def get(self):
        one_handed_weapons = OneHandedWeapons.objects().to_json()
        return Response(one_handed_weapons, mimetype = "application/json", status = 200 )

class OneHandedWeaponApi(Resource):
    def get(self, name):
        one_handed_weapon = OneHandedWeapons.objects().get(name = name).to_json()
        return Response(one_handed_weapon, mimetype = "application/json", status = 200)