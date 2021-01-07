//
//  CelsiusToFahrenheit.c
//  
//
//  Created by Erli Cai on 25/12/2020.
//

#include <stdio.h>

int main(){
    
    float celsius, fahrenheit;
    
    int lower = 0;
    int higher = 300;
    int step = 20;
    
    celsius = lower;
    while (celsius <= higher){
        fahrenheit = 9.0*celsius/5.0 +32.0;
        printf("%3.0f %6.0f\n", celsius, fahrenheit);
        celsius += 20;
    }

    return 0;
}
