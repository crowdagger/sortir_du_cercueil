define config.window = "hide"

define angele = Character('Angèle')
define william = Character("William")
define loup = Character("Loup")
define carimall = Character("Carimall")
define ekul = Character("Comte d'Ekul")
define femme1 = Character("Femme mystérieuse")
define femme2 = Character("Femme mystérieuse")
define femme3 = Character("Femme mystérieuse")
define inqui = Character("Inquisiteur")

label start:
    scene black
    with fade

    show text "Lizzie Crowdagger présente" with dissolve

    $ renpy.pause(2.0)

    show text "SORTIR DU CERCUEIL" with dissolve

    $ renpy.pause(2.0)

    scene black
    with dissolve

    """
    {a=call_in_new_context:william}William{/a} fit un sourire crispé à la petite fille qui lui tirait la langue et tourna la tête vers la fenêtre de la diligence.

    Le paysage de la Transye Vanille était magnifique, avec ses belles forêts enneigées et ses montagnes majestueuses ; mais il commençait à s’en lasser un peu.

    William était un artiste dans le besoin, aussi avait-il accepté la proposition du comte d’Ekul, qui le payait grassement pour qu’il vienne dans son château dresser le portrait de {a=call_in_new_context:carimall}sa fille{/a}.

    Il n’avait juste pas réalisé que le voyage serait si long, que la diligence lui ferait si mal aux fesses, qu’il ne pourrait pas fumer pendant aussi longtemps et qu’il y aurait tant de monde à l’intérieur.

    La voiture était en effet pleinement occupée : {a=call_in_new_context:jeunes_hommes}deux jeunes hommes bien habillés{/a} partageaient sa banquette, tandis qu’il faisait face à un couple hétérosexuel accompagné de leur {a=call_in_new_context:petit_monstre}petit monstre{/a}.

    Il y avait aussi une septième passagère, qui, faute de place, avait la moitié du corps proprement à travers celui de son voisin.

    Si Angèle pouvait se mettre dans cette position, c’était parce qu’elle n’existait pas vraiment et n’était qu’une {a=call_in_new_context:hallucation}hallucination{/a} de l’artiste.


    La diligence se mit enfin à ralentir, ce qui signifiait que le voyage touchait à sa fin.

    Il n’était pas encore arrivé, car il ne s’agissait que d’un embranchement auquel le comte d’Ekul avait promis d’envoyer son cocher.

    William espérait qu’il tiendrait parole : le soleil commençait à disparaître derrière l’horizon et il ne tenait pas à passer la nuit dans la forêt.

    Alors que les chevaux s’arrêtaient, la mère de la petite fille lui attrapa le poignet et lui murmura quelques mots.

    William se contenta de hocher la tête et descendit de la voiture avec soulagement.

    Tandis que le cocher expédiait sans ménagement les deux valises du jeune homme au sol, la femme continua de parler, avant de faire finalement un signe de croix.

    La diligence repartit.
    """

    angele "Qu'est-ce qu'elle disait ?"

    "William s'alluma une cigarette."

    william """
    Oh, rien de bien important.

    De protéger mon cou, quelque chose comme ça.

    Et de {i}buveur décent{/i}.

    Mais il n’y a pas de problème, j’ai pensé à amener une bouteille, je sais que ce sont des choses qui se font.
    """ 

    angele """
    Elle prend vraiment les étrangers pour des gens sans éducation.
    """ 

    william """
    Elle a aussi dit quelque chose… que les choses là-bas n’étaient pas ce qu’elles semblaient être et que le mal était caché là où on ne le soupçonnait pas.
    """ 

    angele "Heureusement que tu aimes bien les mâles, alors." 

    william """
    Ha, ha.

    Bon, j’espère qu’on ne va pas attendre trop longtemps, on se les gèle"""

    angele "Moi, je trouve que ça va."

    william "Toi tu n’existes…"

    loup "AHOUUUUU !!!!" (multiple=2)

    william "Euh… C’était quoi, ça ?" (multiple=2)

    angele "Un loup, non ?"

    "Un nouvel hurlement vint confirmer l’hypothèse de l’hallucination. Il paraissait plus proche."

    william "J’espère que le cocher va arriver vite…"

    "Le jeune homme aperçut un mouvement à la périphérie de son champ de vision. Lorsqu’il tourna la tête, il n’y avait rien."

    william "J’ai cru voir quelque chose."

    angele "Non, il n’y avait rien, rassura Angèle. Tu as rêvé."

    william "Ah."

    angele "Par contre, il y en a un derrière toi."

    "William se retourna lentement et aperçut effectivement un animal qui le fixait de son regard jaune. Puis il en vit un autre sortir d’un fourré voisin."

    william "Bon sang, combien ils sont ?"

    angele "J’en vois cinq. Tout autour de toi."

    william "Hum."

    "Le peintre inspira une bouffée de tabac."

    william "Heureusement que je sais que les loups ne s’attaquent pas aux hommes."

    "Il y eut un moment de silence, pendant lequel les animaux s’approchèrent lentement."

    angele "Tu crois que les loups le savent, eux ?"

    "William soupira."

    william "C’est pas un peu déjà vu, ça ?"

    angele "Quoi ?"

    william "Ta phrase. « Je sais qu’ils ne font pas un truc — tu crois qu’ils le savent, eux ? », c’est aussi refait que le coup du « je ne crois pas en machin — mais on dirait que machin croit en toi »."

    angele "Ben, refait ou pas, t’es dans la merde."

    "William haussa les épaules et essaya de s’approcher doucement d’un arbre. Il n’était pas très doué en escalade mais, s’il apprenait vite, il avait peut-être une chance de s’en sortir vivant."

    angele "Quelqu’un approche."

    """
    William stoppa net, décidant que si quelqu’un arrivait pour le sauver du pétrin il valait mieux pour son prestige qu’il ne soit pas en train d’essayer de grimper de manière ridicule.

    Les loups faisaient des cercles autour de lui en se léchant les babines ; puis, subitement, ils tournèrent la tête vers le chemin et prirent la fuite.

    William tourna la tête à son tour en fronçant les sourcils et aperçut une jeune femme en robe rouge. Elle était grande, avait les cheveux noirs, la peau parfaitement blanche et les yeux verts. Globalement, elle était irréellement magnifique.
    """

    william "Euh…"

    william "Je suppose que vous n’êtes pas le cocher ?"

    carimall """
    Père m’a demandé d’accompagner notre serviteur pour venir vous chercher.

    Excusez-moi du retard, mais nous avons perdu une roue sur le chemin. Le cocher est en train de réparer.

    Je m’appelle Carimall."""

    "Elle tendit gracieusement sa main à William."

    william "William."
    
    "Il lui serra la main."
    
    angele "Hum, je crois que tu étais censé lui faire un baise-main."

    carimall "Je vais prendre vos bagages, William."

    "Elle attrapa les deux valises."

    william "Cela risque d’être un peu lourd…"

    "Elle les souleva comme si elles n’avaient rien pesé."

    william "Euh, bon, ben, d’accord. Je vous suis."

    jump scene_1

