label william:
    "William était un jeune hommme aux longs cheveux noirs et aux yeux bleu sombre au physique élancé. Il portait un vieux manteau rapiécé qui était clairement fait pour des régions au temps plus clément."
    $ stats.visited.add("william")

    return

label carimall:
    "William savait juste qu'elle s'appelait Carimall, mais n'avait même pas idée de son âge. Il espérait qu'elle n'était pas trop jeune. Les enfants se montraient étrangement réticents à l'idée de rester immobiles pour qu'on leur dresse le portrait."
    $ stats.visited.add("carimall")

    return

label jeunes_hommes:
    "William avait, un moment, essayé de nouer la conversation avec l'un d'entre eux, jusqu'à ce qu'il réalise que tous deux étaient en voyage d'affaire et, par ailleurs, tristement {i}mariés{/i}. Quelle déception."

    return

label petit_monstre:
    """
    Ce n’était pas vraiment que William n’aimait pas les enfants : il les supportait tout à fait lorsqu’ils étaient suffisamment loin de lui, qu’ils restaient immobiles et se taisaient.

    Non seulement la fille était à moins d’un mètre mais en plus elle avait l’affreuse tendance à faire des grimaces et à discuter.
    
    Pire, elle lui avait même parlé directement, situation dont il s’était sorti en feignant de ne pas comprendre la langue locale.
    """
    $ stats.visited.add("petit_monstre")

    return

label hallucination:
   """
   Il avait tout fait pour que le phénomène cesse : arrêter de boire, boire beaucoup plus, prier et même se faire exorciser, mais rien n’y avait fait.

   Ce n’était pas vraiment gênant lorsqu’il était seul, si ce n’est qu’elle lui tapait sur les nerfs.

   Mais lorsqu’il était accompagné, il ne pouvait se permettre de lui répondre sans passer pour un fou et, comme Angèle ne se taisait pas pour autant, c’était une situation on ne peut plus frustrante.
   """
   $ stats.visited.add("hallucination")

   return


label gay:
   """
   William vivait maintenant bien son homosexualité, mais ça n'avait pas toujours été le cas.

   L'adolescence avait été particulièrement difficile.

   Est-ce que c'était à cause de ça qu'il s'était accompagnée d'une maudite personnalité imaginaire ?
   """

   $stats.visited.add("gay")

   return


label animal:
    "C'était, clairement, un {i}très{/i} gros chien."
    
    $stats.visited.add("animal")

    return 


label ekul:
    "C’était un homme de taille moyenne et de forte corpulence, aux cheveux noirs épais et broussailleux, qui avait quelque chose d’un peu effrayant dans le regard."

    $ stats.visited.add("ekul")

    return 


label main:
    """
    William serra et desserra les doigts pour tenter d'y faire circuler le sang.

    Il n'avait jamais compris ces gens qui voulaient toujours montrer qu'ils étaient les plus forts, y compris dans un geste aussi banal.
    """

    $ stats.visited.add("main")

    return 

label side_nuit:
   """
   William fronça les sourcils.

   Une telle promenade nocturne, et par un temps pareil, ne lui semblait pas très raisonnable.

   Il haussa cependant les épaules.

   Clairement, depuis qu'il avait mis les pieds dans ce fiacre, le domaine du raisonnable se tenait solidement à l'écart."""

   $ stats.visited.add("nuit")

   return

label side_tableau:
    """William n'était pas mécontent de son travail, même si, d'un point de vue purement esthétique, il aurait préféré la peindre devant un crépuscule, ou pourquoi pas une pleine lune."""

    $ stats.visited.add("tableau")
    return

label side_cloitree:
    """
    « Cloitrée » n'était peut-être pas le bon terme : William avait pu constater que la jeune femme n'avait pas peur de sortir, y compris en pleine nuit.

    Mais il n'était pas certain que ses balades en solitaire soient une grande source d'épanouissement."""

    $ stats.visited.add("cloitree")
    return

label side_comte_carimall:
    """
    Le comte semblait cependant beaucoup moins disert qu'hier. Était-ce parce qu'il n'avait pas picolé ?

    Ou alors était-ce la présence de sa fille qui expliquait son changement de comportement ?"""

    $ stats.visited.add("comte_carimall")
    return 


