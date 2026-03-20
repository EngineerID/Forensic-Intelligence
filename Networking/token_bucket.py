import time
import random

class TokenBucket:
    """Simple token bucket rate limiter simulation"""
    def __init__(self, rate: float, burst: float):
        self.rate = rate          # tokens per second
        self.burst = burst        # max bucket size
        self.tokens = burst
        self.last_time = time.time()

    def consume(self, amount: float = 1.0) -> bool:
        """Try to consume tokens; return True if allowed"""
        now = time.time()
        self.tokens += (now - self.last_time) * self.rate
        self.tokens = min(self.tokens, self.burst)
        self.last_time = now
        
        if self.tokens >= amount:
            self.tokens -= amount
            return True
        return False

# Demo: simulate bursty traffic
if __name__ == "__main__":
    limiter = TokenBucket(rate=10.0, burst=20.0)  # 10 units/sec, burst up to 20
    for i in range(30):
        size = random.choice([1, 5, 15])  # simulate packet sizes
        allowed = limiter.consume(size)
        print(f"t={i:2d} | size={size:2d} | allowed={allowed} | tokens={limiter.tokens:.1f}")
        time.sleep(0.2)