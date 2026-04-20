import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

def selection_sort(values):
    for min_index in range(len(values)):
        min_value = values[min_index]
        min_ind = min_index
        for i in range(min_index, len(values)):
            if values[i] < min_value:
                min_ind = i
                min_value = values[i]
        values[min_ind], values[min_index] = values[min_index], values[min_ind]
    return values

def bubble_sort(values):
    plt.ion()
    plt.show()
    for i in range(len(values)):
        for j in range((len(values)) - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

    plt.ioff()
    plt.show()
    print(values)




if __name__ == "__main__":
    values = random_numbers(5)# 10 čísel v rozsahu 0–100
    print(values) # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    selc = selection_sort(values)
    values = random_numbers(20)
    print(values)
    bub = bubble_sort(values)
    print(selc)
    print(bub)

