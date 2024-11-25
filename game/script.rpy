# The script of the game goes in this file.

# CHARACTER VARIABLES ========================================================================================================================================================================
define you = Character("You")
define anon = Character("???")
define anon2 = Character("???")
define anon3 = Character("???")
define mom = Character("Mom")
define hli = Character("Hli")
define husband = Character("Elderly Husband")
define wife = Character("Elderly Wife")
define mc = Character("Stage MC")
define imi = Character("Imi")
define actor = Character("Actor")
define granny = Character("Medicine Granny")
define rep = Character("Booth Representative")
define claire = Character("Claire")
define anime = Character("Anime Merch Booth Owner")
define fbi = Character("FBI Agent")
define rose = Character("Rose Booth Owner")

# IMAGE SPRITES!  ========================================================================================================================================================================
image momI = "mom.PNG"
image hliI = "hli.PNG"
image imiI = "imi.PNG"
image claireI = "claire.PNG"
image animeI = "anime.PNG"
image repI = "rep.PNG"
image fbiI = "fbi.PNG"
image coupleI = "couple.PNG"
image actorI = "actor.PNG"
image grannyI = "granny.PNG"
image roseI = "rose.PNG"
image mcI = "mc.PNG"
image guyI = "guy.PNG"
image anonI = "anon.PNG"

image rando1 = "rando1.png"
image rando2 = "rando2.png"
image rando3 = "rando3.png"
image keychainI = "keychain.png"

image toss = "tossref.png"
image farm = "farmref.png"



image balltossbg:
    "balltossbg.png"
    xysize(1920,1080)
    
image stagebg:
    "stagebg.png"
    xysize(1920,1080)
    
image stageclosebg:
    "stageclosebg.png"
    xysize(1920,1080)
    
image boothbg:
    "boothbg.jpg"
    xysize(1920,1080)
    
image garagebg:
    "garagebg.png"
    xysize(1920,1080)
    
image garagedarkbg:
    "garagedarkbg.png"
    xysize(1920,1080)

image roombg:
    "roombg.png"
    xysize(1920,1080)

image livingroombg:
    "livingroombg.png"
    xysize(1920,1080)

image enterbg:
    "enterbg.png"
    xysize(1920,1080)

image centerbg:
    "centerbg.png"
    xysize(1920,1080)

image animeboothbg:
    "animeboothbg.png"
    xysize(1920,1080)

image claireboothbg:
    "claireboothbg.png"
    xysize(1920,1080)


image actorboothbg:
    "actorboothbg.png"
    xysize(1920,1080)

image grannyboothbg:
    "grannyboothbg.png"
    xysize(1920,1080)

image imiboothbg:
    "imiboothbg.png"
    xysize(1920,1080)

image rosesboothbg:
    "rosesboothbg.png"
    xysize(1920,1080)

image animeboothbg:
    "animeboothbg.png"
    xysize(1920,1080)

image drivebg:
    "drivebg.png"
    xysize(1920,1080)

image doodelor:
    "doodlelor.png"
    xysize(1920,1080)




# The game starts here. ========================================================================================================================================================================

