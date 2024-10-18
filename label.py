from PIL import Image, ImageDraw, ImageFont


def draw_numbers(image_path, start_point, end_point, group_x_spacing, group_y_spacing, number_x_spacing, font_size):
    # 打开图片
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)

    # 起始点和终止点
    start_x, start_y = start_point
    end_x, end_y = end_point

    # 当前数字
    number = 0

    # 从右到左，从上到下绘制数字
    y = start_y
    while y <= end_y:
        x = start_x
        while x >= end_x:
            for i in range(3):
                draw.text((x - i * number_x_spacing, y), str(number), font=font, fill=(0, 0, 255))
                number += 1
            x -= group_x_spacing
        y += group_y_spacing

    # 保存标注后的图片
    image.save('output.png')


def main():
    draw_numbers('output.png', (2230, 278), (353, 3000), 147, 333, 48, 15)
