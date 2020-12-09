class VidyaGameConsole:
    def __init__(self):
        self.accumulator = 0

    def executeInstruction(code, value) -> int:
        """
            Executes instruction, updates accumulator accordingly, and returns jump to next instruction
        """

        # Each instruction returns an pair of values that represensts: INSTRUCTION JUMP VALUE, ACCUMULATOR INCREASE VALUE
        isr = {
            'acc': lambda val: 1, val,  
            'nop': lambda val: 0, 0,
            'jmp': lambda val: val, 0,
        }

        jmp, acc = isr[code]

        self.accumulator += acc

        return jmp


with open('Input.txt') as file:
    lines = file.readlines()

    console = VidyaGameConsole()

    isr_index = 0
    executed = set()

    while isr_index not in executed:
        # Parse instruction at lines[isr_index]

        # Execute instruction

        # Track execution of instruction

    print(console.accumulator)
