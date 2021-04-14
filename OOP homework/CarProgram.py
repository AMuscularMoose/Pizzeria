import CarClass as c


def main():
    year_model = input("What is the year model of the car?")
    make = input("What is the make of the car?")

    car_accel = c.Car(year_model, make)

    for count in range(5):
        print(
            "The current speed of the vehicle now is ",
            car_accel.get_speed(),
            " and will now accelerate.",
        )
        car_accel.accelerate()
    for count in range(5):
        print(
            "The current speed of the vehicle now is ",
            car_accel.get_speed(),
            " and will now brake.",
        )
        car_accel.brake()


main()