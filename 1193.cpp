//
// Created by minis on 2023-06-20.
//
#include <iostream>
using namespace std;
int main() {
	int x;
	cin >> x;
	int i = 0;
	for (; (i)*(i-1) / 2 < x; i++);
	cout << (i-1)*(i) / 2 - x << '/' << x - (i-1)*(i-2) / 2 << endl;
	return 0;
}