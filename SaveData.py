import csv
import numpy as np
import os


def WriteSignal2CSV(times, signals, output_dir, output_file='output_2.csv'):
    output_path = os.path.join(output_dir, output_file)
    signal_data = []
    for i in range(len(times)):
        signal_data.append(times[i])
        signal_data.append(signals[i])

    with open(output_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(signal_data)

