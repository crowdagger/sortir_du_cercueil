label credits:
    scene black with dissolve

    play music "no_joke_is_all_that_counts.mp3" fadein 1.0 fadeout 1.0

    python:
        if stats.nonchalance_max == 0:
            stats.nonchalance_max = 1
        if stats.artiste_max == 0:
            stats.artiste_max = 1
        if stats.maugreance_max == 0:
            stats.maugreance_max = 1
        if stats.rebellion_max == 0:
            stats.rebellion_max = 1
        if stats.chatoyance_max == 0:
            stats.chatoyance_max = 1
        if stats.prudence_max == 0:
            stats.prudence_max = 1
        

    show screen stats with dissolve

    $ renpy.pause()

    hide screen stats

    scene black with dissolve

    $ credits_speed = 25

    show text "[gui.about!t]\n"  at Move((0.5, 1.0), (0.5, -2.0), credits_speed, xanchor=0.5, yanchor=0)
    with Pause(credits_speed+10) 

    $ renpy.pause()
    
    return
