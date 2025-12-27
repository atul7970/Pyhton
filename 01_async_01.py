import asyncio

async def make_pizza():
    print ("Starting to make pizza...")
    await asyncio.sleep(2)  # Simulate time taken to make pizza
    print ("Pizza is ready!")

asyncio.run(make_pizza())
