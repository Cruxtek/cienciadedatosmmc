 from dataclasses import dataclass
 @dataclass
 class Record:
 total:int
 win:int
 def cal_ratio(self):
 return self.win/self.total
 def update(self, prob):
 self.total += 1
 self.win += np.random.random() < prob

def cal_greedy_regret(N = 100, probs = [0.5, 0.3, 0.2], evaluation_step = 10):
 K = len(probs)
 Records = [Record(0,0) for _ in range(K)]
 # initial evaluation step
 for i in range(K):
 Records[i].total = evaluation_step
 Records[i].win = np.sum([np.random.random() < probs[i] for _ in 
range(10)])
 # get the index of the most successful slot machine so far
 slots_trajectory = []
 slot_index = np.argmax([record.cal_ratio() for record in Records])
 slots_trajectory.append(slot_index)
 for i in range(N - evaluation_step * K):
 # play the remaining 70 rounds
 Records[slot_index].update(probs[slot_index])
 slot_index = np.argmax([record.cal_ratio() for record in Records])
 slots_trajectory.append(slot_index)
 # print(Records)
 return max(probs)*N - sum([Records[i].total*probs[i] for i in 
range(K)]), slots_trajectory