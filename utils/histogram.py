import numpy as np
import matplotlib.pyplot as plt
import cv2

def histogramProcess(resource_file, destination_file):
    image = cv2.imread(resource_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    histogramVector = open(f"./{destination_file}_vector.txt", "w")
    # Define parameters
    vector = []

    colors = ("red", "green", "blue")
    channel_ids = (0, 1, 2)
    plt.figure()
    plt.xlim([0, 255])
    for channel_id, c in zip(channel_ids, colors):
        histogram, bin_edges = np.histogram(
            image[:, :, channel_id], bins=255, range=(0, 255)
        )
        plt.plot(bin_edges[0: -1], histogram, color=c)
        plt.xlim([0, 255])
        for i in range(0, len(histogram), 1):
            vector.append(histogram[i])

    histogramVector.write(f"{vector}\n")
    plt.savefig(destination_file)
    plt.close()
    histogramVector.close()
