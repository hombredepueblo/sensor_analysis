import random

def simulate_sensor(n=100):
    values = []

    for _ in range(n):
        values.append(random.uniform(20, 30))

    return values


def main():

    data = simulate_sensor()

    print("Total:", len(data))
    print("Max:", max(data))
    print("Min:", min(data))


if __name__ == "__main__":
    main()