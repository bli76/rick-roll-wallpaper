// After compiling this C++ program, move the exe file into the same directory as the python file

#include <iostream>
#include <string>
#include <filesystem>
#include <unistd.h>
#include <windows.h>
#include <stdlib.h>

using std::string;

int main()
{
    // Get current directory
    char tmp[256];
    getcwd(tmp, 256);
    string cd = tmp;

    // Modify the increment and sleep timer to change the fps
    for (int i = 0; i <= 1500; i+=25)
    {
        string path = cd + "\\frames\\frame" + std::to_string(i) + ".jpg";
        
        SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, (PVOID *)path.c_str(), SPIF_SENDCHANGE);
        
        sleep(1);
    }

    // Switch back to old wallpaper
    string path = cd + "\\wallpaper.png";
    SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, (PVOID *)path.c_str(), SPIF_SENDCHANGE);

    return EXIT_SUCCESS;
}

