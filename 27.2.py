import asyncio
import random


# Define the main asynchronous function
async def main():
    # Iterate over numbers from 1 to 10
    for i in range(1, 11):
        # Generate a random delay between 1 and 5 seconds
        delay = random.randint(1, 5)
        # Pause the execution of the coroutine for the randomly chosen delay
        await asyncio.sleep(delay)
        # Print the current number and the delay
        print(f"{i}, delay: {delay}")
