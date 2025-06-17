from collections import defaultdict,deque

class LogSystems:
     def __init__(self, capacity: int):
         self.capacity = capacity
         self.recent_logs = deque(maxlen=capacity)
         self.user_logs = defaultdict(list)
         self.level_count = defaultdict(int)


     def add_log(self, line: str):
         arr = line.split();
         user = arr[2]
         user = user[:len(user)-1]
         level = arr[1]
         timestamp = arr[0]
         timestamp = timestamp[1:len(timestamp)-1]
         message = line.split(': ',1)[1]


         log = {
             "timestamp": timestamp,
             "level": level,
             "user": user,
             "message": message
         }
         self.user_logs[user].append(log)
         self.level_count[level] += 1
         self.recent_logs.append(log)
