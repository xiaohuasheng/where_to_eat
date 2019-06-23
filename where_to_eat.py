# coding=utf-8

# 根据喜欢，就近原则选出要吃什么
import json
import math
import random
import operator

# 控制要不要打印出餐厅得分
is_debug = False


# is_debug = True


def get_best_select(current_location):
    # 获取最佳选择，如果有多个分数一样的，就随机选，只有一个，就返回这个
    max_score_list = get_max_score_list(current_location)
    can_select_number = len(max_score_list)
    if can_select_number > 1:
        return random.choice(max_score_list)
    else:
        return max_score_list[0]


def get_max_score_list(current_location):
    """
    根据目前所处位置，获取分数最大的几个地点
    :param current_location: 目前的位置
    :return:
    """
    foods_sort_by_score = calculate_score(current_location, get_data())
    several_select = []
    first_food_score = 0
    for food, score in foods_sort_by_score:
        if not several_select:
            several_select.append(food)
            first_food_score = score
        elif score >= first_food_score:
            several_select.append(food)
        else:
            break
    return several_select


def get_data():
    try:
        with open('foods.json', 'r', encoding='utf-8') as f:
            food_list = json.load(f)
            return food_list
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


def calculate_score(current_location, food_list):
    """
    根据距离和喜欢程度，给所有餐厅打分
    分数=喜欢*5 + 3*距离
    :param current_location:
    :param food_list:
    :return:
    """
    food_score_list = {}
    for food in food_list:
        name = food['name']
        location = food['location']
        favorite = food['favorite']
        # 计算距离
        distance = int(
            math.sqrt((current_location["x"] - location["x"]) ** 2 + (current_location["y"] - location["y"]) ** 2))
        # 计算分数
        score = favorite * 5 + distance * 3
        food_score_list[name] = score
    # 分数由大到小排序
    food_score_list = sorted(food_score_list.items(), key=operator.itemgetter(1), reverse=True)
    if is_debug:
        print(food_score_list)
    return food_score_list


if __name__ == '__main__':
    tips = "请告诉我你现在在哪里？1宿舍，2饭堂，3图书馆，4教学楼，都不是？请输入5\n"
    location_name = int(input(tips))
    if location_name == 1:
        location_x_y = {"x": 3, "y": 4}
    elif location_name == 2:
        location_x_y = {"x": 2, "y": 2}
    elif location_name == 3:
        location_x_y = {"x": 5, "y": 9}
    elif location_name == 4:
        location_x_y = {"x": 6, "y": 10}
    elif location_name == 5:
        location_str = input("你的坐标是多少？ 比如10,15\n")
        if not location_str:
            print("输入不正确\n")
            exit(0)
        location_x_y = location_str.split(',')
        location_x_y = {"x": int(location_x_y[0]), "y": int(location_x_y[1])}
    else:
        print("输入不正确\n")
        exit(0)

    best_select = get_best_select(location_x_y)
    if best_select:
        print("最好的选择是:" + best_select)
    else:
        print("对不起，没找到合适的")
