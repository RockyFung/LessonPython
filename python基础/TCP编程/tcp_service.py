import socket, threading, time

#创建一个基于IPV4和TCP协议的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定端口
s.bind(('127.0.0.1', 9999))

#监听， 参数为指定等待连接的最大数值
s.listen(5)
print('等待连接。。。')


# 方法实现
def tcplink(sock, addr):
	print('接收到一个新的连接 %s:%s' % addr)
	# 向客户端发送一个欢迎语
	sock.send(b'welcome!')
	# 接收客户端传的参数
	while True:
		# 一次接收1kb
		data = sock.recv(1024)
		time.sleep(1)

		# 如果data没有值，或者客户端传了exit就退出循环
		if not data or data.decode('utf-8') == 'exit':
			break

		# 处理客户端的参数后再返回给客户端
		ss = ('hello, %s' % data.decode('utf-8')).encode('utf-8')
		sock.send(ss)

	# 关闭连接
	sock.close()
	print('来自%s:%s的连接已经关闭' % addr)
	

# 通过永久循环来接收客户端的连接 accept()会等待并返回一个客户端连接
while True:
	# 等待并接收一个客户端连接
	sock, addr = s.accept()
	# 创建新线程来处理TCP连接
	t = threading.Thread(target=tcplink, args=(sock,addr))
	t.start()

















