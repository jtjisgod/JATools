class Log :
    debug = True
    def p(self, str) :
        if self.debug :
            print(str)
    def kv(self, k, v) :
        if self.debug :
            print(k + " : " + v)
