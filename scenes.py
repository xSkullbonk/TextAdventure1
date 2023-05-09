import sys, time, classes, functions

# def slow_print(input_str):
#     for c in input_str:
#         sys.stdout.write(c)
#         sys.stdout.flush()
#         time.sleep(0.05)
#     sys.stdout.write('\n')

# Introszene
def intro(): 
    functions.slow_print("Du kommst langsam zu Bewusstsein.")
    functions.slow_print("Du fühlst die warme Sonne auf deinem Rücken.")
    functions.slow_print("Getrocknete Salzkristalle spannen sich um deinen Körper, ")
    functions.slow_print("wie eine zweite Haut.")
    functions.slow_print("Eine Möwe umsingt den friedsam säuselnden Wind")
    functions.slow_print('UNBEKANNT: "...Wie ist dein Name?" ')
    inputname = input()
    player = classes.playerobject(inputname)
    functions.slow_print('...Woher kam diese Stimme?')
    functions.slow_print('Du versuchst, deine Augen zu öffnen, aber ein stechender Schmerz hält dich davon ab...')
    functions.slow_print('Die Stimme hört sich irgendwie hohl an,')
    functions.slow_print('als würde jemand in einen Joghurtbecher sprechen...')
    functions.slow_print('SPRECHENDER JOGHURTBECHER: "Soso, dein Name ist also ' + player.name + '..." ')
    time.sleep(0.5)
    functions.slow_print('"Hier, nimm erst mal diesen BongBong"')
    time.sleep(1)
    functions.slow_print('...')
    functions.slow_print('Du musst ihn schon nehmen.')
    time.sleep(0.5)
    functions.slow_print('// Du ortest die Stimme und greifst in den Joghurtbecher //')
    time.sleep(1)
    functions.slow_print("--BONBON ERHALTEN--")
    player.inventory.append("BonBon")  
    time.sleep(1)
    functions.slow_print("Na dann, könnten wir ja mal darüber reden, ")
    functions.slow_print("wie du auf dieser einsamen Insel gelandet bist...")
    scene1()

def scene1():
    x = input("Kannst du dich überhaupt an irgendetwas erinnern? ").upper()
    if x == "JA":
        time.sleep(1)
        functions.print('Ja? An was erinnerst du dich denn?')
        input("\n")
        time.sleep(2)
        functions.print("Ich glaube, du babbelst...") 
    elif x == "NEIN":
        functions.slow_print("Toll, ich weiß es auch nicht.")
    else: 
        functions.slow_print("Also, da hast du irgendetwas gesagt was grade nicht passt.") 
        functions.slow_print("Versuchen wir das noch mal?") 
        functions.slow_print("//Der Joghurtbecher räuspert sich und macht weiter, ")
        functions.slow_print("als wäre nichts geschehen//")
        scene1()
    
