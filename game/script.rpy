# Define character

define TonyStark = Character('Tony Stark', color="#c8ffc8")

define ColonelMarkus = Character('Colonel Marcus', color="#c8ffc8")

define Armurier = Character('L\'armurière', color="#c8ffc8")

define HaroldTrotner = Character('Harold Trotner', color="#c8ffc8")

define Mandy = Character('Mandy', color="#c8ffc8")

define Barmaid = Character('Barmaid', color="#c8ffc8")

init:
    image black = "#000000"
    image CIABuilding = im.Scale("cia.jpg", 1280, 720)
    image Desk = im.Scale("desk.png", 1280, 720)
    image Armory = im.Scale("armory.png", 1280, 720)
    image Library = "library.png"
    image Street = "street.jpg"
    image Street1 = "street1.jpg"
    image Street2 = "street2.jpg"
    image CoffeeShop = im.Scale("coffeeshop.jpg", 1280, 720)
    image BarInt = "barint.jpg"

    image TonyStark = "TonyStark.png"
    image ColonelMarkus = "ColonelMarkus.png"
    image HaroldTrotner = "HaroldTrotner.png"
    image Barmaid = "barmaid.png"

    image FinalScreen = "images/main_menu.png"

    $ weapon = "nothing"
    $ laliste = False

label start:

    scene CIABuilding

    "Quartier Général du Centre Anti-Terroriste (C.A.T.) , New-York City"

    scene Desk

    show TonyStark
    with dissolve

    "L'agent Tony Stark est dans le bureau de son super-viseur au quartier général de CIA à Langley"
    "On attend juste le bruit ambient des autres bureaux"

    TonyStark "Bonjour, Colonel."

    hide TonyStark
    show ColonelMarkus
    with dissolve

    ColonelMarkus "Bonjour, Stark."

    ColonelMarkus "Un de nos réseaux d'agent double en Irak a été infiltré par une taupe."

    ColonelMarkus "Nous devons a tout prix protéger ces agents.\nLa liste de ces agents doit être récupéré."

    hide ColonelMarkus
    show TonyStark
    with dissolve

    TonyStark "Okay, comme d'habitude, je suis votre homme."

    hide ColonelMarkus
    hide TonyStark

    show TonyStark at left
    show ColonelMarkus at right

    ColonelMarkus "Cette liste, vous pouvez la récupérer discrètement soit chez notre agent Harold Trotner au Carnegie Library"
    ColonelMarkus "ou soit chez Helen Connelly, la tenancière du bar le 'CypherPunk'."

    jump DeskChoice1

    return


label DeskChoice1:

    menu:
        "Allez au Toy shop pour récupérer du matériel et des armes":
            jump ToyShop
        "Allez au Carnegie Library":
            jump CarnegieLibrary
        "Allez au Old Firearm shop":
            jump CoffeeShop
    return


label ToyShop:
    scene Armory

    "Au Toy Shop, une joli jeune fille s'affaire à ranger et à nettoyer proprement les armes."

    Armurier "Oh oh Tony !!! Comment vas-tu ?"
    Armurier "Voici ce que je te peux te proposer comme matos de pro, fait un seul choix mais fait le bien !"

    jump ToyShopChoice1

    return


label ToyShop1:
    scene Armory

    Armurier "Hey, t'as pas choisi d'arme !!!"

    jump ToyShopChoice1

    return


label ToyShopChoice1:
    menu:
        "Prendre un pistolet":
            "Le pistolet est Sig Sauer P226"
            $ weapon = "Sig_Sauer_P226"
            jump ToyShopChoice1
        "Prendre un fusil d'assaut":
            "Le fusil d'assault est HK-416"
            $ weapon = "HK-416"
            jump ToyShopChoice1
        "Prendre un fusil de sniper":
            "Le fusil de sniper est un BAR"
            $ weapon = "BAR"
            jump ToyShopChoice1
        "Prendre un fusil à pompe":
            "Le fusil à pompe est Mossberg"
            $ weapon = "Mossberg"
            jump ToyShopChoice1
        "Prendre un gilet par balle":
            "Le gilet est un Blackhawk"
            $ weapon = "Blackhawk"
            jump ToyShopChoice1
        "Quitter le magasin de jouet":
            jump DeskChoice1
    return

label CarnegieLibrary:
    if weapon == "nothing" :
        jump ToyShop1

    scene Street
    "Dans la ville Washington"

    scene Library
    "Dans la bibliothèque Carnegie"

    show HaroldTrotner:
        xalign 0.5
        yalign 0.5
    with dissolve

    "Au Carnegie Library"

    HaroldTrotner "Désolé, mais je n'ai rien du tout à vous refiler"

    jump Street2

    return


label Street2:
    show black
    scene Street2
    "Dans les rue de New-York"

    menu:
        "Allez au coffee shop" if laliste == False:
            jump CoffeeShop
        "Allez au bureau du C.A.T." if laliste == True:
            jump endmission
    return


label CoffeeShop:
    if weapon == "nothing" :
        jump ToyShop1

    show black

    scene CoffeeShop
    "Devant la coffeeshop"

    scene barint at truecenter
    "A l'intérieur du bar"

    show Barmaid
    with dissolve

    Barmaid "Bonsoir, je m'appel Mandy, que puis-je vous servir ?"
    jump choiceCoffeeshop

    return

label choiceCoffeeshop:
    menu:
        "Je veux juste un café":
            TonyStark "Mmmh, good coffee !"
            jump choiceCoffeeshop
        "Vous avez des informations":
            jump choiceCoffeeshop
        "Je veux la liste":
            jump choiceCoffeeshop1
        "Partir du bar":
            jump Street3
    return


label choiceCoffeeshop1:
    show black
    scene barint at truecenter
    "A l'intérieur du bar"

    show Barmaid
    with dissolve

    Barmaid "Voici la liste"

    $ laliste = True

    jump choiceCoffeeshop
    return


label Street3:
    show black
    scene Street2
    "Dans les rue de New-York"

    menu:
        "Allez au Carnegie Library":
            jump CarnegieLibrary
        "Allez au bureau du C.A.T." if laliste == True:
            jump endmission
    return


label endmission:
    scene Desk

    show TonyStark at left
    show ColonelMarkus at right

    ColonelMarkus "Vous avez réussi la mission !"

    ColonelMarkus "Mais on vient de me prévenir que l'agent Trotner a été retrouvé mort."

    ColonelMarkus "Il vous faut à tout prix récupérer et protéger l'agent Mandy !"

    jump endchapter

    return


label endchapter:
    scene FinalScreen
    show black

    "A suivre..."

    return
