#include <iostream>
#include <algorithm>
#include <cstdlib>

int main() {
	int N, M;
	std::cin >> N >> M;
	int **Matrix;
	Matrix = (int**) malloc(sizeof(int*) * N);
	for (int i = 0; i < N; i++) {
		Matrix[i] = (int*) malloc(sizeof(int) * M);
		for (int j = 0; j < M; j++) {
			scanf("%1d", &Matrix[i][j]);
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			int num;
			scanf("%1d", &num);
			Matrix[i][j] += num;
		}
	}
	int counter = 0;
	for (int i = 0; i < std::max(N-2, 0); i++) {
		for (int j = 0; j < std::max(M-2, 0); j++) {
			if (Matrix[i][j] % 2) {
				counter += 1;
				Matrix[i][j] += 1;
				Matrix[i+1][j] += 1;
				Matrix[i+2][j] += 1;
				Matrix[i][j+1] += 1;
				Matrix[i+1][j+1] += 1;
				Matrix[i+2][j+1] += 1;
				Matrix[i][j+2] += 1;
				Matrix[i+1][j+2] += 1;
				Matrix[i+2][j+2] += 1;
			}
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (Matrix[i][j] % 2) {
				counter = -1;
				break;
			}
		}
	}
	std::cout << counter << std::endl;
	return 0;
}