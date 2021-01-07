//
//  anonymous_func.c
//  
//
//  Created by Erli Cai on 24/12/2020.
//

#include <stdio.h>

int main(int argc, char* argv[])
{
    struct{
        char name[10];
        int number;
        float height;
    } student;
    
    student.number = 20;
    
    printf("%d \n", student.number);
}
