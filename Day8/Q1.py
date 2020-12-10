class VidyaGameConsole:
    def __init__(self):
        self.accumulator = 0

    def executeInstruction(self, code, value) -> int:
        """
            Executes instruction, updates accumulator accordingly, and returns jump to next instruction
        """

        # Each instruction returns an pair of values that represensts: INSTRUCTION JUMP VALUE, ACCUMULATOR INCREASE VALUE
        isr = {
            'acc': lambda val: (1, val),
            'nop': lambda val: (1, 0),
            'jmp': lambda val: (val, 0),
        }

        jmp, acc = isr[code](value)

        self.accumulator += acc

        return jmp


with open('Input.txt') as file:
    lines = file.readlines()

    console = VidyaGameConsole()

    isr_index = 0
    executed = set()

    while isr_index not in executed:
        executed.add(isr_index)

        # Parse instruction at lines[isr_index]
        instruction = lines[isr_index].split(" ")
        code, value = instruction[0], int(instruction[1])

        # Execute instruction
        jmp = console.executeInstruction(code, value)

        # Track execution of instruction
        isr_index += jmp

    print(console.accumulator)
