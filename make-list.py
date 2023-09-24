import csv
import sys
import os
import time

def extract_last_value(input_string):

    values = input_string.split(":")

    return values[-1]

def count_total_lines(file_path):
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        return sum(1 for _ in file)

def process_file_real_time(input_file, output_file, total_lines):
    try:
        with open(input_file, 'r', encoding='ISO-8859-1') as input_file:
            with open(output_file, 'w') as output_file:
                lines_processed = 0
                start_time = time.time()
                for line in input_file:
                    last_value = extract_last_value(line.strip())
                    output_file.write(f"{last_value}\n")

                    lines_processed += 1
                    if lines_processed % 10345 == 0:
                        elapsed_time = time.time() - start_time
                        progress_percent = (lines_processed / total_lines) * 100
                        lines_per_second = lines_processed / elapsed_time
                        print(f"Processed: {lines_processed} lines ({progress_percent:.2f}%), "
                              f"Speed: {lines_per_second:.2f} lines/second", end='\r')
                        sys.stdout.flush()

                print("\nOHHHH HELLL YEAHH, IT'S DONE BABYYYY.")
    except FileNotFoundError:
        print(f"File not found: {input_file}")

script_directory = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) < 3:
    print("Usage: python script.py input_file output_file")
    sys.exit(1)

input_file = os.path.join(script_directory, sys.argv[1])
output_file = os.path.join(script_directory, sys.argv[2])

total_lines = count_total_lines(input_file)

process_file_real_time(input_file, output_file, total_lines)
