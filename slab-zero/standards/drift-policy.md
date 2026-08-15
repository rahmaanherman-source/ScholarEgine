# Drift Policy

Drift is evaluated against the dependency set recorded at verification time. Code, dependency locks, external API/schema state, verification policy/standards, and evidence artifacts may each be monitored. A drift event changes only affected VERIFIED/CURRENT items to STALE. Historical evidence is never deleted. An unscoped or unsupported probe fails closed rather than claiming CURRENT.
