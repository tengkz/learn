#include<iostream>
#include<thread>
#include<mutex>
#include<condition_variable>
#include<unistd.h>

std::mutex mtx;
std::condition_variable cv1,cv2;
bool ready1 = false, ready2 = false;

void print_id(int id)
{
    std::unique_lock<std::mutex> lck(mtx);
    if(id%2==0)
        while(!ready1) 
            cv1.wait(lck);
    else
        while(!ready2)
            cv2.wait(lck);
    std::cout<<"thread"<<id<<std::endl;
}

void go()
{
    std::unique_lock<std::mutex> lck(mtx);
    ready1 = true;
    cv1.notify_all();
    ready2 = true;
    cv2.notify_all();
}

int main()
{
    std::thread threads[10];
    for(int i=0;i<10;i++)
        threads[i] = std::thread(print_id,i);
    std::cout<<"10 threads ready to race..."<<std::endl;
    go();
    for(auto& th:threads) th.join();

    return 0;
}