# 0.0 Start - Morning
label start:
    default notTalkToCouple = True
    default notTalkToGirl = True
    default notTalkToGuy = True
    default notCompletedStage = True
    default notCompletedBall = True

    default notTalkToAnime = True
    default notTalkToInsurance = True
    default notTalkToMed = True
    default notTalkToActor = True
    default notTalkToImi = True

    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene balltossbg
    #with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # Start - Morning
    stop music
    scene doodlelor
    with fade
    pause 3
    scene roombg
    with fade

    play music "Viktor Kraus - Blueberries.mp3"

    you "{i}groan{/i} what time is it..."
    show momI
    mom "Wake up!!! It's time to go to the Hmong New Year!"
    mom "Get out of bed sleepy head!"
    hide momI
    you "{i} urgggh"
    you "It's that time of the year again..."
    you "The Hmong New Year..."
    show farmref
    you "It's a yearly celebration that was traditionally meant to honor a year of harvest..."
    hide farmref
    show tossref
    you "... and be a grounds for finding love with the infamous ball toss game..."
    hide tossref
    you "... But I'm not so lucky-"
    scene drivebg
    play sound "cardrive.mp3" volume 1.5
    pause 4
    scene garagebg
    with fade
    show momI
    mom "Hurry up! We'll be late!!!"

        # Screen changes to parked car in parking garage; heels clicking sound
    show momI
    mom "You're so slow- we'll meet you inside."
    play sound "running.wav"
    hide momI
    you "{i}groan{/i}"
    you "..."
    you "Well, I guess I better get going."

        # Screen shakes and blacks out.
    scene garagedarkbg
    "!!!"
    you "What was that!!?"
    show anonI
    anon "AHHHHH!!!"
    "You feel a hand brush past your shoulder and squeeze your arm. "
    anon "Why are the lights off!?!"
    anon "Did a power outage really happen at the Ex-Sell Energy Center!?"
    "The voice of a girl..."
    "You haven't heard that in a long time..."
    you "Um.. excuse me..."
    "The girl releases her hand from your grip."
    "It's dark but you can hear the kindness in her voice."
    anon "Ahh, sorry! I'm really scared of the dark."
    anon "I grabbed you without realizing it..."
    play sound "heartbeat.mp3"
    "You feel your face growing red..."
    "Maybe this year isn't as bad as you thought."

    menu:
        "What should you do?"

        "Ask her to accompany you during the New Year":
            jump start_1

        "Grab her hand":
            jump start_2

# 0.1.1 Ask her to accompany you during the New Year
label start_1:
    you "Hey... um-"
    hide anonI
    anon "I gotta go!!!" #SOUND
    play sound "running.wav"
    scene garagebg
    "The lights flicker on again and you're standing alone in the parking garage."
    "Who was that..."
    show keychainI
    "You look down and notice a keychain and pick it up..."
    jump keychain

# 0.1.2 Grab her hand
label start_2:
    "You feel the sweat in your pits swell up as you take a deep breath and reach for her hand."
    "Exhilarated by the feeling of love, your hand shoots out on its own and reaches for something."
    "It's not her hand."
    "It's a keychain???"
    anon "Ack!!!" #SOUND
    play sound "running.wav"
    hide anonI
    "It sounds like she ran off..."
    "The lights flicker on again and you're standing alone in the parking garage."
    scene garagebg
    show keychainI
    "You look at the keychain."
    jump keychain

# 0.2 Keychain
label keychain:
    "This keychain..."
    "This is your answer to love."
    you "I need to find its original owner."
    "Empowered by this new purpose, you march into the Ex-Sell Energy Center- ready to find the love of your life."
    hide keychainI
    jump center 

# 1.0 Center
label center:
    scene centerbg
    if notCompletedBall or notCompletedStage:
        "This place is crowded..."
        "How are you going to find her..."
        menu:
            "Where should you look?"

            "The Ball Toss Spot" if notCompletedBall:
                jump balltoss
            "The Main Stage" if notCompletedStage:
                jump stage
    else:
        jump main_area

# 1.1.1 Ball Toss Spot =======================================================================================================================
label balltoss:
    scene balltossbg
    you "Maybe she's somewhere in the crowd."
    you "I'll ball toss around and see if she's here."
    jump balltoss_2

label balltoss_2:
    scene balltossbg
    if notTalkToCouple or notTalkToGirl or notTalkToGuy:
        menu:
            you "Hmmm, who to ball toss with..." 

            "An Old Couple" if notTalkToCouple:
                jump couple

            "A random girl" if notTalkToGirl:
                jump girl

            "A random guy" if notTalkToGuy:
                jump guy
    else:
        you "Seems like I've already talked to everyone..."
        you "Better try something else..."
        $ notCompletedBall = False
        jump center

