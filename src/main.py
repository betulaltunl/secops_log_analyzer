from log_reader import read_log_file
from log_analyzer import analyze_failed_attempts, find_suspicious_ips
from report_writer import write_to_csv

log_file_path = "logs/log1.txt"
output_file = "reports/suspicious_ips_report.csv"
threshold = 5

log_lines = read_log_file(log_file_path)
failed_attempts = analyze_failed_attempts(log_lines)
suspicious_ips = find_suspicious_ips(failed_attempts, threshold)
write_to_csv(suspicious_ips, output_file)

print(f"Şüpheli IP adresleri {output_file} dosyasına yazıldı.")