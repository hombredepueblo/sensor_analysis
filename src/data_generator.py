import random
import pandas as pd

def generate_sensor_data(n=1000):

    data = []

    for i in range(n):

        value = random.uniform(20,30)

        data.append({
            "timestamp": i,
            "temperature": value
        })

    return pd.DataFrame(data)


if __name__ == "__main__":

    df = generate_sensor_data()

    df.to_csv("data/sensor_data.csv", index=False)

    print("Dataset created")
    