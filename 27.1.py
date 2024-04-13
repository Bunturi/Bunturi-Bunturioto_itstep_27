import asyncio

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