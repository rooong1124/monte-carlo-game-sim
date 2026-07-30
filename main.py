import numpy as np

# 模擬一局
def simulate_game(threshold):
    arr_size = 64
    box = np.zeros(arr_size, dtype=int)
    rand_cnt = 0
    spec_cnt = 0

    while np.count_nonzero(box) < arr_size:
        if np.count_nonzero(box) < threshold:
            random_indices = np.random.choice(arr_size, size=5)
            box[random_indices] = 1
            print(np.count_nonzero(box))
            rand_cnt = rand_cnt + 1

        else:
            true_indices = np.flatnonzero(box == 0)
            if true_indices.size > 0:
                box[true_indices[0]] = 1
                print(np.count_nonzero(box))
                spec_cnt = spec_cnt + 1

    print(f"隨機開啟五個箱子次數： {rand_cnt} 次")
    print(f"指定開啟某個箱子次數: {spec_cnt} 次")

# rnage:0~63
simulate_game(56)
