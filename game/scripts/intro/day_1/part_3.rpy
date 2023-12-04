label intro_day_1_3:
    scene bg bedroom_night with fade

    show petra default at left
    # Yawn SFX
    petra "It's already night?" 
    petra "I didn't even notice... Well, at least I'm done studying everything Nina told me to." 

    petra "I guess now I'm free for the entire day tomorrow." 
    petra "..." 
    petra "(What Nina said… I still can't stop thinking about it….)" 
    petra "(Make friends? She makes it sound so easy...)" 
    petra "(I've never had friends before... I spent all those years on my own... so I don't even know how to make friends...)"
    petra "(I didn't even know it was a skill that you have to actively hone…)"
    petra "(... and I still don't even know how to talk to people properly.)"
    petra "(I've hardly been able to express myself at all... whatever happens, I just go along with it...)"
    petra "(Is this really okay? I don't even feel like I'm ready for something like this..)."
    petra "(What if I don't agree to do the task? What happens then?)"
    petra "(... I hope nothing bad...)"
    petra "(No, no… I'm being pessimistic again... I need to stop thinking like this.)"
    petra "(But I don't know... am I really supposed to just go up to people and talk to them?? And just like that, they'll become my friend??)" 
    petra "That sounds... stupid." 
    petra "..." 
    
    show petra sad
    petra "And even if I did go up to people and talk to them..." 
    petra "Who would even want to be my friend..." 
    petra "..."

    show petra shy
    petra "... Ugh, I feel tired just thinking about all of these things." 
    petra "(I'll think about this later...)" 

    show petra default
    petra "I just need to clear my mind... Maybe with some light reading."

    scene bg bedroom_night with fade
    show petra default at left

    petra "..." 

    show petra softsadsmile
    petra "That was a good read." 

    show petra default
    petra "(Hmm... how long have I been reading?)"
    petra "Oh, it's almost time for the present reveal!"

    if prologue_rejection_flag:
        petra "I-I better get going... I don't want to cause more trouble..." 
    else:
        petra "I might as well go to the garden now…" 
    
    scene bg hallway_night with fade
    # Blocking: Petra sprite moving across the screen from left to right

    show petra shy
    petra "(Hmm... it's been a few minutes. They're late.)"
    
    show petra default
    petra "Hmm... it's a pleasant night."
    petra "(They'll be here soon anyway, so I guess I might as well take a stroll.)"

    # walking sfx (still indoors, in the Rehab center)

    scene bg garden_night with fade

    petra "..." 
    # stepping on grass sfx 
    petra "(... such a nice breeze.)"
    petra "(But being here on my own... It's a little lonely.)"
    petra "..." 

    scene bg garden_night with fade
    # Blocking: Petra on left side, flip horizontally and back to make her look around

    show petra default at left
    
    # TODO animate this somehow
    
    show petra default at left
    petra "Hmm?"
    petra "(I don't think I've ever been to this part of the garden...)" 

    show petra shocked
    petra "The flowers here...!" 
    petra "They're... glowing!?" 

    # Scene: blue glowing flowers from cg or extra art (if we can) cut-in or extra BG not sure
    # I'll check in with Azu to see if we can do that
    scene bg garden_night_glowing
    
    petra "Whoa it's... beautiful!" 

    # deleted to let glowing garden stay for a bit longer

    # not sure about this position just yet
    show petra thinking at right 
    petra "(Are flowers supposed to glow? I'm not sure...)" 

    show petra softsadsmile
    petra "(But it's so pretty... such a soft, gentle glow.)"
    petra "(It's just like...)" 
    petra "The auroras back home... " 

    show petra anxious
    petra "... and still cold like home..."

    show petra default
    petra "..."
    # bush leaves rustling sfx

    petra "Huh?" 
    # bush leaves rustling 
    petra "... is anyone there?" 
    # Blocking: Petra's sprite moves left to right and again right to left 

    show petra shocked
    petra "... !" 
    petra "W-what was that?" 

    show reimu default at outer_left

    petra "(Wait, is that a person?)"

    show petra terrified # should exist now
    petra "(Is that person... {i}Floating???{/i})"
    petra "(W-What!!?? Am I seeing things??)"

    # Blocking: Reimu's sprite flips horizontally back and forth, as if she's looking around 

    petra "(No way... i-it's... i-it's-)"
    petra "... a g-g-ghost?!" 
    petra "(Hide!!!)"

    # Blocking: Petra's sprite moves to the far right of the screen 
    # bush leaves rustling sfx

    reimu "... where... am I?"
    # Blocking: Reimu's sprite moves a bit closer to the center, slowly (If you can make it slow that would be great but if you can't, that's fine). So the sprite is somewhere around center-left. 

    show petra terrified # should exist now
    petra "..."

    # Blocking: Petra's sprite shivers/shakes, should give the feeling that Petra is scared 
    petra "(I need to get out of here!)" 

    reimu "... these flowers, who planted them?"

    show petra terrified # should exist now
    
    # Blocking: Petra's sprite moves further right to the edge of the screen a bit of her sprite is off screen 
    # bush leaves rustling sfx (in time with her sprite moving) 
    petra "..."

    # Blocking: Petra's sprite moves even further right, now half or 1/4 of her sprite can't be seen 
    # bush leaves rustling sfx (in time with her sprite moving) 

    petra "(I'm almost out…)" 

    show petra shocked
    petra "... ! " 
    petra "(Huh!? Something's stuck to my foot!?)"
    # vines breaking or twig snapping sfx along with the above dialogue

    petra "Buaaah!!" 
    # bush leaves rustling sfx (along with the above dialogue) 

    # After the above noise, a "thump" kind of noise happens to show Petra hit the ground. Sfx note.
    # Blocking: Petra's sprite moves down a few centimeters, to show that she's on the ground 

    # Blocking: pan screen towards Petra, sprite is now center-right. 

    show reimu determined
    reimu "...!" 
    reimu "Was that a— Oh, a person!"
    # Blocking: Reimu's sprite moves to the center, close to Petra 

    show petra terrified # should exist now
    petra "(Oh no oh no oh no! She's coming towards me!!)" 
    # Blocking: Petra's sprite trembles 

    show reimu default
    reimu "... did you trip? Are you okay?" 

    show petra shocked
    # Blocking: Petra stops trembling 
    petra "... !?" 
    petra "(...''are you okay?'' ...why is she asking me that!?!?!)"

    reimu "..." 
    petra "..." 
    reimu "... are you scared cause I'm a ghost?"
    reimu "You know, that's kinda rude…" 

    show petra terrified # should exist now
    petra "(... WHAT IS SHE ON ABOUT?? WHAT IS GOING ON??)" 
    reimu "Not all ghosts are bad." 
    petra "(NOT ALL GHOSTS?? ...THERE'S MORE???)" 
    reimu "Well, at least that's what I think…"
    reimu "I don't know about other ghosts, but I won't hurt you."
    petra "(W-What? Am I hearing this right?! Am I going insane??!)"
    reimu "..." 
    petra "..."
    reimu "You don't believe me... Rude."

    # Blocking: Reimu's sprite moves to the far left 

    show petra shocked
    petra "(... what the hell just happened…?)"
    petra "(Did she just– She just called me rude and left?? I–)" 

    # Blocking: Reimu's sprite flips horizontally back and forth, as if she's looking around 

    show petra terrified # should exist now
    petra "(She's not doing anything to me? She really left me alone...?)"

    show petra anxious
    petra "(Well, she did say she wouldn't hurt me... And she even asked if I was okay.)"

    show petra thinking
    petra "(And not to mention, if she really wanted to hurt me, she would have done that by now.)"

    show petra default
    petra "(I guess there is some truth to what she's saying…)"
    # Blocking: Petra's sprite moves back to its original height, to show she's standing again

    petra "(I'd rather not test my luck today though... I better try to leave while she's still distracted.)"
    # Blocking: Petra's sprite moves a few millimeters to the right of the screen, kinda to show she took a step

    # Blocking: Reimu's sprite flips to face petra
    reimu "Hey! Rude Girl! Before you leave…" 

    show petra shocked
    petra "Huh!??" 
    petra "(What now?! Please! I just wanna go back to my room!)"

    show reimu sad
    reimu "Do you know who planted these flowers?"
    petra "... w-what?"

    show petra default
    petra "... the f-flowers?"

    scene cg reimu_intro 

    reimu "Yes... I want to know about them." 
    reimu "... do you know who planted these flowers?"
    petra "... no, I don't know." 
    reimu "..." 
    reimu "I see, I was hoping to find the person who planted these... Maybe they'd recognise me." 
    petra "... recognise you?" 
    reimu "Yes..."
    petra "..." 
    reimu "..."

    scene bg garden_night

    show petra anxious at slightleft
    show reimu sad at slightright 
    # Blocking: Petra and Reimu's sprite are at the center of the screen, they are standing next to each other, like at talking distance

    petra "(Why would the person planting the flowers recognize her? Does she live in the garden or something?!)"
    petra "(No, I would have been told if we had a resident ghost here... I think?)"  


    show reimu default
    reimu "... you keep staring at me without saying anything."

    show reimu determined
    "Oh, do I remind you of someone?!" 

    show petra shocked
    petra "Fweeh?! Uhh, was I?!"

    show petra terrified # should exist now
    petra " I-I'm s-s-sorry! I d-didn't mean to...!" 

    show reimu default
    reimu "... it's fine, but why were you staring? Are you sure you don't recognise me?"

    show petra shocked
    petra "(... ! S-She's not angry?)"

    show petra default
    petra "(Actually… She doesn't look bothered at all...)"
    petra "(She's more concerned about being recognised... )" 
    petra "... no, I don't recognise you..." 

    show reimu sad
    reimu "..." 
    reimu "Another dead end..." 

    petra "...dead end?"
    petra "Excuse me, but are you looking for something?" 

    reimu "..." 
    reimu "... yes, my memories."

    show petra shocked
    petra "(Her memories!?)" 

    reimu "Ever since I woke up, I can't remember anything about my past, so I've been floating from place to place..."

    show petra shy
    petra "(Wandering around with nowhere to go or anyone to count on...)" 
    petra "(Maybe I don't have it that bad…)"

    show reimu determined
    reimu "But these flowers!" 
    reimu "They feel familiar! I don't know why but I feel comfortable when I see them." 

    show reimu sad
    reimu "... it's soft, gentle glow... reminds me of home." 
    reimu "Hah, even though I can't even remember my home... but it just feels like it... I don't know how to explain it." 

    show petra default
    petra "(... home, huh?)" 
    
    show petra sad
    petra "(But she's smiling... I guess she must've actually been fond of her home…)" 
    petra "H-Hey-"

    # Blocking: Nina, Selen and Rosemi's sprites have not appeared yet, you only hear their voices

    rosemi "Petra!!" 
    petra "Fweh?" 
    selen "Petra, where are you?!!" 
    nina "Petraaaa!!" 

    # bush leaves rustling sfx 

    show petra shocked
    petra "... oh, they're looking for me!"
    nina "Hey, there's someone over there! Is that you, Petra?" 

    show petra default
    petra "Y-Yes! I'm here!" 

    show reimu default
    reimu "...??"

    # bush leaves rustling sfx 

    # Blocking: Nina sprite appears left of screen as Petra and Reimu's sprites move to the right to make room
    # Blocking: Nina's sprite is a bit further away from Petra and Reimu's sprites, here Petra and Reimu's sprites are on the right, Nina is on the far left
    show nina happy at left
    show petra at slightright
    show reimu at bump_right(200), outer_right

    nina "Petra! There you are!" 

    show nina surprised
    nina "... !!!" 
    nina "... i-is that??" 
    nina "No... it can't be..." 
    nina "... you left so long ago–" 
    nina "... Reimu? Is that really you?" 

    show reimu determined
    reimu "... !!" 

    show reimu angry:
        linear 0.25 xpos 0.7
    
    # Reimu's sprite quickly moves close to Nina 
    reimu "Y-Yes! It's me! I'm Reimu!"
    reimu "You know me!?" 
    reimu "You really know me!? Can you tell me what happened?? Who am I? Where am I from?!" 
    reimu "Please tell me everything! I need to know!" 

    show nina worried
    nina "E-Excuse me? Tell you? What are you talking about?"
    nina "Why do I need to tell you about yourself? Reimu, what happened?!" 

    show reimu sad
    reimu "..." 
    reimu "... I can't remember anything." 
    reimu "My memories are gone..." 

    nina "..."
    nina "... your memories... are gone?" 

    show nina worried
    nina "... I see…" 

    show reimu sad
    reimu "You understand? So you'll help me?" 

    nina "... ..."
    nina "...I'm sorry, Reimu... but I can't help you." 


    reimu "W-What?? What do you mean?"  
    reimu "You knew my name right? So you must know more about me!" 
    reimu "Maybe my age… Or what I used to do… Or at least who you are to me?" 

    nina "I- I'm sorry... I-" 
    nina "... we... we were just acquaintances." 
    nina ".... we only met before once, so I don't know much about you other than your name." 

    show reimu angry
    reimu "No! No, no, no, that can't be!" 

    show reimu angry
    reimu "Please, you're the only person that has ever recognised me! Please try to remember, you must know something! Anything!" 

    show petra anxious
    show nina worried
    petra "...!" 
    nina "Reimu, calm down!"
    nina "I know you're worried and confused right now, but it's going to be okay. Trust me, you'll remember everything in due time." 

    show reimu angry
    reimu "And when is that?! Why not now!? Just tell me already!!" 

    # Nina's sprite moves closer to Reimu 
    nina "Listen, I can't give you the answers you want. You need to wait for the right time..."

    reimu "The right time?! What do you mean by ''the right time''?! That doesn't mean anything!!"
    reimu "Why do I have to wait?! It's been years!! I can't wait any longer! I won't wait!"

    nina "Reimu please–" 
    selen "What's going on over there? Who's shouting?" 
    selen "Hey, is anyone there!?" 
    rosemi "Petra! Nina! There you are." 

    # Blocking: Selen and Rosemi sprites appear on screen from the left, shuffle all other sprites right a little, pan out if necessary
    show petra default at spread(5, 5)
    show reimu angry at spread(5, 4)
    show nina worried at spread(5, 3)
    show selen worried at spread(5, 1)
    show rosemi worried at spread(5, 2), rosemi_bump

    selen "What's going on h-"

    show selen shocked
    selen "... I-Is… Is that a g-g-ghost!?" 
    selen " ..." 
    selen "AAAAAAAAAAAAAAAAHH!!!" 
    # if possible Selen screaming sfx clip for the above dialogue

    show rosemi shocked
    show petra shocked
    show nina surprised
    show reimu default
    reimu "... Not again…" 

    scene bg garden_night with fade

    show petra default at spread(5, 1)
    show reimu default at spread(5, 2)
    show rosemi default at spread(5, 3), rosemi_bump
    show selen default at spread(5, 4)
    show nina default at spread(5, 5)

    selen "So what you're telling me is that you woke up as a ghost and you have no memories of your past life…" 
    reimu "Yes." 
    selen "So you've been wandering around the world looking for your memories?"
    reimu "That's right."
    selen "And you stumbled into this facility after following the glowing flowers?" 
    reimu "Yeah…" 
    selen "... I see." 
    reimu "I swear I'm telling the truth, you have to believe me!" 
    selen "Yes, of course! We believe you! After all, this isn't even close to the weirdest thing I've ever heard."
    
    show reimu happy
    reimu "Really!? Thank goodness! Can you tell me about these flowers?" 

    # se Puzzled/Confused 
    show selen worried
    selen "The flowers?"

    show reimu sad
    reimu "Yes. I don't know why, but... these flowers feel familiar, like I'm supposed to know them..." 
    reimu "It felt like they were trying to show me something... which is why I followed them in the first place…" 

    show reimu sad
    selen "Hmm... I don't know much about these flowers, but I think Rosemi should, right?" 

    show rosemi worried
    rosemi "Well, I don't know if this'll be of much help, but these are Forget-Me-Nots. I found a patch of them in the forest behind the Rehab Center." 
    rosemi "I was on a stroll one night and they caught my eyes." 

    show rosemi happy
    rosemi "They were so pretty, I wanted to show them to everyone else!"

    show rosemi distant
    rosemi "Especially one of our new residents... so I decided to pick a few and plant them in the garden." 
    rosemi "And eventually, I've nurtured the first few to this huge patch." 

    show petra default
    petra "(For one of the new residents?)" 

    show petra thinking
    petra "(Hmm… I don't think they've gotten any new residents in a while... The most recent one would be...)" 

    show petra shocked
    petra "(Me!?)" 
    petra "(Were these flowers... Planted for me?!)" 
    petra "..." 

    if prologue_rejection_flag:
        show petra anxious
        petra "(I- Is this really all for me?)"

        show petra default
        petra "(How do– What am I… A whole patch of flowers?)"

        show petra softsadsmile
        petra "(... I really have to stop overthinking everything.)"
        petra "(... I'll have to thank them later.)"

    else:
        show petra softsadsmile
        petra "(You guys...)"
        petra "(And to think that I've been so anxious around them...)"
        petra "(... I'll have to thank them later.)"

    jump intro_day_1_4