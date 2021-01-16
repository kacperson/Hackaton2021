#include <stdio.h>
#include <windows.h>
#include <time.h>
#include <string>
#include <iostream>
#include <vector>
#include <atlimage.h>
#include <fstream>

void GetScreenShot(void)
{

    int x1, y1, x2, y2, w, h;

    // get screen dimensions
    std::cout << "Point to Left Top corner of the window, then type Y and Enter";
    getchar();
    getchar();
    POINT LeftTop;
    GetCursorPos(&LeftTop);
    //ScreenToClient(hwnd, &LeftTop);
    std::cout << "Point to Right Bottom corner of the window, then type Y and Enter";
    getchar();
    getchar();
    POINT RightBottom;
    GetCursorPos(&RightBottom);
    //ScreenToClient(hwnd, &RightBottom);
    x1 = LeftTop.x;
    y1 = LeftTop.y;
    x2 = RightBottom.x;
    y2 = RightBottom.y;
    w = x2 - x1;
    h = y2 - y1;

    // copy screen to bitmap
    HDC     hScreen = GetDC(NULL);
    HDC     hDC = CreateCompatibleDC(hScreen);
    HBITMAP hBitmap = CreateCompatibleBitmap(hScreen, w, h);
    HGDIOBJ old_obj = SelectObject(hDC, hBitmap);
    BOOL    bRet = BitBlt(hDC, 0, 0, w, h, hScreen, x1, y1, SRCCOPY);

    std::vector<BYTE> buf;
    IStream* stream = NULL;
    HRESULT hr = CreateStreamOnHGlobal(0, TRUE, &stream);
    CImage image;
    ULARGE_INTEGER liSize;

    // screenshot to jpg and save to stream
    image.Attach(hBitmap);
    image.Save(stream, Gdiplus::ImageFormatJPEG);
    IStream_Size(stream, &liSize);
    DWORD len = liSize.LowPart;
    IStream_Reset(stream);
    buf.resize(len);
    IStream_Read(stream, &buf[0], len);
    stream->Release();

    // put the imapge in the file
    std::fstream fi;
    fi.open("test.bmp", std::fstream::binary | std::fstream::out);
    fi.write(reinterpret_cast<const char*>(&buf[0]), buf.size() * sizeof(BYTE));
    fi.close();

    // save bitmap to clipboard
    OpenClipboard(NULL);
    EmptyClipboard();
    SetClipboardData(CF_BITMAP, hBitmap);
    CloseClipboard();

    // clean up
    SelectObject(hDC, old_obj);
    DeleteDC(hDC);
    ReleaseDC(NULL, hScreen);
    DeleteObject(hBitmap);
}
