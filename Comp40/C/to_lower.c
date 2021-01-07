//
//  to_lower.c
//  
//
//  Created by Erli Cai on 23/12/2020.
//

#include "to_lower.h"
#include<stdio.h>
#include<ctype.h>
#include<stdlib.h>

char *str_lower(char *s)
{
    char *stemp = s;
    
    while (*stemp != '\0'){
        *stemp = tolower(*stemp);
        stemp++;
    }
    return s;
}

int main(int argc, char *argv[])
{
    char *oh = "oh";
    char hello[15] = "Hello";
    char there[] = "there";
    
    printf("%s, %s %s \n",
           oh, str_lower(hello), there);
    
    // line below will raise an error
    // printf("%s", str_lower(oh));
}
