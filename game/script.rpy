## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

image chara default = "testChara.png"

define s = Character('???', color = "#ffffff")

init:
    image bg black = "#000000"

## The game starts here.

label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg black

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    show chara default

    ## These display lines of dialogue.

    ## I think I'll make use of no label for player... I guess
    "..."

    s "..."

    s "Who are you?"

    menu:
        "Nobody.":
            jump nobody
            
        "I'm you.":
            jump you
            
    label nobody:
        s "I see... That's fine."
        s "Then..."
        jump end
        
    label you:
        s "...what?"
        jump end
        
    label end:
        "Just leave me alone."
        
    ## This ends the game.

    return
