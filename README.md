# SIEM-Attack-Dashboard-# DVWA Security Monitoring Dashboard

Real-time cybersecurity monitoring system using ELK Stack to detect and visualize web application attacks.

## 🎯 Project Overview

Built a comprehensive security monitoring solution that:
- Monitors vulnerable web applications in real-time
- Detects attack patterns and anomalies
- Visualizes security events through interactive dashboards
- Processes 1,000+ security events with <1ms latency

## 🛠️ Tech Stack

- **Docker** - Container orchestration
- **Elasticsearch** - Log storage and indexing
- **Filebeat** - Log shipping and processing
- **Kibana** - Data visualization and dashboards
- **DVWA** - Vulnerable web application (target)
- **Python** - Attack simulation scripts

## 📊 Dashboard Features

### Attack Timeline Analysis
- Real-time attack pattern detection
- 359 attack requests monitored
- Peak attack volume visualization

### Container Activity Monitoring
- Multi-system log aggregation
- 26% attack traffic identification
- Cross-container security visibility

### Threat Metrics
- Instant attack volume indicators
- Security operations center (SOC) ready
- Real-time alerting capabilities

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/[username]/DVWA-Security-Monitoring-Dashboard

# Start monitoring stack
docker-compose up -d

# Run attack simulation
python3 attack-scripts/Attack.py

# Access dashboard
open http://localhost:5601
