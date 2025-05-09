# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("Oskar Gottfried", color="#f00032")
define regime_leader = Character("Paladin Victor Franz", color="#880000")
define resistance_fighter = Character("Robert Manfrïed", color="#00d0d0")

define content_censored = False

# The game starts here.

label start:
    "2089, the last year of the old world..."
    "The year of a war brought on by the limitless greed of superpowers, and the limited resources of the planet to which they were confined."
    
    "The war was the most destructive in the history of humanity."
    "Hundreds of millions of soldiers forced into the meat grinders of machine gun fire.{w=0.5} Conventional strikes of unfathomable scale.{w=0.75}\nBillions of lives lost."

    "But as the war raged on, the great powers got desperate for a quick victory.{w=0.2} Their resources completely depleted, their land in a state of near complete destruction, and their populations in a state of irreparable decay."
    "But they had yet to turn to their most destructive technology—one that allowed man to wield the power of stars.{w=0.5} One that had once only been seen as a deterrent, but that had now become the offensive weapon of choice."
    
    "It was unclear who fired first;{w=0.25} nor did that matter...{w=0.5} The effects of the decision were catastrophic."
    #Explosion sound & image
    "The great cities of the world were reduced to ash under balls of nuclear fire."
    "The smaller nations immediately capitulating as their lands erupted into blazing infernos."

    "But still, these superpowers survived."
    "Their land decimated,{w=0.1} resources non-existent,{w=0.1} and populations nearly wiped off the face of the earth."
    "Their world enveloped in an impenetrable dark cloud of ash;{w=0.2} the seasons forgotten in favor of a harsh winter that would last for the next 500 years."

    "But their militaries{w=0.25}—their militaries still stood strong."
    "And so began the last days of their control."

    "The land of smaller countries was annexed and ransacked for paltry sums of resources.{w=0.3}\nBut that was not enough to satisfy the growing demands of the starved empires."

    "As their stockpiled resources dwindled, modern technologies became too expensive to field, and tactics slowly devolved until there were only infantrymen."
    #Scene change to WWI trenches
    "Infantrymen and hundreds of thousands of miles of curving trenches."

    "But all sides knew the collapse of their fronts was inevitable."
    "Their men only stayed under threat of death and the measly rations that they earned."
    "And their ammunition stockpiles were almost completely gone."

    "The Asian fronts were the first to collapse."
    "The supplies sent by the superpowers being redirected elsewhere;{w=0.2} the tens of millions of war-torn souls were forgotten."
    "Without resupply they would soon die in the freezing deserts of central asia,{w=0.1} and the sub-zero forests of northern siberia."

    "Soon, too, collapsed the fronts in Africa,{w=0.2} South America,{w=0.2} and Australia;{w=0.4} their resources completely spent on the products of war."
    "The great powers{w=0.25}—The only powers{w=0.25}—of the earth consolidating their resources to fight until the very last man perished."

    "Millions of men were forgotten on the uninhabitable islands of the seven seas."
    "And millions more perished in the deserts of Arabia and in the mountains of northern Europe."

    "Slowly, the main fronts of the war decayed.{w=0.4}\nThe great powers slowly losing their grasp on their soldiers."
    "Soldiers who had only stayed to aquire sustenance in the cold nuclear wasteland that used to be their world."

    "Until,{w=0.2} one day,{w=0.2} after billions of casualties:{w=0.5} the fighting stopped."
    "Leaving the victor alone and uncontested."

    "And that victor?{w=0.8}\nThey called themselves 'The Regime'."
    "And they were the sole power of the broken world."
    "They are the sole power of the broken world."
    "They are the sole power of this world."
    "..."


label beginning:
    "You, [player], wake up to the sound of your government-provided alarm clock on the brisk morning of July 24th, 2137."
    
    menu censor_content:
        "And as you get out of bed you face your first choice, which is displayed via the screen inside your eyes."
        "Censor Graphic Images":
            $ content_censored = True
        "Don't Censor Graphic Images":
            $ content_censored = False
    
    "You continue about your morning routine before arriving at your place of work."
    "A large skyscraper in the center of the world's only city."

    
        

    # This ends the game.
    return
