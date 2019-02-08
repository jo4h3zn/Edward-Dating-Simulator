import random
day = 1
# global variable to keep track of the days (replaces counter for 5 day loop)
LP = 10
# LovePoints, how to win, unlocks new paths, core of the game really.


def lp_up(level):
    global LP
    print(posReacTable.get(random.randint(0, 9)))
    if level == 1:
        LP += 1
    if level == 2:
        LP += 3
    if level == 3:
        LP += 5


def lp_down(level):
    global LP
    print(negReacTable.get(random.randint(0, 9)))
    if level == 1:
        LP -= 1
    if level == 2:
        LP -= 3
    if level == 3:
        LP -= 5


def lp_big_up(level):
    global LP
    print(extraPosReacTable.get(random.randint(0, 9)))
    if level == 1:
        LP += 10
    if level == 2:
        LP += 15
    if level == 3:
        LP += 20


def lp_big_down(level):
    global LP
    print(extraNegReacTable.get(random.randint(0, 9)))
    if level == 1:
        LP -= 10
    if level == 2:
        LP -= 15
    if level == 3:
        LP -= 20


posReacTable = {
    0: "Edward is pleased with you.",
    1: "Edward smiles at you.",
    2: "Edward makes eye contact with you and smiles",
    3: "Edward giggles.",
    4: "You made Edward happy!",
    5: "The corners of Edward's luscious lips turn up slightly.",
    6: "Edward gives you a thumbs up.",
    7: "Edward chuckles.",
    8: "You can see Edward's pleasure with your actions.",
    9: "Edward makes physical contact with you.",
    }

negReacTable = {
    0: "Edward is displeased with you.",
    1: "Edward frowns at you.",
    2: "Edward makes eye contact with you and frowns",
    3: "Edward looks displeased.",
    4: "You made Edward sad!",
    5: "The glourious light in Edward's eyes dims a little.",
    6: "Edward shoots you a sideways glance",
    7: "Edward groans under his breath.",
    8: "You can see Edward's displeasure with your actions.",
    9: "Edward makes an awkward glance away from you.",
    }

extraPosReacTable = {
    0: "",
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
    }

extraNegReacTable = {
    0: "",
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
}
