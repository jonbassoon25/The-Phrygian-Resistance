# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("You", color="#f00032")
define regime_leader = Character("Paladin Victor Franz", color="#880000")
define resistance_fighter = Character("Robert Gustav", color="#00d0d0")
define unnamed_official = Character("Military Official", color="#990000")

define content_censored = False
define document_read = False
define bloodnote_read = False

# The game starts here.

label start:
    play music "Introduction Background.mp3" loop volume 0.5

    scene earth
    with fade
    "2089, the last year of the old world..."
    "The year of a war brought on by the limitless greed of superpowers, and the limited resources of the planet to which they were confined."
    
    scene war modern
    with dissolve

    "The war was the most destructive in the history of humanity:"
    scene combat modern
    with dissolve
    "Hundreds of millions of soldiers forced into the meat grinders of machine gun fire."
    scene bombing modern
    with dissolve
    "Conventional strikes of unfathomable scale."
    scene destruction conventional
    with dissolve
    "Billions of lives were lost."

    "But as the war raged on, the great powers got desperate for a quick victory."
    "Their resources completely depleted, their land in a state of near complete destruction, and their populations in a state of irreparable decay."
    
    scene black
    with dissolve
    "But they had yet to turn to their most destructive technology—one that allowed man to wield the power of stars.{w=0.5} Once only seen as a deterrent, it became the offensive weapon of choice."
    
    "It was unclear who fired first;{w=0.25} but it did not matter...{w=0.5} The effects were catastrophic."
    # Raw nuclear test footage for audio: https://catalog.archives.gov/id/25979
    #play sound "Nuclear Explosion - short" noloop
    play sound "Nuclear Explosion - long.mp3" noloop
    scene nuclear explosion
    with Fade(0, 1, 4, color="#FFF")
    "The great cities of the world were reduced to ash under balls of nuclear fire."
    scene firestorm
    with dissolve
    "With smaller nations immediately capitulating as their lands erupted into blazing infernos."

    "But still, these superpowers survived."
    "Their land decimated,{w=0.1} resources non-existent,{w=0.1} and populations nearly wiped off the face of the earth."

    scene nuclear dustcloud
    with dissolve
    "Their world enveloped in an impenetrable dark cloud of ash;{w=0.2} the seasons forgotten in favor of a harsh winter that would last for the next 500 years."

    scene military formation
    with dissolve
    "But their militaries{w=0.25}—their militaries still stood strong."
    "And so began the last days of their control."

    scene looting soldiers
    with dissolve
    "The land of smaller countries was annexed and ransacked for paltry sums of resources.{w=0.3}\nBut that was not enough to satisfy the growing demands of the starved empires."

    "As their stockpiled resources dwindled, modern technologies became too expensive to field, and tactics slowly devolved until there were only infantrymen..."
    
    scene trenches
    with fade
    "Infantrymen and hundreds of thousands of miles of curving trenches."
    
    scene undersupplied soldiers
    with dissolve
    "But all sides knew the collapse of their fronts was inevitable."
    "Their men only stayed under threat of death and for the measly rations that they earned."
    "And their ammunition stockpiles were almost completely gone."

    scene asian front
    with dissolve
    "The Asian fronts were the first to collapse."
    "The supplies sent by the superpowers being redirected elsewhere;{w=0.2} the tens of millions of war-torn souls were forgotten."
    "Without resupply they died in the freezing deserts of central Asia,{w=0.1} and the sub-zero forests of Northern Siberia."

    scene retreating soldiers
    with dissolve
    "Soon, too, collapsed the fronts in Africa,{w=0.2} South America,{w=0.2} and Australia;{w=0.4} their resources completely spent on the products of war."
    "The great powers{w=0.25}—The only powers{w=0.25}—of the earth consolidated their resources to fight until the very last man perished."

    scene stranded island garrisons
    with dissolve
    "Millions of men were forgotten on the uninhabitable islands of the seven seas."
    scene african front
    with dissolve
    "And millions more perished in the deserts of Arabia and in the mountains of northern Europe."

    scene late trenches
    with dissolve
    "Slowly, as the main fronts of the war decayed, the great powers slowly lost their grasp on their soldiers."
    "Soldiers who had only stayed to acquire sustenance in the cold nuclear wasteland that used to be their world."

    scene black
    with dissolve
    "Until,{w=0.2} one day,{w=0.2} after billions of casualties:{w=0.5} the fighting stopped."
    "Leaving the victor alone and uncontested."

    "And that victor?{w=0.8}\nThey called themselves 'The Regime'."
    "And they were the sole power of the broken world."
    "They are the sole power of the broken world."
    "They are the sole power of this world."
    stop music fadeout 1.0
    "..."


