# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You")
define anon = Character("???")
define mom = Character("Mom")
define hli = Character("Hli")
define husband = Character("Elderly Husband")
define wife = Character("Elderly Wife")
define mc = Character("Stage MC")
define imi = Character("Imi")
define actor = Character("Actor")
define granny = Character("Medicine Granny")
define rep = Character("Booth Representative")
define amy = Character("Amy")
define anime = Character("Anime Merch Booth Owner")
define fbi = Character("FBI Agent")
define rose = Character("Rose Booth Owner")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "I'm testing if these changes have applied..."
    e "testing some more gitignore stuff... "

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
