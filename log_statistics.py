import re
import matplotlib.pyplot as plt
import numpy as np


def analyze_log_file(filename):
    with open(filename, 'r') as f:
        log_text = f.read()

    duration_pattern = re.compile(r'duration = (\d{2}):(\d{2}):(\d{2}).(\d{6})')
    durations = []

    for match in duration_pattern.finditer(log_text):
        hours = int(match.group(1))
        minutes = int(match.group(2))
        seconds = int(match.group(3))
        microseconds = int(match.group(4))
        duration = hours * 3600 + minutes * 60 + seconds + microseconds * 1e-6
        durations.append(duration)

    num_durations = len(durations)
    mean_duration = np.mean(durations)
    median_duration = np.median(durations)
    min_duration = np.min(durations)
    max_duration = np.max(durations)

    print(f"Statistics for {filename}")
    print(f"Number of durations: {num_durations}")
    print(f"Mean duration: {mean_duration:.6f} seconds")
    print(f"Median duration: {median_duration:.6f} seconds")
    print(f"Minimum duration: {min_duration:.6f} seconds")
    print(f"Maximum duration: {max_duration:.6f} seconds")

    plt.hist(durations, bins=20)
    plt.xlabel('Duration (seconds)')
    plt.ylabel('Frequency')
    plt.title(f'Duration Distribution: {filename}')
    plt.show()


# filename1 = 'input/logs/001_piggy/003_Denison3D_piggy01_bulk03.txt'

filename1 = 'input/logs/001_piggy/001_Denison3D_piggy01_bulk01.txt'
analyze_log_file(filename1)

filename2 = 'input/logs/002_virtual_machine/gNavigator[PID=25116][DB=Denison3D][Project=004_enh][Flow=001_enh]_2023-05-17_11-18-14.0.log'
analyze_log_file(filename2)




