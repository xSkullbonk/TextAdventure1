
# Klasse für Spielerobjekt
class playerobject:
    def __init__(self, name):
        self.name = name
        self.inventory = []

inpname = input("Wie ist dein Name? ")
player = playerobject(inpname)

print("Soso, dein Name ist also " + player.name + "... ")
print("Hier, nimm erst mal diesen BongBong")

print("--BONBON ERHALTEN--")
player.inventory.append("BonBon")

# print(player.inventory)
# if "BonBon" in player.inventory:
#     print("hat geklappt!")
# else: print("hat nicht geklappt!")

def intro: 
    inpname = input("Wie ist dein Name? ")
    player = playerobject(inpname)
    print("SPRECHENDER JOGHURTBECHER: Soso, dein Name ist also " + player.name + "... ")

    print("Hier, nimm erst mal diesen BongBong")
    print("--BONBON ERHALTEN--")
    player.inventory.append("BonBon")

    print("Na dann, könnten wir ja mal darüber reden, wie du auf dieser einsamen Insel gelandet bist...")
    x = input("Kannst du dich überhaupt an irgendetwas erinnern? ")
    if x = upper("ja"):
        input("")

    