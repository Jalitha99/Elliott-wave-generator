import random
import csv

def waveLength(x1, x2, y1, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def rule_0(point1, point2, point3, point4, point5, point6, point7, point8, point9):
    # general structure of elliott waves
    return (point1 < point2 and point2 > point3 and point3 < point4 and point4 > point5
            and point5 < point6 and point6 > point7 and point7 < point8 and point8 > point9 and point6 > point4)


def rule_1(point1, point3):
    # is_valid_wave2_retracement
    return point3 > point1


def rule_2(point1, point2, point3, point4, point5, point6):
    # is_wave3_shortest
    wave1_len = waveLength(1, 2, point1, point2)
    wave3_len = waveLength(3, 4, point3, point4)
    wave5_len = waveLength(5, 6, point5, point6)
    return wave3_len > wave1_len and wave3_len > wave5_len


def rule_3(point2, point5):
    # is_valid_wave4_price_territory
    return point5 > point2


def rule_4(point6, point7, point8):
    # waveB_shorter_than_waveA
    return (point6 - point7) > (point8 - point7)


def rule_5(point6, point7, point8):
    # waveB_is20percent
    return (point8 - point7) > ((point6 - point7) * 0.2)


def rule_6(point7, point8, point9):
    # waveC_longer_waveBPercent
    return (point8 - point9) > ((point8 - point7) * 0.9)


def rule_7(point7, point8, point9):
    # waveC less than 5 times waveB
    return (point8 - point9) < ((point8 - point7) * 5)


def checkRules(point1, point2, point3, point4, point5, point6, point7, point8, point9):
    return rule_0(point1, point2, point3, point4, point5, point6, point7, point8, point9) and (
        rule_1(point1, point3)
    ) and (
               rule_2(point1, point2, point3, point4, point5, point6)
           ) and (
               rule_3(point2, point5)
           ) and (
               rule_4(point6, point7, point8)
           ) and (
               rule_5(point6, point7, point8)
           ) and (
               rule_6(point7, point8, point9)
           ) and (
               rule_7(point7, point8, point9)
           )


elliott_waves = []
for i in range(0, 70000000):
    # Generate an array of 9 random elements
    random_array = [round(random.uniform(0, 10), 2) for _ in range(9)]
    point1, point2, point3, point4, point5, point6, point7, point8, point9 = random_array[0], random_array[1], random_array[2], random_array[3], random_array[4], random_array[5], random_array[6], random_array[7], random_array[8]
    if checkRules(point1, point2, point3, point4, point5, point6, point7, point8, point9):
        elliott_waves.append(random_array)
print(elliott_waves)
print("elliott waves generated :", len(elliott_waves))
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(elliott_waves)