# Networking Systems & Optimization Theory

**Foundations for building resilient, fair, and high-performance distributed systems.**

This collection distills the essential theory and practical techniques from advanced computer networking — focused on programmability, resource allocation, performance modeling, and stability under real-world constraints.

### Who This Is For
- **Systems & infrastructure engineers** building scalable platforms (data centers, cloud, edge, governance systems)
- **Quantitative developers & researchers** working on optimization engines, digital twins, or performance-critical finance/energy applications
- **Architects** who need to guarantee bandwidth, latency, fairness, and congestion-free operation
- **Anyone** designing or debugging systems where "fair sharing" and "predictable performance" are non-negotiable (exactly the requirements behind institutional recovery and patented AI optimization)

### Core Topics

**1. Internet Architecture & Design Philosophy**  
End-to-end argument, stateless core, "smart edges / dumb network" evolution, and the Tussle in Cyberspace (competing requirements and trust).

**2. Modern Network Programmability**  
Software-Defined Networking (SDN) principles, control-plane / data-plane separation, open interfaces, and network virtualization/slicing.

**3. Traffic Modeling & Characterization**  
On-off models (voice), hierarchical web traffic, burstiness, heavy-tailed (Pareto) vs exponential distributions and their impact on queues/loss.

**4. Queuing Theory & Performance Modeling**  
M/M/1 and M/M/m models, delay/utilization analysis, and extensions for multi-server systems.

**5. Scheduling & Fairness**  
Max-Min fairness & Water-filling algorithm, Generalized Processor Sharing (GPS), Weighted Fair Queuing (WFQ), and practical trade-offs.

**6. Rate Limiting & Traffic Shaping**  
Token bucket algorithm, policing vs shaping, burst control.

**7. Congestion Control**  
Binary feedback, Additive Increase Multiplicative Decrease (AIMD), stability, fairness, and efficiency lines.

### Folder Structure
- `/concepts/` — TBD distilled notes & diagrams (Water-filling, WFQ walkthroughs, etc.)
- `/code/`     — TBD
- `/readings/` — TBD

### Live Code Demos
- [Token Bucket Rate Limiter](Networking/token_bucket.py)  
- [Water-Filling Allocator](Networking/water_filling.py)  
- [Pareto Traffic Generator (Coming Soon)](Networking/pareto_traffic_gen.py)  
- [M/M/1 Queue Model (Coming Soon)](Networking/mm1_queue.py)  
- [Weighted Fair Queuing Simulator](Networking/wfq_simulator.py)