import time
import asyncio

from concurrent.futures import ProcessPoolExecutor

def encrypt_data(data):
    return f"Encrypting data: {data[::-1]}"


async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt_data, "Sensitive Information")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
    time.sleep(3)  # Simulating a CPU-bound task