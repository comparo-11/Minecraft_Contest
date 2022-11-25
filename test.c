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
        // han = detectMobsDetail(1, han);
        ibuf = detectMobsAbout(1, ibuf);

        // printf("完了\n");
        // printf("%d\n", strlen(han));
        // printf("%c\n\n", han[0]);
        
        // for(int i=0; i < strlen(han); i++) {
        //     printf("%c", han[i]);
        // }
        printf("\n");
        printf("\n");
        // printf("%d", ibuf);
        for(int i=0; i < sizeof(ibuf)/4; i++) {
            printf("%d", ibuf[i] - '0');
        }
        printf("\n");
        sleep(5);
    }
}
