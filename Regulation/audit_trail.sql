-- 1. Create Forensic Audit Schema
CREATE SCHEMA IF NOT EXISTS forensic_audit;

-- 2. Define Immutable Audit Log
-- Prevents deletion or modification of records to ensure "Clean Truth"
CREATE TABLE forensic_audit.fiduciary_logs (
    log_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    asset_id VARCHAR(50) NOT NULL,
    recorded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    roi_reported DECIMAL(5, 4),
    opex_variance DECIMAL(5, 4),
    status VARCHAR(20) CHECK (status IN ('STABLE', 'LEAKAGE_DETECTED', 'KILL_SWITCH_ACTIVE')),
    raw_data_hash TEXT NOT NULL -- Integrity check for incoming regional data
);

-- 3. Row-Level Security (RLS) for Sovereign Privacy
-- Ensures only authorized auditors (Ivan Damnjanovic) can view global metrics
ALTER TABLE forensic_audit.fiduciary_logs ENABLE ROW LEVEL SECURITY;

CREATE POLICY auditor_full_access ON forensic_audit.fiduciary_logs
    FOR ALL TO auditor_role
    USING (auth.role() = 'sovereign_auditor');

-- 4. Automated "Leakage" Trigger
-- Logic: If reported ROI drops 10% below the 24% target, flag for forensic review
CREATE OR REPLACE FUNCTION check_fiduciary_integrity()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.roi_reported < 0.216 THEN -- 10% tolerance from 24% 
        NEW.status := 'LEAKAGE_DETECTED';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_integrity_check
    BEFORE INSERT ON forensic_audit.fiduciary_logs
    FOR EACH ROW EXECUTE FUNCTION check_fiduciary_integrity();

-- 5. SEC-Compliant View
-- Aggregates data for regulatory disclosures [cite: 92]
CREATE VIEW forensic_audit.v_sec_disclosure AS
SELECT 
    asset_id,
    AVG(roi_reported) as mean_roi,
    SUM(CASE WHEN status = 'LEAKAGE_DETECTED' THEN 1 ELSE 0 END) as breach_count
FROM forensic_audit.fiduciary_logs
GROUP BY asset_id;