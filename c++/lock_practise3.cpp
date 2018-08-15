#include<iostream>
#include<thread>
#include<mutex>

std::mutex foo,bar;

void task_a()
{
    std::lock(foo,bar);
    std::unique_lock<std::mutex> lck1(foo,std::adopt_lock);
    std::unique_lock<std::mutex> lck2(bar,std::adopt_lock);
    std::cout<<"task a\n";
}

void task_b()
{
    std::unique_lock<std::mutex> lck1,lck2;
    lck1 = std::unique_lock<std::mutex>(bar,std::defer_lock);
    lck2 = std::unique_lock<std::mutex>(foo,std::defer_lock);
    std::lock(lck1,lck2);
    std::cout<<"task b\n";
}

int main()
{
    std::thread t1(task_a);
    std::thread t2(task_b);
    t1.join();
    t2.join();

    return 0;
}