# 1.1.1.1 Old Couple
label couple:
    $ notTalkToCouple = False
    show coupleI
    you "Hmm, maybe I can talk to this couple. They look nice."
    "As you approach the couple, you hear them talking."
    wife "Ohh, cov hluas no mas... tsis keej kiag li os!"
    husband "Oi! Txoj hais li kos mas..."
    "You don't know how to speak Hmong... "
    "Better stay away from that conversation."
    hide coupleI
    jump balltoss_2

# 1.1.1.2 Random Girl
label girl:
    $ notTalkToGirl = False
    show hliI
    "This girl doesn't look too bad."
    "And it seems like she's waiting for someone too!"
    you "Oh hey... I was wondering if you wanted to ball toss together."
    anon "Hmm?"
    anon "Oh, hi- sorry. I didn't notice you there."
    anon "I was just looking around..."
    you "Oh.. Um are you looking for someone?"
    anon "Yes."
    anon "..."
    you "Can I maybe help you?"
    anon "Ahh no, it's kind of weird."
    anon "I randomly met him earlier at the parking ramp, but didn't get his phone number."
    "!!!"
    you "I'm looking for someone too!"
    you "I also ran into her at the parking ramp."
    anon "{i}gasp{/i}"
    you "Is this perhaps yours?"
    "You pull out the keychain and the girl inspects it."
    "She looks at it closely, furrowing her brows."
    anon "Ummm, no."
    anon "And I told you, I'm looking for someone not {i}something{/i}"
    you "What?"
    anon "You know what- I'm Hli."
    hli "If you happen to run into someone looking for me, could you direct them to me?"
    hli "I'll just be over there."
    you "..."
    you "What if I'm the one you're looking for?"
    hli "I'm not so sure.. That keychain doesn't belong to me."
    you "Oh.. okay"
    "Hmm, weird."
    "It would've been perfect if Hli was the one you were looking for- but I guess that'd make the game too easy..."
    hide hliI
    jump balltoss_2

# 1.1.1.2 Random Guy
label guy:
    $ notTalkToGuy = False
    show guyI
    "This guy looks knowledgable. Maybe he'll know something helpful."
    you "Excuse me."
    anon "Woah!!!"
    you "Sorry, um- I just have a question."
    anon "Woah woah woah. Slowwwww down."
    anon "I don't go that way."
    anon "And even if I did, you're definitely not my type."
    anon "I prefer taller guys."
    anon "..."
    anon "If I was- {i}you know...{/i} not straight."
    anon "But I'm 100 percent straight dude"
    you "Okay..."
    you "Can I just ask a question?"
    anon "Okay okay, but I already warned you: I'm straight."
    you "Uh huh- sure okay whatever."
    you "Anyway, I'm looking for a girl, any chance you know someone who owns this keychain?"
    you "Or seen anyone who's looking for one..."
    "You pull out the keychain for the guy to see."
    "He closely inspects it."
    anon "Oh!! Yeah- I've seen these before."
    anon "They're in the small shopping area to the left."
    anon "But I think that area's currently packed right now..."
    anon "Some Hmong actor from Laos is hosting a booth or something."
    anon "People are lined up like crazy."
    you "Oh... but do you know who this might belong to?"
    anon "Ehh, no. Just seen it being sold at a booth."
    anon "Maybe the owner can help you. I don't know."
    anon "..."
    anon "You know I like girls right?"
    you "..."
    "This is getting weird. You leave."
    hide guyI
    jump balltoss_2


            
        


