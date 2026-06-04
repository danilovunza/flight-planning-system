"""
Flight Planning System

Author: Danilo Vunza
Course: COSC 2436

Description:
Flight planning system demonstrating
aviation operations and OOP concepts.
"""


class Aircraft:

    def __init__(
        self,
        registration,
        model,
        max_takeoff_weight,
        fuel_capacity
    ):

        self.registration = registration
        self.model = model
        self.max_takeoff_weight = max_takeoff_weight
        self.fuel_capacity = fuel_capacity


class Airport:

    def __init__(
        self,
        icao,
        name,
        city
    ):

        self.icao = icao
        self.name = name
        self.city = city


class Flight:

    def __init__(
        self,
        flight_number,
        origin,
        destination,
        distance
    ):

        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.distance = distance


class FuelPlanner:

    def calculate_fuel(
        self,
        distance
    ):

        trip_fuel = distance * 2.5

        reserve_fuel = 1500

        contingency_fuel = (
            trip_fuel * 0.05
        )

        total_fuel = (
            trip_fuel +
            reserve_fuel +
            contingency_fuel
        )

        return {
            "trip_fuel": trip_fuel,
            "reserve_fuel": reserve_fuel,
            "contingency_fuel": contingency_fuel,
            "total_fuel": total_fuel
        }


class WeightBalance:

    def calculate_takeoff_weight(
        self,
        passengers,
        baggage,
        fuel
    ):

        passenger_weight = (
            passengers * 190
        )

        total_weight = (
            passenger_weight +
            baggage +
            fuel
        )

        return total_weight


class Weather:

    def __init__(
        self,
        temperature,
        wind_speed,
        visibility
    ):

        self.temperature = temperature
        self.wind_speed = wind_speed
        self.visibility = visibility


def main():

    aircraft = Aircraft(
        "N123AA",
        "Boeing 737-800",
        174200,
        46000
    )

    origin = Airport(
        "KIAH",
        "George Bush Intercontinental",
        "Houston"
    )

    destination = Airport(
        "KORD",
        "O'Hare International",
        "Chicago"
    )

    flight = Flight(
        "AA101",
        origin,
        destination,
        925
    )

    fuel_planner = FuelPlanner()

    fuel = fuel_planner.calculate_fuel(
        flight.distance
    )

    weight_system = WeightBalance()

    takeoff_weight = (
        weight_system.calculate_takeoff_weight(
            passengers=120,
            baggage=4000,
            fuel=fuel["total_fuel"]
        )
    )

    weather = Weather(
        temperature=28,
        wind_speed=12,
        visibility=10
    )

    print("=" * 60)

    print("FLIGHT PLANNING SYSTEM")

    print("=" * 60)

    print(f"Flight: {flight.flight_number}")

    print(
        f"Route: "
        f"{origin.icao} -> "
        f"{destination.icao}"
    )

    print(
        f"Distance: "
        f"{flight.distance} NM"
    )

    print("\nFUEL PLAN")

    print(
        f"Trip Fuel: "
        f"{fuel['trip_fuel']:.2f} lbs"
    )

    print(
        f"Reserve Fuel: "
        f"{fuel['reserve_fuel']:.2f} lbs"
    )

    print(
        f"Contingency Fuel: "
        f"{fuel['contingency_fuel']:.2f} lbs"
    )

    print(
        f"Total Fuel: "
        f"{fuel['total_fuel']:.2f} lbs"
    )

    print("\nWEIGHT & BALANCE")

    print(
        f"Takeoff Weight: "
        f"{takeoff_weight:.2f} lbs"
    )

    print(
        f"Maximum Weight: "
        f"{aircraft.max_takeoff_weight} lbs"
    )

    print("\nWEATHER")

    print(
        f"Temperature: "
        f"{weather.temperature}°C"
    )

    print(
        f"Wind Speed: "
        f"{weather.wind_speed} kt"
    )

    print(
        f"Visibility: "
        f"{weather.visibility} SM"
    )


main()
