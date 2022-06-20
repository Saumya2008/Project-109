from cv2 import findCirclesGrid
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_dev = statistics.stdev(data)

first_std_dev_start, first_std_dev_end = mean-std_dev, mean+std_dev
second_std_dev_start, second_std_dev_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_dev_start, third_std_dev_end = mean-(3*std_dev), mean+(3*std_dev)

fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[
              0, 0.17], mode="lines", name="Standard deviation 1"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[
              0, 0.17], mode="lines", name="Standard deviation 1"))
fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[
              0, 0.17], mode="lines", name="Standard deviation 2"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[
              0, 0.17], mode="lines", name="Standard deviation 2"))
fig.show()

# making list of data within all standard deviations and printing the result.
list_of_data_within_1_std_dev = [
    result for result in data if result > first_std_dev_start and result < first_std_dev_end]
list_of_data_within_2_std_dev = [
    result for result in data if result > second_std_dev_start and result < second_std_dev_end]
list_of_data_within_3_std_dev = [
    result for result in data if result > third_std_dev_start and result < third_std_dev_end]

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_dev))
print("{}% of data lies within 1 standard deviation".format(
    len(list_of_data_within_1_std_dev)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(
    len(list_of_data_within_2_std_dev)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(
    len(list_of_data_within_3_std_dev)*100.0/len(data)))
