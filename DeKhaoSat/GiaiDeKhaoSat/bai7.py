'''
Nếu ngày hôm nay Nắng thì xác suất ngày hôm sau cũng Nắng là 0.3 và xác suất ngày hôm sau
Mưa là 0.7. Nếu ngày hôm nay Mưa thì xác suất ngày hôm sau Mưa là 0.4, xác suất ngày hôm
sau Nắng là 0.6.
Giả định xác suất Nắng một ngày nào đó là 0.5. Viết và công thức và chương trình tính xác suất
Nắng/Mưa ngày sau đó 1 tuần
'''

import numpy as np


def solve(sunny_sunny_prob, sunny_rain_prob, rain_sunny_prob, rain_rain_prob,
          sunny_curr_prob, num_days_after):
    rain_curr_prob = 1 - sunny_curr_prob
    for i in range(1, num_days_after + 1):
        sunny_next_prob = sunny_curr_prob * sunny_sunny_prob + rain_curr_prob * rain_sunny_prob
        rain_next_prob = sunny_curr_prob * sunny_rain_prob + rain_curr_prob * rain_rain_prob

        sunny_curr_prob = sunny_next_prob
        rain_curr_prob = rain_next_prob

        print("After {} days: Probability of sunny : {:.6f} - Probability of rain : {:.6f}"
          .format(i, sunny_curr_prob, rain_curr_prob))

    return sunny_next_prob, rain_next_prob


if __name__ == "__main__":
    sunny_sunny_prob = 0.3
    sunny_rain_prob = 0.7
    rain_sunny_prob = 0.6
    rain_rain_prob = 0.4

    sunny_curr_prob = 0.5
    num_days_after = 7

    sunny_future_prob, rain_future_prob = solve(
        sunny_sunny_prob,
        sunny_rain_prob,
        rain_sunny_prob,
        rain_rain_prob,
        sunny_curr_prob,
        num_days_after
    )

    print("\nAfter {} days: Probability of sunny : {} - Probability of rain : {}"
          .format(num_days_after, sunny_future_prob, rain_future_prob))