label scene_1:
   scene black
   with fade

   """Lorsqu’ils atteignirent le fiacre accidenté, le cocher était en train de terminer de réparer et ils ne durent attendre que quelques minutes avant de poursuivre leur chemin vers le château d’Ekul."""

   carimall """Je suis tellement heureuse de voir quelqu’un !

   Nous ne recevons pas beaucoup, vous savez."""

   "William aperçut la silhouette lugubre du château, le chemin sinueux bordé de ravins qui menait vers lui et la pleine lune en partie masquée par une tour."

   william "Je vois vraiment pas pourquoi…"

   "Mais il marmonnait trop bas pour que la jeune femme l’entende."

   jump scene_2

label scene_2:
    scene black
    with fade
   
    "Le comte d’Ekul attendait sur le pas de la porte. C’était un homme de taille moyenne et de forte corpulence, aux cheveux noirs épais et broussailleux, qui avait quelque chose d’un peu effrayant dans le regard."

    ekul """Bienvenue dans ma demeure !

    Entrez-y librement et de votre plein gré !"""

    william "Ben, vu le chemin que j’ai fait, je ne comptais pas rester dehors."

    "William marmonnait trop bas pour que son interlocuteur l’entende."

    ekul "Bienvenue dans ma demeure ! Entrez-y librement, et laissez un peu de la joie que vous y apportez !"

    angele "Faudrait voir à changer de disque."

    "De son côté, William s’inclinait respectueusement et serrait la main du comte, ou, plutôt, se faisait broyer la main par lui."

    william "Ravi de faire votre connaissance, Monsieur le comte."

    ekul "Venez. Vous devez mourir de faim. Je vais prendre vos bagages."

    "Le jeune homme n’eut pas le temps de protester, car l’homme s’était déjà emparé des deux valises. Le cocher était occupé à détacher les chevaux, tandis que Carimall avait disparu."

    william "Et votre fille ?"

    ekul "Oh, elle est repartie. Elle aime se promener la nuit. Venez, suivez-moi."

    jump scene_3