# 1.1.2 Main Stage =======================================================================================================================
label stage:
    scene stagebg
    "You head to the main stage- maybe you'll find luck there."
    show mcI
    mc "Please give the singer Cha Lis another round of applause!" #SOUND
    mc "..."
    mc "Alright, now I would like to welcome a very, very special guest."
    mc "The {i}very{/i} senator of our {i}xeev{/i} Minnesota, Imi Clobasure!!!!" 
    hide mcI
    #SOUND
    "You watch as Imi walks up on stage..."
    show imiI
    "She looks somewhat familiar."
    imi "Thank you, thank you."
    #SOUND 
    imi "Thank you, thank you."
    imi "Wow, it's so great to be here."
    imi "Thank you, thank you."
    you "Wait a minute..."
    you "That voice..."
    you "It sounds familiar!!!"
    play sound "heartbeat.mp3"
    "You feel your heart start to pump."
    "It's a voice full of kindness- just like at the parking garage..."
    you "Is this a coincidence?"
    you "I need to take a closer look."
    $ notCompletedStage = False
    menu:
        "What should you do?"

        "Go up to the stage":
            jump stage_front
        "Continue observing from afar":
            jump afar

# 1.1.2.1 Go Up To Stage
label stage_front:
    scene stageclosebg
    "You decide to go up to the stage."
    "There's no better way to know than being up close."
    # SCENE
    "Senator Imi is still giving her speech."
    you "Wow, her voice is so..."
    you "Official sounding..."
    show imiI
    imi "Thank you again for having me."
    imi "Nyob zoo xyoo tshiab!"
    "Your muscles tense up."
    "The heavy English accent in her attempt to speak Hmong catches you off guard."
    "This voice is way too familiar..."
    #SOUND
    "By the time you look up, Imi has already walked off stage."
    hide imiI
    "All you see is her back"
    "Getting smaller and smaller..."
    "Then you hear a voice."
    show repI
    anon "I love our senator."
    you "Huh?"
    anon "Oh what- sorry. I didn't realize I said that aloud."
    anon "Imi's just {i}such{/i} an amazing leader..."
    anon "..."
    anon "If you want, you should visit her at her booth later in the evening."
    anon "I heard she'll be giving out keychains."
    you "Keychains, huh..."
    hide repI
    "It looks like the remaining stage line-up is just beauty pageant stuff... "
    "Let's go back and check out the main area."
    jump center


# 1.1.2.2 Observe From Afar
label afar:
    "You decide it's too much of a hassle to go down to the front of the stage."
    "It might seem too desparate too."
    imi "I love Minnesota and our Hmong community."
    imi "Thank you for having me."
    hide imiI
    #SOUND
    show mcI
    mc "Please give our senator Imi another round of applause!"
    #SOUND
    mc "Imi will be at her booth giving out keychains later this evening."
    mc "So please drop by and give her a visit!"
    hide mcI
    you "Keychains!?"
    you "This doesn't feel like a coincidence..."
    you "Maybe you should've gone up to the stage and checked her out closer..."
    "Hmm, it looks like the remaining stage line up is just beauty pageant stuff..."
    "Let's go back and check out the main area."
    jump center

# 2.1 Return To Main Area =======================================================================================================================
label main_area:
    scene centerbg
    you "Sometimes I forget how uneventful the Hmong New Year is..."
    you "{i}sigh{/i} Back to the beginning..."
    you "I just feel like maybe I'm looking in the wrong places..."
    #SOUND
    play sound "fight.mp3"
    show rando1
    anon "There's a fight!!!"
    hide rando1
    show rando2
    play sound "pipe.mp3" volume 0.7
    anon2 "Ooh I want to see!"
    hide rando2
    #SOUND
    show rando3
    play sound "fight.mp3"
    anon3 "Fight back! Fight back!!!"
    hide rando3
    you "Shit!! I better get out of there!"
    "You rush out to the escalator area to avoid the fight."
    "You notice a few FBI agents rush past you."
    you "The FBI???"
    you "That's a little excessive."
    you "..."
    scene boothbg
    "The shopping area has cleared up since everyone has gone to see the fight."
    "This is the perfect time to find the original keychain owner!!!"
    stop sound
    jump shopping

