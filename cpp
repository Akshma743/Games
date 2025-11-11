/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;

class Addition {
    int a, b, sum;

public:
    
    Addition(int x, int y) {
        a = x;
        b = y;
        sum = a + b;
    }

    
    void display() {
        cout << sum << endl;
    }
};

int main() {
   
    Addition obj(10, 20);
    obj.display();

    return 0;
}
