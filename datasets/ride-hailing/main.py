import pandas as pd
from faker import Faker
import random
import uuid
import sqlite3

# Number of records to generate
NUM_DRIVERS = 1000
NUM_PASSENGERS = 2000
NUM_RIDES = 5000
NUM_VEHICLES = 1000

# Initialize Faker
fake = Faker()

# 1. Generate Drivers Data (Using range() for unique IDs)
drivers = []
for driver_id in range(1, NUM_DRIVERS + 1):
    driver = {
        'driver_id': driver_id,
        'driver_name': fake.name(),
        'phone_number': fake.phone_number(),
        'license_number': fake.unique.license_plate(),
    }
    drivers.append(driver)

drivers_df = pd.DataFrame(drivers)

# 2. Generate Passengers Data (Using range() for unique IDs)
passengers = []
for passenger_id in range(1, NUM_PASSENGERS + 1):
    passenger = {
        'passenger_id': passenger_id,
        'passenger_name': fake.name(),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
    }
    passengers.append(passenger)

passengers_df = pd.DataFrame(passengers)

# 3. Generate Vehicles Data (Using a combination of vehicle details)
vehicles = []
for vehicle_id in range(1, NUM_VEHICLES + 1):
    vehicle = {
        'vehicle_id': vehicle_id,
        'driver_id': random.choice(drivers_df['driver_id']),  # FK to Drivers
        'vehicle_type': random.choice(['Car', 'Motorbike', 'Van']),
        'vehicle_model': f"{fake.company()} {fake.word()}",  # Using company and word as a proxy for vehicle model
        'license_plate': fake.unique.license_plate(),
    }
    vehicles.append(vehicle)

vehicles_df = pd.DataFrame(vehicles)

# 4. Generate Rides Data
rides = []
for ride_id in range(1, NUM_RIDES + 1):
    ride = {
        'ride_id': ride_id,
        'driver_id': random.choice(drivers_df['driver_id']),  # FK to Drivers
        'passenger_id': random.choice(passengers_df['passenger_id']),  # FK to Passengers
        'vehicle_id': random.choice(vehicles_df['vehicle_id']),  # FK to Vehicles
        'start_location': fake.address(),
        'end_location': fake.address(),
        'start_time': fake.date_time_this_year(),
        'end_time': fake.date_time_this_year(),
        'fare': round(random.uniform(5.0, 100.0), 2),  # Random fare
    }
    rides.append(ride)

rides_df = pd.DataFrame(rides)

# 5. Generate Payments Data (UUID for payment_id)
payments = []
for ride in rides_df.itertuples():
    payment = {
        'payment_id': str(uuid.uuid4()),  # Use UUID for unique payment_id
        'ride_id': ride.ride_id,  # FK to Rides
        'payment_method': random.choice(['Credit Card', 'Cash', 'E-Wallet']),
        'amount': ride.fare,  # Same as fare from the ride
        'payment_time': fake.date_time_this_year(),
    }
    payments.append(payment)

payments_df = pd.DataFrame(payments)

# SQLite database connection
conn = sqlite3.connect('ride_hailing_service.db')

# Save data to SQLite tables
drivers_df.to_sql('drivers', conn, if_exists='replace', index=False)
passengers_df.to_sql('passengers', conn, if_exists='replace', index=False)
vehicles_df.to_sql('vehicles', conn, if_exists='replace', index=False)
rides_df.to_sql('rides', conn, if_exists='replace', index=False)
payments_df.to_sql('payments', conn, if_exists='replace', index=False)

# Commit and close the SQLite connection
conn.commit()
conn.close()

# Display confirmation
print("Data has been saved to SQLite database: ride_hailing_service.db")
