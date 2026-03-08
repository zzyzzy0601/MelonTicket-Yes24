import pyautogui
import time
from playsound import playsound  # 引入播放声音的模块
import keyboard  # 引入键盘监听模块

# 定义多个refresh按钮的位置，每个位置用一个元组 (x, y) 表示
refresh_positions = [
    #(1115, 320),
    #(1337, 323),
    (1193, 282),
    (1187, 309),
    (1193, 335),
    #(1257, 282),

]

# "Seat Selection Completed"按钮的坐标
complete_button_x = 1220  # 横坐标
complete_button_y = 1001  # 横坐标

# 启动vpn的坐标
vpn_button_x = 1466
vpn_button_y = 1562

# 设定刷新和点击的间隔时间（秒）
refresh_interval = 5.3
# 座位区的截图区域 (基于图片中的位置, 你可能需要调整这些值)
seat_area_x = 60  # 座位区的起始横坐标98
seat_area_y = 275  # 座位区的起始纵坐标
seat_area_width = 940  # 座位区的宽度810
seat_area_height = 580  # 座位区的高度500


# 定义灰色和白色范围，包括更广泛的浅色
def is_gray_or_white(r, g, b):
    # 检查米色
    #if 250 <= r <= 260 and 250 <= g <= 260 and 210 <= b <= 220:
        #return False
    # 粉色部分
    if 250 <= r <= 260 and 170 <= g <= 180 and 210 <= b <= 220:
        return False
    # 检查是否在 (200, 200, 200) 到 (255, 255, 255) 的范围内，或者是非常浅的其他颜色
    if 180 <= r <= 255 and 200 <= g <= 255 and 180 <= b <= 255:
        return True
    # 检查是否是浅棕色系（避免误判）
    if 170 <= r <= 240 and 150 <= g <= 210 and 150 <= b <= 255:
        return True

    return False


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

                        # 启动vpn按钮
                        pyautogui.moveTo(vpn_button_x, vpn_button_y)
                        pyautogui.click()
                        break

                if seat_found:
                    break

            if seat_found:
                print("座位选择已完成，退出脚本。")  # 调试信息
                # 播放完成音乐
                #playsound("D:\MONEY\money\BOOM.mp3")
                break

        if seat_found:
            break

except KeyboardInterrupt:
    print("程序被用户手动停止。")


                    #time.sleep(0.5)
                    #pyautogui.moveTo(276, 584)
                    #pyautogui.click()
                    #pyautogui.write('13966646002')