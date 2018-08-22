
import matplotlib.pyplot as plt


def histogram(data, title=None, xlabel=None, ylabel=None):
    """Caller should do: plt.show() """
    plt.hist(data)
    if title: plt.title(title)
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)

    return plt


def histogram_from_dict(data, title=None, xlabel=None, ylabel=None):
    """Caller should do: plt.show() """
    plt.bar(data.keys(), data.values())
    if title: plt.title(title)
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)

    return plt

