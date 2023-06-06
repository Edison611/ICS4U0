#include <iostream>
#include <chrono>
#include <random>
using namespace std;

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int x;
    cout << "Enter the range of the list: ";
    cin >> x;
    
    for (int j = 0; j < 25; j++){
        int arr[x];
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<> dis(1, x);
        for (int i = 0; i < x; i++) {
            arr[i] = dis(gen);
        }
        
        auto start = chrono::high_resolution_clock::now();
        insertionSort(arr, x);
        auto stop = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
        cout << "Time taken by insertion sort: " << duration.count() / 1000000.0 << " seconds" << endl;
    }
    return 0;
}
