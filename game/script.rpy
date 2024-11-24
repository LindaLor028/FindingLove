# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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


# The game starts here.

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

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # Start - Morning
    you "{i}groan{/i} what time is it..."
    mom "Wake up!!! It's time to go to the Hmong New Year!"
    mom "Get out of bed sleepy head!"
    you "{i} urgggh"
    you "It's that time of the year again..."
    you "The Hmong New Year..."
    you "It's a yearly celebration that was traditionally meant to honor a year of harvest..."
    you "... and be a grounds for finding love with the infamous ball toss game..."
    you "... But I'm not so lucky-"
    mom "Hurry up! We'll be late!!!"

        # Screen changes to parked car in parking garage; heels clicking sound
    mom "You're so slow- we'll meet you inside."
    you "{i}groan{/i}"
    you "..."
    you "Well, I guess I better get going."

        # Screen shakes and blacks out.
    
    "!!!"
    you "What was that!!?"
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
    anon "I gotta go!!!" #SOUND
    "The lights flicker on again and you're standing alone in the parking garage."
    "Who was that..."
    "You look down and notice a keychain and pick it up..."
    jump keychain

# 0.1.2 Grab her hand
label start_2:
    "You feel the sweat in your pits swell up as you take a deep breath and reach for her hand."
    "Exhilarated by the feeling of love, your hand shoots out on its own and reaches for something."
    "It's not her hand."
    "It's a keychain???"
    anon "Ack!!!" #SOUND
    "It sounds like she ran off..."
    "The lights flicker on again and you're standing alone in the parking garage."
    "You look at the keychain."
    jump keychain

# 0.2 Keychain
label keychain:
    "This keychain..."
    "This is your answer to love."
    you "I need to find its original owner."
    "Empowered by this new purpose, you march into the Ex-Sell Energy Center- ready to find the love of your life."
    jump center 

# 1.0 Center
label center:
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
    you "Maybe she's somewhere in the crowd."
    you "I'll ball toss around and see if she's here."
    jump balltoss_2

label balltoss_2:
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
    you "Hmm, maybe I can talk to this couple. They look nice."
    "As you approach the couple, you hear them talking."
    wife "Ohh, cov hluas no mas... tsis keej kiag li os!"
    husband "Oi! Txoj hais li kos mas..."
    "You don't know how to speak Hmong... "
    "Better stay away from that conversation."
    jump balltoss_2

# 1.1.1.2 Random Girl
label girl:
    $ notTalkToGirl = False
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
    jump balltoss_2

# 1.1.1.2 Random Guy
label guy:
    $ notTalkToGuy = False
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
    jump balltoss_2


            
        


# 1.1.2 Main Stage =======================================================================================================================
label stage:
    "You head to the main stage- maybe you'll find luck there."
    mc "Please give the singer Cha Lis another round of applause!" #SOUND
    mc "..."
    mc "Alright, now I would like to welcome a very, very special guest."
    mc "The {i}very{/i} senator of our {i}xeev{/i} Minnesota, Imi Clobasure!!!!" 
    #SOUND
    "You watch as Imi walks up on stage..."
    "She looks somewhat familiar."
    imi "Thank you, thank you."
    #SOUND 
    imi "Thank you, thank you."
    imi "Wow, it's so great to be here."
    imi "Thank you, thank you."
    you "Wait a minute..."
    you "That voice..."
    you "It sounds familiar!!!"
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
    "You decide to go up to the stage."
    "There's no better way to know than being up close."
    # SCENE
    "Senator Imi is still giving her speech."
    you "Wow, her voice is so..."
    you "Official sounding..."
    imi "Thank you again for having me."
    imi "Nyob zoo xyoo tshiab!"
    "Your muscles tense up."
    "The heavy English accent in her attempt to speak Hmong catches you off guard."
    "This voice is way too familiar..."
    #SOUND
    "By the time you look up, Imi has already walked off stage."
    "All you see is her back"
    "Getting smaller and smaller..."
    "Then you hear a voice."
    anon "I love our senator."
    you "Huh?"
    anon "Oh what- sorry. I didn't realize I said that aloud."
    anon "Imi's just {i}such{/i} an amazing leader..."
    anon "..."
    anon "If you want, you should visit her at her booth later in the evening."
    anon "I heard she'll be giving out keychains."
    you "Keychains, huh..."
    "It looks like the remaining stage line-up is just beauty pageant stuff... "
    "Let's go back and check out the main area."
    jump center


