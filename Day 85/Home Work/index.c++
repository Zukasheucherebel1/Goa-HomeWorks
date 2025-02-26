 // Define a struct to represent a person
#include <iostream>
#include <string>
using namespace std;

struct Person {
    string name;
    int age;    
};                        
int main() {
    Person person1;
    person1.name = "Gocha";
    person1.age = 16;
    
    cout << "Name: " << person1.name << endl;
    cout << "Age: " << person1.age << endl;
    
    return 0;
}                   
