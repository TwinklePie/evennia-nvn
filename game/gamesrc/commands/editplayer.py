"""
Contains everything involved in editplayer/editchar

"""
from ev import syscmdkeys
from ev import Command
from contrib.menusystem import MenuNode, MenuTree
from ev import utils

CMD_NOMATCH = syscmdkeys.CMD_NOMATCH
CMD_NOINPUT = syscmdkeys.CMD_NOINPUT


def printchar(caller):
    """
    Prints current character values
    """
    db = caller.db

    outstr = "      Full Name: %s\n" % db.full_name
    outstr += "         Gender: %s\n" % db.gender
    outstr += "        Species: %s\n" % db.species
    outstr += "      Alignment: %s\n" % db.alignment
    outstr += "            Age: %s\n" % db.age
    outstr += "   Apparent Age: %s\n" % db.apparent_age
    outstr += "      Sexuality: %s\n" % db.sexuality
    outstr += "           Coat: %s\n" % db.coat
    outstr += "           Mane: %s\n" % db.mane
    outstr += "     Cutie Mark: %s\n" % db.cutie_mark
    outstr += "           Eyes: %s\n" % db.eyes
    outstr += "         Height: %s\n" % db.height
    outstr += "         Weight: %s\n" % db.weight
    outstr += "Character Notes: %s\n" % db.character_notes
    outstr += "   Player Notes: %s\n" % db.player_notes
    outstr += " RP Preferences: %s\n" % db.rp_prefs
    caller.msg(outstr)
    return


