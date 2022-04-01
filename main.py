import random


class Character:
    name = "nothing"
    totalLife = 0
    life = 0
    attack = 0
    defence = 0
    hasCounterStrike = False
    type = "Character"

    def __init__(self, name, totalLife, attack, defence, hasCounterStrike = False):
        self.name = name
        self.totalLife = totalLife
        self.life = totalLife
        self.attack = attack
        self.defence = defence
        self.hasCounterStrike = hasCounterStrike


    def Attack(self):
        totalAttack = 0
        for i in range(0, self.attack):
            randNum = random.randint(0, 1)
            if randNum == 0:
                totalAttack += 1
        # print(self.name, "attacked with a", self.attack, "and rolled a", totalAttack)
        return totalAttack

    def Defend(self):
        totalDefence = 0
        for defenceDice in range(0, self.defence):
            randNum = random.randint(0, 2)
            if randNum == 0:
                totalDefence += 1
        # print(self.name, "defended with a", self.defence, "and rolled a", totalDefence)

        return totalDefence

    def dealDamage(self, damage):
        if damage > 0:
            self.life -= damage
            # print(self.name, "got hurt", damage)
            if self.life < 0:
                self.life = 0

    def takeTurn(self, otherPlayer):
        # print (self.name, self.life, "/", self.totalLife)
        if otherPlayer.life == 0:
            return
        damage = self.Attack() - otherPlayer.Defend()
        otherPlayer.dealDamage(damage)
        self.counterStrike(otherPlayer, damage)

    def restoreHealth(self):
        self.life = self.totalLife

    def counterStrike(self, otherPlayer, damage):
        if otherPlayer.hasCounterStrike and damage < 0:
            self.dealDamage(damage * -1)
            # print(self.name, "got hurt from counter strike")


class Sonlen(Character):
    def __init__(self, name, totalLife, attack, defence):
        Character.__init__(self, name, totalLife, attack, defence)

    def DragonHealing(self):
        if self.life != self.totalLife:
            randNum = random.randint(1, 20)
            if randNum < 6:
                self.life += 1

    def DragonSwoop(self, otherPlayer):
        randNum = random.randint(1, 20)
        if randNum < 6:
            otherPlayer.dealDamage(1)

    def takeTurn(self, otherPlayer):
        self.DragonHealing()
        Character.takeTurn(self, otherPlayer)
        self.DragonSwoop(otherPlayer)


class Syvarris(Character):
    def __init__(self, name, totalLife, attack, defence):
        Character.__init__(self, name, totalLife, attack, defence)

    def takeTurn(self, otherPlayer):
        Character.takeTurn(self, otherPlayer)
        Character.takeTurn(self, otherPlayer)


class Heirloom(Character):
    def __init__(self, name, totalLife, attack, defence):
        Character.__init__(self, name, totalLife, attack, defence)

    def Defend(self):
        return Character.Defend(self) + 1


class Ironwill(Character):
    rolledAShieldLastAttack = False

    def __init__(self, name, totalLife, attack, defence):
        Character.__init__(self, name, totalLife, attack, defence)

    def Attack(self):
        return Character.Attack(self) * 2

    def Defend(self):
        defenceRolled = Character.Defend(self)
        if defenceRolled > 0:
            self.rolledAShieldLastAttack = True
        else:
            self.rolledAShieldLastAttack = False
        return defenceRolled

    def dealDamage(self, damage):
        if not self.rolledAShieldLastAttack or damage < 1:
            Character.dealDamage(self, damage)
        else:
            Character.dealDamage(self, 1)


class Hawthorne(Character):
    def __init__(self, name, totalLife, attack, defence):
        Character.__init__(self, name, totalLife, attack, defence)

    def takeTurn(self, otherPlayer):
        attackedRolled = Character.Attack(self)
        damage = attackedRolled - otherPlayer.Defend()
        otherPlayer.dealDamage(damage)
        self.counterStrike(otherPlayer, damage)
        if attackedRolled > 1:
            Hawthorne.takeTurn(self, otherPlayer)


class Krug(Character):
    def __init__(self, name, totalLife, attack, defence):
        Character.__init__(self, name, totalLife, attack, defence)

    def takeTurn(self, otherPlayer):
        self.attack = 2 + self.totalLife - self.life
        Character.takeTurn(self, otherPlayer)
        Character.takeTurn(self, otherPlayer)


class MacDirk(Character):
    def __init__(self, name, totalLife, attack, defence):
        Character.__init__(self, name, totalLife, attack, defence)

    def takeTurn(self, otherPlayer):
        Character.takeTurn(self, otherPlayer)
        if self.life > 1:
            Character.takeTurn(self, otherPlayer)
            Character.dealDamage(self, 1)


class Jotun(Character):
    def __init__(self, name, totalLife, attack, defence):
        Character.__init__(self, name, totalLife, attack, defence)

    def takeTurn(self, otherPlayer):
        if random.randint(1, 20) > 13:
            if random.randint(1, 20) > 11:
                otherPlayer.dealDamage(2)
        Character.takeTurn(self, otherPlayer)


class Kaemon(Character):

    def __init__(self, name, totalLife, attack, defence, hasCounterStrike=False):
        Character.__init__(self, name, totalLife, attack, defence, hasCounterStrike)

    def takeTurn(self, otherPlayer):
        Character.takeTurn(self, otherPlayer)
        Character.takeTurn(self, otherPlayer)


