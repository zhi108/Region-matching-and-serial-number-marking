import cv2


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"点击坐标：({x}, {y})")


# 读取PNG图像
image = cv2.imread("output.png")
# 显示图像
cv2.imshow("Image", image)
# 设置鼠标回调函数
cv2.setMouseCallback("Image", click_event)
# 等待按键
cv2.waitKey(0)
# 关闭所有窗口
cv2.destroyAllWindows()
