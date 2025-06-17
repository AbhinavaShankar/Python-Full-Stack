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

     def get_user_logs(self, user_id: str):
         return self.user_logs.get(user_id, [])

     def count_levels(self):
         return dict(self.level_count)

     def get_recent_logs(self):
         return self.recent_logs

     def filter_logs(self, keyword: str) :
         keyword_lower = keyword.lower()
         return [log for log in self.recent_logs if keyword_lower in log["message"].lower()]

logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]


ls = LogSystems(capacity=3)


for log in logs:
    ls.add_log(log)

print("Logs for user1:")
print(ls.get_user_logs("user1"))

print("Log level counts:")
print(ls.count_levels())

print("Logs containing 'connect':")
print(ls.filter_logs("connect"))

print("Recent logs (capacity = 3):")
print(ls.get_recent_logs())
