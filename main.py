from classes.game import Person, bcolors

magic = [
    {"name": "Fire", "cost": 10, "dmg": 60},
    {"name": "Thunder", "cost": 15, "dmg": 80},
    {"name": "Blizzard", "cost": 40, "dmg": 160},
]

player = Person(500, 10, 50, 34, magic)
enemy = Person(900, 10, 40, 100, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

name = {0: {"name": "PLAYER 1", "obj": player}, 1: {"name": "PLAYER 2", "obj": enemy}}

print()
while running:
    dmg = 0
    cost = 0
    if i == 20:
        break
    if name[1 if i % 2 == 0 else 0]["obj"].get_hp() <= 0:
        print(bcolors.OKGREEN + name[i % 2]["name"] + " win!" + bcolors.ENDC)
        break
    elif name[i % 2]["obj"].get_hp() <= 0:
        print(
            bcolors.OKGREEN
            + name[1 if i % 2 == 0 else 0]["name"]
            + " win!"
            + bcolors.ENDC
        )
        break
    print("==================================")
    print(bcolors.OKGREEN + name[i % 2]["name"] + " TURN " + bcolors.ENDC)
    player.choose_action()
    choice = input("Choose an action: ")
    if choice == "1" or choice == "Attack":
        dmg = name[i % 2]["obj"].generate_damage()
        name[1 if i % 2 == 0 else 0]["obj"].take_damage(dmg)
    elif choice == "2" or choice == "Magic":
        name[i % 2]["obj"].choose_magic()
        mag = input("Choose a magic: ")
        try:
            dmg = magic[int(mag) - 1]["dmg"]
            cost = magic[int(mag) - 1]["cost"]
            if cost > name[i % 2]["obj"].get_mp():
                print(bcolors.FAIL + "\n Not Enough MP \n" + bcolors.ENDC)
                life_choice = input(" DO YOU WANT USE HP FOR MP: RATIO is 4:1 [Y/n] >")
                if life_choice == "Y" or life_choice == "y":
                    dmgp = round(0.25 * cost)
                    print(name[i % 2]["obj"].get_hp())
                    if name[i % 2]["obj"].get_hp() > dmgp:
                        name[i % 2]["obj"].take_damage(dmgp)
                        print(
                            bcolors.FAIL
                            + bcolors.BOLD
                            + "BECAUSE "
                            + name[i % 2]["name"]
                            +" CHOSE A DEAL OF HP TO MP EXCHANGE "
                            + bcolors.BOLD
                            + " HE TOOK DAMAGE OF: "
                            + str(dmgp)
                            + " HIS HP IS: "
                            + str(name[i % 2]["obj"].get_hp())
                            + bcolors.ENDC
                        )
                    else:
                        print(bcolors.WARNING + "\n DEATH AVERTED \n " + bcolors.ENDC)
                name[1 if i % 2 == 0 else 0]["obj"].take_damage(dmg)
        except:
            pass
        for x in range(len(magic)):
            try:
                if magic[x]["name"] == mag:
                    dmg = magic[x]["dmg"]
                    name[1 if i % 2 == 0 else 0]["obj"].take_damage(magic[x]["dmg"])
            except:
                continue
    else:
        break
    print(
        bcolors.FAIL
        + bcolors.BOLD
        + name[1 if i % 2 == 0 else 0]["name"]
        + " TOOK DAMAGE OF: "
        + str(dmg)
        + " HIS HP IS: "
        + str(name[1 if i % 2 == 0 else 0]["obj"].get_hp())
        + bcolors.ENDC
    )
    i += 1

print(player.generate_damage())
print(player.generate_spell_damage(1))
print(enemy.get_hp())
print(player.get_hp())
