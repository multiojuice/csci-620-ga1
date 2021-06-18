import matplotlib.pyplot as plt


def labelingPartitions(allNumber) -> object:
    def formattingVal(pct):
        val = int(round(pct * allNumber / 100))
        return "{v:d}\n{p:.2f}%".format(p=pct, v=val)
    return formattingVal


def plottingChart(figName: str, titleChart: str, labelChart: list, dataChart: list) -> None:
    """
    helper function create pie chart
    :return: not required

    """
    # create chart with label
    figInstance = plt.figure(dpi=2160)
    plt.plot(labelChart, dataChart, "ro-", color="xkcd:sky blue", label="Trends over periods")
    plt.legend(loc="upper left")
    plt.xlabel("Periods (Age)")
    plt.ylabel("Quantity")
    plt.title(titleChart)
    # create plot with data
    for label, data in zip(labelChart, dataChart):
        plt.text(label, data, "%.0f" % data, ha="center", va="bottom", fontsize=5)
    # save fig, clear memory usage
    figInstance.savefig(figName)
    plt.close(figInstance)


def baringChart(figName: str, titleChart: str, labelChart: list, dataChart: list) -> None:
    """
    helper function create bar chart
    :return: not required

    """
    # create chart with label
    figInstance = plt.figure(dpi=2160)
    plt.bar(labelChart, dataChart, color="xkcd:sky blue", width=0.3)
    plt.title(titleChart)
    plt.xlabel("Groups")
    plt.ylabel("Quantity")
    # create bar with data
    for index, val in enumerate(dataChart):
        plt.text(index, val, str(val))
    # save fig, clear memory usage
    figInstance.savefig(figName)
    plt.close(figInstance)


def pieingChart(figName: str, titleChart: str, labelChart: list, dataChart: list) -> None:
    """
    helper function create pie chart
    :return: not required

    """
    # create chart with label
    figInstance = plt.figure(dpi=2160)
    allNumber = sum(dataChart)
    plt.pie(x=dataChart, labels=labelChart, autopct=labelingPartitions(allNumber), textprops={"fontsize": 5}, pctdistance=0.9, labeldistance=1.08, radius=1.2)
    plt.title(titleChart)
    # save fig, clear memory usage
    figInstance.savefig(figName)
    plt.close(figInstance)
