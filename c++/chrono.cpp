#include<iostream>
#include<ratio>
#include<chrono>

int main()
{
    typedef std::chrono::duration<int> seconds_type;
    typedef std::chrono::duration<int,std::milli> milliseconds_type;
    typedef std::chrono::duration<int,std::ratio<60*60>> hours_type;

    hours_type h_oneday(24);
    seconds_type s_oneday(60*60*24);
    milliseconds_type ms_oneday(s_oneday);

    seconds_type s_onehour(60*60);
    hours_type h_onehour(std::chrono::duration_cast<hours_type>(s_onehour));
    milliseconds_type ms_onehour(s_onehour);

    std::cout<< ms_onehour.count()<<"ms in 1h"<<std::endl;
    return 0;
}
