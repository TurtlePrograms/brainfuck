class BrainFuckInterpreter:
    values = []
    pointer = 0
    
    position = {"row": 0, "col": 0}
    loopDepth = 0
    lines = []
    
    def __init__(self,path):
        self.values = [0] * 255
        self.pointer = 0
        
        self.position = {"row": 0, "col": -1}
        with open(path) as file:
            self.lines = file.readlines()
    
    def nextPosition(self):
        self.position["col"]+=1
        if self.position["col"] >= len(self.lines[self.position["row"]]):
            self.position["col"] = 0
            self.position["row"] += 1
            if self.position["row"] >= len(self.lines):
                self.position["row"] = -1
    
    def previousPosition(self):
        self.position["col"] -= 1
        if self.position["col"] < 0:
            self.position["row"] -= 1
            if self.position["row"] < 0:
                self.position["row"] = -1
                return
            self.position["col"] = len(self.lines[self.position["row"]]) - 1
    
    def interpret(self):
        while True:
            self.nextPosition()
            if self.position["row"] == -1:
                break
            self.processCommand(self.currentCommand())

    def currentValue(self):
        return self.values[self.pointer]
    
    def currentCommand(self):
        return self.lines[self.position["row"]][self.position["col"]]

    def changeValue(self,change):
        self.values[self.pointer] += change
        self.values[self.pointer] = max(0, min(255, self.currentValue()))
        
    def changePointer(self,change):
        self.pointer += change
        self.pointer = max(0, min(self.pointer, len(self.values) - 1))

    def restartLoop(self):
        depth = 1
        while depth > 0:
            self.previousPosition()
            if self.currentCommand() == "[":
                depth -= 1
            elif self.currentCommand() == "]":
                depth += 1

    def skipLoop(self):
        depth = 1
        while depth > 0:
            self.nextPosition()
            if self.currentCommand() == "[":
                depth += 1
            elif self.currentCommand() == "]":
                depth -= 1
    
    def processCommand(self, command):
        match command:
            case "+":
                self.changeValue(1)
            case "-":
                self.changeValue(-1)
            case ".":
                print(chr(self.currentValue()), end="")
            case ">":
                self.changePointer(1)
            case "<":
                self.changePointer(-1)
            case "[":
                self.loopDepth+=1
                if (self.currentValue() == 0):
                    self.skipLoop()
            case "]":
                if (self.currentValue() != 0):
                    self.restartLoop()
                else:
                    self.loopDepth -=1
            case ",":
                self.values[self.pointer] = ord(input())
            case "///":
                self.position["row"] = +1
                self.position["col"] = -1
            case _:
                pass

