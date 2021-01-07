//
//  doublepointertest.c
//  
//
//  Created by Erli Cai on 06/01/2021.
//

#include <stdio.h>
#include "../Hanson/include/list.h"
typedef struct Car Car;

struct Car{
    char *name;
    int year;
};

int main(){
    
    Car mycar = {"Benz", 2018};
    Car *retrieved_car;
    
    List_T mylist = List_list(&mycar);
    List_pop(mylist, (void **) &retrieved_car);
    
    printf("%s\n", mycar.name);
}