label scene_3:
    scene black
    with fade
    
    "Le comte d’Ekul fit s’asseoir son invité à une grande table où avait été servi un dîner copieux."

    ekul "Excusez-moi de ne pas vous accompagner, mais j’ai déjà mangé."

    william "Ce n’est pas grave."

    "Le peintre se servit une aile de poulet."

    william "Vu l’heure, je comprends."

    "Il mangea en quantité, pendant que le comte lui posait des questions sur son voyage. Puis ce dernier l’invita à aller s’asseoir devant la cheminée."

    william "Oh. Un instant."

    "Il se dirigea vers ses valises et en sortit une bouteille de vin, qu’il apporta au comte."

    william "Tenez, pour vous remercier de m’accueillir."

    ekul "C’est très aimable à vous. Cependant, je ne bois pas… de vin."

    william "Oh."

    "Il s'assit."

    william "Pardonnez-moi. Je l’ignorais."

    "Le comte s’assit à son tour, fit tourner la bouteille, et écarquilla les yeux en lisant l’étiquette."

    ekul "Cela dit, pour un petit Mondar de 1724, je crois que je pourrais faire une exception."

    jump scene_4

label scene_4:
    scene black
    with fade
    "Le comte partagea ce qui restait de la bouteille entre son verre et celui de William. Tous deux étaient passablement éméchés."

    william "Eh ben, Comte, pour quelqu’un qui ne boit pas… de vin, je trouve que vous êtes un buveur décent."

    ekul "Non, mais quand je dis pas de vin, c’est surtout celui des péquenots du coin."

    ekul "Vu le temps qu’on se trimballe, forcément… Je ne bois pas… de piquette, quoi."

    william """
    Vous faites bien, Comte.

    Faut pas boire n’importe quoi, c’est ma devise."""

    ekul "Mais parfois, nécessité fait loi."

    "Le comte avait pris un air grave, incitant son invité à incliner la tête en approbation."

    william """
    ’videmment.

    Mais dans ce cas…"""

    "Il parut réfléchir pendant quelques secondes."

    william """
    Ça compte pas.

    Bon. J’crois qu’j’vais aller roupiller."""

    ekul """
    Je vais vous montrer votre chambre.

    Demain, vous pourrez dormir aussi tard que vous le voudrez. Je devrai m’absenter jusqu’en fin d’après-midi."""

    william "Boulot, boulot, hein ?"

    jump scene_5

