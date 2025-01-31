import numpy as np
import matplotlib.pyplot as plt

# Parameters
np.random.seed(42)  # For reproducibility
arrival_rate = 1.5# Lambda (arrivals per time unit)
service_rate = 2.0# Mu (service completions per time unit)
num_customers = 1000# Generate inter-arrival times and service times
inter_arrival_times = np.random.exponential(1/arrival_rate, num_customers)
service_times = np.random.exponential(1/service_rate, num_customers)

# Arrival times
arrival_times = np.cumsum(inter_arrival_times)

# Start service times
# start_service_times[0] = arrival_times[0]  # The first customer is served immediately# Departure times
start_service_times = np.maximum(arrival_times, np.roll(np.cumsum(service_times), 1))
departure_times = start_service_times + service_times

# Calculate performance metrics
waiting_times = start_service_times - arrival_times
total_times_in_system = departure_times - arrival_times
mean_waiting_time = np.mean(waiting_times)
mean_total_time_in_system = np.mean(total_times_in_system)
server_utilization = np.sum(service_times) / departure_times[-1]

print(f"Mean waiting time: {mean_waiting_time:.2f}")
print(f"Mean time in system: {mean_total_time_in_system:.2f}")
print(f"Server utilization: {server_utilization:.2f}")

# Plot the results
plt.figure(figsize=(10, 5))
plt.hist(waiting_times, bins=30, alpha=0.7, label='Waiting Times')
plt.hist(total_times_in_system, bins=30, alpha=0.7, label='Total Times in System')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.legend()
plt.title('M/G/1 Queue Simulation')
plt.show()
