class Cmd:
    def __init__(self):
        ...
    def Decode(self,cmd):

        tokens = {"Args":cmd.split(">",1)[1].split(","),"Cmd":cmd.split(">",1)[0]}
        for i in range(len(tokens["Args"])):
            base = ""
            try:
                tokens["Args"][i] = tokens["Args"][i].split(":",1)
            except:
                ...
        print(tokens["Args"])

        return tokens
#ddd = Cmd()
#print(ddd.Decode("$stats>gda:2342,gs:321,kruto:asdas"))