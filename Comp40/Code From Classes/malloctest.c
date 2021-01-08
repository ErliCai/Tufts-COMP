//
//  malloctest.c
//  
//
//  Created by Erli Cai on 08/01/2021.
//

#include <stdio.h>
#include <stdlib.h>

#define SIZE 1000000

int main(int argc, char **argv)
{
    char *p;
    
    /* Attempt to allocate SIZE bytes of memory */
    p = malloc(SIZE);
    
    /* See if it worked */
    if (p == NULL) {
        fprintf(stderr, "Failed to malloc %d bytes of memory\n", SIZE);
        return EXIT_FAILURE;
    }
    
    fprintf(stderr, "Successfully allocate %d bits of memory at %p\n", SIZE, p);
    
    free(p);
    
    return EXIT_SUCCESS;
}
