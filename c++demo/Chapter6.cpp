//
// Created by zhangwenning on 2020/4/26.
//
#include <iostream>
#include <vector>

using namespace std;

void swapPointer(int *s, int *t)
{
    int temp = *s;
    *s = *t;
    *t = temp;
}
void testSwapPointer()
{
    int a = 10, b= 20;
    int *s = &a, *t = &b;
    cout << a << ",  "<<b<<endl;
    swapPointer(s, t);
    cout << a <<",   "<<b<<endl;
}



//int main(int argc, char ** argv)
//{
////    testSwapPointer();
//    for (int i=0; i!=argc; i++)
//    {
//        cout << "argc["<<i<<"]:  "<< argc[i]<<endl;
//    }
//    return 0;
//}

void print(vector<int> vInt, unsigned index)
{
    unsigned sz = vInt.size();
    if (!vInt.empty() && index < sz){
        cout << vInt[index] <<endl;
        index++;
        print(vInt, index);
    }
}

void testRecursion()
{
    int a[] = {1,2,3,4,5,6,7};
    vector<int> v(a, a+5);
    print(v, 0);
}

int main()
{
//    testSwapPointer();
//    main();
    testRecursion();
    return 0;
}