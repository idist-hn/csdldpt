import numpy as np
import cv2
import matplotlib.pyplot as p
import os

# Định nghĩa lớp Point để nhận tọa độ các điểm ảnh
# Các điểm này, sau này để chọn các điểm "hạt giống"

class Point:
    def __init__(self,x,y):
      self.x = x
      self.y = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y

# xác định giá trị mức xám khác nhau của điểm ảnh
def getGrayDiff(img,currentPoint,tmpPoint):
    return abs(int(img[currentPoint.x,currentPoint.y]) - int(img[tmpPoint.x,tmpPoint.y]))

# Định nghĩa các 8 điểm lân cận để xem xét nở vùng (kết nối)
def selectConnects():
    connects = [Point(-1, -1), Point(0, -1), Point(1, -1), Point(1, 0), Point(1, 1), Point(0, 1), Point(-1, 1), Point(-1, 0)]
    return connects

# Định nghĩa hàm regionGrow để thực hiện nở vùng
def regionGrow(img,seeds,thresh): # img: ảnh; seeds: danh sách điểm hạt giống; thresh: ngưỡng
    m, n = img.shape
    seedMark = np.zeros([m, n]) # Tạo mảng để đánh dấu các điểm hạt gống,
                                 # Tức là, mảng này chứa ảnh ảnh và có các điểm hạt giống
    seedList = [] # Tạo danh sách chứa điểm hạt giống
    for seed in seeds:
        seedList.append(seed)      # Thêm các điểm hạt giống vào danh sách chứa điểm hạt giống
    label = 1                     # khởi tạo nhãn có giá trị = 1
    connects = selectConnects()   # Tạo các kết nối với 8 điểm lân cận
    while(len(seedList)>0): # Lặp qua danh sách chứa điểm hạt giống seedList
          # lấy điểm hạt giống đầu tiên trong danh sách chứa điểm hạt giống
          currentPoint = seedList.pop(0)
          # đánh dấu (gán nhãn) cho điểm hạt giống
          seedMark[currentPoint.x,currentPoint.y] = label
          for i in range(8):    # xem xét (lặp qua) 8 điểm lân cận
               tmpX = currentPoint.x + connects[i].x
               tmpY = currentPoint.y + connects[i].y
               if tmpX < 0 or tmpY < 0 or tmpX >= m or tmpY >= n:
                    continue
               # Tính sự sai khác nhau giá trị mức xám của điểm ảnh hiện tại
               # với từng điểm (8 điểm) lân cận nó
               grayDiff = getGrayDiff(img,currentPoint,Point(tmpX,tmpY))
               # Nếu nhỏ hơn ngưỡng và trong vùng ảnh gốc
               if grayDiff < thresh and seedMark[tmpX,tmpY] == 0:
                    # Đánh dấu điểm đó thành điểm hạt giống và gán nhãn
                    seedMark[tmpX,tmpY] = label
                    # Thêm điểm được đánh dấu vào danh sách điểm hạt giống
                    seedList.append(Point(tmpX,tmpY))
     # Trả về ảnh có chứa các điểm hạt giống (được gán nhãn) là ảnh phân đoạn
    return seedMark

def regionGrowing(path, savePath):
        # Đọc ảnh
        imgName = os.path.basename(path)
        img = cv2.imread(path,0)
        # imgName = imgName.split('.')[0]
        # dir = f'./{imgName}'
        # isExist = os.path.exists(dir)
        # if not isExist:
        #     os.makedirs(dir)
        #     print("The new directory is created!")
        # os.chdir(dir)

        # img = cv2.imread(str(i) + '.jpg',0)
        # Chọn 3 điểm làm điểm hạt gống. Có thể chọn số điểm cho ảnh khác
        seeds = [Point(10, 10), Point(300, 400), Point(100, 300)]
        # Thực hiện tăng vùng bằng cách gọi hàm regionGrow
        img_result = regionGrow(img, seeds, 5)  #5: là giá trị ngưỡng, gía trị này thay đổi phụ thuộc ảnh ta quy định
        cv2.imwrite(savePath, img_result)
        # cv2.imwrite(os.path.join(dir, f'{imgName}_reasonGrow.jpg'), img_result)