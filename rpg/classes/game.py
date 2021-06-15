import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Character:
    def __init__(self, hp, mp, atk, df, magic):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def gen_mel_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def gen_mag_dmg(self, i):
        magl = self.magic[i]["dmg"] - 5
        magh = self.magic[i]["dmg"] + 5
        return random.randrange(magl, magh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
            return self.hp

    def reduce_mp(self, cost):
        self.hp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp(self, i):
        return self.magic[i]["cost"]

    def choose_action