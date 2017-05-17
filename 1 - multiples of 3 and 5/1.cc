#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cout << "Usage: ./multiples_of_3_and_5 sumBelowThisNumber" << endl;
        return 0;
    }
    int sum = 0;
    unsigned int ceiling = stoi(argv[1]);
    for (unsigned i = 1; i < ceiling; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
        }
    }
    cout << "Sum: " << sum << endl;
    return 0;
}