label beginning:
    scene black
    with fade
    play sound "Alarm.mp3" loop
    scene bedroom
    with fade

    "You wake up to the sound of your government-provided alarm clock on the brisk morning of July 24th, 2137."
    stop sound fadeout 0.5
    play music "Dystopian-Background.mp3" fadein 2.0 volume 0.15
    
    menu censor_content:
        "And as you get out of bed you face your first choice, which is displayed via the screen inside your eyes."
        "Censor Graphic Images":
            $ content_censored = True
        "Don't Censor Graphic Images":
            $ content_censored = False
    
    "You continue about your morning routine before promptly arriving at your place of work."

    scene city buildings
    with dissolve
    "An unassuming skyscraper in the center of Europe's only city."

    scene office
    with dissolve
    "You enter the building and find your place in The Department of Information."
    "Your task today is to help with the removal of documents published by the 'Fake New Organizations' of the past."

    scene full desk
    with dissolve
    "You certainly have your work cut out for you today."
    
    scene cubicle
    with dissolve
    "You begin the painstaking process of bringing these documents to your desk to sort, and then you begin sorting; removing any documents published by organizations that were determined to be 'Fake news'."

    show classified folder at truecenter
    with dissolve
    "After a number of hours of painful work, you come across a folder labeled 'Classified' with no news organization listed on it."

    menu decision_one:
        "What do you do?"
        "Open the folder and read it's contents before destroying it":
            $ document_read = True
        "Don't open the folder and destroy it":
            $ document_read = False
    
    hide classified folder
    with dissolve
    if not document_read:
        play sound "paper-shredder.mp3" volume 1.0 #this is intentional
        "You destroy the document without even taking it out of the folder, and continue on with your day."
        stop sound fadeout 1.0
        jump post_document


label reading_document:
    show classified materials at truecenter
    with dissolve
    "The Document" "Messages from Project Falcon: Classified{w=0.5}\nFor the eyes of Regime Leadership {b}Only{/b}"
    play sound "page-flip.mp3" volume 0.1
    "The Document" "April 17th, 2104 - The collection of resources continues to yield little to none of the components required for this project."
    "The Document" "It's a miracle we can find anything useful in this wasteland."
    play sound "page-flip.mp3" volume 0.1
    "The Document" "July 23rd, 2104 - Incremental progress continues on the collection of resources; however, rocket fuel has become increasingly hard to come by."
    "The Document" "Our scouts have also reported sightings of humanoid figures in the distance. This has not been confirmed."
    play sound "page-flip.mp3" volume 0.1
    "The Document" "I believe The Regime continues to be the only group with the resources to stay alive outside of our cities."
    play sound "page-flip.mp3" volume 0.1
    "The Document" "September 14th, 2104 - The collection of resources is almost complete, and we are setting up camp to pass the winter."
    "The Document" "Our scouts have reported seeing dim lights in the distance the last few nights. We might not be alone out here."
    play sound "page-flip.mp3" volume 0.1
    "The Document" "September 23rd, 2104 - A group of unidentified individuals assaulted the camp last night. They were promptly dealt with."
    "The Document" "However, it is clear that the military must be prepared to fight what could possibly be another great war in the near future."
    play sound "page-flip.mp3" volume 0.1
    "The Document" "November 11th, 2104 - Our collection of rations disappeared last night. Someone snuck into the camp without being detected by the lookouts."
    "The Document" "We most likely won't make it through the winter. The coordinates of our camp are attached in this letter so that the resources we collected may be recovered."
    "The Document" "Before that can happen, it is clear that whoever blocked our progress must be dealt with first. {w=0.5}Included is a note we found in the raided storeroom, stained with the blood of its guard."
    "\[End of the Document]"

    "You notice a small note stuck on the back of the document"
    menu read:
        "Do you read it?"
        "Yes":
            $ bloodnote_read = True
            show bloodstained note at truecenter
            with dissolve
            "Bloodstained Note" "Ζήτω οι Φρύγες. Long Live the Phrygian Resistance!"
        "No":
            $ bloodnote_read = False

    hide bloodstained note
    hide classified materials
    with dissolve
    play sound "paper-shredder.mp3" volume 0.2
    "As you destroy the document so that nobody could notice you reading it, you contemplate it's meaning."
    stop sound fadeout 1.0
    "You had always been told that The Regime was alone in the world. It's savior."
    "But was that really the case?"

    if bloodnote_read:
        "Who even are the Phrygians anyways?"

    "Regardless, you decide to continue your day as normal so you don't appear suspicious."


