import argparse
import os
import sys
from difflib import get_close_matches

import BasicToBrainFuck
import BrainFuckToBasic
import BrainFuckInterpreter

def validate_file(filename, required_ext, must_exist=True):
    """Ensures the filename has the correct extension and optionally checks existence."""
    if not filename.endswith(required_ext):
        filename += required_ext
    
    if must_exist and not os.path.isfile(filename):
        sys.exit(f"Error: File '{filename}' does not exist.")
    
    return filename

def validate_output_file(filename, required_ext, overwrite):
    """Ensures output filename has the correct extension and checks for overwrite permission."""
    if not filename.endswith(required_ext):
        filename += required_ext
    
    if os.path.isfile(filename) and not overwrite:
        sys.exit(f"Error: File '{filename}' already exists. Use --overwrite to replace it.")
    
    return filename

def suggest_mode(user_input, valid_modes):
    """Suggests the closest valid mode if the user enters an incorrect one."""
    match = get_close_matches(user_input, valid_modes, n=1, cutoff=0.6)
    if match:
        sys.exit(f"Error: Invalid mode '{user_input}'. Did you mean '{match[0]}'?")
    else:
        sys.exit(f"Error: Invalid mode '{user_input}'. Choose from {', '.join(valid_modes)}")

def main():
    valid_modes = {
        "interpret": "bf",
        "convert-bf-to-bfb": "bftobfb",
        "convert-bfb-to-bf": "bfbtobf",
        "bf": "bf",
        "bftobfb": "bftobfb",
        "bfbtobf": "bfbtobf",
        "select": "select"
    }
    
    parser = argparse.ArgumentParser(description="Brainfuck Converter Script")
    parser.add_argument("mode", help="Conversion mode (e.g., 'interpret', 'convert-bf-to-bfb', 'convert-bfb-to-bf')")
    parser.add_argument("input", nargs="?", help="Input file name")
    parser.add_argument("output", nargs="?", help="Output file name (required for certain modes)")
    parser.add_argument("--overwrite", action="store_true", help="Allow overwriting output files")
    
    args = parser.parse_args()
    mode = valid_modes.get(args.mode.lower())
    inputArg = args.input
    outputArg = args.output
    
    
    if not mode:
        suggest_mode(args.mode, valid_modes.keys())
        
    if args.mode == "select":
        print("Select a mode:\n1. Interpret BrainFuck code\n2. Convert BrainFuck to Basic\n3. Convert Basic to BrainFuck")
        mode = input("Enter the number of the mode: ")
        if mode == "1":
            mode = "bf"
            print("Enter the name of the BrainFuck file to interpret:")
            inputArg = input()
        elif mode == "2":
            mode = "bftobfb"
            print("Enter the name of the BrainFuck file to convert to Basic:")
            inputArg = input()
            print("Enter the name of the output Basic file: (Optional)")
            outputArg = input()
        elif mode == "3":
            mode = "bfbtobf"
            print("Enter the name of the Basic file to convert to BrainFuck:")
            inputArg = input()
            print("Enter the name of the output BrainFuck file: (Optional)")
            outputArg = input()
        else:
            sys.exit("Error: Invalid mode selection.")
        
                
    
    if mode == "bf":
        # BrainFuck interpreter
        input_file = validate_file(inputArg, ".bf")
        interpreter = BrainFuckInterpreter.BrainFuckInterpreter(input_file)
        interpreter.interpret()
    elif mode == "bftobfb":
        # Basic to BrainFuck conversion
        input_file = validate_file(inputArg, ".bf")
        output_file = outputArg or input_file.replace(".bf", ".bfb")
        output_file = validate_output_file(output_file, ".bfb", args.overwrite)
        BrainFuckToBasic.BrainFuckToBasic(input_file, output_file)
        print(f"Output written to {output_file}")
    elif mode == "bfbtobf":
        # BrainFuck to Basic conversion
        input_file = validate_file(inputArg, ".bfb")
        output_file = outputArg or input_file.replace(".bfb", ".bf")
        output_file = validate_output_file(output_file, ".bf", args.overwrite)
        BasicToBrainFuck.BasicToBrainFuck(input_file, output_file)
        print(f"Output written to {output_file}")
    
if __name__ == "__main__":
    main()
