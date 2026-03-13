from data_generator import generate_sensor_data
from analysis import basic_statistics


def main():

    df = generate_sensor_data()

    stats = basic_statistics(df)

    print(stats)


if __name__ == "__main__":
    main()