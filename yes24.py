import pyautogui
import time
from playsound import playsound  # 引入播放声音的模块
import keyboard  # 引入键盘监听模块

# 定义多个refresh按钮的位置，每个位置用一个元组 (x, y) 表示
refresh_positions = [
    (1205,309),
    (1355,309),
    (1355,309),
]

# "Seat Selection Completed"按钮的坐标
complete_button_x = 1271  # 横坐标
complete_button_y = 1010  # 纵坐标

# 设定刷新和点击的间隔时间（秒）
refresh_interval = 1.2
# 座位区的截图区域
seat_area_x = 10  # 座位区的起始横坐标
seat_area_y = 152  # 座位区的起始纵坐标

seat_area_width = 1074  # 座位区的宽度
seat_area_height = 895  # 座位区的高度


# 定义灰色和白色范围，包括更广泛的浅色
def is_gray_or_white(r, g, b):
    if r==0 and g==204 and b==204:
        return False

    return True


try:
    while True:
        seat_found = False

        if keyboard.is_pressed('space'):
            print("检测到空格键，程序终止...")
            break

        # 循环点击refresh按钮的位置
        for pos in refresh_positions:
            print(f"点击刷新按钮位置: {pos}...")  # 调试信息
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
            time.sleep(refresh_interval)

            print("检测座位...")  # 调试信息

            # 截取座位选择区域的截图，用于检测可用座位的颜色
            screenshot = pyautogui.screenshot(region=(seat_area_x, seat_area_y, seat_area_width, seat_area_height))

            # 检测是否有彩色（非灰色、非白色）的方块
            for x in range(screenshot.width):
                for y in range(screenshot.height):
                    r, g, b = screenshot.getpixel((x, y))
                    if not is_gray_or_white(r, g, b):
                        print(f"找到彩色座位在位置: ({x}, {y}), RGB: ({r}, {g}, {b})")  # 调试信息
                        pyautogui.click(x + seat_area_x + 5, y + seat_area_y + 5)  # 点击对应位置
                        time.sleep(0.2)

                        # 点击"Seat Selection Completed"按钮
                        pyautogui.moveTo(complete_button_x, complete_button_y)
                        pyautogui.click()
                        seat_found = True

                        time.sleep(0.5)
                        pyautogui.moveTo(1350, 977)
                        pyautogui.click()

                        time.sleep(0.5)
                        pyautogui.moveTo(276, 584)
                        pyautogui.click()
                        pyautogui.write('19133232735')
                        pyautogui.moveTo(1350, 977)
                        pyautogui.click()

                        time.sleep(0.5)
                        pyautogui.moveTo(56, 990)
                        pyautogui.click()
                        time.sleep(0.2)
                        pyautogui.moveTo(636, 990)
                        pyautogui.click()
                        pyautogui.moveTo(381, 383)
                        pyautogui.click()
                        break
                        break

                if seat_found:
                    break

            if seat_found:
                print("座位选择已完成，退出脚本。")  # 调试信息
                break

        if seat_found:
            break

except KeyboardInterrupt:
    print("程序被用户手动停止。")
