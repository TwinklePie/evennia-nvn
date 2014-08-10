"""

Template for Characters

Copy this module up one level and name it as you like, then
use it as a template to create your own Character class.

To make new logins default to creating characters
of your new type, change settings.BASE_CHARACTER_TYPECLASS to point to
your new class, e.g.

settings.BASE_CHARACTER_TYPECLASS = "game.gamesrc.objects.mychar.MyChar"

Note that objects already created in the database will not notice
this change, you have to convert them manually e.g. with the
@typeclass command.

"""
from ev import Character as DefaultCharacter


class Character(DefaultCharacter):
    """
    The Character is like any normal Object (see example/object.py for
    a list of properties and methods), except it actually implements
    some of its hook methods to do some work:

    at_basetype_setup - always assigns the default_cmdset to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead)
    at_after_move - launches the "look" command
    at_post_puppet(player) -  when Player disconnects from the Character, we
                    store the current location, so the "unconnected" character
                    object does not need to stay on grid but can be given a
                    None-location while offline.
    at_pre_puppet - just before Player re-connects, retrieves the character's
                    old location and puts it back on the grid with a "charname
                    has connected" message echoed to the room

    """
    def at_object_creation(self):
        "This is called when the object is first created, only"
        self.db.approved = False
        
        self.db.full_name = ""
        self.db.gender = "(unset)"
        self.db.species = "(unset)"
        self.db.alignment = ""
        self.db.job = ""
        self.db.age = ""
        self.db.apparent_age = ""
        self.db.coat = ""
        self.db.mane = ""
        self.db.eyes = ""
        self.db.cutie_mark = ""
        self.db.sexuality = ""
        self.db.height = ""
        self.db.weight = ""
        self.db.short_desc = ""
        self.db.smell = ""
        self.db.smell_notify = ""
        self.db.taste = ""
        self.db.taste_notify = ""
        self.db.feel = ""
        self.db.feel_notify = ""
        self.db.look_notify = ""
        self.db.hide_location = False
        self.db.hide_idle = False
        self.db.rp_prefs = ""
        self.db.player_notes = ""
        self.db.character_notes = ""
        self.db.special = ""
        
        self.db.power = 1
        self.db.combat_score = 1
    
    pass
