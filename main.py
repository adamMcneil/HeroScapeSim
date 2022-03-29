import random


class Character:
    totalLife = 0
    life = 0
    attack = 0
    defence = 0
    name = "nothing"

    def __init__(self, name, totalLife, attack, defence):
        self.name = name
        self.totalLife = totalLife
        self.life = totalLife
        self.attack = attack
        self.defence = defence

    def Attack(self):
        totalAttack = 0
        for i in range(0, self.attack):
            randNum = random.randint(0, 1)
            if randNum == 0:
                totalAttack += 1
        return totalAttack

    def Defend(self):
        totalDefence = 0
        for defenceDice in range(0, self.defence):
            randNum = random.randint(0, 2)
            if randNum == 0:
                totalDefence += 1
        return totalDefence

    def dealDamage(self, damage):
        if damage > 0:
            self.life -= damage
            if self.life < 0:
                self.life = 0

    def takeTurn(self, otherPlayer):
        damage = self.Attack() - otherPlayer.Defend()
        otherPlayer.dealDamage(damage)

    def restoreHealth(self):
        self.life = self.totalLife


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
    print("turn is both people going")
    print("Average number of turns:", totalTurns / totalBattles)
    print("Most turns taken:", maxNumberOfTurns)
    print("Lest turns taken:", minNumberOfTurns)


ben = Character("ben", 1, 3, 2)
adam = Character("adam", 10, 4, 1)

sonlen = Sonlen("Sonlen", 6, 4, 3)
syvarris = Syvarris("Syvarris", 4, 3, 2)
heirloom = Heirloom("Heirloom", 4, 4, 2)
morgrimm = Heirloom("Morgrimm", 6, 4, 2)
venecWarlord = Character("Vence Warlord", 6, 4, 3)
ironwill = Ironwill("Migol Ironwill", 5, 2, 4)
carr = Character("Agent Carr", 4, 6, 4)

aLotOfBattles(carr, syvarris, 10000)
