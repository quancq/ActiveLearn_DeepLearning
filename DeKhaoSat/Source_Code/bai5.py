'''
Cho một con xúc xắc có 6 mặt được đánh số từ 1 đến 6. Viết chương trình tính giá trị xấp xỉ của
xác xuất tổng của 5 lần tung liên tiếp bằng 17. Gợi ý: Bạn không cần tìm công thức chính xác để
tính xác xuất đấy, bạn có thể dùng phương pháp mô phỏng (simulation). Bạn có thể tìm hiểu về
định lý giới hạn trung tâm (Central limit theorem) và phân phối chuẩn (normal distribution).
'''

import numpy as np


def solve(num_faces_dice, num_roll_dice, sum):
    result = np.zeros(shape=(num_roll_dice, sum+1), dtype=np.float32)
    result[0, 1: num_faces_dice] = 1 / num_faces_dice
    for i in range(1, result.shape[0]):
        for s in range(1, result.shape[1]):
            # Calculate result[i, s]
            result[i, s] = np.sum(result[i-1, max(0, s-num_faces_dice): s]) / num_faces_dice

    print(result)
    return result[-1, -1]


if __name__ == "__main__":
    num_faces_dice = 6
    num_roll_dice = 5
    sum = 17

    prob = solve(num_faces_dice, num_roll_dice, sum)
    print("Prob sum of {} roll the dice equal {} : {}".format(num_roll_dice, sum, prob))
