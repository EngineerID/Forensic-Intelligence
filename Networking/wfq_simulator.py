# wfq_simulator.py
import heapq
import random
from collections import deque

class WFQSimulator:
    """Very simple Weighted Fair Queuing simulator"""
    def __init__(self, weights):
        self.weights = weights  # dict: flow_id -> weight
        self.queues = {fid: deque() for fid in weights}
        self.virtual_time = 0.0
        self.finish_times = {}  # flow -> last packet finish time
        self.event_queue = []   # (time, event_type, flow_id, size)

    def arrive(self, time, flow_id, size):
        """Packet arrival"""
        heapq.heappush(self.event_queue, (time, 'arrive', flow_id, size))

    def run(self, max_time=100.0):
        stats = {fid: {'served': 0, 'bytes': 0} for fid in self.weights}
        
        while self.event_queue and self.event_queue[0][0] <= max_time:
            t, event, fid, size = heapq.heappop(self.event_queue)
            
            if event == 'arrive':
                self.queues[fid].append((t, size))
                # Schedule departure using WFQ finish time
                phi = self.weights[fid]
                f_time = max(self.virtual_time, self.finish_times.get(fid, t)) + size / phi
                self.finish_times[fid] = f_time
                heapq.heappush(self.event_queue, (f_time, 'depart', fid, size))
            
            elif event == 'depart':
                if self.queues[fid]:
                    arrival_t, pkt_size = self.queues[fid].popleft()
                    stats[fid]['served'] += 1
                    stats[fid]['bytes'] += pkt_size
                    self.virtual_time = max(self.virtual_time, t)
        
        return stats

# Demo
if __name__ == "__main__":
    sim = WFQSimulator({1: 1.0, 2: 2.0, 3: 0.5})  # flow weights
    
    # Generate some arrivals
    for t in range(0, 50, 2):
        fid = random.choice([1,2,3])
        size = random.randint(100, 800)
        sim.arrive(t, fid, size)
    
    results = sim.run(max_time=100)
    print("WFQ Results:")
    for fid, st in results.items():
        print(f"Flow {fid} (weight {sim.weights[fid]}): {st['served']} pkts, {st['bytes']} bytes")