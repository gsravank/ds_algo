import matplotlib.pyplot as plt


def plot_point_ax(ax, x, y, marker='o', color='b'):
    _ = ax.plot([x], [y], marker=marker, color=color)
    return


def plot_line_ax(ax, x1, y1, x2, y2, color='b'):
    _ = ax.plot([x1, x2], [y1, y2], color=color)
    return


def plot_text_ax(ax, x, y, text):
    _ = ax.text(x, y, text)
    return
