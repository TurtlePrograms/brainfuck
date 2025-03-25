class AdvancedToBrainFuck:
    
    def moveTo(pointer,target):
        movement = ">" * (target - pointer) if target > pointer else "<" * (pointer - target)
        pointer = target
        return movement,pointer
    
    def move_value(targetFrom, targetTo, pointer,depth=0):
        tempSpot = 5 + depth
        result = f""
        start = pointer
        moveTo,pointer = AdvancedToBrainFuck.moveTo(pointer, targetFrom)
        result += moveTo
        moveTo,pointer = AdvancedToBrainFuck.moveTo(pointer, targetTo)
        result += f"[{moveTo}+"
        moveTo,pointer = AdvancedToBrainFuck.moveTo(pointer, tempSpot)
        result += f"{moveTo}+"
        moveTo,pointer = AdvancedToBrainFuck.moveTo(pointer, start)
        result += f"{moveTo}-]"
        moveTo,pointer = AdvancedToBrainFuck.moveTo(pointer, tempSpot)
        result += f"{moveTo}["
        moveTo,pointer = AdvancedToBrainFuck.moveTo(pointer, targetFrom)
        result += f"{moveTo}+"
        moveTo,pointer = AdvancedToBrainFuck.moveTo(pointer, tempSpot)
        result += f"{moveTo}-]"
        return result,pointer
        #[>> +>+<<<-]"
        

        return result, pointer


    def process(command,parts,pointer):
        if command == "set":
            if len(parts) == 2:
                return (f"[-]{'+'*ord(parts[1])}",pointer)
            elif len(parts) == 4:
                # move to position
                target = int(parts[1])
                moveTo,pointer = AdvancedToBrainFuck.moveTo(pointer, target)
                return (f"{moveTo}[-]{'+'*ord(parts[3])}",pointer)
        elif command == "copy":
            print("copy")
            print(parts)
            targetFrom = int(parts[1])
            targetTo = int(parts[3])
            print(f"targetFrom: {targetFrom}, targetTo: {targetTo}") 
            return AdvancedToBrainFuck.move_value(targetFrom, targetTo,pointer)
        return ("",pointer)