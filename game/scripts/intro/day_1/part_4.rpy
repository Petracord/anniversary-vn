label intro_day_1_4:
    show reimu determined
    reimu "You found them in the forest? Can you show me exactly where?!" 

    show petra default
    show rosemi worried
    rosemi "Well... It's been a while... So I don't really remember exactly where I found them."

    show reimu sad
    reimu "... of course, just my luck." 
    rosemi "I'm sorry Reimu, I wish I could help more..." 

    show rosemi default
    rosemi "Actually, if you want I can accompany you to the forest, we can walk through my usual jogging routes, maybe that could give you some clues?" 

    show reimu happy
    reimu "...!" 
    reimu "Really!? You'd do that for me?" 

    show rosemi happy
    rosemi "Of course! Why not? After all, it's my job to help people!" 
    rosemi "Though, I usually work with people who have very special needs... But it's fine! I'm sure helping you won't be any different!" 

    show reimu default
    reimu "Special needs?" 
    rosemi "Yeah, we mainly help special existences to–"

    show rosemi worried
    rosemi "... !" 
    rosemi "... um… Reimu, hold on a sec." 

    # Blocking: Rosemi's sprite moves away from Reimu, then stands very close to Selen and Nina's sprites 
    # it should look like the three are huddled and having a small private chat 
    # the following dialogues are all in a smaller font to show that they are whispering, petra and Reimu are not listening to the convo 

    show rosemi excited:
        spread(5, 3)
        linear 0.5 xoffset 100

    rosemi "{size=*0.5}$s^J& hear me out \%#@ff$Gh^$jsH@*4&\%$(#*sd4&^$ special existence?{/size}" 

    show nina worried:
        spread(5, 5)
        linear 0.5 xoffset -100
    nina "{size=*0.5}#\%HJf8Df(\%^& ghost #@\%$\%** count &3*\%(^*rk$^& an ''existence'' \%^GJfi&f^\%@*9.{/size}"

    show selen shocked
    selen "{size=*0.5}... \%&^( are you suggesting\%(^(\%&(\%(*^*^#$@$\%$*?!{/size}" 
    rosemi "{size=*0.5}&\%@*&\%? #(*^#&#@&! $*^\%^$^\%#&**&)(^*$Rehab Center's resources.{/size}" 
    rosemi "{size=*0.5}@uB6#& come on, how often ^\%&\%$6dH=#^+*?*&\%=1f5#&^ special existence!{/size}" 
    nina "{size=*0.5}$^*0&^G=3md$O&b(^$( would make it easier ^\%4#.{/size}" 

    show selen worried
    selen "{size=*0.5}\%*(*^yhg$kFio#3r7)hd#@.{/size}"

    show selen happy
    selen "{size=*0.5}@3^ worth a shot jKu4O)K*3&^\%5$=#\%&.{/size}" 

    show nina happy
    show rosemi happy
    nina "{size=*0.5}&\%P*g4^0kP$*& Head Researcher ^\%Hu@J$93*\%.{/size}"
    rosemi "{size=*0.5}&\%G38gO*#Obh&)jr37Ho20P$\%^#=-3J*kd\%30(u^\%$^\%& won't turn Reimu @^*W\%5y*$.{/size}" 
    selen "{size=*0.5}$\%E^K3r& go talk &j-\%9#F\%*)$@ if she's interested.{/size}" 

    # Blocking: Rosemi, Reimu and Nina's sprites move back to the spots they were at before they became huddled together 

    show rosemi happy:
        linear 0.5 xoffset -100
    show nina happy:
        linear 0.5 xoffset 100
    rosemi "Reimu, I have to ask you a very important question to decide how we can help you from here on." 
    rosemi "... how would you like to live as a human?" 

    show reimu determined
    reimu "...?!"
    reimu "But... but I'm-!" 
    reimu "I'M ALREADY DEAD!!" 

    show petra deadpan
    petra "(... I bet she tells that to all her ''special'' girls.)" 

    scene bg bedroom_night with fade

    show petra default at spread(4, 1)
    show rosemi default at spread(4, 2)
    show selen happy at spread(4, 3)
    show nina happy at spread(4, 4)

    petra "(Hmm... should I tell them now?)"
    rosemi "Thank goodness that everything worked out with Reimu!" 
    nina "Yeah, I'm glad that she joined." 

    show selen worried
    selen "... just when I thought I was done with paperwork." 

    show rosemi happy
    rosemi "Haha, I don't think we'll ever be done with paperwork." 

    show petra thinking
    petra "(Is now a good time?)"
    petra "(Maybe tomorrow? But wouldn't it be too late tomorrow... )"

    show petra shy
    petra "(When are you supposed to thank people for stuff like this…?)"

    show rosemi happy
    rosemi "But don't worry, I'll help you with it! We'll start early in the morning."

    show selen happy
    selen "Thanks, speaking of which, we should get to sleep." 

    nina "Yep, it's getting late, and we shouldn't keep Petra up any longer." 

    show petra shocked
    petra "(Ah, they're leaving!)" 
    petra "(W-Wait! I still don't know what to do-!)"

    selen "Yeah, see ya, Petra. Have a good night." 
    rosemi "Good night, Petra."

    show petra default
    petra "Wait-! I– Umm…" 
    rosemi "Hmm? Yes Petra?" 

    show petra anxious
    petra "(Ah I spoke without thinking...)"

    show petra shy
    petra "(Well... Since I'm here now... I might as well say it.)"

    show petra default
    petra "A-About the... Umm you see, I-"

    show petra shy
    petra "Well... I want to– s-say–"
    petra "(Geez, stop fumbling– Just say it!)"
    petra "I was thinking... you know... about the present."

    show petra default
    petra "... t-thank you."

    show petra softsadsmile
    petra "... thank you for the flowers." 
    petra "I really like them..."

    show rosemi shocked
    show selen shocked
    show nina surprised
    
    RoSeNi "... !!" 

    nina "When did you...?" 
    selen "Oh, when Rosemi was explaining..."

    show rosemi default
    rosemi "..." 

    show petra default
    show rosemi happy
    rosemi "I'm glad you like them."

    show rosemi worried
    rosemi "Even though we couldn't present them to you ourselves..." 
    petra "It's fine." 
    petra "We all got pretty caught up with Reimu." 
    rosemi "Yeah..." 

    show rosemi default
    rosemi "Hmm… Actually, if it's fine with you, do you want to go see them again tomorrow? They should be in bloom for a few more nights."

    show petra softsadsmile
    petra "... sure." 

    rosemi "And you two are coming along too, right?" 

    show nina happy
    nina "I wouldn't miss it."

    show selen happy
    selen "Absolutely! And I'll be the first to arrive this time." 

    # Ember Happy bark sfx 
    ember "Arf!" 

    show selen worried
    selen "Ember… You are the last dragon that has any right to remind me about paperwork."

    show petra softsadsmile
    petra "...heh."

    scene bg bedroom_night with fade

    show petra default at left
    # Pomf sfx 
    petra "..." 


    # Yawn sfx with this dialogue if you can 
    petra "Haa, it's been a long day." 
    petra "So much happened today." 
    petra "... To think we have a new member…" 
    petra "... and she's a ghost." 
    petra "... " 
    petra "Losing all of your memories…" 

    # Can we insert a ''Flashback'' here? Like show screenshots or images of previous scenes throughout the day? I was thinking of screenshots of the time Nina greeted Petra in the morning, screenshot of the moment where Ember was nibbling on her fish hair clip, all of them having breakfast together, then Petra seeing the flower patch present. It's supposed to be like, Petra suddenly remembering good memories, thinking about her own set of memories she doesn't want to forget.
    # Day 1 Scene Montage
    # I'll see if I can cut something together
    
    # Update, I don't think I'll be able to cut something together before Petra's 
    # birthday since we'd need footage from an otherwise finished demo

    # flash back end, back to petra's room (night) BG

    show petra softsadsmile
    petra "Even though it hasn't been that long... I guess I'd be sad too." 

    # Scene : fades to a black screen, as if Petra is closing her eyes and falling asleep

    petra ".... zzz" 

    jump intro_day_2