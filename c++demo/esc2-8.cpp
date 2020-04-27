//
// Created by zhangwenning on 2020/4/24.
//

#include <iostream>

using namespace std;

int esc2_8()
{
    cout<< "2\x4d\012";
    cout<<"2\tM\n";
    return 0;
}

int pointer()
{
    int a = 1, b = 2;
    int *p1 = &a;
    cout << p1 <<"----------"<< *p1 << endl;
    p1 = &b;
    cout << p1 <<"----------"<< *p1 << endl;
    *p1 = 20;
    cout << p1 <<"----------"<< *p1 << endl;
    b = 30;
    cout << p1 <<"----------"<< *p1 <<endl;
    return 0;
}

int testauto(){
    int i = 0, &r = i;
    auto a = r;
    const int ci = i, &cr = ci;
    auto b = ci;
    auto c = cr;
    auto d = &i;
    auto e = &ci;
    auto &g = ci;
    cout << a << " "<< b <<" "<< c << " "<<d<<" "<<e<<" "<<g<<endl;
    a = 42;
    b = 42;
    c = 42;
//    d = 42; //d 是一个指针，赋值非法
//    e = 42;
//    g = 42; //g 是一个常量引用，赋值非法
    return 0;
}

int testAutoType(){
    const int i = 42;
    auto j = i;
    const auto &k = i;
    auto *p = &i;
    const auto j2 = i, &k2 = i;
    cout << typeid(i).name() << endl;
    cout << typeid(j).name() <<endl;
    cout << typeid(k).name() << endl;
    cout << typeid(p).name() << endl;
    cout<< typeid(j2).name() << endl;
    cout << typeid(k2).name() << endl;
    return 0;
}

int testDecltype(){
    int a = 3;
    auto c1 = a;
    int c = a;
    decltype(a) c2= a;
    decltype((a)) c3 = a;

    const int d = 5;
    auto f1 = d;
    int f = d;
    decltype(d) f2 = d;

    cout << typeid(c1).name() << endl;
    cout << typeid(c).name() << endl;
    cout << typeid(c2).name() << endl;
    cout << typeid(c3).name() << endl;
    cout << typeid(f1).name() << endl;
    cout << typeid(f).name() << endl;
    cout << typeid(f2).name() << endl;
    c1++;
    c++;
    c2++;
    c3++;
    f1++;
    f++;
    return 0;
}

int main()
{
//    esc2_8();
//    pointer();
//    testauto();
//    testAutoType();
    testDecltype();
    return 0;
}