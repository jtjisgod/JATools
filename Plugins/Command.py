import Plugins.libLog
import Plugins.libApktools
import Plugins.libApkAnalyzer
from termcolor import colored
import os
import sys

class Command :
    apktools = None
    commands = None
    def __init__(self) :
        self.path = "./"
        self.apktools = Plugins.libApktools.Apktools(self.path)
        self.commands = (
            ("decompile", "Application decompile with apktools", self.apktools.decompile),
            ("recompile", "Application re-build with apktools", self.apktools.rebuild),
            ("q", "Quit", sys.exit)
        )
        pass
    def getCommands(self) :
        return self.commands
    def inputCmd(self) :
        cmd = input(">> ")
        for command in self.commands :
            if cmd == command[0] :
                sure = input("Are you sure? (Y/n) : ")
                if sure == "Y" or sure == "y" :
                    command[2]()
                    return 1
                else :
                    return 2
        return 0
