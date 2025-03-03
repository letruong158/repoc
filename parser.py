import csv
import sys

def parse_warnings(log_file, output_csv):
    with open(log_file, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Line", "File", "Message"])
        
        for line in infile:
            parts = line.strip().split(':', 2)
            if len(parts) == 3 and parts[0].isdigit():
                writer.writerow(parts)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 parser.py <logfile>")
        sys.exit(1)

    parse_warnings(sys.argv[1], "warnings.csv")