class Squad(Character):
    type = "Squad"
    def __init__(self, name, totalLife, attack, defence, hasCounterStrike=False):
        Character.__init__(self, name, totalLife, attack, defence, hasCounterStrike)

    def takeTurn(self, otherPlayer):
        for i in range(0, self.life):
            if otherPlayer.life == 0:
                return
            Character.takeTurn(self, otherPlayer)

    def dealDamage(self, damage):
        if damage > 0:
            self.life -= 1
        if self.life < 0:
            self.life = 0


class Imperium(Squad):
    def __init__(self, name, totalLife, attack, defence):
        Character.__init__(self, name, totalLife, attack, defence)

    def takeTurn(self, otherPlayer):
        for i in range(0, self.life):
            Character.takeTurn(self, otherPlayer)
            Character.takeTurn(self, otherPlayer)


class OmnicronSnipers(Squad):
    def __init__(self, name, totalLife, attack, defence):
        Character.__init__(self, name, totalLife, attack, defence)

    def Attack(self):
        return Character.Attack(self) * 2


class Vipers(Squad):
    def __init__(self, name, totalLife, attack, defence):
        Character.__init__(self, name, totalLife, attack, defence)

    def takeTurn(self, otherPlayer):
        Squad.takeTurn(self, otherPlayer)
        while random.randint(1, 20) > 15:
            Squad.takeTurn(self, otherPlayer)


class Tagawa(Squad):
    def __init__(self, name, totalLife, attack, defence):
        Character.__init__(self, name, totalLife, attack, defence, True)

    def takeTurn(self, otherPlayer):
        for i in range(0, self.life):
            if otherPlayer.type == "Squad":
                self.attack = 3 + otherPlayer.totalLife - otherPlayer.life
            if otherPlayer.life == 0:
                return
            Character.takeTurn(self, otherPlayer)


def Battle(character1, character2):
    numberOfTurns = 0
    while character1.life > 0:
        character1.takeTurn(character2)
        numberOfTurns += 1
        if character2.life < 1:
            break
        character2.takeTurn(character1)
        numberOfTurns += 1
    # print(character1.name, "life:", character1.life)
    # print(character2.name, "life:", character2.life)
    if character2.life == 0:
        return True, numberOfTurns
    else:
        return False, numberOfTurns


def aLotOfBattles(character1, character2, totalBattles, doPrint=False):
    timeCharacter1Won = 0
    totalTurns = 0
    maxNumberOfTurns = -1
    minNumberOfTurns = 100000
    for i in range(0, totalBattles // 2):
        if doPrint:
            print("Battle", i + 1)
        # Battle 1
        character1.restoreHealth()
        character2.restoreHealth()
        battleReturn = list(Battle(character1, character2))
        numOfTurns = battleReturn[1]
        totalTurns += numOfTurns
        if numOfTurns < minNumberOfTurns:
            minNumberOfTurns = numOfTurns
        if numOfTurns > maxNumberOfTurns:
            maxNumberOfTurns = numOfTurns
        if battleReturn[0]:
            timeCharacter1Won += 1
        # Battle 2
        character1.restoreHealth()
        character2.restoreHealth()
        battleReturn = list(Battle(character2, character1))
        numOfTurns = battleReturn[1]
        totalTurns += numOfTurns
        if numOfTurns < minNumberOfTurns:
            minNumberOfTurns = numOfTurns
        if numOfTurns > maxNumberOfTurns:
            maxNumberOfTurns = numOfTurns
        if not battleReturn[0]:
            timeCharacter1Won += 1

    print(character1.name, "win percentage:", timeCharacter1Won / totalBattles * 100)
    print("turn is one person going")
    print("Average number of turns:", totalTurns / totalBattles)
    print("Most turns taken:", maxNumberOfTurns)
    print("Lest turns taken:", minNumberOfTurns)


def test(character, numberOfTestes):
    total = 0
    for i in range(0, numberOfTestes):
        total += character.Defend()
    print(total / numberOfTestes)


ben = Character("ben", 1, 3, 2)
adam = Character("adam", 10, 4, 1)
testCharacter = Character("test", 4, 4, 3)
squad = Squad("new Squad", 3, 100, 3)

sonlen = Sonlen("Sonlen", 6, 4, 3)
syvarris = Syvarris("Syvarris", 4, 3, 2)
heirloom = Heirloom("Heirloom", 4, 4, 2)
morgrimm = Heirloom("Morgrimm", 6, 4, 2)
venecWarlord = Character("Vence Warlord", 6, 4, 3)
ironwill = Ironwill("Migol Ironwill", 5, 2, 4)
carr = Character("Agent Carr", 4, 6, 4)
hawthorne = Hawthorne("Sir Hawthore (blind rage)", 6, 3, 4)
hawthorne2 = Character("Sir Hawthorne (not blind rage)", 6, 4, 4)
krug = Krug("Krug", 8, 2, 3)
macdirk = MacDirk("Alastair Macdirk", 6, 5, 3)
jotun = Jotun("Jotun", 7, 8, 4)
tor_kul_na = Character("Tor-Kul-Na", 6, 6, 5)
thanos = Character("Thanos", 6, 6, 7)
greenDragon = Character("Green Dragon", 9, 5, 5, True)
kaemon = Kaemon("Kaemon Awa", 4, 4, 4, True)

imperium = Imperium("Samira Kyrie", 3, 3, 3)
omnicron = OmnicronSnipers("Omnicron Snipers", 3, 1, 3)
vipers = Vipers("Elite Onyx Vipers", 3, 3, 2)
lavaMosters = Squad("Lava Monsters", 3, 4, 4)
blueSamurai = Squad("Kozuke Samurai", 3, 5, 3, True)
orangeSamurai = Tagawa("Tagawa Samurai", 3, 3, 5)

aLotOfBattles(blueSamurai, orangeSamurai, 10000)
# test(adam, 100000)
