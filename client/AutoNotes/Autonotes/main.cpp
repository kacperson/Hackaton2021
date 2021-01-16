#include "functions.h"
#include <iostream>
#include <windows.h>
int main()
{
    int x1, y1, x2, y2, w, h, seconds, slides_counter;
    // get screen dimensions
    std::cout << "Point to Left Top corner of the window, then type Y and Enter";
    getchar();
    getchar();
    POINT LeftTop;
    GetCursorPos(&LeftTop);

    std::cout << "Point to Right Bottom corner of the window, then type Y and Enter";
    getchar();
    getchar();
    POINT RightBottom;
    GetCursorPos(&RightBottom);

    x1 = LeftTop.x;
    y1 = LeftTop.y;
    x2 = RightBottom.x;
    y2 = RightBottom.y;
    w = x2 - x1;
    h = y2 - y1;
    seconds = 3;
    char stop = ' ';
    std::cout << "Press ESC to stop the program";
    while (/*stop != char(27)*/true) {
        GetScreenShot(x1, y1, w, h);
        Sleep(seconds * 1000);
    }
    return 0;
}