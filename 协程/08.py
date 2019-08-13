import threading
import asyncio

async def hello():
    print("Here we go! (%s)" % threading.currentThread())
    print("Start! (%s)" % threading.currentThread())
    await asyncio.sleep(2)
    print("Done! (%s)" % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()