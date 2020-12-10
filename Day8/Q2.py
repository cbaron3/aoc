# # Change nop to jump or jump to nop such that the program executes by reaching the end of the file instead of looping

# # IF NOP, CHANGE TO JUMP AND PERFORM SAME PROCESS AS PERFORM (MAKE FUNCTION)
# # CHECK TERMINATION AKA EXECUTING INSTRUCTION WITH ISR_INDEX + LEN(LINES)-1
# import copy


# class VidyaGameConsole:
#     def __init__(self):
#         self.accumulator = 0

#     def executeInstruction(self, code, value) -> int:
#         """
#             Executes instruction, updates accumulator accordingly, and returns jump to next instruction
#         """

#         # Each instruction returns an pair of values that represensts: INSTRUCTION JUMP VALUE, ACCUMULATOR INCREASE VALUE
#         isr = {
#             'acc': lambda val: (1, val),
#             'nop': lambda val: (1, 0),
#             'jmp': lambda val: (val, 0),
#         }

#         jmp, acc = isr[code](value)

#         self.accumulator += acc

#         return jmp


# def checkTerimination(ind, e, lines, console_copy, c, v):
#     executed = set(e)
#     isr_index = 0

#     executed.add(ind)
#     jmp = console_copy.executeInstruction(c, v)
#     isr_index += jmp

#     if isr_index == len(lines):
#         print("Here now")
#         return True, console_copy.accumulator

#     while isr_index not in executed:
#         executed.add(isr_index)

#         # Parse instruction at lines[isr_index]
#         instruction = lines[isr_index].split(" ")
#         code, value = instruction[0], int(instruction[1])

#         jmp = console_copy.executeInstruction(code, value)

#         # Track execution of instruction
#         isr_index += jmp

#         if isr_index == len(lines):
#             print("Here")
#             return True, console_copy.accumulator

#     return False, 0


# with open('Input.txt') as file:
#     lines = file.readlines()

#     console = VidyaGameConsole()

#     isr_index = 0
#     executed = set()

#     while isr_index not in executed:
#         executed.add(isr_index)

#         swap = {
#             "nop": "jmp",
#             "jmp": "nop",
#         }

#         # Parse instruction at lines[isr_index]
#         instruction = lines[isr_index].split(" ")
#         code, value = instruction[0], int(instruction[1])

#         if code != "acc":
#             found, acc = checkTerimination(isr_index, executed,
#                                            lines, copy.deepcopy(console), swap[code], value)

#             if found:
#                 print(acc)
#                 # break

#         # Execute instruction
#         jmp = console.executeInstruction(code, value)

#         # Track execution of instruction
#         isr_index += jmp

#     # print(console.accumulator)

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

    # Swap if needed
    swap = {
        "nop": "jmp",
        "jmp": "nop",
        "acc": "acc"
    }

    for index, line in enumerate(lines):
        console = VidyaGameConsole()
        isr_index = 0
        executed = set()

        while isr_index not in executed:
            executed.add(isr_index)

            # Parse instruction at lines[isr_index]
            instruction = lines[isr_index].split(" ")
            code, value = instruction[0], int(instruction[1])

            # Swap the one instruction in the outer for loop iteration
            if isr_index == index:
                code = swap[code]

            jmp = console.executeInstruction(code, value)

            isr_index += jmp

            # Check for "normal termination" aka program ends by executing the last instruction in the list
            if isr_index == len(lines):
                # Hahahahaha so much for using a smart solution
                print(console.accumulator)
                break
