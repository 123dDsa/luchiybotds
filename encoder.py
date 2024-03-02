class Decoder:
    def __init__(self,file):
        self.file = open(file, "r")
    def Decode(self):
        lines = self.file.readlines()
        tokensList = []
        for line in lines:
            #print(line)
            tokens = {"user":line.split(":",2)[1],
                    "stats":line.split("{",1)[1].split("}",1)[0].split(",")}
            stats = {}
            #print(tokens["user"])
            #print(tokens["stats"])
            for stat in tokens["stats"]:
                stats[stat.split(":")[0]] = stat.split(":")[1]
                #print(stat)
            #print(stats)
            tokens["stats"] = stats
            tokensList.append(tokens)
        return tokensList
        self.file.close()
class Reg:
    def __init__(self):
        ...
    def register(self,id,name):
        file = open("test.test","a")
        file.write("\nuser:"+id+":{money:0,diamons:0,name:"+name+"}")