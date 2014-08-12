"""
Example command module template

Copy this module up one level to gamesrc/commands/ and name it as
befits your use.  You can then use it as a template to define your new
commands. To use them you also need to group them in a CommandSet (see
examples/cmdset.py)

"""

from ev import Command

class CmdHoof(Command):
    """
    This provides information about the selected character.

    Usage: 
      +hoof <name>

    This command is similar to @finger, pinfo, or cinfo on other systems in that
    it provides publically accessible information about the character.
    """

    key = "+hoof"
    help_category = "General"

    def func(self):
        """This performs the actual command"""
        caller = self.caller
        if not self.args:
            caller.msg("Hoof who?")
            return
        #print "general/hoof:", caller, caller.location, self.args, caller.location.contents
        if self.args == " me":
            obj = caller
        else:
            obj = caller.search(self.args)
        if not obj:
            caller.msg("Hoof who?")
            return
        #print obj, obj.location, caller, caller == obj.location
        outstr = "{m==============================================================================\n"
        outstr += "{y%s {Wthe {g%s %s" % (obj.name, obj.db.gender, obj.db.species)
        if caller.locks.check_lockstring(caller, "dummy:perm(Wizards)"):
            if obj.db.approved:
                outstr += " (Approved)\n"
            else:
                outstr += " {r(Unapproved)\n"
        else:
            outstr += "\n"
        if obj.db.full_name:
            outstr += "    {wFull Name: {g%s\n" % obj.db.full_name
        if obj.db.alignment:
            outstr += "    {wAlignment: {g%s\n" % obj.db.alignment
        if obj.db.age:
            outstr += "          {wAge: {g%s\n" % obj.db.age
        if obj.db.apparent_age:
            outstr += " {wApparent Age: {g%s\n" % obj.db.apparent_age
        if obj.db.sexuality:
            outstr += "    {wSexuality: {g%s\n" % obj.db.sexuality
        if obj.db.coat:
            outstr += "         {wCoat: {g%s\n" % obj.db.coat
        if obj.db.mane:
            outstr += "         {wMane: {g%s\n" % obj.db.mane
        if obj.db.cutie_mark:
            outstr += "   {wCutie Mark: {g%s\n" % obj.db.cutie_mark
        if obj.db.eyes:
            outstr += "         {wEyes: {g%s\n" % obj.db.eyes
        if obj.db.height:
            outstr += "       {wHeight: {g%s\n" % obj.db.height
        if obj.db.weight:
            outstr += "       {wWeight: {g%s\n" % obj.db.weight
        #HOME
        outstr += "{m==============================================================================\n"
        if obj.db.character_notes:
            outstr += "Character Notes: {g%s\n" % obj.db.character_notes
        if obj.db.player_notes:
            outstr += "   Player Notes: {g%s\n" % obj.db.player_notes
        if obj.db.rp_prefs:
            outstr += " RP Preferences: {g%s\n" % obj.db.rp_prefs
        if obj.db.character_notes or obj.db.player_notes or obj.db.rp_prefs:
            outstr += "{m==============================================================================\n"
        caller.msg(outstr)