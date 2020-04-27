//
// Created by zhangwenning on 2020/4/26.
//

#include <iostream>

using namespace std;

int testSwitch()
{
    unsigned int aCnt, eCnt, iCnt, oCnt, uCnt;
    char ch;
    cout << "Input string" << endl;
    while(cin >> ch && ch != '0'){
        switch(ch)
        {
            case 'a':
            case 'A':
                aCnt++;
                break;
            case 'e':
            case 'E':
                eCnt++;
                break;
            case 'i':
            case 'I':
                iCnt++;
                break;
            case 'o':
            case 'O':
                oCnt++;
                break;
            case 'u':
            case 'U':
                uCnt++;
                break;
        }
    }
    cout << aCnt << endl;
    cout << eCnt << endl;
    cout << iCnt << endl;
    cout << oCnt << endl;
    cout << uCnt << endl;
    return 0;
}

int testCount()
{
    string currString, preString = " ", maxString;
    int currCnt = 1, maxCnt = 1;
    cout << "Input string:" << endl;
    while (cin >> currString && currString != "00")
    {
        if(currString == preString)
        {
            currCnt++;
            if(maxCnt < currCnt)
                maxCnt = currCnt;
                maxString = preString;
        }else {

            currCnt = 1;
        }
        preString = currString;

    }
    if (maxCnt == 1)
        cout << "total only one value" << endl;
    else{
        cout << "maxValue:   " << maxString <<"    numbers is:   "<< maxCnt << endl;
    }
    return 0;
}
int main()
{
//    testSwitch();
    testCount();
    return 0;
}