label side_ekul_vivant:
    $ stats.visited.add("ekul_vivant")

    nvl clear
    window hide
    scene black
    with fade
    play music "undying_love.mp3" fadein 1.0 fadeout 1.0 
    window show

    """
    Lorsqu'il rentra dans le château pour vérifier si, par miracle, le comte d'Ekul n'avait pas survécu, William fut surpris de trouver celui-ci assis sur un fauteuil, un cigare à la bouche.
    """

    ekul "Ah, William. J'ai peur que votre visite chez nous ne vous ait quelque peu... transformé."

    william vampire """
    Effectivement, Monsieur le Comte.

    Mais je suis heureux de vous voir en vie.
    """

    ekul """
    Ce n'est pas exactement le bon terme, non.

    Et appelez-moi Vladimir, voulez-vous ?

    Je vous dois la non-vie, après tout."""

    "William arbora un sourire, et s'approcha du fauteuil où était assis le comte."

    william """
    Hé bien, dans ce cas, Vladimir.

    Vous n'auriez pas un autre de ces cigares, par hasard ?"""

    if stats.ekul >= 5 and "appetits" in stats.flags:
        ekul "Bien sûr."

        """Il ouvrit la petite boîte qu'il avait à côté de lui, et en tendit un à William.

        Tandis que celui-ci le mettait dans sa bouche, Vladimir se leva et gratta une allumette."""

        play sound "cigarette.mp3"

        william "Merci."

        ekul "De rien."

        "Un sourire carnassier aux lèvres, il posa sa main sur la joue du peintre."

        "Celui-ci écarta le cigare de sa bouche et sourit à son tour."

        william "Monsieur le Comte serait-il d'humeur à... {i}élargir l'horizon de ses appétits{/i} ?"

        "Pour toute réponse, le comte d'Ekul l'embrassao avec fougue."
        jump fin
    jump epilogue

label side_jamais:
    $ stats.visited.add("jamais")

    """
    William réfléchit. D'accord, probablement pas {i}jamais{/i}, si ? Elle n'était probablement pas née comme ça.

    Ou était-ce possible que si ?"""
    return

label side_chef:
    $ stats.visited.add("chef")

    """Du moins, William supposait qu'il s'agissait du chef, à cause de la magnifique cape blanche et de la coiffe qu'il portait."""
    return

label side_epuisement:
    $ stats.visited.add("epuisement")

    """
    En tout cas, {i}William{/i} était épuisé.

    Il n'était pas certain que ce soit le cas de son adversaire, et se demandait si celui-ci ne se contentait pas de jouer avec lui.
    """

    return


label scene_13_bis:
    $ stats.visited.add("13bis")

    "William grimaça."

    william "Facile à dire. C'est un changement que tu n'as pas eu à subir, hein ?"

    "Carimall lui fit un petit sourire."

    carimall "Effectivement."

        play sound "cigarette.mp3" 

    "William s'alluma une cigarette. Il estimait l'avoir bien méritée."

    "Il devait cependant admettre que la douleur commençait à s'estomper. Ou qu'il se remettait à délirer, il n'était pas trop sûr."

    carimall "Quand tu disais que ce que j’étais réellement n’avait pas d’importance…"

    william "Oui ?"

    carimall "Tu avais compris que je n'étais pas née fille ?"

    "William secoua la tête."

    william "Non, pas à ce moment là. Je pensais encore que tu parlais d'être une vampire."

    carimall "Oh."

    willam "C'est {i}après{/i} que j'ai deviné."

    "Carimall lui fit un sourire un coin."

    carimall "Dans tous les cas, merci. De ne pas m'avoir rejetée."

    "William inspira une bouffée de tabac en lui jetant un regard triste. Y avait-il vraiment un mérite à ne pas s'être montré une ordure ? Est-ce que la barre était si basse ?"

    carimall "Malheureusement, aucune chance qu'un homme aussi sensible soit attiré par les femmes, pas vrai ?"

    "William éclata de rire."

    william "Je ne sais pas. Je veux dire, ce n'est clairement pas mon cas, mais j'ose espérer que certains de {i}ces gens-là{/i} rehaussent un peu le niveau."

    jump side_ekul_vivant

    

    