label scene_5:
    scene black
    with fade
    "William se réveilla en grognant et se demanda où il était. Puis les évènements de la veille lui revinrent en mémoire et il comprit pourquoi il avait mal à la tête."

    angele """C’est drôle.

    Il n’y a pas grand-monde, dans cette baraque."""

    william "Laisse-moi dormir…"

    "Il se retourna dans le lit."

    angele "Il est plus de midi !"

    william "Et alors ? Le comte a dit qu’il rentrerait tard."

    angele "Tu devrais aller explorer le château avant qu’il ne rentre !"

    william "Quoi ? Et pourquoi je ferais ça ?"

    angele "Ben, il y a peut-être des trucs de mystérieux ?"

    william "Oh, ouais, super. Non, je crois que je vais continuer ma grasse mâtinée."

    """
    Le jeune homme se leva finalement vers cinq heures de l’après-midi et alla chercher de quoi manger, ce qui s’avéra plus difficile que prévu étant donné que le château était immense et qu’il n’avait que des souvenirs flous du chemin qu’il avait suivi pour arriver à sa chambre.

    À un moment, il crut apercevoir Carimall dans un couloir et voulut aller la saluer, mais lorsqu’il suivit la jeune femme dans la chambre où elle était entrée, il n’y avait plus personne.
    """

    william "J’ai vraiment trop bu hier, moi."

    """
    Lorsqu’il se retourna, il réalisa qu’il n’était plus seul, mais face à trois jeunes femmes à la beauté envoûtante et aux vêtements élaborés quoique peu couvrants. Il décida qu’il avait dû confondre, de loin, l’une d’entre elles avec la fille du comte.

    Les trois dames s’avancèrent vers William, qui recula d’un pas, et elles se parlèrent à l’oreille. Puis elles gloussèrent et le dévisagèrent."""

    femme1 "Il est jeune et fort."

    "Elle se lécha la lèvre d’un air trop sensuel au goût du jeune homme."
    femme1 "À toutes trois il nous donnera un baiser."

    """
    Le jeune homme écarquilla les yeux d’un air horrifié, attrapa un coussin, l’envoya à la figure de celle qui avait prononcé la phrase et se fraya un passage à travers les femmes.

Alors qu’il sortait de la pièce, il faillit percuter le comte d’Ekul, qui, lui, désirait apparemment y entrer.

    Il semblait furieux.
    """

    ekul "Vous l’avez touché ?"

    william """Non.

    Mais il s’en est fallu de peu."""

    "Le comte se tourna vers lui."

    ekul "Eh bien, elles n’ont pas l’air de vous avoir fait beaucoup d’effet."

    femme2 "C’est vrai, ça. C’est vexant."

    william "Ben, ça aurait été trois beaux gars, j’aurais peut-être pas dit non… mais là, des femmes…"

    ekul "Vous voulez dire que… ?"

    "Le comte recula d’un pas."

    william "Euh, ça va."

    william "Sans vouloir vous vexer, Comte, j’ai dit des {i}beaux{/i} gars."

    ekul "Oh."

    "Le comte semblait plus rassuré que vexé."

    ekul "Bien. Avez-vous mangé ?"

    william "Non, d’ailleurs, si vous pouviez me montrer sur un plan où se trouve le salon…"

    jump scene_6

label scene_6:
    scene black
    with fade

    """
    William fut une nouvelle fois le seul à dîner, même si le comte et Carimall discutaient à côté de lui pendant qu’il mangeait.

Ensuite, il suivit la jeune femme pour commencer à peindre son portrait. Elle posa de manière très conventionnelle, mais eut simplement une requête étrange :
    """

    carimall "Je pose à l’intérieur, mais est-ce que vous pourriez dessiner un ciel bleu derrière moi ?"

    william """Bien sûr.

    Ou un coucher de soleil, ce serait plus joli, non ?"""

    carimall """
    Non !

    Le ciel bleu.

    Et un soleil.

    S’il vous plaît ? Vous comprenez ?

    J’ai des problèmes de peau. Le soleil me donne d’affreuses rougeurs… qu’au moins sur un portrait je puisse y avoir droit."""

    william "Cela doit être dur."

    carimall "Vous n’imaginez pas. Et en plus, nous sommes dans un pays si reculé…"

    william """
    Il faut voir le bon côté des choses. Les paysages sont magnifiques.

    Je vais vous peindre devant un superbe décor."""

    carimall "Mouais."

    "Elle ne paraissait pas très convaincue."

    jump scene_7

label scene_7:
    """
    William termina la première ébauche du tableau à peine avant l’aube.
    """

    carimall "C’est magnifique."

    "Elle contemplait le tableau la représentant devant un ciel trop bleu pour être vrai."

    carimall "J’aimerais tellement pouvoir sortir sous un tel soleil…"

    william "As-tu essayé ?"

    "Il s’était mis à la tutoyer dans le courant de la nuit."

    carimall "Ne dis pas de bêtise."

    "Sa réponse avait été sèche, et elle lui tourna le dos."

    carimall "Je… je ne peux pas sortir en plein jour. Ça me tuerait."

    william "Et rester là ?"

    "Il s'alluma une cigarette."

    william """
    Tu ne crois pas que c’est aussi en train de te tuer ?

    Tu appelles ça vivre, rester cloitrée dans ce vieux château ?"""

    carimall """
    J’irais où, de toute façon ?

    Les gens du coin me détestent tous, maintenant.

    Je suis un monstre, pour eux."""

    william "Pourquoi ? Tu n’as pas grand-chose de monstrueux."

    carimall "J’ai trop… changé pour eux, je suppose. Je…"

    william "Tu pleures ?"

    "L’artiste posa sa main sur l’épaule de la jeune femme."

    carimall "Non !"

    "Elle se retourna à nouveau, ignorant la larme de sang qui avait coulé sur sa joue."

    william "Écoute…"

    "Il essuya la larme de sang avec son doigt."

    william """
    Je ne connais pas vos voisins, mais le monde est grand.

    Et il est plus beau à voir le jour.
    """

    "Carimall sourit et saisit le poignet du jeune homme, qui fit une moue mi-horrifiée, mi-interrogative tandis qu’elle léchait la larme rouge qui se trouvait sur son doigt."

    jump scene_8

