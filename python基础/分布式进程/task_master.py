import random,time,queue
from multiprocessing.managers import BaseManager

#发送任务队列
task_queue = queue.Queue()

#接收结果队列
result_queue = queue.Queue()

#从BaseManager继承QueueManager
class QueueManager(BaseManager):
	pass

# 把两个queue都注册到网络上，callable参数关联了queue对象
QueueManager.register('get_task_queue', callable=lambda:task_queue)
QueueManager.register('get_result_queue', callable=lambda:result_queue)


#绑定端口5000，设置验证码abck
manager = QueueManager(address=('', 5000), authkey=b'abcd')

#启动queue
manager.start()

#获得通过网络访问的queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#放几个任务进去
for i in range(10):
	n = random.randint(0, 1000)
	print('put task %d ' % n)
	task.put(n)

# 从result队列读取结果
print('try get results')
 # 需要等task_worker.py 把任务结果放到result的queue中才会接收到
for i in range(10):
	r = result.get(timeout=100)
	print('result:%s' % r)


# task_workder.py执行完任务后关闭
 #关闭
manager.shutdown()
print('master exit')














