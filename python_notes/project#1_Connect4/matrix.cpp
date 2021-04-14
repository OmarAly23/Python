#include <iostream>
using namespace std;
int main(void){
    int row=7,column=6;
    for(int i=0;i<row;i++){
        for(int j=0;j<column;j++){
            cout << "| ";
        }
        cout << endl;
    }
}