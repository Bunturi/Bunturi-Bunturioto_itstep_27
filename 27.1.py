import asyncio
import time

# Define an asynchronous function to simulate drinking coffee
async def drink_coffee():
    print("Start Drinking Coffee")
    await asyncio.sleep(2)
    print("Finished Drinking Coffee")

# Define an asynchronous function to simulate eating breakfast
async def eat_breakfast():
    print("Start Eating Breakfast")
    await asyncio.sleep(5)
    print("Finished Eating Breakfast")


# Define the main asynchronous function
async def main():
    start_time = time.time()  # Record the start time

    # Gather both asynchronous tasks to execute concurrently
    all_tasks = asyncio.gather(drink_coffee(), eat_breakfast())
    await all_tasks

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f"Elapsed Time: {elapsed_time:.2f} Seconds")


