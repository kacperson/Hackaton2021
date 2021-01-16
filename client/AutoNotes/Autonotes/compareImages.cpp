#include <stdio.h>
#include <windows.h>
#include <time.h>
#include <string>
#include <iostream>
#include <vector>
#include <atlimage.h>
#include <fstream>

float compareImages(HBITMAP img1, HBITMAP img2)
{
    std::vector<BYTE> buf1;
    IStream* stream1 = NULL;
    HRESULT hr1 = CreateStreamOnHGlobal(0, TRUE, &stream1);
    CImage image1;
    ULARGE_INTEGER liSize1;

    std::vector<BYTE> buf2;
    IStream* stream2 = NULL;
    HRESULT hr2 = CreateStreamOnHGlobal(0, TRUE, &stream2);
    CImage image2;
    ULARGE_INTEGER liSize2;

    image1.Attach(img1);
    image1.Save(stream1, Gdiplus::ImageFormatJPEG);
    IStream_Size(stream1, &liSize1);
    DWORD len1 = liSize1.LowPart;
    IStream_Reset(stream1);
    buf1.resize(len1);
    IStream_Read(stream1, &buf1[0], len1);

    stream1->Release();

    image2.Attach(img2);
    image2.Save(stream2, Gdiplus::ImageFormatJPEG);
    IStream_Size(stream2, &liSize2);
    DWORD len2 = liSize2.LowPart;
    IStream_Reset(stream2);
    buf2.resize(len2);
    IStream_Read(stream2, &buf2[0], len2);

    stream2->Release();

    if (buf1.size() != buf2.size())
        std::cout << "kekw jesteœmy w piŸdzie";
    unsigned long samePixelNumber=0;
    for (int i = 0; i < buf1.size() > buf2.size() ? buf2.size() : buf1.size(); i++)
    {

        if (buf1[i] == buf2[i]) {
            samePixelNumber++;
        }
    }

	return (float)(long double)samePixelNumber/buf1.size();
}