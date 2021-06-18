from helper import baringChart, plottingChart, pieingChart
import csv


def visualizingData(typeChart: str, titleChart: str, labelChart: list, dataChart: list) -> None:
    """
    control function over chart type and proper computation requires
    :return: not required

    """
    # initialization of figure
    figName = "fig/" + typeChart + " - " + titleChart + ".png"
    # decide type of chart
    if typeChart == "Bar":
        baringChart(figName, titleChart, labelChart, dataChart)
    if typeChart == "Pie":
        pieingChart(figName, titleChart, labelChart, dataChart)
    if typeChart == "Line":
        plottingChart(figName, titleChart, labelChart, dataChart)
    # prompt for execution
    print(figName)


def restoringNumber(listStringNumbers: list):
    """
    helper function restoring string val to float form
    :return: list of float val

    """
    return list(map(lambda val: float(val), listStringNumbers))


def entrance():
    """
    entrance load data summarized and generate graphs
    :return: not required

    """
    # load, read as list, var initialization
    fileSummarized = open("summarized.csv", newline="")
    listsElements = list(csv.reader(fileSummarized, delimiter=","))
    chartInstance, indexReading = [], 0
    # infinite loop pour data into list of chart instance, till reach document's end
    while True:
        # fetch curr content
        currElement = listsElements[indexReading]
        # validate if skip separation row
        if len(currElement) == 0:
            # reading forward to next row
            indexReading += 1
            continue
        # # unpack type, validate condition
        if len(currElement) == 1:
            [currChart] = currElement
            # if read reaches end, halt further creating
            if currChart == "end":
                break
            # fetch chart data for normal reading, pass to chart generation function
            [typeChart, titleChart] = currChart.split(": ")
            labelChart, dataChart = listsElements[indexReading + 1], listsElements[indexReading + 2]

            visualizingData(typeChart, titleChart, labelChart, restoringNumber(dataChart))

            # reading forward to next chart
            indexReading += 3

    # prompt for finish
    print("Finished Visualization, figures saved")





if __name__ == '__main__':
    entrance()
