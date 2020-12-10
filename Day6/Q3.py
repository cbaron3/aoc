import time

elapsed_time = []

for i in range(100):
    start_time = time.time()

    def common_answers(ind):
        tracked = defaultdict(int)

        common = set(ind[0])

        for a in ind:
            common = common.intersection((set(a)))
        return len(common) - 1

    with open('Input.txt') as file:
        group_answers = []
        answer = 0

        for line in file:
            if line != '\n':
                group_answers += [line*1000]
            else:
                answer += common_answers(group_answers)
                group_answers = []

        answer += common_answers(group_answers)

    elapsed_time.append(time.time() - start_time)
print(sum(elapsed_time)/len(elapsed_time))