label scene_8:
    scene black
    with fade

    """
    Le soleil se levait sur un paysage effectivement magnifique qui plaisait beaucoup à William, surtout vu d’une des tours du château.

    La vue plaisait beaucoup moins à Carimall, qui se tenait à l’abri du soleil derrière le renfoncement de la porte."""

    carimall "Je… je ne peux pas…"

    william "Bien sûr que si."

    "Il lui attrapa la main."

    william "C’est dans la tête. Je suis avec toi, d’accord ?"

    carimall "Mais toi tu n’es pas… enfin…"

    william "Ferme les yeux."

    carimall "Ce n’est pas une bonne idée. S’il te plaît…"

    william "Ferme les yeux."

    """
    La jeune femme obéit et abaissa ses paupières, pendant que l’artiste la tirait vers la lumière.

    Alors qu’elle s’avançait, deux nouvelles larmes rouges coulèrent sur ses yeux.

    William s’avança encore de deux pas avant de se retourner. Il vit alors la fumée qui se dégageait du visage de la jeune femme et se demanda s’il n’avait pas fait une erreur en amenant la fille de son hôte en plein jour.
    """

    jump scene_9

label scene_9:
    scene black
    with fade

    """
    Le comte d’Ekul se retourna dans son cercueil et réalisa que quelque chose ne tournait pas rond.

    Il retira le couvercle de ce qui lui servait de lit, s’assit et tourna la tête d’un côté, puis de l’autre.

    Il réalisa alors que sa fille n’était pas là et en fut contrarié.
    """

    jump scene_10

label scene_10:
    scene black
    with fade
    
    carimall "C’est… magnifique…"

    """
    Carimall était ébahie par le lever de soleil auquel elle n’avait pour l’heure jamais eu droit.

    William la regardait, un peu moins inquiet que quelques minutes plus tôt. Elle avait toujours le visage rouge, mais il n’y avait plus de fumée et la brûlure n’avait l’air que superficielle.
    """

    carimall "Merci."

    "Elle serra plus fort la main du jeune homme qu’elle tenait toujours. Il y eut alors un moment magique tandis qu’ils restaient silencieux, contemplant le paysage qui s’ensoleillait peu à peu."

    carimall """
    Tu sais…

    J’ai eu pas mal de changements dans ma vie ces derniers temps."""

    william "Je sais. Ça ne doit pas être facile."

    carimall """Pas tout le temps, non.

    Je…

    Est-ce que tu me vois comme un monstre ?"""

    william """
    Non !

    Bien sûr que non. Je te l’ai dit…"""

    carimall "Mais tu ne sais pas ce que je suis réellement…"

    william "Je m’en moque. Ce n’est pas ça qui…"

    ekul "BORDEL DE DIEU D’ARTISTE DÉBILE !" with vpunch

    "William se retourna et réalisa que le comte d'Ekul se tenait derrière eux, protégé du soleil par le battant de la porte."

    william "Hum. Peut-être que tu ferais mieux de rentrer."

    carimall "Oui. On poursuivra cette discussion ce soir."

    "Le peintre regarda la jeune femme rentrer vers l’ombre protectrice du château, puis fit de même quelques instants plus tard."

    "Il fut alors plaqué contre le mur par le comte, qui commença à lui serrer la gorge." with vpunch

    ekul "Je devrais vous tuer, espèce de crétin !"

    william "Vous dites ça sur…. le coup de la colère, Comte."

    ekul "Vous auriez pu la tuer, espèce de taré !"

    william "Je ne crois… pas…"

    ekul "Vous n’avez aucune idée de ce qu’elle est !"

    william "Vous… réalisez… peux… pas… respirer ?"

    ekul "Vous n’avez aucune idée de ce qu’elle est."

    "Le comte d'Ekul relâcha le peintre. William s’écroula par terre."

    ekul "Si vous lui faites du mal, croyez-moi, je vous le ferai payer cher."

    "Le jeune homme essaya péniblement de reprendre sa respiration pendant que son hôte s’éloignait."

    angele "Il a de la poigne, ce type."

    "William se releva avec difficulté."

    william "Ouais."

    angele "« Vous n’avez aucune idée ce qu’elle est », Non mais, tu l’as entendu ?"

    william "Ouais."

    angele "Elle ne sort pas au soleil, elle a la peau blanche, elle chiale des larmes de sang et on devrait ne pas se douter que c’est une vampire ?"

    william """
    C’est une sorte de tradition, je suppose.

    Je pense que je serais mal vu si je ne faisais pas celui qui ne sait pas."""

    angele "Par contre, je pense qu’au moins Carimall fait semblant de ne pas voir que tu fais semblant de ne pas voir qu’elle est une vampire."

    william """Je ne sais pas.

    Mais je crois que je vais aller me coucher. Tes raisonnements me filent mal au crâne."""

    jump scene_11

