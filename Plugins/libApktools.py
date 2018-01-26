import os
import sys
import subprocess
from Plugins.libLog import Log

log = Log()

class Apktools :
    toolPath = os.path.dirname(os.path.abspath(__file__)) + "/"
    apktools = "java -jar " + toolPath + "apktools.jar "
    path = ""

    apk = "app.apk"
    apkdir = "app"
    target = "app_rebuild.apk"

    def __init__(self, path) :
        self.path = path
        self.apk = path + self.apk
        self.apkdir = path + self.apkdir
        self.target = path + self.target

        if os.path.isfile(self.apk) :
            log.p("APK Loaded ... '" + self.apkdir + "'")
        else :
            log.p("Error, No such file '" + path + "'")
            sys.exit()

    def rebuild(self) :
        os.system(self.apktools + "b " + self.apkdir + " -o " + self.target)
        log.p("Recompiled...")

    def decompile(self) :
        os.system(self.apktools + "d " + self.apk)
        log.p("Decompiled...")
