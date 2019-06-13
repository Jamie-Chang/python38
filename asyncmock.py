# https://docs.python.org/3.8/library/unittest.mock.html?#module-unittest.mock
import asyncio
from unittest.mock import patch


class a:
    async def stuff(self):
        return 'stuff'


async def test():
    with patch('__main__.a', autospec=True):
        obj = a()
        await obj.stuff()
        obj.stuff.assert_awaited_once_with()

asyncio.run(test())
