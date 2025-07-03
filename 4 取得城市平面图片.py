import pyautogui
import time
import os
import pyscreenshot
import pandas as pd

'''
运行此程序前应使用鼠标坐标捕获工具确认各个坐标位置是否正确，并尽量保存并关闭其余无关程序
运行此程序前应确保此环境最小化后显示自定义地图
运行此程序前应将输入法调至英文
此程序运行中如无异常尽量避免操作鼠标或键盘
'''

if __name__ == '__main__':
    picture_type = 'a'  # 自定义地图中无建筑图像时设定为a，有建筑图像时设定为b

    df = pd.read_excel(f'3 城市poi聚类结果.xlsx')
    data = df[['name', 'location', 'class']].values

    pyautogui.moveTo(1810, 20)  # pycharm或其余环境最小化点击位置
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)

    for i in range(0, len(data)):
        pyautogui.moveTo(870, 130)  # 腾讯地图自定义样式中纬度输入框位置
        time.sleep(0.5)
        pyautogui.doubleClick()
        time.sleep(0.5)
        pyautogui.typewrite(data[i][1].split(',')[1])
        time.sleep(1)

        pyautogui.moveTo(1000, 130)  # 腾讯地图自定义样式中经度输入框位置
        time.sleep(0.5)
        pyautogui.doubleClick()
        time.sleep(0.5)
        pyautogui.typewrite(data[i][1].split(',')[0])
        time.sleep(3)

        image_demo = pyscreenshot.grab(bbox=(540, 160, 1380, 1000))  # 屏幕截取矩形范围

        if not os.path.exists(f"4 城市平面图片/{data[i][2]}"):
            os.makedirs(f"4 城市平面图片/{data[i][2]}", exist_ok=True)
        image_demo.save(f"4 城市平面图片/{data[i][2]}/{i}_{data[i][0]}_{picture_type}.png")
        time.sleep(2)

    pyautogui.moveTo(1800, 10)  # 网页最小化点击位置
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
