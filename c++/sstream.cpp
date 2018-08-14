#include<iostream>
#include<sstream>
#include<string>
int main()
{
    std::string str = "I am coding ...";
    std::istringstream is(str);
    do
    {
        std::string substr;
        is>>substr;
        std::cout<<substr<<std::endl;
    }while(is);
    return 0;
}
