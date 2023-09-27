from .db import db

class OneHandedWeapons(db.Document):
    name = db.StringField(required = True, unique = True)
    compendium_entry = db.IntField(required = True, unique = True)
    base_damage = db.IntField(required = True)
    shown_damage = db.IntField(required = True)
    max_durability = db.StringField(required = True)
    effects = db.ListField(db.StringField(), required = True)
    max_extralife = db.IntField(required = True)
    fuse_damage = db.IntField(required = True)
    fused_effects = db.ListField(db.StringField(), required = True)
    zonai_fuse_damage_bonus = db.IntField(required = True)
    shieldbase_damage = db.IntField(required = True)

class TwoHandedWeapons(db.Document):
    name = db.StringField(required = True, unique = True)
    actor_name = db.StringField(required = True)
    compendium_entry = db.IntField(required = True, unique = True)
    base_damage = db.IntField(required = True)
    shown_damage = db.IntField(required = True)
    max_durability = db.StringField(required = True)
    effects = db.ListField(db.StringField(), required = True)
    max_extralife = db.IntField(required = True)
    fuse_damage = db.IntField(required = True)
    fused_effects = db.ListField(db.StringField(), required = True)
    zonai_fuse_damage_bonus = db.IntField(required = True)
    shieldbase_damage = db.IntField(required = True)

class Bows(db.Document):
    name = db.StringField(required = True, unique = True)
    actor_name = db.StringField(required = True)
    compendium_entry = db.IntField(required = True, unique = True)
    base_damage = db.IntField(required = True)
    max_durability = db.StringField(required = True)
    effects = db.ListField(db.StringField(), required = True)
    range = db.IntField(required = True)
    drawing_time = db.IntField(required = True)
    reload_time = db.IntField(required = True)
    fuse_damage = db.IntField(required = True)
    fused_effects = db.ListField(db.StringField(), required = True)
    fancy_bow_effects = db.ListField(db.StringField(), required = True)

class Shields(db.Document):
    name = db.StringField(required = True, unique = True)
    actor_name = db.StringField(required = True)
    compendium_entry = db.IntField(required = True, unique = True)
    base_guardpower = db.IntField(required = True)
    base_damage = db.IntField(required = True)
    max_durability = db.StringField(required = True)
    surf_damage_rate = db.IntField(required = True)
    surf_friction_rate = db.IntField(required = True)
    effects = db.ListField(db.StringField(), required = True)
    fuse_damage = db.IntField(required = True)
    fused_effects = db.ListField(db.StringField(), required = True)

class Enemies(db.Document):
    name = db.StringField(required = True, unqiue = True)
    actor_name = db.StringField(required = True, unique = True)
    compendium_entry = db.IntField(required = True, unique = True)
    max_life = db.IntField(required = True)
    base_damage = db.IntField(required = True)
    base_damage_melee_weapon = db.IntField(required = True)
    base_damage_ranged_weapon = db.IntField(required = True)
    drops = db.ListField(db.StringField(), required = True)
    exp_given = db.IntField(required = True)

class Animals(db.Document):
    name = db.StringField(required = True, unqiue = True)
    actor_name = db.StringField(required = True, unique = True)
    compendium_entry = db.IntField(required = True, unique = True)
    max_life = db.IntField(required = True)

class MonsterParts(db.Document):
    name = db.StringField(required = True, unqiue = True)
    actor_name = db.StringField(required = True, unique = True)

class ElixirParts(db.Document): # Insects
    name = db.StringField(required = True, unqiue = True)
    actor_name = db.StringField(required = True, unique = True)

class CookingParts(db.Document): # Raw Foods
    name = db.StringField(required = True, unqiue = True)
    actor_name = db.StringField(required = True, unique = True)

class FuseParts(db.Document): # Non-Monster Items that can be fused, but not consumed (ie. Diamonds)
    name = db.StringField(required = True, unqiue = True)
    actor_name = db.StringField(required = True, unique = True)