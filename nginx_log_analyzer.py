import os
import re
from collections import Counter
from datetime import datetime

# Use relative path for log file
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "access.log")
REPORT_FILE = f"nginx_report_{datetime.now().strftime('%Y-%m-%d')}.txt"

# Create logs directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Check if the access log exists
if not os.path.exists(LOG_FILE):
    print(f"❌ Log file not found: {LOG_FILE}")
    exit(1)

try:
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except Exception as e:
    print(f"⚠️ Failed to read log file: {e}")
    exit(1)

# Data containers
ips = []
paths = []
codes = []
agents = []

# Extract data from log lines
for line in lines:
    parts = line.split()
    if len(parts) < 12:
        continue

    ips.append(parts[0])
    paths.append(parts[6])
    codes.append(parts[8])

    # Extract User-Agent from the last quoted string
    user_agent = re.findall(r'"([^"]*)"$', line)
    if user_agent:
        agents.append(user_agent[0])

# Helper to write top 5 counts
def write_top(title, items, file_obj):
    file_obj.write(f"\n{title}\n")
    for item, count in Counter(items).most_common(5):
        file_obj.write(f"{item}: {count}\n")

# Write report
with open(REPORT_FILE, "w", encoding='utf-8') as f:
    f.write("📝 NGINX Log Analysis Report\n")
    write_top("📌 Top 5 IP Addresses", ips, f)
    write_top("📌 Top 5 Requested Paths", paths, f)
    write_top("📌 Top 5 Response Codes", codes, f)
    write_top("📌 Top 5 User Agents", agents, f)

print(f"\n✅ Report saved to: {REPORT_FILE}")