label shopping:
    scene boothbg
    if notTalkToInsurance or notTalkToActor or notTalkToMed or notTalkToImi:
        menu:
            "Where should you look?"
            "Insurance Booth" if notTalkToInsurance:
                jump insurance
            "Movie Booth" if notTalkToActor:
                jump movie
            "Anime Merch Booth" if notTalkToAnime:
                jump anime
            "Medicine Booth" if notTalkToMed:
                jump med
            "Senator Imi's Booth" if notTalkToImi:
                jump imi_booth
    else:
        jump rose_booth

#2.1.1 Pyramid Scheme
label insurance:
    scene claireboothbg
    $ notTalkToInsurance = False
    show claireI
    "You decide to check out the Insurance Booth."
    you "Hmm, let me ask if this person knows anything about the keychain..."
    you "Hi- do you know if anyone has lost a keychain and is looking for it?"
    anon "Hi!!! Are you interseted in buying life insurance?"
    you "Oops- I don't think she heard me."
    "You pull the keychain from your pocket and repeat the question."
    anon "..."
    "She pauses and her eyes dart from you to the keychain a few times."
    anon "Hmm..."
    anon "Well- wait a minute!!!"
    anon "It's me- Claire! Don't you remember me?"
    you "What? Claire???"
    "You realize it {i}is{/s} Claire!!!"
    play sound "heartbeat.mp3"
    "Claire was your first crush and you liked her for five years straight..."
    "Such an interesting time to be alive..."
    claire "Gosh- it's been a minute... What have you been up to?"
    "You two exchange a few words. Sharing life updates and such."
    "You never imagined Claire working in Insurance..."
    claire "Anyhoo, what brings you to this booth? Needing life insurance?"
    you "Umm, well actually. Have you seen this keychain before?"
    claire "..."
    claire "Oh! Yes. Yes. It's mine."
    claire "Thanks for returning it to me."
    "Claire tries to take the keychain from you, but you surprisingly grip it firmly in your hand."
    "Something doesn't feel right..."
    "Claire laughs."
    claire "Alright alright, you can keep it."
    claire "It means a lot to me, so in return- you should do me a favor."
    claire "Or really- it's a favor for yourself."
    claire "My company is offering a promotion for the Hmong New Year holiday and it's a great deal..."
    "You muffle out Claire's words- pondering on if she truly is the original keychain owner."
    "It wouldn't surprise you if it was Claire though... you two clicked back then."
    you "Thanks Claire, but I should get going."
    claire "Don't you want to sign the policy though!?"
    "You smile and shake your head."
    hide claireI
    you "Maybe next time..."
    jump shopping

#2.1.2 Movie Booth
label movie:
    $ notTalkToActor = False
    scene actorboothbg
    show actorI
    "You decide to check out the Movie Booth- especially since there's no longer a line."
    actor "Where'd everyone go?"
    you "Oh.. a fight broke out."
    actor "Hmm, I see."
    actor "That's what people like nowadays..."
    actor "..."
    actor "Anyway, welcome to my booth."
    actor "Let me know if there's any movies you like."
    actor "They're all on sale since people keep pirating it on Youtube."
    you "..."
    you "Actually, I was wondering if you've seen anyone with this keychain."
    "You show the actor the keychain and he shakes his head."
    actor "No, it doesn't look familiar."
    actor "..."
    actor "On second thought, I've seen that at a merchandise booth."
    actor "The owner is a fine young lady. She sells a lot of those keychains actually."
    actor "Maybe it belongs to her?"
    you "Ohh, okay. Thank you."
    hide actorI
    jump shopping
    