label post_document:
    play sound "buzzer.mp3" volume 0.4
    "You soon hear the notification for lunch, allowing you to put your work aside to get food."

    scene office hallway
    with dissolve
    "However, on your way to the building's cafeteria, you are stopped by a military official."

    show military official
    with dissolve
    unnamed_official "Hello sir, are you Oskar Gottfrïed?"

    "He speaks again without giving you a change to answer."

    unnamed_official "You have been selected for conscription into the Global Coalition Army. Follow me."

    menu follow:
        "Do you follow him?"
        "Yes":
            "You follow him to a military building."
        "No":
            unnamed_official "Come on now, let's go."
            "He grabs you by the arm and drags you with him to a military building."
    
    scene conscription office
    with dissolve
    "You are assigned your military equipment: 2 sets of clothes, a surprisingly light bulletproof vest, and a rifle."
    
    scene trucking
    with dissolve
    "And then you are shipped away from the city, and into the surrounding wasteland."

    scene black
    with fade
    "Later than night you are woken up by a man whom you have never seen before."

    "???" "Are you a new conscript?"

    menu question: #the progression of menu names is really something spectacular, isn't it.
        "Yes":
            "???" "Did you read the document that was sent to you secretly? The one about Project Falcon?"
            if document_read:
                menu question2:
                    "Yes":
                        "???" "So then you know why you were conscripted to fight."
                    "No":
                        "???" "I see... You passed this inspection."
                        "He quickly leaves."
                        jump immoral_path
            else:
                menu question2b:
                    "No":
                        "???" "I see... You passed this inspection."
                        "He quickly leaves."
                        jump immoral_path
        "No":
            "???" "Strange, I could've sworn you were."
            "He walks away."
            jump immoral_path
    
    "???" "The regime has enemies. The Phrygana."
    "???" "They are planning to assault one of their villages tomorrow. One full of innocent people without any protection."
    "???" "I'm asking you for your help in telling The Phrygana of this before it is too late."
    "???" "Will you help?"
    menu question3:
        "Yes":
            "???" "Good, come with me. Let's get out of here."
        "No":
            "???" "You're a sick person. Serving the regime without a thought of anyone else."
            "He quickly leaves."
            jump immoral_path
    
    "???" "By the way, I'm [resistance_fighter]."


label side_with_revolutionaries:
    resistance_fighter "Be careful not to wake anyone. We don't want to get caught sneaking out."
    "Exit the barracks with [resistance_fighter], careful not to disturb the sleeping soldiers."
    "However, as you sneak out of the camp's walls, you are spotted by the perimeter guards."
    "They shout 'Halt! What are you doing?!' and proceed to chase to you as [resistance_fighter] pulls you forward."
    
    "Bullets whiz past you as you run away from the camp."
    "As you reach the edge of a forested area, [resistance_fighter] is hit and falls to the ground, groaning."

    menu decision:
        "Do you stay and help him?"
        "Yes":
            "You kneel down next to him, stopping the bleeding as soldiers from the camp run towards you."
            jump helpful_death
        "No":
            "You leave him behind and run into the forest."

    "As you run through the forest, you are grabbed from behind and pulled to the ground."
    "A bag is put over your head and you are handcuffed."
    scene black
    with fade
    
    "You are dragged through the forest and eventually feel yourself be brought inside of a building."
    "Soon later, you are placed on a chair and the bag is removed from your head."

    #scene interrogation
    #show interrogator

    "???" "Hello."
    "???" "Is there anything you would like to tell us? Your reason for fleeing the camp?"

    menu question4:
        ""
        "Yes, The Regime is planning to assault a village full of civilians.":
            "He looks at you skeptically."
        "No.":
            jump questioned_allegiance
            
    "And why should we believe you?"
    menu question5:
        ""
        "I know of project Falcon.":
            
        "{i}Stare blankly{/i}":
            "He shakes his head, sighs, and leaves."
            jump servant_death


label questioned_allegiance:


label servant_death:


label helpful_death:
    "As the soldiers get closer, they raise their rifles and fire on you and [resistance_fighter]."
    "Both of you are killed."
    jump death


label immoral_path:
    "Early the next morning, you are woken up at the break of dawn."


label death:
    "You have died."

    # This ends the game.
    return
