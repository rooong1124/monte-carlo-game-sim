import numpy as np
import matplotlib.pyplot as plt

# 模擬一局
def simulate_game(threshold):
    box_num = 64
    boxes = np.zeros(box_num, dtype=int)
    rand_cnt = 0
    spec_cnt = 0

    while np.count_nonzero(boxes) < box_num:
        # 隨機方式
        if np.count_nonzero(boxes) < threshold:
            random_indices = np.random.choice(box_num, size=5)
            boxes[random_indices] = 1
            rand_cnt = rand_cnt + 1

        # 指定方式
        else:
            unopen_indices = np.flatnonzero(boxes == 0)
            boxes[unopen_indices[0]] = 1
            spec_cnt = spec_cnt + 1

        # print(f"已開啟 {np.count_nonzero(boxes)} 個")

    print(f"隨機開啟五個箱子次數： {rand_cnt} 次")
    print(f"指定開啟某個箱子次數： {spec_cnt} 次")

    return rand_cnt * 25 + spec_cnt * 40



# 重複執行數次
def many_times(threshold, times=5000):
    costs = []
    for _ in range(times):
        costs.append(simulate_game(threshold))

    return costs



# 所有閾值的情況
def all_thresholds(times=5000):
    all_costs = []
    for i in range(65):
        all_costs.append(many_times(i, times))

    return all_costs
        


c = all_thresholds(1000)

for x, y in enumerate(c):
    plt.scatter([x] * len(y), y, s=2, alpha=0.15)
    
plt.xlabel("Threshold")
plt.ylabel("Cost")
plt.savefig('a.png', dpi=300)
plt.show()