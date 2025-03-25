from advanced import AdvancedToBrainFuck

class BasicToBrainFuck:
    def __init__(self, input, output):
        self.input = input
        self.output = output
        self.main()
        
    def main(self):
        pointer = 0  # To track the current position
        result = [] 

        with open(self.input) as file:
            lines = file.readlines()

        for line in lines:
            commands, *comment = line.split("///")
            commands = commands.strip()
            parts = commands.split()

            if not parts:
                if comment:
                    result.append("\n///" + "".join(comment))
                continue  # Skip empty lines

            command = parts[0]

            if command == "move":
                direction, steps = parts[1], int(parts[2]) if len(parts) == 3 else 1
                if direction == "right":
                    result.append(">" * steps)
                    pointer += steps  # Update pointer position
                elif direction == "left":
                    result.append("<" * steps)
                    pointer -= steps  # Update pointer position
                elif direction == "to":
                    target = int(parts[2])
                    movement = ">" * (target - pointer) if target > pointer else "<" * (pointer - target)
                    result.append(movement)
                    pointer = target  # Update pointer position

            elif command in {"increase", "decrease"}:
                symbol = "+" if command == "increase" else "-"
                amount = int(parts[1]) if len(parts) == 2 else 1
                result.append(symbol * amount)

            elif command in {"output", "input", "loop", "endloop"}:
                result.append({ 
                    "output": ".", "input": ",", 
                    "loop": "[", "endloop": "]"
                }[command])
            else:
                bf, pointer = AdvancedToBrainFuck.process(command, parts, pointer)
                result.append(bf)

            if comment:
                result.append("///" + "".join(comment))

        with open(self.output, "w") as file:
            file.write("".join(result))  # Join list into a single string
