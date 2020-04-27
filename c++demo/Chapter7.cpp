//
// Created by zhangwenning on 2020/4/26.
//
#include <iostream>
#include <string>

using namespace std;

class Window_mgr
{
public:
    void clear();
};

class Screen
{
    friend void Window_mgr::clear();
private:
    unsigned height = 0, width = 0;
    unsigned cursor = 0;
    string contents;
public:
    Screen() = default;
    Screen(unsigned ht, unsigned wd, char c)
        :height(ht), width(wd), contents(ht * wd, c){ }
};

void Window_mgr::clear()
{

}

int main()
{

    return 0;
}