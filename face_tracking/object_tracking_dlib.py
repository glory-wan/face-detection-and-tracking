import cv2
import dlib


def show_info():
    pos1 = (10, 20)
    pos2 = (10, 40)
    pos3 = (10, 60)
    pos4 = (10, 80)
    info1 = "put left button, select an area, stract tracking"
    info2 = "'1': starting tracking, '2': stop tracking, 'Esc': exit "
    cv2.putText(frame, info1, pos1, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
    cv2.putText(frame, info2, pos2, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
    if tracking_state:
        cv2.putText(frame, "tracking now", pos3, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
    else:
        cv2.putText(frame, "no track", pos3, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    info4 = "press '' key to exit"
    cv2.putText(frame, info4, pos4, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))


points = []


def mouse_event_handler(event, x, y, flags, parms):
    global points  # 定义为全局变量
    if event == cv2.EVENT_LBUTTONDOWN:  # 鼠标左键按下
        points = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:  # 鼠标左键松开
        points.append((x, y))


capture = cv2.VideoCapture(0)

cv2.namedWindow("Object Tracking", cv2.WINDOW_NORMAL)  # 创建一个窗口， cv2.WINDOW_NORMAL 窗口大小可调整
cv2.resizeWindow("Object Tracking", 1280, 960)  # 调整窗口尺寸
cv2.setMouseCallback("Object Tracking", mouse_event_handler)

tracker = dlib.correlation_tracker()

tracking_state = False

while True:
    ret, frame = capture.read()
    show_info()

    if len(points) == 2:
        cv2.rectangle(frame, points[0], points[1], (0, 255, 0), 2)  # points[0]:(x, y) points[1]:(x, y)
        dlib_rect = dlib.rectangle(points[0][0], points[0][1], points[1][0], points[1][1])

    if tracking_state is True:
        tracker.update(frame)  # 更新画面
        pos = tracker.get_position()  # 获取位置的坐标
        cv2.rectangle(frame, (int(pos.left()), int(pos.top())), (int(pos.right()), int(pos.bottom())), (255, 0, 0), 3)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        if len(points) == 2:
            tracker.start_track(frame, dlib_rect)  # 把坐标信息传给tracker
            tracking_state = True
            points = []
    elif key == ord('2'):
        points = []
        tracking_state = False
    elif key == ord('\x1b'):
        break

    cv2.imshow("Object Tracking", frame)

capture.release()
cv2.destroyAllWindows()
