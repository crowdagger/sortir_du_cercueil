screen stats:
    window: 
        vbox:
            xalign 0.5
            spacing 20
            text "STATISTIQUES":
                xalign 0.5
                grid 3 7:
                spacing 20
                $ nonchalance = (100.0 * stats.nonchalance)/stats.nonchalance_max
                $ prudence = (100.0 * stats.prudence)/stats.prudence_max
                $ chatoyance = (100.0 * stats.chatoyance)/stats.chatoyance_max
                $ rebellion = (100.0 * stats.rebellion)/stats.rebellion_max
                $ maugreance = (100.0 * stats.maugreance)/stats.maugreance_max
                $ artiste = (100.0 * stats.artiste)/stats.artiste_max
                $ meticulosite = (100.0 * len(stats.visited))/ 5
                                
                text "NONCHALANCE" xalign 0.5
                text "[nonchalance:.0f] %" xalign 0.5
                bar value nonchalance range 100.0 xsize 150

                text "PRUDENCE" xalign 0.5
                text "[prudence:.0f] %" xalign 0.5
                bar value prudence range 100.0 xsize 150
                
                text "CHATOYANCE" xalign 0.5
                text "[chatoyance:.0f] %" xalign 0.5
                bar value chatoyance range 100.0 xsize 150

                text "REBELLION" xalign 0.5
                text "[rebellion:.0f] %" xalign 0.5
                bar value rebellion range 100.0 xsize 150

                text "MAUGREANCE" xalign 0.5
                text "[maugreance:.0f] %" xalign 0.5
                bar value maugreance range 100.0 xsize 150

                text "ARTISTE" xalign 0.5
                text "[artiste:.0f] %" xalign 0.5
                bar value artiste range 100.0 xsize 150                    

                text "MÉTICULOSITÉ" xalign 0.5
                text "[meticulosite:.0f] %" xalign 0.5
                bar value meticulosite range 100.0 xsize 150                    
                