# 1.1.2.2 Observe From Afar
label afar:
    "You decide it's too much of a hassle to go down to the front of the stage."
    "It might seem too desparate too."
    imi "I love Minnesota and our Hmong community."
    imi "Thank you for having me."
    #SOUND
    mc "Please give our senator Imi another round of applause!"
    #SOUND
    mc "Imi will be at her booth giving out keychains later this evening."
    mc "So please drop by and give her a visit!"
    you "Keychains!?"
    you "This doesn't feel like a coincidence..."
    you "Maybe you should've gone up to the stage and checked her out closer..."
    "Hmm, it looks like the remaining stage line up is just beauty pageant stuff..."
    "Let's go back and check out the main area."
    jump center

# 2.1 Return To Main Area =======================================================================================================================
label main_area:
    you "Sometimes I forget how uneventful the Hmong New Year is..."
    you "{i}sigh{/i} Back to the beginning..."
    you "I just feel like maybe I'm looking in the wrong places..."
    #SOUND
    anon "There's a fight!!!"
    anon2 "Ooh I want to see!"
    #SOUND
    anon3 "Fight back! Fight back!!!"
    you "Shit!! I better get out of there!"
    "You rush out to the escalator area to avoid the fight."
    "You notice a few FBI agents rush past you."
    you "The FBI???"
    you "That's a little excesive."
    you "..."
    "The shopping area has cleared up since everyone has gone to see the fight."
    "This is the perfect time to find the original keychain owner!!!"
    jump shopping

label shopping:
    if notTalkToInsurance or notTalkToActor or notTalkToMed or notTalkToImi:
        menu:
            "Where should you look?"
            "Insurance Booth" if notTalkToInsurance:
                jump insurance
            "Movie Booth" if notTalkToActor:
                jump movie
            "Anime Merch Booth" if notTalkToAnime:
                jump merch
            "Medicine Booth" if notTalkToMed:
                jump med
            "Senator Imi's Booth" if notTalkToImi:
                jump imi_booth
    else:
        jump rose_booth

#2.1.1 Pyramid Scheme
label insurance:
    $ notTalkToInsurance = False
    "You decide to check out the Insurance Booth."
    you "Hmm, let me ask if this person knows anything about the keychain..."
    you "Hi- do you know if anyone has lost a keychain and is looking for it?"
    anon "Hi!!! Are you interseted in buying this product?"
    you "Oops- I don't think she heard me."
    "You pull the keychain from your pocket and repeat the question."
    anon "..."
    "She pauses and her eyes dart from you to the keychain a few times."
    anon "Hmm..."
    anon "Well- wait a minute!!!"
    anon "It's me- Claire! Don't you remember me?"
    you "What? Claire???"
    "You realize it {i}is{/s} Claire!!!"
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
    you "Maybe next time..."
    jump shopping

#2.1.2 Movie Booth
label movie:
    $ notTalkToActor = False
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
    jump shopping
    
#2.1.3 Anime Merch Booth
lable anime:
    $ notTalkToAnime = False
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
    jump shopping


#2.1.4 Medicine Booth
label med:
    $ notTalkToMed = False
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
    jump shopping 


# 3.1 Wrap up ====================================================================================================
label rose_booth:
    "{i}sigh{/i} There's nowhere else to go now..."
    "And the day's almost ending."
    "Disheartened, you unknowingly stumble into a sign and it falls on the floor."
    "The sign reads:$5 for a rose"
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
    
    menu:
        "Gather your clues up and decide which one you'll confess to!"
        
        "Buy a red rose - Senator Imi":
            jump imi_end
        "Buy a white rose - Anime Booth Owner":
            jump anime_end
        "Buy a pink rose - Hli"
            jump hli_end
        "Buy a purple rose - Claire"
            jump claire_end
        

    # This ends the game.

    return
