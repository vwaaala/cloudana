# slashing_watchdog.py
# TODO: This task enforces SLAs by monitoring worker heartbeats and job timeouts.

import datetime

# TODO: scan_for_inactive_workers()
# - Query all workers with last_seen older than SLA threshold
# - For each: mark as inactive, log violation, optionally slash

# TODO: scan_for_expired_jobs()
# - Check jobs in PENDING or IN_PROGRESS state with timestamps beyond deadline
# - Call job_service.cancel_job(job_id)
# - Optionally log and trigger slashing

# TODO: periodic_loop()
# - Run both monitors in an interval loop
# - Track logs of which accounts were slashed and why
