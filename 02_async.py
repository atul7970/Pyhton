import asyncio

async def pizza(name):
    print(f"Starting to make {name} pizza...")
    await asyncio.sleep(4)
    print(f"{name} pizza is ready!")

async def main():
    await asyncio.gather(
        pizza("Margherita"),
        pizza("Pepperoni"),
        pizza("Hawaiian")
    )

asyncio.run(main())