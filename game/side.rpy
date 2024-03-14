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
    William serra et desserra les doigts pour tenter d'y faire circuler à nouveau circuler le sang.

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

    Mais il n'était pas certain que ses balades en solitaire soient une grande source de satisfaction."""

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

    ekul "Ah, William. J'ai peur que votre visite chez moi ne vous ait... transformé."

    william vampire """
    Effectivement, monsieur le Comte.

    Mais je suis heureux de vous voir en vie.
    """

    ekul """
    Ce n'est pas exactement le bon terme, non.

    Et appelez-moi Vlad, voulez-vous ?

    Je vous dois la non-vie, après tout."""

    "William arbora un sourire, et s'approcha du fauteuil où était assis le comte."

    william """
    Hé bien, dans ce cas, Vlad.

    Vous n'auriez pas un autre de ces cigares, par hasard ?"""

    if stats.ekul >= 5 and "appetits" in stats.flags:
        ekul "Bien sûr."

        """Il ouvrit la petite boîte qu'il avait à côté de lui, et en tendit un à William.

        Tandis que celui-ci le mettait dans sa bouche, Vlad se leva et gratta une allumette."""

        play sound "cigarette.mp3"

        william "Merci."

        ekul "De rien."

        "Un sourire carnassier aux lèvres, il posa sa main sur la joue du peintre."

        "Celui-ci écarta le cigare de sa bouche et sourit à son tour."

        william "Monsieur le comte serait-il d'humeur à... {i}élargir l'horizon de ses appétits{/i} ?"

        "Pour toute réponse, le comte d'Ekul l'embrassa avec fougue."
        jump fin
    jump epilogue

    
