#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include<time.h>
#include "control.h"

int main(int argc, char *argv){
    char *han;
    int *ibuf;
    /*
    int flag=0;
    init();
    setTime();
    exePython();
    setSurvival();*/
    init();
    exePython();

    while(rk){
        han = detectMobs(han, 1);

        // printf("完了\n");
        // printf("%d\n", strlen(han));
        // printf("%c\n\n", han[0]);
        
        for(int i=0; i < strlen(han); i++) {
            printf("%c", han[i]);
        }
        // for(int i=0; i < sizeof(ibuf) / sizeof(int); i++) {
        //     printf("%d", ibuf[i]);
        // }
        printf("\n");
        sleep(5);
    }
}
