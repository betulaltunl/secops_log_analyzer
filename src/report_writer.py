import csv

def write_to_csv(suspicious_ips, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['suspicious_ip']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for ip in suspicious_ips:
            writer.writerow({'suspicious_ip': ip})