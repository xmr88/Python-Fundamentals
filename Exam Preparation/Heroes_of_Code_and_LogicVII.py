def heroes_of_code():
    n = int(input())
    heroes = {}
    
    for _ in range(n):
        name, hp, mp = input().split()
        heroes[name] = [min(100, int(hp)), min(200, int(mp))]
    
    while True:
        command = input()
        if command == "End":
            break
        
        parts = command.split(" - ")
        action, hero = parts[0], parts[1]
        
        if action == "CastSpell":
            mp_needed, spell = int(parts[2]), parts[3]
            if heroes[hero][1] >= mp_needed:
                heroes[hero][1] -= mp_needed
                print(f"{hero} has successfully cast {spell} and now has {heroes[hero][1]} MP!")
            else:
                print(f"{hero} does not have enough MP to cast {spell}!")
        
        elif action == "TakeDamage":
            damage, attacker = int(parts[2]), parts[3]
            heroes[hero][0] -= damage
            if heroes[hero][0] > 0:
                print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!")
            else:
                print(f"{hero} has been killed by {attacker}!")
                del heroes[hero]
        
        elif action == "Recharge":
            amount = int(parts[2])
            recovered = min(200 - heroes[hero][1], amount)
            heroes[hero][1] += recovered
            print(f"{hero} recharged for {recovered} MP!")
        
        elif action == "Heal":
            amount = int(parts[2])
            recovered = min(100 - heroes[hero][0], amount)
            heroes[hero][0] += recovered
            print(f"{hero} healed for {recovered} HP!")
    
    for hero, stats in heroes.items():
        print(f"{hero}\n  HP: {stats[0]}\n  MP: {stats[1]}")

heroes_of_code()
