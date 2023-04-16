import cv2
import numpy as np

video_path = 'object_tracking/asset/video.mp4'
cap = cv2.VideoCapture(video_path)

output_size = (187, 333) # (width, height)

# initialize writing video
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('%s_output.mp4' % (video_path.split('.')[0]), fourcc,
                    cap.get(cv2.CAP_PROP_FPS), output_size)

if not cap.isOpened():
    exit()

tracker = cv2.TrackerCSRT_create() # csrt object tracker 초기화

# ROI : region of interest
ret, img = cap.read() # 첫 번째 프레임 read

cv2.namedWindow('Select Window')
cv2.imshow('Select Window', img)

# setting ROI
rect = cv2.selectROI('Select Window', img, fromCenter=False, showCrosshair=True)
cv2.destroyWindow('Select Window')

# initialize tracker
tracker.init(img, rect) # tracker가 img와 rect를 tracking하도록 setting

while True:
    ret, img = cap.read()
    
    if not ret:
        exit()
    
    success, box = tracker.update(img) # img에서 rect로 설정한 image와 비슷한 object의 position을 반환
    
    left, top, width, height = [int(v) for v in box]
    
    # 중심점 구하기
    center_x = left + width / 2
    center_y = top + height / 2
    
    result_top = int(center_y - output_size[1] / 2)
    result_bottom = int(center_y + output_size[1] / 2)
    result_left = int(center_x - output_size[0] / 2)
    result_right = int(center_x + output_size[0] / 2)
    
    result_img = img[result_top:result_bottom, result_left:result_right].copy()
    
    out.write(result_img)
    
    cv2.rectangle(img, pt1=(left, top), pt2=(left + width, top + height), 
                color=(255, 255, 255), thickness=3)
    
    cv2.imshow('result_img', result_img)
    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break