import re

def analyze_failed_attempts(log_lines):
    failed_attempts = {}
    for line in log_lines:
        if "Failed password" in line:
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
            if ip[0] in failed_attempts:
                failed_attempts[ip[0]] += 1
            else:
                failed_attempts[ip[0]] = 1
    return failed_attempts

def find_suspicious_ips(failed_attempts, threshold):
    suspicious_ips = []
    for ip, count in failed_attempts.items():
        if count > threshold:
            suspicious_ips.append(ip)
    return suspicious_ips