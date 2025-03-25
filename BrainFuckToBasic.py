class BrainFuckToBasic:
    def __init__(self,input,output):
        self.input = input
        self.output = output
        self.main()
        
    def main(self):
        result = [] 

        with open(self.input) as file:
            lines = file.readlines()

        for line in lines:
            commands, *comment = line.split("///")
            commentString = "".join(comment).strip()
            commands = commands.strip()

            if not commands:
                if commentString:
                    result.append("///" + commentString)
                continue  # Skip empty lines

            commands += " "# To make sure the last command is processed
            lastChar = ""
            counter = 0
            for char in commands:
                if lastChar == "":
                    lastChar = char
                    counter = 1
                    continue
                
                if char == lastChar:
                    counter += 1
                else:
                    if lastChar:
                        if lastChar == "+":
                            result.append(f"increase {counter}")
                        elif lastChar == "-":
                            result.append(f"decrease {counter}")
                        elif lastChar == ">":
                            result.append(f"move right {counter}")
                        elif lastChar == "<":
                            result.append(f"move left {counter}")
                        elif lastChar == ".":
                            result.append("output")
                        elif lastChar == ",":
                            result.append("input")
                        elif lastChar == "[":
                            result.append("loop")
                        elif lastChar == "]":
                            result.append("endloop")
                        else:
                            print(f"Unknown char {lastChar}")
                    lastChar = char
                    counter = 1
            if comment:
                if len(result) > 0:
                    result[-1] += " ///" + commentString
                else:
                    result.append("///" + commentString)
                
                
        
        with open(self.output, "w") as file:
            file.write("\n".join(result))