#2.1.3 Anime Merch Booth
label anime:
    scene animeboothbg
    $ notTalkToAnime = False
    show animeI
    "You decide to check out the Anime Booth- maybe the owner knows something..."
    you "Oh hi."
    anime "Sorry- cash only and no returns."
    you "Actually, I was wondering if you've seen this keychain before."
    "You hold up the keychain and the Anime Booth Owner looks at it."
    "She heavily inspects it, repeatedly flipping the keychain over and over."
    anime "Yeah- We sell these at my booth."
    "She gestures to an empty rack."
    anime "We {i}just{/i} ran out of stock. Those keychains are pretty popular this year."
    anime "Are you trying to buy this?"
    you "No- no. I'm just looking for the original owner of this keychain."
    anime "Ohhh, that's definitely not easy. Like I said: a lot of people bought these keychains."
    anime "Is there a specific place you found that keychain?"
    you "Yeah... In the parking garage ."
    anime "When the lights went off?"
    you "What? YES- exactly when the lights went off!"
    anime "Ohhh, the keychain must've fell from my box."
    anime "The sudden power outage startled me."
    "The booth owner laughs nervously."
    anime "I'm kind of scared of the dark."
    "Your jaw drops."
    "She's {i}scared{/i} of the dark..."
    "The booth owner inspects your expression then suddenly stands up."
    anime "Ohh- don't worry. You can keep this keychain- even if it technically did belong to me."
    anime "I won't call the cops on you or anything."
    you "Well- it's not that. I just- ..."
    "Before you can finish your sentence, the booth owner gets a phone call and gives you small wave."
    "She looks busy...maybe you can come back."
    hide animeI
    jump shopping


#2.1.4 Medicine Booth
label med:
    $ notTalkToMed = False
    scene grannyboothbg
    show grannyI
    "You decide to check out the Medicine Booth- maybe the elderly lady will know something."
    "Oh shit- you don't really know how to speak Hmong-"
    granny "Oh! Nyob zoo me tub. Puas muaj dab tsis koj xav yuas?"
    "You smile and try your best to communicate with her."
    you "Oh, gew uh. Gew tsis yuas os."
    "This conversation is going horrible."
    granny "I didn't realize you couldn't speak Hmong."
    granny "It's okay- we can do English."
    you "???"
    granny "..."
    "You decide to get to the point and ask if she's seen the keychain."
    granny "Hmm..."
    granny "Why yes. I {i}have{/i} seen it. I think belongs to my friend's granddaughter."
    granny "..."
    granny "Maybe you should try talking to her if you haven't. She's at the Insurance booth."
    you "Okay! Thank you."
    hide grannyI
    jump shopping 

label imi_booth:
    $ notTalkToImi = False
    scene imiboothbg
    "You decide to go to Senator Imi's Booth- maybe you'll see the keychains there."
    "It's the lady from earlier..."
    show repI
    rep "Hello! Have you registered to vote for the next elections?"
    you "Yes."
    rep "Perfect! Make sure to tell your family and friends."
    you "Actually-"
    you '...'
    you "Is Senator Imi here?"
    rep "Ohh, no. She'll come later in the day. Still doing prep for some other stuff."
    rep "How can I help you?"
    you "Well, I was wondering if this keychian belonged to her..."
    "You pull out the keychain and show it to the Booth Representative."
    "She looks at it for a second and opens her mouth in shock."
    rep "W-where did you get this!?
    "
    "Suddenly, an FBI agent steps between you and the Booth Representative."
    hide repI
    show fbiI
    fbi "Excuse me, but Senator Imi's Booth won't be open until later."
    fbi "I advise you to come back."
    you "What???"
    "The Booth Representative looks at you, eyes wide open, as the FBI Agent guides you from the booth."
    hide fbiI
    "That was odd..."
    jump shopping



