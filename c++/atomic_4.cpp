#include<atomic>
#include<vector>
#include<iostream>
#include<chrono>
#include<thread>

std::vector<int> data;
std::atomic_bool data_ready(false);

void writer_thread()
{
    data.push_back(10);
    data_ready = true;
}

void reader_thread()
{
    while(!data_ready.load())
    {
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }
    std::cout<<"data is "<<data[0]<<"\n";
}

int main()
{
    std::thread t1(writer_thread);
    std::thread t2(reader_thread);
    t1.join();
    t2.join();
    return 0;
}
