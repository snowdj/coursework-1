#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include <windows.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <iphlpapi.h>
#include <stdio.h>
#include <iostream>

#pragma comment(lib, "Ws2_32.lib")

using namespace std;

int main() {
	WSADATA wsaData;
	int iResult;

	// Initialize Winsock
	WORD wVersionRequested = MAKEWORD(2, 2);  // Use the MAKEWORD(lowbyte, highbyte) macro declared in Windef.h
	iResult = WSAStartup(wVersionRequested, &wsaData);
	if (iResult != 0) {
		printf("WSAStartup failed: %d\n", iResult);
		return 1;
	}

	cout << "Ver: " << wsaData.wVersion << endl;
	cout << "HVer: " << wsaData.wHighVersion << endl;
	cout << "szDescription: " << wsaData.szDescription << endl;
	cout << "szSystemStatus: " << wsaData.szSystemStatus << endl;

	WSACleanup();
	return 0;
}