# 3.1 Wrap up ====================================================================================================
label rose_booth:
    "{i}sigh{/i} There's nowhere else to go now..."
    "And the day's almost ending."
    scene rosesboothbg
    "Disheartened, you unknowingly stumble into a sign and it falls on the floor."
    "The sign reads:$5 for a rose"
    show roseI
    rose "Oh no my sign!"
    "The owner of a rose booth runs toward you and grabs the sign from your feet."
    rose "Sorry about that. My sign is not taped very well."
    you "Oh no- it's my fault. I wasn't being careful."
    "You look down at the Rose Booth. He's selling all sorts of flowers..."
    rose "Would you like to buy a rose? They're only $5."
    rose "I know it's sort of old-fashioned but I find that people still really like them."
    rose "As long as you choose the right one, you're bound to find love!"
    you "Choose, huh..."
    you "..."
    you "That's it!!!"
    "All you need to do is choose!!!"
    you "That's a great idea!"
    rose "Huh?"
    you "I'll buy a rose!"
    "Before the day ends, you need to find that girl!"
    hide roseI
    
    menu:
        "Gather your clues up and decide which one you'll confess to!"
        
        "Buy a red rose - Senator Imi" (badge="imi"):
            jump imi_end
        "Buy a white rose - Anime Booth Owner" (badge="anime"):
            jump anime_end
        "Buy a pink rose - Hli" (badge="hli"):
            jump hli_end
        "Buy a purple rose - Claire" (badge="claire"):
            jump claire_end

label imi_end:
    play music "slow_techno_track_2.ogg"
    you "The keychain, the voice..."
    you "All the clues are adding up..."
    you "It just has to be Senator Imi!"
    scene imiboothbg
    "You decide to wait until her booth opens again."
    show repI
    rep "You're back!"
    you "Ahaha... yeah."
    you "Where's Senator Imi?"
    rep "She should be coming... right abouuuut..."
    rep "Now!"
    play sound "heartbeat.mp3"
    hide repI
    #SOUND
    "You see Senator Imi walking up to the booth, adorned by FBI agents."
    show imiI
    imi "Thank you, thank you."
    "She stops and looks at you."
    "The eye contact..." #SOUND
    you "Um, S-senator Imi.."
    you "I- I..."
    you "I believe this belongs to you."
    "You hand her the keychain along with the red rose."
    "Her mouth hangs open."
    "Then she laughs nervously and tucks her hair behind her ear."
    imi "Ahaha..."
    imi "SECURITY!!!!"
    hide imiI
    "Before you realize what's happening, a group of FBI agents pounce on you."
    "You're suffocated by their weight and can't get up."
    #TODO
    "..."
    "Well, I guess Hmong people really {i}do{/i} make history."
    return 

label anime_end:
    play music "05 - DownTempo Avenue.mp3"
    "The parking garage... The keychain..."
    "It's got to be the Anime Booth Owner!"
    scene animeboothbg
    "You sprint over to her booth." 
    you "H-hey!" 
    "As you catch your breath, you see her turn around- eyes open."
    show animeI
    anime "Oh? You again? What's up?"
    "You pull the keychain out of your pocket and show it to her- still catching your breath."
    "Before you can explain yourself, she rapidly turns her head away from the keychain."
    anime "Woah, what are you doing?"
    you "This belongs to you right?"
    anime "W-what... Noooo, no way!!!"
    you "But earlier you said those were yours."
    anime "..."
    you "..."
    you "Can I just talk to you about something?"
    play sound "heartbeat.mp3"
    you "What happened in the parking garage... I have never felt that way before." #SOUND
    you "I- I think I like you and I really want to know you better."
    "Silence. You look up at the Anime Booth Owner and notice that she's smiling."
    anime "Wow. I thought you had forgotten about me."
    anime "This is a lot to take in- can I go to the bathroom and wash my face first?"
    you "Sure"
    "You watch her open her register and put all the cash in her fanny pack. She smiles at you."
    anime "I use dollars to wipe..."
    hide animeI
    "That's kind of weird..."
    "She then walks towards the bathroom..."
    "And makes a sharp turn towards an FBI Agent standing at Imi's booth!?"
    "They talk for a bit then she points at you."
    "You see the FBI Agent walk towards you... This is getting weird."
    you "Um... can I help you?"
    show fbiI
    fbi "Can I see that keychain?"
    you "What?"
    fbi "I heard from that lady that you've been selling counterfeit anime merch???"
    fbi "YOU THINK THAT'S FUNNY!?"
    hide fbiI
    "Before you realize what's happening, a group of FBI agents pounce on you."
    "You're suffocated by their weight and can't get up."
    #TODO
    "..."
    "Well, I guess Hmong people really {i}do{/i} make history."
    return 


