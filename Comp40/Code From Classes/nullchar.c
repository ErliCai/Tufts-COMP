//
//  nullchar.c
//  
//
//  Created by Erli Cai on 03/01/2021.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    
    char World[] = "World";
    
    World[1] = '\0';
    printf("%s %lu\n", World, strlen(World));
    
    World[3] = 'm';
    printf("%s %lu\n", World, strlen(World));
    
    World[1] = 'o';
    World[4] = '\0';
    printf("%s %lu\n", World, strlen(World));
}
