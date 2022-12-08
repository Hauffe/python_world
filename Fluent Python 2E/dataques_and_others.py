from collections import deque

dq = deque(range(10), maxlen=10)
dq

dq.rotate(3) #Rotating with n > 0 takes items from the right end and prepends them to the left; when n < 0 items are taken from left and appended to the right.
dq

dq.rotate(-1)
dq

dq.appendleft(-1)
dq

dq.extend([11, 22, 33])
dq

dq.extendleft([10, 20, 30, 40])
dq