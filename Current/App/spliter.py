class newSpliter():
    def split(self,val:str):
        lastx = 0;
        count = 0;

        camUrl = ""
        gsName = ""
        pin = ""
        auth = ""

        for x in range(len(val)):

            value = 0

            if val[x] == "|":
                value = val[lastx:x] 
                count += 1
                if count == 1:
                    camUrl = value
                if count == 2:
                    gsName = value
                if count == 3:
                    pin = value
                if count == 4:
                    auth = value

                lastx = x + 1
            if x == len(val)-1:
                auth = val[lastx:x+1]
                count += 1

                lastx = x + 1
        t = (camUrl, gsName, pin, auth)
        return t