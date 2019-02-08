import random
import Control as c


def run():
    global random_table
    func = random_table.get(random.randint(0, 9))
    func()


def dropped_pencil():
    print("Code Goes Here")


random_table = {
    0: dropped_pencil,
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
