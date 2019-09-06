import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(('127.0.0.1', 9999))

# 接收欢迎语
print(s.recv(1024).decode('utf-8'))

# 发送多个数据
for data in [b'Rocky', b'Candy', b'Lily']:
	# 发送数据
	s.send(data)
	# 打印接收的数据
	print(s.recv(1024).decode('utf-8'))

# 给服务器发送关闭指令
s.send(b'exit')

# 关闭连接
s.close()