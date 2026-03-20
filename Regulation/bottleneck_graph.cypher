// 1. Structural Setup: Identifying the Institutional "Snares"
// We add 'Processing_Power' to departments to simulate throughput
MATCH (n) DETACH DELETE n;

CREATE (p:Process {name: "Sovereign Capital Deployment", target_roi: 0.24})
CREATE (d1:Department {name: "Operations", risk_weight: 0.10, capacity: 100})
CREATE (d2:Department {name: "Legal_Compliance", risk_weight: 0.40, capacity: 30})
CREATE (d3:Department {name: "Finance_Treasury", risk_weight: 0.15, capacity: 80})
CREATE (d4:Department {name: "Regional_Admin", risk_weight: 0.65, capacity: 15}) // Critical Bottleneck

// 2. The Dependency Chain with "Cost of Delay" (CoD)
CREATE (p)-[:INITIATED_BY]->(d1)
CREATE (d1)-[:REQUIRES_APPROVAL {lag_days: 5, value_at_risk: 50000}]->(d2)
CREATE (d2)-[:REQUIRES_APPROVAL {lag_days: 14, value_at_risk: 250000}]->(d4)
CREATE (d4)-[:REQUIRES_APPROVAL {lag_days: 4, value_at_risk: 40000}]->(d3)
CREATE (d3)-[:FINALIZES]->(p)

// 3. RE-WRITE: The "Forensic Leakage" Query
// This query calculates the cumulative 'Value at Risk' across the entire chain
MATCH path = (start:Department)-[:REQUIRES_APPROVAL*]->(end:Department)
WHERE end.name = "Finance_Treasury"
UNWIND relationships(path) AS rel
WITH path, sum(rel.value_at_risk) AS total_leakage, sum(rel.lag_days) AS total_days
RETURN nodes(path) AS Chain, total_days, total_leakage
ORDER BY total_leakage DESC;

// 4. THE KILL-SWITCH TRIGGER (Logic only)
// If total_days > 20, we flag the asset for 'Structural Defense' intervention
MATCH (p:Process)
WHERE p.name = "Sovereign Capital Deployment"
WITH p
MATCH (d:Department {name: "Regional_Admin"})-[r:REQUIRES_APPROVAL]->()
WHERE r.lag_days > 10
SET p.status = "INTERVENTION_REQUIRED", p.alert = "Fiduciary Integrity Breach at Regional level";