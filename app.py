# import Plugins.libLog
# import Plugins.libApktools
# import Plugins.libApkAnalyzer
from termcolor import colored
import os

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

# import os

# log = Plugins.libLog.Log()
#
# path = "./"

# getMainActivity
# log.kv("Main Activity", apkAnalyzer.mainActivity)


# ShadowExplorer

import Plugins.Command


command = Plugins.Command.Command()

while True :

    clear()
    print("""\n\n\n
    \t\t ▄▄▄██▀▀▀▄▄▄     ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████
    \t\t   ▒██  ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒
    \t\t   ░██  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄
    \t\t▓██▄██▓ ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
    \t\t ▓███▒   ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
    \t\t ▒▓▒▒░   ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
    \t\t ▒ ░▒░    ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
    \t\t ░ ░ ░    ░   ▒    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░
    \t\t ░   ░        ░  ░            ░ ░      ░ ░      ░  ░      ░
    \n\n\n""")

    menues = command.getCommands()
    print("┌──────────────────────────────【 JTJ APK TOOLS 】──────────────────────────────┐")
    print("│ " + ("%77s"%("")) + " │")
    for menu in menues :
        menustr = colored("%15s"%menu[0], "yellow") + " : " + "%55s"%menu[1]
        print("│ " + ("%86s"%(menustr)) + " │")
    print("│ " + ("%77s"%("")) + " │")
    print("└───────────────────────────────────────────────────────────────────────────────┘")
    print("\n" * 3)
    chkCmd = command.inputCmd()
    print("\n\n\n")
    if chkCmd == 0 :
        print("Command is not available")
    elif chkCmd == 2 :
        print("Cancel")
    else :
        print("Command Success")
    input("")










#
