import Plugins.libLog
import Plugins.libApktools
import Plugins.libApkAnalyzer
from termcolor import colored
import os
import sys

class Command :
    apktools = None
    apkAnalyzer = None
    commands = None
    def __init__(self) :
        self.path = "./"
        self.init()
    def init(self) :
        self.apktools = Plugins.libApktools.Apktools(self.path)
        self.apkAnalyzer = Plugins.libApkAnalyzer.ApkAnalyzer(self.path)
        self.commands = (
            ("path", "Change Path", self.changePath),
            ("main", "show main activity", self.apkAnalyzer.getMainActivity),
            ("show-activities", "List of Activities", self.apkAnalyzer.showActivities),
            # ("comment-actvities", "List of Activities", self.showActivities),
            # ("comment-actvities", "List of Activities", self.showActivities),
            ("decompile", "Application decompile with apktools", self.apktools.decompile),
            ("recompile", "Application re-build with apktools", self.apktools.rebuild),
            ("q", "Quit", sys.exit)
        )
    def changePath(self) :
        self.path = input("Change path to : ") + "/"
        self.init()
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
