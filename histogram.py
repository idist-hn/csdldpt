import numpy as np
import matplotlib.pyplot as plt
import cv2
image = cv2.imread('./venv/Images/img/1.jpg')
colors = ("red", "green", "blue")
channel_ids = (0, 1, 2)
plt.figure()
plt.xlim([0, 256])
for channel_id, c in zip(channel_ids, colors):
    histogram, bin_edges = np.histogram(
        image[:, :, channel_id], bins=256, range=(0, 256)
    )
    plt.plot(bin_edges[0:-1], histogram, color=c)
    print (histogram)
    # plt.xlim([-0.5, 255.5])

plt.title("Color Histogram")
plt.xlabel("Color value")
plt.ylabel("Pixel count")


plt.show()
