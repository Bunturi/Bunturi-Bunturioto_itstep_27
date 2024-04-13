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


# Define the main asynchronous function to test the above functions
async def test_functions():
    # Define a list of numbers to test
    numbers = [12, 17, 88, 15, 4, 18, 47, 55, 24, 42]
    tasks = []

    # Create a list of tasks by appending tasks for each number
    for number in numbers:
        tasks.append(square_if_even(number))
        tasks.append(check_even(number))

    # Execute all tasks concurrently and collect their results
    results = await asyncio.gather(*tasks)