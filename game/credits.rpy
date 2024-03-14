## Texte placé sur l'écran "À propos" du jeu. Placez le texte entre triples
## guillemets, et laissez une ligne entre les paragraphes.

define gui.about = _p("""
LICENCE

Creative Commons By-SA 4.0


ÉCRITURE

{a=https://crowdagger.fr}Lizzie Crowdagger{/a}

MOTEUR

{a=https://www.renpy.org/}Ren'Py{/a}


ILLUSTRATIONS

{a=https://pixabay.com/fr/photos/nuit-ch%C3%A2teau-corbeau-fantaisie-3129908/}Illustration de titre{/a} : {a=https://pixabay.com/fr/users/peterpang252-7818586/}peterpang252 sur Pixabay{/a}

{a=https://opengameart.org/content/mostly-16x18-characters-and-48x48-portraits-repack}Portraits{/a} : Art by Charles Gabriel and Antifarea.
Commissioned by {a=https://opengameart.org}OpenGameArt.org{/a}


MUSIQUES

Dark Quest : {a=https://opengameart.org/content/dark-quest}Alexandr Zhelanov{/a} (CC-By)

{a=https://opengameart.org/content/rpg-battle-theme-the-last-encounter-0}The Last Encounter{/a} : {a=http://www.matthewpablo.com}Matthew Pablo{/a} (CC-By)

Piano Loop : {a=https://opengameart.org/content/emotional-piano-loop}Extenz{/a} (CC0)

Chaos Castle : {a=https://opengameart.org/content/chaos-castle}FoxSynergy{/a} (CC-By)

Vampire's Piano : {a=https://opengameart.org/content/vampires-piano}TAD{/a} (CC0)

Rival's theme : {a=https://opengameart.org/content/rivals-theme}Bobjt{/a} (CC-By)

{a=https://opengameart.org/content/dream-raid-cinematic-action-soundtrack}Dream Raid{/a} : {a=http://www.matthewpablo.com}Matthew Pablo{/a} (CC-By)

{a=https://opengameart.org/content/colossal-boss-battle-theme}Blackmoore Colossus{/a} : {a= http://www.matthewpablo.com}Matthew Pablo{/a} (CC-By)

Decisions : {a=https://opengameart.org/content/decisions-1}FrancisLeeMusic{/a} (CC-By)

Oops : {a=https://opengameart.org/content/oops}Alexandr Zhelanov{/a} (CC-By)

{a=https://opengameart.org/content/funny-and-cute-acoustic-ending-theme}A second a day from birth{/a} : {a=https://airyluvs.com/}SOUND AIRYLUVS by ISAo{/a} (OGA-By)

{a=https://opengameart.org/content/no-joke-is-all-that-counts}No Joke is All That Counts{/a} : {a=https://www.patreon.com/Snabisch}Snabisch{/a} (CC-By)



SONS

Vent : {a=https://opengameart.org/content/wind1}Luke.RUSTLTD{/a} (CC0)

Cigarette : {a=https://freesound.org/people/AldebaranCW/sounds/453082/}AldebaranCW{/a} (CC0, raccourci)

Loup : {a=https://freesound.org/people/sandboks/sounds/503516/}Sandboks{/a} (CC0, raccourci)






MERCI D'AVOIR JOUÉ

Retrouvez d'autres textes sur {a=https://crowdagger.fr}https://crowdagger.fr{/a}








""")


label credits:
    window hide
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
