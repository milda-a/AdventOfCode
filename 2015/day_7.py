import read_data

wire_signals = {}
wire_instructions = {}


def evaluate(wire, instructions):
    if wire_signals.get(wire, None):
        return wire_signals[wire]
    elif len(instructions) == 1:
        wire_signals[wire] = (
            evaluate(wire_signals[instructions[0]], wire_instructions[instructions[0]])
            if instructions[0].isalpha()
            else int(instructions[0])
        )
        return wire_signals[wire]
    else:
        if "NOT" in instructions:
            wire_signals[wire] = ~evaluate(
                instructions[1], wire_instructions[instructions[1]]
            )
        else:
            i_1 = (
                evaluate(instructions[0], wire_instructions[instructions[0]])
                if instructions[0].isalpha()
                else int(instructions[0])
            )
            i_2 = (
                evaluate(instructions[2], wire_instructions[instructions[2]])
                if instructions[2].isalpha()
                else int(instructions[2])
            )
            if "OR" in instructions:
                wire_signals[wire] = i_1 | i_2
            elif "AND" in instructions:
                wire_signals[wire] = i_1 & i_2
            elif "LSHIFT" in instructions:
                wire_signals[wire] = i_1 << i_2
            elif "RSHIFT" in instructions:
                wire_signals[wire] = i_1 >> i_2
        return wire_signals[wire]


def main(source):
    for instruction in source:
        split_up = instruction.split(" ")
        wire_instructions[split_up[-1]] = split_up[:-2]
        wire_signals[split_up[-1]] = None
    # print(wire_instructions)
    for wire, instruction in wire_instructions.items():
        evaluate(wire, instruction)
    print(wire_signals["a"])


if __name__ == "__main__":
    main(read_data.read_in_data("inputs/day_7.txt"))
