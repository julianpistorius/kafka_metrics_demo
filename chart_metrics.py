import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style


def animate(i):
    print('i:', i)
    graph_data = open('metrics.csv', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    timestamp_offset = 0
    previous_timestamp = None
    for index, line in enumerate(lines):
        if len(line) > 1:
            timestamp_str, cpu_pct = line.split(',')
            timestamp = int(timestamp_str)
            if previous_timestamp is None:
                timestamp_offset = 0
            else:
                timestamp_offset += timestamp - previous_timestamp
            xs.append(timestamp_offset)
            ys.append(cpu_pct)
            previous_timestamp = timestamp
    ax1.clear()
    ax1.plot(xs, ys)


if __name__ == '__main__':
    style.use('fivethirtyeight')

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
