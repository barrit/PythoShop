import csv
import matplotlib.pyplot as plt


def plot(name):
    csv_path = name + '.csv'

    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row

        r_values = []
        g_values = []
        b_values = []
        for row in reader:
            x, y, r, g, b = map(int, row)
            r_values.append(r)
            g_values.append(g)
            b_values.append(b)

    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(8, 8))

    ax1.hist(r_values, bins=256, range=(0, 255), color='red')
    ax1.set_ylabel('R Value')

    ax2.hist(g_values, bins=256, range=(0, 255), color='green')
    ax2.set_ylabel('G Value')

    ax3.hist(b_values, bins=256, range=(0, 255), color='blue')
    ax3.set_ylabel('B Value')

    plt.xlabel('Pixel Value')
    plt.show()