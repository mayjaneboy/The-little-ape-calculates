import os
import math
import sys
import keyboard
from PIL import ImageGrab
import pyautogui
import cv2
import pytesseract

flag = True
while flag:
    flag = False

    if keyboard.is_pressed('space'):
        print('游戏结束！')
        sys.exit()
    pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract\tesseract.exe'
    # 设定tesseract可执行文件的路径，让python能够找到它（是一个独立的软件）


    ImageGrab.grab(bbox=(100,270,160,330)).save('picture1.png')
    #捕获屏幕区域并保存
    ImageGrab.grab(bbox=(245, 280, 305, 320)).save('picture2.png')


    img1 = cv2.imread('picture1.png') # OpenCV 中用于读取图像文件的函数
    img2 = cv2.imread('picture2.png')
    # 将图片文件加载为一个多维数组（即 NumPy 数组）返回给img变量，
    # 每个元素代表图片中的一个像素点和对应的颜色值

    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) # OpenCV 中的颜色空间转换函数
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # 用于将图像从一种颜色空间转换到另一种颜色空间
    # 第二个参数为标志参数，告诉 OpenCV 函数如何转换颜色空间
    # cv2.COLOR_BGR2GRAY就是从 BGR 颜色空间转换为灰度图像，以来简化图像处理
    _, thresh1 = cv2.threshold(img1,150,100,cv2.THRESH_BINARY)
    _, thresh2 = cv2.threshold(img2, 150, 100, cv2.THRESH_BINARY)
    # OpenCV 中用于图像阈值化处理的函数。它将图像中的像素值与指定的阈值进行比较，
    # 依据设定的规则将像素值转换为新的值。常见的用法是将图像转化为二值图像：只有黑色和白色。
    # 但并不是严格的黑和白，而是根据阈值确定两个输出值
    # _ 表示忽略我们不关系的返回值（返回的是用于确定实际应用的阈值，通常和提供的阈值相同）
    # thresh 是二值化处理后的图像结果，包含了处理后的像素值（0 或 100）。
    # 它是一个 NumPy 数组，表示二值化后的图像。

    result1 = pytesseract.image_to_string(thresh1,config='--psm 6')
    result2 = pytesseract.image_to_string(thresh2, config='--psm 6')
    # 从二值化处理后的图像 thresh 中提取文本，并对结果进行处理
    # pytesseract 是 Tesseract OCR 的 Python 接口，用于在图像中进行文本识别
    # image_to_string() 函数用于从输入的图像中提取文本，返回识别到的字符串。
    # split('?') 用于将提取到的文本按 ? 字符进行分割，生成一个列表，返回给result
    # 如“12?34”，split('?') 会将它们分割成 ['12', '34']。

    try:
        result1 = result1.strip()
        result2 = result2.strip()
        # 移除字符串开头和结尾的空白字符（包括空格、换行符、制表符等）
        # 如果传递了参数，则还会移除指定的字符。
        # 返回的仍然是字符串

        num1 = math.floor(float(result1))
        num2 = math.floor(float(result2))
        # 将字符串转换成浮点型数据，并向下取整

        if num1 > num2:
            pyautogui.moveTo(100, 600, duration=0.5)
            # pyautogui 库中的一个函数
            # 将光标移动到指定的屏幕坐标 (100, 600)，并在给定的时间内(单位是s)完成移动。
            # 绝对移动，给出的坐标是相对整个屏幕的
            pyautogui.mouseDown()  # pyautogui 库中的一个函数
            # 模拟按下鼠标按钮的操作(默认是左键，可以加参数确定是哪个按键)
            # 而不会立即松开,直到调用 pyautogui.mouseUp() 函数
            pyautogui.move(170, 70, duration=1)
            pyautogui.move(-170, 70, duration=1)
            # move为相对移动，给出的坐标是相对于光标当前坐标的

            print(f'{num1} > {num2}')
            flag = True
        else:
            pyautogui.moveTo(300, 600, duration=0.5)
            pyautogui.mouseDown()
            pyautogui.move(-200, 70, duration=1)
            pyautogui.move(200, 70, duration=1)

            print(f'{num1} < {num2}')
            flag = True
        pyautogui.mouseUp()
    except (IndexError,ValueError) as e:
        flag = True
        print('未捕获到内容!')