label hli_end:
    scene balltossbg
    play music "Summer_Days_WIP.wav"
    "The parking garage..."
    "There's not a lot of clues to build off from, but it might just be Hli."
    "Besides, she's the most likely character to choose from a player's perspective."
    "You decide to go back to the Ball Toss area (now that the fight has been broken out)"
    "..."
    play sound "heartbeat.mp3"
    "There she is!" #SOUND
    show hliI
    hli "Oh! It's you."
    hli "Any luck in finding your person?"
    you "Well, it's actually you."
    you "I'm certain"
    hli "What..?"
    you "Yes. Did you run into your person while the parking garage happened to blackout."
    hli "Blackout?"
    you "Yes."
    hli "..."
    hli "Are you really the one from this morning?"
    hli "What about the keychain?"
    you "..."
    you "Maybe you should take another look at it."
    "You pull out the keychain and Hli looks at it again."
    hli "{i}gasp{/i}"
    hli "It DOES belong to me!!!"
    hli "Sorry- I didn't recognize it earlier because I thought it was a dupe."
    hli "Someone's selling dupes at one of the booths... "
    hli "Anyway, then you ARE the one I'm looking for!"
    hide hliI
    #SOUND
    "You and Hli embrace in a hug."
    "Finally!"
    "Love at last!"
    return

label claire_end:
    play music "Kim Lightyear - Friends (Loop Edit).mp3"
    "The keychain, the familiar presence..."
    "It's got to be Claire!"
    scene claireboothbg
    play sound "heartbeat.mp3"
    "You rush over to her booth."
    show claireI
    you "Claire!"
    claire "Oh, hey again!"
    you "Is this really your keychain?"
    claire "Yes! I told you that."
    claire "But like... you can keep it. I don't mind."
    you "Well, actually..."
    "You feel those 5 years of unrequited love overwhelm your chest and you take a deep breath."
    "You never got to confess your feelings back then..."
    "But maybe now was different...you clear your throat."
    you "Well, actually. I've been looking for the owner."
    you "I ran into the owner of this keychain at the parking garage this morning and I can't stop thinking about her."
    "Claire smiles softly."
    you "Are you really the person I've been looking for?"
    claire "I thought you'd never confess."
    "Claire embraces you in a hug."
    "This has been such a long journey."
    "You can't believe you gave up on liking her 2 years ago."
    "If only you had waited 7 years, you wouldn't have had to play this dumb visual novel to find out it's actually her..."
    hide claireI
    scene livingroombg
    "Ten years later, you and Claire are married."
    "You two rent a small apartment and live with two dogs, Chuffy and Wuffy."
    "Claire works while you stay home, clean the house, and do laundry."
    "Then one day, you hear a knock on the door."
    fbi "FBI OPEN UP!"
    you "The FBI???"
    show fbiI
    "You open the door and see the same FBI agent from the New Year 10 years ago..."
    "Weird."
    fbi "You're under arrest for commiting life insurance fraud!!!"
    you "WHAT!?"
    you "Wait- sir, I think there's a misunderstanding."
    you "My wife {i}Claire{/i} works in Life Insurance- I just stay home."
    fbi "THEN EXPLAIN THESE POLICIES IN YOUR NAME!!!"
    "The FBI Agent pulls out a stack of papers and waves it violently."
    fbi "If you don't comply, we're going to have to-"
    you "Wait- wait. Let me just call Claire!"
    fbi "DID YOU JUST INTERRUPT ME!?!!?"
    hide fbiI
    "Before you realize what's happening, a group of FBI agents pounce on you."
    "You're suffocated by their weight and can't get up."
    "..."
    "Well, I guess Hmong people really {i}do{/i} make history."
    return 
