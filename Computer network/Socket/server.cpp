#include<iostream>
#include<winsock.h>
#pragma comment(lib,"ws2_32.lib")
using namespace std;

/*初始化套接字库*/
void initialization() {
	WORD w_req = MAKEWORD(2,2);//版本号
	WSADATA wsadata;
	int err;
	err = WSAStartup(w_req,&wsadata);
	if (err != 0) {
		cout << "初始化套接字库失败！" << endl;
	}
	else {
		cout << "初始化套接字库成功！" << endl;
	}
	//检测版本号
	if (LOBYTE(wsadata.wVersion) != 2 || HIBYTE(wsadata.wHighVersion) != 2) {
		cout << "套接字库版本号不符！" << endl;
	}
	else {
		cout << "套接字库版本正确！" << endl;
	}
}

int main() {
	//定义长度变量
	int send_len = 0;
	int recv_len = 0;
	int len = 0;
	//定义发送缓冲区和接受缓冲区
	char send_buf[100];
	char recv_buf[100];
	//定义服务端套接字，接受请求套接字
	SOCKET s_server;
	SOCKET s_accept;
	//服务端地址客户端地址
	SOCKADDR_IN server_addr;
	SOCKADDR_IN accept_addr;
	initialization();
	//填充服务端信息
	server_addr.sin_family = AF_INET;
	server_addr.sin_addr.S_un.S_addr = htonl(INADDR_ANY);
	server_addr.sin_port = htons(12341);
	//创建套接字
	s_server = socket(AF_INET,SOCK_STREAM,0);
	if (bind(s_server, (SOCKADDR*)&server_addr, sizeof(SOCKADDR)) == SOCKET_ERROR) {
		cout << "套接字绑定失败！" << endl;
		WSACleanup();
	}
	else {
		cout << "套接字绑定成功！" << endl;
	}
	//设置套接字为监听状态
	if (listen(s_server, SOMAXCONN) < 0) {
		cout << "设置监听失败！" << endl;
		WSACleanup();
	}
	else {
		cout << "设置监听成功！" << endl;
	}
	cout << "服务端正在监听连接，请稍等---" << endl;
	//接受连接请求
	len = sizeof(SOCKADDR);
	s_accept = accept(s_server, (SOCKADDR*)&accept_addr, &len);
	if (s_accept == SOCKET_ERROR) {
		cout << "连接失败！" << endl;
		WSACleanup();
		return 0;
	}
	cout << "连接建立，准备接受数据" << endl;
	//接受数据
	while (1) {
		recv_len = recv(s_accept,recv_buf,100,0);
		if (recv_len < 0) {
			cout << "接受失败！" << endl;
			break;
		}
		else {
			cout << "客户端信息：" << recv_buf << endl;
		}
		cout << "请输入回复信息：";
		cin >> send_buf;
		send_len = send(s_accept,send_buf,100,0);
		if (send_len < 0) {
			cout << "发送失败！" << endl;
			break;
		}
	}
	return 0;
}

