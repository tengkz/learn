#include<iostream>
#include<thread>
#include<mutex>

std::mutex mtx;

void print_50(char c)
{
    std::unique_lock<std::mutex> lck;
    lck = std::unique_lock<std::mutex>(mtx);
    for(int i=0;i<50;i++)
        std::cout<<c;
    std::cout<<std::endl;
}

int main()
{
    std::thread t1(print_50,'+');
    std::thread t2(print_50,'-');
    t1.join();
    t2.join();

    return 0;
}
