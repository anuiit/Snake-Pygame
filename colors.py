snakeGradient_color = [
(21, 101, 192),
(31, 97, 181),
(42, 93, 171),
(53, 89, 161),
(64, 85, 151),
(75, 81, 141),
(86, 77, 130),
(97, 73, 120),
(108, 70, 110),
(119, 66, 100),
(130, 62, 90),
(141, 58, 79),
(152, 54, 69),
(163, 50, 59),
(174, 46, 49),
(185, 43, 39)]

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb
