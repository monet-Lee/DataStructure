//
// Created by zhangwenning on 2020/4/25.
//
#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>

using namespace std;

int testPrior()
{
    vector<int> vec;
    srand((unsigned) time (NULL));
    for(int i = 0;i !=10; i++)
        vec.push_back(rand() %100);
    for (auto c : vec)
        cout << c<< "  "<<endl;
    cout <<"*vec.begin():   "<<*vec.begin()<<endl;
    cout << "*(vec.begin()):   "<< *(vec.begin()) << endl;
    cout << "* vec.begin() + 1 :   " << * vec.begin() + 1<<endl;
    cout << "(*(vec.begin())) + 1:   " << (*(vec.begin())) + 1 << endl;
    return 0;
}

int testIfElse()
{
    vector<int> vInt;
    const int sz = 10;
    srand((unsigned) time (NULL));
    for (int i=0; i< sz; i++)
    {
        vInt.push_back(rand() % 100);
        cout << vInt[i]<<endl;
    }
    cout << "----------------"<<endl;
    for (auto &c : vInt){
        c = (c%2==0)? c :c*2;
        cout << c <<endl;
    }
    cout<<"------------------"<<endl;
    for (auto it=vInt.begin(); it!=vInt.end(); it++){
        cout<< *it <<endl;
    }
    return 0;
}

int main()
{
//    testPrior();
    testIfElse();
    return 0;
}
