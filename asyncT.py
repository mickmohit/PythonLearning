import time
import asyncio


async def function1():
  await asyncio.sleep(1)
  print("func 1")
  return "Cole"


async def function2():
  await asyncio.sleep(1)
  print("func 2")
  return "Collin"


async def function3():
  await asyncio.sleep(2)
  print("func 3")
  return "Conrad"


async def main():
  # Create tasks for concurrent execution
  task1 = asyncio.create_task(function1())
  task2 = asyncio.create_task(function2())
  task3 = asyncio.create_task(function3())
  # Await the tasks to get their results
  result1 = await task1
  result2 = await task2
  result3 = await task3

  L = await asyncio.gather(function1(), function2(), function3())
  print(L)


asyncio.run(main())
