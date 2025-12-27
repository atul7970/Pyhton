import asyncio
import aiohttp

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.text() 
    
async def main():
    urls = ["https://httpbin.org/delay/1"]*3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())