label scene_11:
    scene black
    with fade

    angele "Will ?"

    "Le jeune homme ouvrit un œil, grimaça, et le referma."

    angele "Will !"

    william "Hmmmpf ? Quoi ?"

    angele "Tu devrais te lever et descendre dans le hall d’entrée."

    william """Hmmm, hmmm.

    Pourquoi ?"""

    angele "Parce que, si mes calculs sont justes, ça devrait être la guerre d’ici approximativement trente secondes."

    jump scene_12

label scene_12:
    scene black
    with fade

    """
    William se précipita dans le hall d’entrée et arriva en plein milieu d’une bagarre générale.

    Jugeant qu’il n’était pas assez réveillé pour participer à un combat, il se contenta d’observer, en allumant une cigarette pour s’éclaircir les idées.

    Au bout de quelques instants, les conclusions qu’il tira furent les suivantes :

    {b}1 :{/b} une demi-douzaine d’hommes armés étaient entrés dans le château ;

    {b}2 :{/b} leurs tenues semblaient indiquer qu’ils faisaient partie de l’église ;

    {b}3 :{/b} en face d’eux, le comte, sa fille et les trois femmes paraissaient bien démunis.

    Pas étonnant. Il faisait encore jour.

    Le cocher, en revanche, semblait mieux s’en sortir, puisqu’il se transforma en loup géant et parvint à égorger deux hommes et à arracher le cœur d’un troisième avant de mourir d’un carreau en argent qu’il reçut dans la tête.

    Le peintre avança, remarqua que personne ne faisait attention à lui et ramassa une arbalète qu’un homme avait fait tomber.

    Le rapport de force avait évolué avec la mort du cocher car, s’il n’y avait plus que trois assaillants, dont celui qui paraissait être leur chef au vu de sa magnifique cape blanche, les habitants du château semblaient effrayés.

    Le comte regarda sa fille.
    """

    ekul "Fuis !"

    """Il se jeta en hurlant sur un des hommes.

    Mais celui-ci parvint à plonger un pieu dans son corps et Ekul s’écroula, pendant que sa fille prenait la fuite, suivie des trois femmes que William avait croisées la veille.

    Le soldat n’eut cependant pas le temps de se glorifier de son acte, puisqu’il reçut un carreau en pleine tête et mourut aussitôt. Les regards des deux hommes restants se tournèrent vers le peintre."""

    inqui "Qu’avez-vous fait, sombre idiot ?"

    "Pendant qu'il hurlait, le peintre rechargeait son arme."

    inqui "Nous sommes de l’inquisition, venus vous sauver de ces monstres buveurs de sang !"

    william "Vraiment ?"

    inqui "Évidemment ! Ce sont des…"

    william "…vampires ?"

    "Il envoya en souriant un nouveau carreau dans la tête du soldat le moins gradé."

    william "Il aurait fallu que je sois aveugle pour ne pas le réaliser plus tôt."

    inqui "Impie ! Hérétique !"

    """Il dégaina son épée et chargea.

    Le jeune homme lâcha son arbalète devenue inutile et parvint de justesse à ramasser une épée sur un cadavre pour parer le coup.
    """

    $ inqui = "Évêque Cromwey"

    inqui "Je suis l’évêque Cromwey !"

    "Il hurlait entre deux passes d’armes."

    inqui "Prépare-toi à mourir !"

    """William se baissa juste à temps pour éviter la lame, envoya un coup de pied dans les tibias de son adversaire et se précipita dans les escaliers en colimaçon."""

    angele "Je crois que tu aurais dû arrêter le tabac."

    """
    William, en effet, s’épuisait en courant dans les escaliers. Heureusement pour lui, l’évêque n’avait pas un meilleur souffle que lui et il commença à perdre du terrain à partir du quatrième étage.
    """

    angele "Au fait, tu sais où tu vas ?"

    william """
    Évidemment…

    pfff…

    que…

    pfff…

    non…"""

    "Il comprit la remarque perfide d’Angèle lorsqu’il ouvrit la porte qui le bloquait d’un coup de pied rageur et réalisa qu’il se trouvait au sommet d’une tour."

    angele """Il faut voir le bon côté des choses.

    Le paysage est magnifique.

    Il va te tuer devant un superbe décor."""

    """William eut à peine le temps de se retourner et de bloquer l’épée de l’évêque, qui paraissait au contraire rasséréné par un tel paysage.

    Les deux combattants échangèrent quelques bottes, plutôt faiblardes à cause de leur épuisement, avant que d’un geste bien placé l’inquisiteur ne désarme son adversaire.

    Le peintre regarda son épée tomber dans le ravin que surplombait le château et déglutit."""

    inqui "Pourquoi t’es tu donc allié avec ces misérables créatures ?"

    william """
    Carimall est sympathique.

    Qu’est-ce qu’elle a fait de mal ? On ne choisit pas ses parents."""

    inqui """Cette créature est maudite.

    Pire encore que les autres.

    Il faut libérer son âme en brûlant son corps."""

    "William fronça les sourcils."

    william "Pire encore que les autres ?"

    inqui "Oh, tu n’étais pas au courant, hein ?"

    william """
    Peu importe.

    De toute façon, je préfère mille fois les vampires aux ordures de votre espèce."""

    inqui "Tu blasphèmes, misérable, alors qu’il te faudrait te repentir."

    william "J’assume tous mes pêchés."

    inqui "Alors, tu iras en Enfer."

    "William arbora un sourire défiant."

    william """J’aime autant.

    Votre Ciel est beaucoup trop hétérosexuel pour moi."""

    """
    Il se lança alors sur son adversaire.

    La lame de ce dernier lui transperça le cœur.

    Mais William continua à sourire et bascula par-dessus le muret.

    L’évêque réalisa trop tard que William voulait l’entraîner dans sa chute.

    Il parvint néanmoins à se rattraper de justesse à une fissure et se dégagea du jeune homme qui lui tenait la jambe, l’envoyant mourir loin en contrebas.

    Il allait remonter lorsqu’il réalisa que quelqu’un s’était mis debout sur le muret. Levant la tête, il aperçut une femme aux jambes d’autant plus impressionnantes qu’il était situé en dessous."""

    carimall """
    C’est les chaussures à talon.

    Ça fait de longues jambes.

    Et ça a un autre intérêt…"""

    """Elle le lui démontra en lui enfonçant sa chaussure dans la main.

    L'évêque chuta en hurlant."""

    carimall """Ouais, je sais.

    Avec ça, je suis une tombeuse d’hommes."""

    jump scene_13