class CmdBackToStart(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("START")


class CmdBackToFullName(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("fullname")


class CmdFullNameSelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.full_name = self.args
        self.menutree.goto("fullname")


class CmdFullNameDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.full_name = ""
        self.caller.msg("Full Name Cleared.")
        self.menutree.goto("fullname")


class CmdBackToAlignment(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("alignment")


class CmdAlignmentSelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.alignment = self.args
        self.menutree.goto("alignment")


class CmdAlignmentDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.alignment = ""
        self.caller.msg("Alignment Cleared.")
        self.menutree.goto("alignment")


class CmdBackToAge(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("age")


class CmdAgeSelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.age = self.args
        self.menutree.goto("age")


class CmdAgeDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.age = ""
        self.caller.msg("Age Cleared.")
        self.menutree.goto("age")


class CmdBackToApparentAge(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("apparent_age")


class CmdApparentAgeSelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.apparent_age = self.args
        self.menutree.goto("apparent_age")


class CmdApparentAgeDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.apparent_age = ""
        self.caller.msg("Apparent Age Cleared.")
        self.menutree.goto("apparent_age")


class CmdBackToSexuality(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("sexuality")


class CmdSexualitySelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.sexuality = self.args
        self.menutree.goto("sexuality")


class CmdSexualityDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.sexuality = ""
        self.caller.msg("Sexuality Cleared.")
        self.menutree.goto("sexuality")


class CmdBackToGender(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("gender")


class CmdGenderSelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.gender = self.args
        self.menutree.goto("gender")


class CmdGenderDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.gender = ""
        self.caller.msg("Gender Cleared.")
        self.menutree.goto("gender")


class CmdBackToJob(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("job")


class CmdJobSelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.job = self.args
        self.menutree.goto("job")


class CmdJobDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.job = ""
        self.caller.msg("Job Cleared.")
        self.menutree.goto("job")   
 

class CmdBackToMane(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("mane")


class CmdManeSelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.mane = self.args
        self.menutree.goto("mane")


class CmdManeDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.mane = ""
        self.caller.msg("Mane Cleared.")
        self.menutree.goto("mane")               


class CmdBackToEyes(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("eyes")


class CmdEyesSelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.eyes = self.args
        self.menutree.goto("eyes")


class CmdEyesDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.eyes = ""
        self.caller.msg("Eye Color Cleared.")
        self.menutree.goto("eyes")        
        

class CmdBackToHeight(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("height")


class CmdHeightSelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.height = self.args
        self.menutree.goto("height")


class CmdHeightDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.height = ""
        self.caller.msg("Height Cleared.")
        self.menutree.goto("height")    
        
        
class CmdBackToWeight(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("weight")


class CmdWeightSelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.weight = self.args
        self.menutree.goto("weight")


class CmdWeightDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.weight = ""
        self.caller.msg("Weight Cleared.")
        self.menutree.goto("weight")   
        
  
class CmdBackToCutieMark(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("cutie_mark")


class CmdCutieMarkSelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.cutie_mark = self.args
        self.menutree.goto("cutie_mark")


class CmdCutieMarkDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.cutie_mark = ""
        self.caller.msg("Cutie Mark Cleared.")
        self.menutree.goto("cutie_mark")        
        
        
class CmdBackToShortDesc(Command):
    """
    Step back to node0
    """
    key = CMD_NOINPUT
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.menutree.goto("short_desc")


class CmdShortDescSelect(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.short_desc = self.args
        self.menutree.goto("short_desc")


class CmdShortDescDelete(Command):
    """
    Handle setting the full name
    """
    key = CMD_NOMATCH
    locks = "cmd:all()"

    def func(self):
        "Execute the command"
        self.caller.db.short_desc = ""
        self.caller.msg("Short Desc Cleared.")
        self.menutree.goto("short_desc")


class CmdEditCharacter(Command):
    """
    This allows the player to edit their character.

    Usage:
      +editcharacter

    This command allows the player to set fields on the current character. Must be @ic in order to set
    values.
    """

    key = "+editcharacter"
    aliases = ["editplayer", "editcharacter", "+editplayer"]
    help_category = "General"

    def func(self):
        """This performs the actual command"""
        caller = self.caller
        printchar(self.caller)
        "Testing the menu system"

        node0 = MenuNode("START", text="Character Editing",
                         links=["fullname", "gender", "species", "alignment", "job", "age", "apparent_age", "coat",
                                "mane", "eyes", "cutie_mark", "sexuality", "height", "weight", "short_desc", "END"],
                         linktexts=[
                             "Full Name", "Gender", "Species", "Alignment", "Job or Class", "Age", "Apparent Age",
                             "Coat", "Mane", "Eyes", "Cutie Mark", "Sexuality", "Height when Standing", "Weight",
                             "Short Desc for ws", "Quit"],
                         keywords=["F", "G", "S", "AL", "J", "A", "AP", "C", "M", "E", "CM", "SE", "H", "W", "SD",
                                   "Q"],
                         cols=2)
        node1 = MenuNode("fullname",
                         links=["fullname_change", None, "END", "START"],
                         selectcmds=[None, CmdFullNameDelete, None, None],
                         linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                         keywords=["C", "D", "Q", "B"],
                         code="self.caller.msg('Current Full Name: %s' % self.caller.db.full_name)")
        node1b = MenuNode("fullname_change",
                          text="What do you want your full name to be? (Space + CR to make no changes)",
                          links=["START", "END"],
                          keywords=[CMD_NOINPUT, CMD_NOMATCH],
                          selectcmds=[CmdBackToFullName, CmdFullNameSelect],
                          nodefaultcmds=True,
                          code="self.caller.msg('Current Full Name: %s' % self.caller.db.full_name)")

        node2 = MenuNode("gender",
                         links=["gender_change", None, "END", "START"],
                         selectcmds=[None, CmdGenderDelete, None, None],
                         linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                         keywords=["C", "D", "Q", "B"],
                         code="self.caller.msg('Current Gender: %s' % self.caller.db.gender)")
        node2b = MenuNode("gender_change",
                          text="What do you want your gender to be? (Space + CR to make no changes)",
                          links=["START", "END"],
                          keywords=[CMD_NOINPUT, CMD_NOMATCH],
                          selectcmds=[CmdBackToGender, CmdGenderSelect],
                          nodefaultcmds=True,
                          code="self.caller.msg('Current Gender: %s' % self.caller.db.gender)")
                         
        node3 = MenuNode("species", text=("Current Species: %s" % caller.db.species),
                         links=["END", "START"], linktexts=["Quit", "Back to start"],
                         keywords=["Q", "B"])
#        node3b = MenuNode("species_select", text=("Current Species: %s" % caller.db.species),
#                         links=["END", "START"], linktexts=["Quit", "Back to start"],
#                        keywords=["Q", "B"])
        
        node4 = MenuNode("alignment",
                         links=["alignment_change", None, "END", "START"],
                         selectcmds=[None, CmdAlignmentDelete, None, None],
                         linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                         keywords=["C", "D", "Q", "B"],
                         code="self.caller.msg('Current Alignment: %s' % self.caller.db.alignment)")
        node4b = MenuNode("alignment_change",
                          text="What do you want your alignment to be? (Space + CR to make no changes)",
                          links=["START", "END"],
                          keywords=[CMD_NOINPUT, CMD_NOMATCH],
                          selectcmds=[CmdBackToAlignment, CmdAlignmentSelect],
                          nodefaultcmds=True,
                          code="self.caller.msg('Current Alignment: %s' % self.caller.db.alignment)")

        node5 = MenuNode("job",
                         links=["job_change", None, "END", "START"],
                         selectcmds=[None, CmdJobDelete, None, None],
                         linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                         keywords=["C", "D", "Q", "B"],
                         code="self.caller.msg('Current Job: %s' % self.caller.db.job)")
        node5b = MenuNode("job_change",
                          text="What do you want your job to be? (Space + CR to make no changes)",
                          links=["START", "END"],
                          keywords=[CMD_NOINPUT, CMD_NOMATCH],
                          selectcmds=[CmdBackToJob, CmdJobSelect],
                          nodefaultcmds=True,
                          code="self.caller.msg('Current Job: %s' % self.caller.db.job)")

        node6 = MenuNode("age",
                         links=["age_change", None, "END", "START"],
                         selectcmds=[None, CmdAgeDelete, None, None],
                         linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                         keywords=["C", "D", "Q", "B"],
                         code="self.caller.msg('Current Age: %s' % self.caller.db.age)")
        node6b = MenuNode("age_change",
                          text="What do you want your age to be? (Space + CR to make no changes)",
                          links=["START", "END"],
                          keywords=[CMD_NOINPUT, CMD_NOMATCH],
                          selectcmds=[CmdBackToAge, CmdAgeSelect],
                          nodefaultcmds=True,
                          code="self.caller.msg('Current Age: %s' % self.caller.db.age)")
        
        node7 = MenuNode("apparent_age",
                         links=["apparent_age_change", None, "END", "START"],
                         selectcmds=[None, CmdApparentAgeDelete, None, None],
                         linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                         keywords=["C", "D", "Q", "B"],
                         code="self.caller.msg('Current Apparent Age: %s' % self.caller.db.apparent_age)")
        node7b = MenuNode("apparent_age_change",
                          text="What do you want your apparent age to be? (Space + CR to make no changes)",
                          links=["START", "END"],
                          keywords=[CMD_NOINPUT, CMD_NOMATCH],
                          selectcmds=[CmdBackToApparentAge, CmdApparentAgeSelect],
                          nodefaultcmds=True,
                          code="self.caller.msg('Current Apparent Age: %s' % self.caller.db.apparent_age)")
        
        node8 = MenuNode("mane",
                         links=["mane_change", None, "END", "START"],
                         selectcmds=[None, CmdManeDelete, None, None],
                         linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                         keywords=["C", "D", "Q", "B"],
                         code="self.caller.msg('Current Mane: %s' % self.caller.db.mane)")
        node8b = MenuNode("mane_change",
                          text="What do you want your mane to be? (Space + CR to make no changes)",
                          links=["START", "END"],
                          keywords=[CMD_NOINPUT, CMD_NOMATCH],
                          selectcmds=[CmdBackToMane, CmdManeSelect],
                          nodefaultcmds=True,
                          code="self.caller.msg('Current Mane: %s' % self.caller.db.mane)")

        node9 = MenuNode("eyes",
                         links=["eyes_change", None, "END", "START"],
                         selectcmds=[None, CmdEyesDelete, None, None],
                         linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                         keywords=["C", "D", "Q", "B"],
                         code="self.caller.msg('Current Eye Color: %s' % self.caller.db.eyes)")
        node9b = MenuNode("eyes_change",
                          text="What color do you want your eyes to be? (Space + CR to make no changes)",
                          links=["START", "END"],
                          keywords=[CMD_NOINPUT, CMD_NOMATCH],
                          selectcmds=[CmdBackToEyes, CmdEyesSelect],
                          nodefaultcmds=True,
                          code="self.caller.msg('Current Eye Color: %s' % self.caller.db.eyes)")
        
        node10 = MenuNode("cutie_mark",
                          links=["cutie_mark_change", None, "END", "START"],
                          selectcmds=[None, CmdCutieMarkDelete, None, None],
                          linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                          keywords=["C", "D", "Q", "B"],
                          code="self.caller.msg('Current Cutie Mark: %s' % self.caller.db.cutie_mark)")
        node10b = MenuNode("cutie_mark_change",
                           text="What do you want your cutie mark to be? (Space + CR to make no changes)",
                           links=["START", "END"],
                           keywords=[CMD_NOINPUT, CMD_NOMATCH],
                           selectcmds=[CmdBackToCutieMark, CmdCutieMarkSelect],
                           nodefaultcmds=True,
                           code="self.caller.msg('Current Cutie Mark: %s' % self.caller.db.cutie_mark)")

        node11 = MenuNode("sexuality",
                          links=["sexuality_change", None, "END", "START"],
                          selectcmds=[None, CmdSexualityDelete, None, None],
                          linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                          keywords=["C", "D", "Q", "B"],
                          code="self.caller.msg('Current Sexuality: %s' % self.caller.db.sexuality)")
        node11b = MenuNode("sexuality_change",
                           text="What do you want your sexuality to be? (Space + CR to make no changes)",
                           links=["START", "END"],
                           keywords=[CMD_NOINPUT, CMD_NOMATCH],
                           selectcmds=[CmdBackToSexuality, CmdSexualitySelect],
                           nodefaultcmds=True,
                           code="self.caller.msg('Current Sexuality: %s' % self.caller.db.sexuality)")

        node12 = MenuNode("height",
                          links=["height_change", None, "END", "START"],
                          selectcmds=[None, CmdHeightDelete, None, None],
                          linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                          keywords=["C", "D", "Q", "B"],
                          code="self.caller.msg('Current Height: %s' % self.caller.db.height)")
        node12b = MenuNode("height_change",
                           text="What do you want your height to be? (Space + CR to make no changes)",
                           links=["START", "END"],
                           keywords=[CMD_NOINPUT, CMD_NOMATCH],
                           selectcmds=[CmdBackToHeight, CmdHeightSelect],
                           nodefaultcmds=True,
                           code="self.caller.msg('Current Height: %s' % self.caller.db.height)")

        node13 = MenuNode("weight",
                          links=["weight_change", None, "END", "START"],
                          selectcmds=[None, CmdWeightDelete, None, None],
                          linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                          keywords=["C", "D", "Q", "B"],
                          code="self.caller.msg('Current Weight: %s' % self.caller.db.weight)")
        node13b = MenuNode("weight_change",
                           text="What do you want your weight to be? (Space + CR to make no changes)",
                           links=["START", "END"],
                           keywords=[CMD_NOINPUT, CMD_NOMATCH],
                           selectcmds=[CmdBackToWeight, CmdWeightSelect],
                           nodefaultcmds=True,
                           code="self.caller.msg('Current Weight: %s' % self.caller.db.weight)")

        node14 = MenuNode("short_desc",
                          links=["short_desc_change", None, "END", "START"],
                          selectcmds=[None, CmdShortDescDelete, None, None],
                          linktexts=["Change Value", "Delete Value", "Quit", "Back to start"],
                          keywords=["C", "D", "Q", "B"],
                          code="self.caller.msg('Current Short Desc: %s' % self.caller.db.short_desc)")
        node14b = MenuNode("short_desc_change",
                           text="What do you want your short desc to be? (Space + CR to make no changes)",
                           links=["START", "END"],
                           keywords=[CMD_NOINPUT, CMD_NOMATCH],
                           selectcmds=[CmdBackToShortDesc, CmdShortDescSelect],
                           nodefaultcmds=True,
                           code="self.caller.msg('Current Short Desc: %s' % self.caller.db.short_desc)")

        menu = MenuTree(self.caller, nodes=(node0, node1, node2, node3, node4, node5, node6, node7,
                        node8, node9, node10, node11, node12, node13, node14,
                        node1b, node2b, node4b, node5b, node6b, node7b,
                        node8b, node9b, node10b, node11b, node12b, node13b, node14b))
        menu.start()
