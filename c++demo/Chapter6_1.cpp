//
// Created by zhangwenning on 2020/4/26.
//
#include <iostream>
#include <vector>

using namespace std;

int add(int x, int y)
{return x+y;}

int fun1(int x, int y)
{return x-y;}

int fun2(int x, int y)
{return x*y;}

void compute(int x, int y, int (*p)(int x, int y)){
    cout << p(x, y)<<endl;
}

int main()
{
    int x = 20, y = 5;
    compute(x, y, add);
    compute(x, y, fun1);
    return 0;
}