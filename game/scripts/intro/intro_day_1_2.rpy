# Day 1 Part 2

label intro_day_1_2:
    #Scene: Fade into Hallway (day) BG 
    #BGM Meet The Characters

    scene bg hallway

    # All 4 girls are on screen
    show selen happy at right
    show rosemi happy at right
    show nina happy at right
    show petra default at left

    selen "Alright, I'm off to finish up some work."
    nina "Weren't you two supposed to have a day off today?"

    show selen default
    selen "Yeah, but something urgent came up."
    rosemi "Hopefully, we should be finished by today though." 
    rosemi "We can have our day off once we're done."
    nina "I see… Good luck, you two!"
    petra "G-Good luck." 
    rosemi "You too Petra! Good luck with your studies" 
    selen "Catch ya later!" 

    hide selen
    hide rosemi

    nina "Now that we're finally done with breakfast, let's get going."
    petra "... mhm." 

    # Scene: Petra's Room (day) BG 

    show petra thinking
    petra "(Like this… maybe?)"

    show nina worried
    nina "Hmm no, Honey, that's not how this should be solved…" 

    show petra sad
    # petra sigh sfx
    petra "(Of course it's wrong... Surprising nobody at all…)"

    show nina happy
    nina "Here, let me show you!"

    # Extra dialog for choosing "I-I'm not a little kid, you know!"
    if prologue_rejection_flag:
        # BGM stops
        # BGM ambience

        show petra sad # anxious/sad
        petra "... N-No! I-!!"

        show petra angry
        petra "(Don't take my pen from me!! I can write on my own just fine!)" 
        petra "... I- I want to try!" 
        petra "(I will not be babied!)" 

        show nina surprised
        nina "Oh!" 

        show nina default
        nina "..." 

        show nina happy
        nina "I see, alright then! Why don't you give it another shot?" 
        nina "I'm glad to see you so enthusiastic about math today!" 

        show petra angry
        # petra Hmph sfx
        petra "(Yeah! I don't need your help!)"
        petra "(I can do this myself!)"

        show petra default
        # BGM Petra Character Theme
        petra "(I just need to... remember how to do this again...)"

        show petra sad # anxious/sad
        petra "(... H-how do I even do this math again??)"

        show petra annoyed
        petra "Why do I even need to know this useless stuff to integrate into human society anyway!?"

        show nina laugh
        nina "Petra, you know that all the human kids had to learn this same standard curriculum too."
        nina "Not to mention…"

        petra "What… Wh-What's so funny?!"

        nina "Well, it's quite common for human kids to complain about learning 'useless stuff' too."

        show petra angry
        petra "Well, I'm not a kid!"

        show nina worried
        show petra default
        petra "I-I'm not…"

        nina "I… I'm so sorry, Petra."
        nina "I didn't mean to suggest that you were."

        show nina default
        nina "It's just that… These skills are crucial to interacting with humans who all rely on this common understanding of basic math and literacy in their day to day life."
        nina "Whether they realize it or not."

        show petra sad
        petra "I-I know…"
        petra "I'm sorry…"
        petra "L-Let's continue…"

    # Scene: Fade-in-fade-out to Petra's Room (day) BG 
    # BGM Meet The Characters

    scene bg bedroom

    show nina happy
    nina "Good job, Petra! You're learning pretty fast" 
    nina "Your academic progress is on track with our schedule, and your communication skills have improved a lot!" 

    show nina excited
    nina "In fact, I think you're ready to start the next phase of your socialization program!"

    show petra default
    petra "Next… phase?"
    nina "Yes! It's time for some hands-on experience!" 

    show nina happy
    nina "Your primary task for this phase is to interact with other people, and through multiple positive interactions, form acquaintances with whom you'll foster mutually beneficial relationships." 

    show petra confused
    petra "...fweh??" 

    show nina excited
    nina "Friends! Your task is to make friends!"

    show nina happy
    nina "Doesn't it sound exciting? And it's going to be a very useful skill for when you go into the outside world! This is going to be so much fun!"

    show petra shocked
    petra "...FWEHHH!?" 

# TODO: TO BE CONTINUED SCREEN