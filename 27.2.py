import asyncio
import random


# Define the main asynchronous function
async def main():
    # Iterate over numbers from 1 to 10
    for i in range(1, 11):
        # Generate a random delay
        delay = random.randint(1, 5)
        await asyncio.sleep(delay)
        # Print the current number and the delay
        print(f"{i}, delay: {delay}")
    # print all tasks are completed
    print("All Tasks Completed")

# run the main asynchronous function
asyncio.run(main())