label scene_13:
    scene black
    with fade

    """
    William sentait son esprit commencer à flotter au-dessus de son corps dans un état extatique qui ne peut d’ordinaire être atteint qu’après avoir consommé quantité de substances illicites.

    Brutalement, il eut mal.

    Atrocement mal.

    Sans doute pire que ce qu’il n’avait jamais enduré.

    Sa gorge le brûla et pendant quelques secondes il crut qu’on lui avait injecté de la lave dans la bouche.

    Ensuite, il réalisa que ce n’était que du sang.
    """

    carimall "Ah, tu te réveilles."

    william "Aaargl."
    
    "La jeune femme retira le poignet qu’elle s’était ouvert et lança un sourire charmeur au nouveau vampire."

    carimall """
    Je sais, ça fait un peu mal.

    Mais ce n’est qu’une fois pour l’éternité."""

    william "Urgl."

    "Le peintre tâcha de s'asseoir."

    carimall """Attends un peu.

    Ça ira mieux dans quelques instants."""

    william "Si tu… le dis…"

    carimall """Par contre, je te préviens, ton corps va changer un peu, dans les jours qui vont venir…

    Mais il paraît que ce n’est pas si dramatique."""

    william "« Il paraît » ?"

    carimall "Ben, moi je suis née comme ça. Je ne peux pas savoir."

    william "Mais tu as dit hier que tu avais traversé des changements…"

    carimall """
    Oh, oui.

    Je ne parlais juste pas de ça.

    Je pensais que tu avais compris…"""

    william """Non.

    Tu parlais de quoi, alors ?"""

    carimall """Je suis née vampire.

    Par contre, je n’étais pas une petite fille."""

    "William écarquilla les yeux de surprise."

    william "QUOI ?" with vpunch

    william """Tu veux dire qu’il y a des bébés vampires ?

    Je croyais que c’était, tu sais ? On ne naît pas vampire, on meurt vampire."""

    carimall """Pas tout le temps.

    Ce que je te disais ce matin…"""

    "Elle approcha son visage de celui du nouveau vampire."

    william "Quoi ?"

    "Il était vaguement dégouté par les lèvres trop proches de Carimall qui, elle, semblait amusée."

    carimall "Tu disais que ce que j’étais réellement n’avait pas d’importance…"

    william "Euh, ouais."

    "Il repoussa doucement la jeune femme."

    william """
    Je ne le disais pas dans ce sens-là non plus.

    Je ne suis pas attiré par les filles."""

    carimall "Oh."

    "William s'alluma une cigarette. Il estimait l'avoir bien méritée."

    william """Désolé.

    Mais, de toute façon, sans être très à cheval sur la morale, ça n’aurait pas été un peu, euh, incestueux ?

    Je veux dire, t’es comme, genre, ma mère vampirique, non ?"""

    jump epilogue

