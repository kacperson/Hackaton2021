#include <stdio.h>
#include <windows.h>
#include <time.h>
#include <string>
#include <iostream>
#include <vector>
#include <atlimage.h>
#include <fstream>
HBITMAP GetScreenShot(int x1, int y1, int w, int h);
float compareImages(HBITMAP img1, HBITMAP img2);