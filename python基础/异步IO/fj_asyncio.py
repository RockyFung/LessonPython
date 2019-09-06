import time, asyncio
'''
python 3.6之前
@asyncio.coroutine #协程装饰器
def task1():
	print('开始运行task1...')
	yield from asyncio.sleep(2) # 任务耗时2s
	print('task1任务完成')
	return task1.__name__
'''

# python3.6之后
async def task1():
	print('开始运行task1...')
	await asyncio.sleep(2) # 任务耗时2s
	print('task1任务完成')
	return task1.__name__

async def task2():
	print('开始运行task2')
	await asyncio.sleep(5) # 任务耗时3s
	print('task2任务完成')
	return task2.__name__

# 调用函数
async def main():
	# 把任务添加到task中
	tasks = [task1(), task2()]
	# 子生成器
	done, pending = await asyncio.wait(tasks)

	for r in done:
		print('协程无序返回值：' + r.result())

if __name__ == '__main__':
	start = time.time()
	# 创建事件循环对象
	loop = asyncio.get_event_loop()
	try:
		# main（）放入循环事件，知道完成
		loop.run_until_complete(main())
	finally:
		# 关闭循环
		loop.close()

	print('所有任务完成，耗时%.5f秒' % float(time.time() - start))





