// A simple program that computes the sum of two int numbers
#include<cmath>
#include<iostream>
#include<string>

#include "SumTwoConfig.h"

// should we include the MathFunctions header?
#ifdef USE_MYMATH
    #include "MathFunctions.h"
#endif

int main(int argc, char* argv[])
{
    if(argc<2){
        // report version 
        std::cout<<argv[0]<<" Version "<<SumTwo_VERSION_MAJOR<<"."
                 <<SumTwo_VERSION_MINOR<<std::endl;
        std::cout<<"Usage: "<<argv[0]<<" number1 number2"<<std::endl;
        return 1;
    }
    
    int num1 = std::stoi(argv[1]);
    int num2 = std::stoi(argv[2]);

    // which sum function should we use?
#ifdef USE_MYMATH
    int result = mysumtwo(num1,num2);
#else
    int result = num1+num2;
#endif
    
    std::cout<<"The sum of "<<num1<<" and "<<num2<<" is "<<result<<std::endl;
    return 0;
}
