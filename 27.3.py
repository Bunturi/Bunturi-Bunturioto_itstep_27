import asyncio


# Define an asynchronous function to square a number if it's even
async def square_if_even(number):
    if number % 2 == 0:
        await asyncio.sleep(1)  # Simulating some asynchronous operation
        return number ** 2
    else:
        return None


# Define an asynchronous function to check if a number is even
async def check_even(number):
    await asyncio.sleep(1)  # Simulating some asynchronous operation
    return number % 2 == 0  # Return True if the number is even, False otherwise
