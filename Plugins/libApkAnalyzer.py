import os
import sys
import subprocess
from xml.etree.ElementTree import parse
from Plugins.libLog import Log
from termcolor import colored

log = Log()

class ApkAnalyzer :
    toolPath = os.path.dirname(os.path.abspath(__file__)) + "/"
    path = ""
    apkdir = "app/"
    manifest = "app/AndroidManifest.xml"
    manifestRead = ""
    perms = []
    activities = []
    mainActivity = ""
    dictActivities = []


    def __init__(self, path) :
        self.path = path
        self.apkdir = path + self.apkdir
        self.manifest = path + self.manifest

        if os.path.isfile(self.manifest) :
            log.p("Manifest Loaded ... '" + self.manifest + "'")
        else :
            log.p("Error, No such file '" + path + "'")
            sys.exit()

        tree = parse(self.manifest)
        root = tree.getroot()
        application = tree.find("application")

        # Permission
        self.perms = root.findall("uses-permission")

        # Activities
        self.activities = application.findall("activity")
        for activity in self.activities :
            isMain = False
            intentFilters = activity.findall("intent-filter")
            for intentFilter in intentFilters :
                if intentFilter.find("action").get(intentFilter.find("action").keys()[0]) == "android.intent.action.MAIN" :
                    isMain = True
            if isMain == True :
                activityName = activity.get("{http://schemas.android.com/apk/res/android}name")
                self.mainActivity = activityName

        # Activities for Comment
        for activity in self.activities :
            actName = activity.get("{http://schemas.android.com/apk/res/android}name")
            comment = ""
            if actName == self.mainActivity :
                comment += "[Main Activity]"
            self.dictActivities.append([actName, comment])
        self.dictActivities = sorted(self.dictActivities, key=lambda x:x[0])

    def showActivities(self) :
        for i in range(0, len(self.dictActivities)) :
            print(
                (colored("%5d. "%i, "red")) +
                self.dictActivities[i][0] + "\t" +
                colored(self.dictActivities[i][1], "yellow")
            )

    def getMainActivity(self) :
        print(colored("Main Activity", "yellow"), self.mainActivity)







#
