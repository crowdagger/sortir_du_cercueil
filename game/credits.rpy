label credits:
    scene black with dissolve

    play music "no_joke_is_all_that_counts.mp3" fadein 1.0 fadeout 1.0

    $ credits_speed = 25

    show text "[gui.about!t]\n"  at Move((0.5, 1.0), (0.5, -2.0), credits_speed, xanchor=0.5, yanchor=0)
    with Pause(credits_speed+10) 

    $ renpy.pause()
    
    return
