import random as rand


class Monster:
    def __init__(self, namn, hp, styrka):
        self.namn = namn
        self.hp = hp
        self.styrka = styrka


def hantera_vald_dörr(hjältenamn, hjältehp, hjältestyrka, ryggsäck):
    print("Du står framför tre dörrar.")
    print("Bakom en dörr kan det finnas en belöning, bakom en annan ett monster.")

    vald_dörr = rand.randint(1, 3)

    gissning = int(input("Välj en dörr (1, 2 eller 3): "))

    if gissning == vald_dörr:
        print("Grattis! Du hittade en skatt!")
        skattkista = ["bandage", "svärd", "med-kit"]
        skatt = rand.choice(skattkista)

        if skatt == "bandage":
            bonus_hp = 1.5
            print(
                f"Du fick ett bandage och hjälpte dig själv från {hjältehp} till {hjältehp + bonus_hp}!"
            )
            hjältehp += bonus_hp
        elif skatt == "svärd":
            bonus_styrka = 2
            print(
                f"Du fick ett svärd och höjde din styrka från {hjältestyrka} till {hjältestyrka + bonus_styrka}"
            )
            hjältestyrka += bonus_styrka
        elif skatt == "med-kit":
            bonus_hp2 = 10
            print(
                f"Du fick ett med-kit och höjde ditt hp från {hjältehp} till {hjältehp + bonus_hp2}"
            )
            hjältehp += bonus_hp2
        ryggsäck.append(skatt)

    else:
        monster1 = Monster("Chewboka", 10, rand.randint(1, 6))
        monster2 = Monster("Mozambiqe", 5, rand.randint(1, 3))
        monster3 = Monster("Chimpamo", 6, 1)

        random_monster = rand.choice([monster1, monster2, monster3])
        print(
            f"Det var en {random_monster.namn}! Du vann striden men tog {random_monster.styrka} i skada."
        )
        hjältehp -= random_monster.styrka
        print(f"{hjältenamn} har nu {hjältehp} hälsa kvar.")
        if hjältehp <= 0:
            print("Du förlorade spelet!")
        else:
            pass

    return hjältehp, hjältestyrka, ryggsäck


def kolla_stats(hjältenamn, hjältehp, hjältestyrka):
    print(f"Stats för {hjältenamn}:")
    print(f"Hälsa: {hjältehp}")
    print(f"Styrka: {hjältestyrka}")


def kolla_ryggsäck(ryggsäck):
    print("Ryggsäckens innehåll:")
    if not ryggsäck:
        print("Ryggsäcken är tom.")
    else:
        for item in ryggsäck:
            print(f"- Ett Ändvänt {item}")


def main():
    hjältenamn = "P & H"
    hjältehp = 10
    hjältestyrka = rand.randint(0, 10)
    ryggsäck = []

    while hjältehp > 0:
        print(
            """
            Välkommen till Äventyrsspelet!

            Vad vill du göra?
            1. Välj dörr
            2. Kolla ryggsäck
            3. Kolla stats
            """
        )

        val = input("")

        if val == "1":
            hjältehp, hjältestyrka, ryggsäck = hantera_vald_dörr(
                hjältenamn, hjältehp, hjältestyrka, ryggsäck
            )

        elif val == "2":
            kolla_ryggsäck(ryggsäck)
        elif val == "3":
            kolla_stats(hjältenamn, hjältehp, hjältestyrka)
        else:
            print("Välj 1, 2 eller 3!")


if __name__ == "__main__":
    main()
