//
// Created by zhangwenning on 2020/4/25.
//

#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <cstring>

using namespace std;

int testCin(){
    string line;
    cout << "输入字符串" << endl;
    while (getline(cin, line)){
        cout << line << endl;
        break;
    }
    string word;
    cout << "输入单词" << endl;
    while (cin >> word){
        cout << word << endl;
        break;
    }
    return 0;
}

int testAutoCin(){
    string s;
    cout << "输入字符串" << endl;
    getline(cin, s);
    for (auto &c : s){
        c = 'X';
    }
    cout << s << endl;
    return 0;
}

int testIspunct(){
    string s, result;
    cout << "输入字符串" << endl;
    getline(cin, s);
    for (auto c : s){
        if (!ispunct(c))
            cout << c << endl;
    }
    cout <<"------------------"<< endl;

    for (decltype(s.size()) i = 0; i < s.size(); i++)
    {
        if (!ispunct(s[i]))
            result  += s[i];
    }
    cout <<endl << result << endl;

    return 0;
}

int testVector()
{
    vector<int> vInt;
    int i;
    char cont = 'y';
    cout << "Input values:" << endl;
    while (cin >> i){
        vInt.push_back(i);
        cout << "是否继续(y or n)"<<endl;
        cin >> cont;
        if (cont != 'y' && cont != 'Y')
            break;
    }
    for (auto mem : vInt){
        cout << mem << endl;
    }
    return 0;
}

int vectorAdd()
{
    vector<int> vInt;
    int iVal;
    char cont = 'y';
    cout << "Input a array:"<< endl;
    while (cin >> iVal){
        vInt.push_back(iVal);
        cout << "end? y or n"<<endl;
        cin>>cont;
        if (cont != 'y' && cont != 'Y')
            break;
    }
    if (vInt.size() == 0)
        cout << "null array"<<endl;
    for (decltype(vInt.size()) i = 0; i < vInt.size()/2; i++){
        cout << vInt[i] + vInt[vInt.size() - i -1] << endl ;
        if ((i+1)%5 == 0){
            cout <<"---------------"<< endl;
        }
    }
    if (vInt.size() % 2 != 0){
        cout << vInt[vInt.size()/2] << endl;
    }
    return 0;
}


int testCIter()
{
    vector<int> v1;
    vector<int> v2(10);
    vector<int> v3 (10, 42);

    cout << "size of v1:" << "   "<<v1.size() << endl;
    if (v1.cbegin() != v1.cend()){
        for (auto it = v1.cbegin(); it != v1.cend(); it++)
            cout << *it << " " << endl;
    }

    cout << "size of v2:  " << v2.size() << endl;
    if (v2.cbegin() != v2.cend())
    {
        for (auto it=v2.cbegin(); it != v2.cend(); it++)
            cout << *it <<"  "<< endl;
    }
    return 0;


}

int testIter()
{
    vector<string> text;
    string s;
    char cont='y';
    cout << "Input string: "<< endl;
    while(getline(cin, s)){
        text.push_back(s);
        break;
    }
    for (auto it = text.begin(); it != text.end() && !it -> empty(); it++){
        for(auto its = it -> begin(); its != it -> end(); its++){
            *its = toupper(*its);
        }
        cout << *it << endl;
    }
    return 0;
}

int mmInt()
{
    vector<int> vInt;
    srand((unsigned) time(NULL));
    for (int i=0; i<10; i++){
        vInt.push_back(rand() % 1000);
    }
    cout << "random number is: "<< endl;
    for(auto it=vInt.begin(); it != vInt.end(); it++){
        cout << *it <<endl;
    }
    cout << "--------------------------" << endl;
    for (auto it=vInt.begin(); it != vInt.end(); it++){
        *it *= 10;
        cout << *it << endl;
    }
    return 0;
}

int subsection()
{
    vector<unsigned> vUS(11);
    auto it = vUS.begin();
    int iVal;
    char cont = 'y';
    cout << "Input grade array: "<<endl;
    while (cin >> iVal)
    {
        if (iVal < 101)
            ++ *(it + iVal/10);
            cout << "end? y or n" << endl;
            cin >> cont;
        if (cont != 'y')
            break;
    }
    cout << "number of grade: " << vUS.size() << endl;
    cout << "scale of grade: " << endl;
    //iteration to output elements
    for (it = vUS.begin(); it != vUS.end(); it++)
    {
        cout << *it <<endl;
    }
    return 0;
}

int testCString()
{
    char str1[] = "Welcome to";
    char str2[] = "C++ family1";

    char result[strlen(str1) + strlen(str2) -1];
    strcpy(result, str1);
    strcat(result, str2);
    cout << result << endl;
    return 0;
}

int main()
{
//    testCin();
//    testAutoCin();
//    testIspunct();
//    testVector();
//    vectorAdd();
//    testCIter();
//    testIter();
//    mmInt();
//    subsection();

/*
    array<unsigned, 10> arr;
    for (int i =0; i<arr.size();i++){
        cout << arr.at(i)<<endl;
    }
    int it = arr.at(1);
    cout << ++ arr.at(1)+9  << endl;
*/
    testCString();
    return 0;
}