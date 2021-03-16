# list manipulation
# pseudocodes included in comments

# import required modules
import numpy as np
import matplotlib.pyplot as plt
# create 2 lists
gene_lengths = [9410,394141,4442,105338,19149,76779,
              126550,36296,842,15981]
exon_counts = [51,1142,42,216,25,650,32533,57,1,523]
# convert lists into arrays
lengths_array = np.array(gene_lengths)
counts_array = np.array(exon_counts)
# calculate average length, store in an array, sort at the same time
sorted_average_length_array = sorted(lengths_array/counts_array)
# convert result into list and print
print(list(sorted_average_length_array))
# draw the pie chart
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1)
plt.pie(sorted_average_length_array, shadow=True, explode=explode)
plt.title("Average Exon Lengths")
plt.show()

