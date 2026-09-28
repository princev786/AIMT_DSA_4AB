import math
n=5
effA = 2
effB = 3
effC = 5

tasksA = n
tasksB = 0
tasksC = 0
completed = 0
time = 0

while completed<n:
    time+=1
    doneA = min(tasksA,effA)
    tasksA -= doneA
    doneB = min(tasksB,effB)
    tasksB -= doneB
    doneC = min(tasksC,effC)
    tasksC -= doneC
    completed += doneC
    tasksB += doneA
    tasksC += doneB

print(time)