label epilogue:
    scene black
    with fade

    """
    William décida, en allumant un de ces énormes cigares dont lui avait fait cadeau le comte pour le remercier de sa visite, que le voyage de retour s’annonçait plus sympathique que celui de l’aller.

    Déjà, son hallucination, bien que toujours présente, se taisait, et c’était quelque chose qui était assez rare pour qu’il prenne la peine d’en profiter pleinement.

    Mais surtout, la voiture était, étonnamment, beaucoup moins remplie qu’à l’aller.

    En face de lui, il n’y avait que Carimall, terriblement nerveuse à l’idée de quitter sa terre natale pour la première fois.

    Il y avait eu du monde au départ de la diligence, pourtant.

    Mais lorsqu’il avait répondu au sourire d’une vieille femme repoussante en souriant à son tour de toutes ses dents, elle avait marmonné quelques mots tous bas et tous les voyageurs s’étaient soudainement souvenus qu’ils avaient des choses bien plus importantes à faire qu’accomplir un voyage.

    Comme quoi, décida le vampire, il ne fallait jamais négliger les vertus d’un simple sourire."""

    william "Ça va ?"

    """
    Carimall regardait par la fenêtre la silhouette du château disparaitre.

    Même s’il n’y aurait pas de belle et éternelle histoire d’amour entre eux, il l’avait convaincue de l’accompagner, au moins pendant un moment.

    Elle ne pouvait pas rester enfermée à jamais dans un cercueil à fuir les rayons du soleil.
    
    Enfin, techniquement, elle pouvait.

    Mais le jeune homme voulait lui montrer qu’elle pouvait aussi faire {i}autrement{/i}.
    """

    carimall """Je crois que ça va aller.

    J’ai juste un peu peur."""

    william "J’imagine. Tu voulais aller quelque part en particulier ?"

    carimall "Non. Loin."

    william "Je dois te prévenir… Dans le vaste monde, il est possible que tout le monde ne t’accepte pas comme tu es."

    carimall "Je sais. Grâce à l’évêque, je suis parée."
    
    william "Tu veux dire qu’il t’a fait comprendre ce que pouvait être l’intolérance ?"

    "Carimall sourit."

    carimall """
    Oh, non.

    Je veux dire que j’ai récupéré son arbalète et son épée."""

    """William hocha la tête et décida que le comte avait sans doute eu tort de s’inquiéter pour l’avenir de sa fille.

    Elle n’avait peut-être pas une grande expérience du monde, mais elle avait apparemment déjà compris comment il fonctionnait."""

    jump fin 

label fin:
    scene black with dissolve

    show text "FIN" with dissolve

    $ renpy.pause(2.0)
    
    show text "ECRITURE : LIZZIE CROWDAGGER" with dissolve

    $ renpy.pause(2.0)
    
    show text "LICENCE : CC By-SA 4.0" with dissolve

    $ renpy.pause(2.0)

    
    return
