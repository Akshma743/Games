# empty dictionary
users = {}

n = int(input("Enter number of users: "))

# Take details and store in dictionary
for i in range(n):
    user_id = input("Enter User ID: ")
    name = input("Enter User Name: ")
    age = int(input("Enter User Age: "))
    
    # Store details in dictionary
    users[user_id] = {"Name": name, "Age": age}

print("\nAll Users Data:", users)

# Search  user id
search_id = input("\nEnter User ID to search details: ")

if search_id in users:
    print("User Details:")
    print("ID:", search_id)
    print("Name:", users[search_id]["Name"])
    print("Age:", users[search_id]["Age"])
else:
    print("User not found!")
/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;


void sortNumbers() {
    int arr[10];

    
    cout << "Enter 10 numbers: ";
    for (int i = 0; i < 10; i++) {
        cin >> arr[i];
    }

    
    for (int i = 0; i < 10; i++) {
        for (int j = i + 1; j < 10; j++) {
            if (arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    
    cout << "Sorted numbers: ";
    for (int i = 0; i < 10; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    sortNumbers(); 
    return 0;
}


#include <iostream>
using namespace std;

// Function to check if a number is prime
bool isPrime(int n) {
    if (n <= 1) {
        return false; // 0 and 1 are not prime
    }
    for (int i = 2; i * i <= n; i++) { 
        if (n % i == 0) {
            return false; 
        }
    }
    return true; 

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;

    if (isPrime(num)) {
        cout << num << " is a prime number." << endl;
    } else {
        cout << num << " is not a prime number." << endl;
    }

    return 0;
}
