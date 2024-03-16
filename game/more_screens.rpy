screen stats():
    window: 
        vbox:
            xalign 0.5
            spacing 20
            text "STATISTIQUES":
                xalign 0.5
            $ secondes = renpy.get_game_runtime()
            $ heures = int(secondes // 3600)
            $ minutes = int(secondes - heures * 3600) //60
            $ secondes = int(secondes - heures * 3600 - minutes * 60)

            grid 3 7:
                spacing 20
                $ nonchalance = (100.0 * stats.nonchalance)/stats.nonchalance_max
                $ prudence = (100.0 * stats.prudence)/stats.prudence_max
                $ chatoyance = (100.0 * stats.chatoyance)/stats.chatoyance_max
                $ rebellion = (100.0 * stats.rebellion)/stats.rebellion_max
                $ compassion = (100.0 * stats.compassion)/stats.compassion_max
                $ artiste = (100.0 * stats.artiste)/stats.artiste_max
                $ meticulosite = (100.0 * len(stats.visited))/ 12
                                
                text "NONCHALANCE" xalign 0.5
                text "[nonchalance:.0f] %" xalign 0.5
                bar value nonchalance range 100.0 xsize 150 left_bar "gui/bar/left_red.png" right_bar "gui/bar/right_red.png"

                text "PRUDENCE" xalign 0.5
                text "[prudence:.0f] %" xalign 0.5
                bar value prudence range 100.0 xsize 150 left_bar "gui/bar/left_orange.png" right_bar "gui/bar/right_orange.png"
                
                text "CHATOYANCE" xalign 0.5
                text "[chatoyance:.0f] %" xalign 0.5
                bar value chatoyance range 100.0 xsize 150 left_bar "gui/bar/left_yellow.png" right_bar "gui/bar/right_yellow.png"

                text "REBELLION" xalign 0.5
                text "[rebellion:.0f] %" xalign 0.5
                bar value rebellion range 100.0 xsize 150 left_bar "gui/bar/left_green.png" right_bar "gui/bar/right_green.png"

                text "COMPASSION" xalign 0.5
                text "[compassion:.0f] %" xalign 0.5
                bar value compassion range 100.0 xsize 150 left_bar "gui/bar/left_cyan.png" right_bar "gui/bar/right_cyan.png"

                text "INTELLIGENCE" xalign 0.5
                text "[artiste:.0f] %" xalign 0.5
                bar value artiste range 100.0 xsize 150 left_bar "gui/bar/left_indigo.png" right_bar "gui/bar/right_indigo.png"

                text "MÉTICULOSITÉ" xalign 0.5
                text "[meticulosite:.0f] %" xalign 0.5
                bar value meticulosite range 100.0 xsize 150 left_bar "gui/bar/left_magenta.png" right_bar "gui/bar/right_magenta.png"
        
            
                
            text "TEMPS ÉCOULÉ : [heures]H[minutes]'[secondes]''" xalign 0.5
            $ percent = renpy.count_seen_dialogue_blocks() * 100 / renpy.count_dialogue_blocks()
            text "TEXTE VU (TOUTES PARTIES CUMULÉES) : [percent:.0f] %" xalign 0.5
