"""
Питон - синхроненный, код выполняется последовательно и ждёт выполнения прошлой инструкции,
это вызвано задержкой - блокировака вход/выход

Минимизации таких задержек:
Асинхронность - происходит независимо друг от друга в одном потоке
 (Coroutines - cooperative subroutine - подпрограммы
await - приостанавливает выполнение текущей подпрограммы Coroutine (накормить конкретно взятого животного) и вызывает ожидание

Корутин - это любая функция с префиксом async
TASK - это объект, который оборачивает корутин, .gather() or .create_task()
Future - пустая структура для заполнения данными 
"""


from time import sleep
import asyncio
import random

animals = ("🐯", "🦓", "🦒", "🐼", "🐪", "🦘", "🐘", "🦍", "🕷", "🦥")

def feed_task(animal):
    """Synchronous task."""
    spend_time = round((random.randint(4, 8) * .1), 2)
    sleep(spend_time)
    print(f"Feed {animal} completed during {spend_time} sec")


async def feed_task_coroutine(animal):
    """Coroutine task"""
    spend_time = round((random.randint(4, 8) * .1), 2)
    await asyncio.sleep(spend_time)
    print(f"Feed {animal} completed during {spend_time} sec")


def synch():
    """ Synchronous """
    for index, element in enumerate(animals):
        feed_task(element)

async def asynch():
    """ Asynchronous """
    tasks = [feed_task_coroutine(i) for i in animals]
    await asyncio.gather(*tasks)


if __name__ == "__main__":

    print("---------- WELCOME TO CIRCUS --------- \n")

    print('\tSynchronous:')
    synch()

    print('\n\tAsynchronous:')
    asyncio.run(asynch())


""" 
This is study pet-project where the main idea take out to follow the footages to define fundamentals differences between synchronous and asynchronous programming using actually Python's package as acyncio.

Introduction
Imagine you are enterpriser own circus, you have got the majority of animals. Each of them refer in list sequence. Take to measure the random time to feed them. Outcome attached to the repository




Checkout System for Boutique Store. When client require list of products which should packed and calculated overall price the order. Preset of boutiques products may choose default using text emoji's for data visualization of orders


"""