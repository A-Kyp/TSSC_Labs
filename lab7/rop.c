#include <stdio.h>
 
void surprise(int b){
    if (b == 0x87654321) {
        puts("SURPRISE\n");
        system("/bin/sh");
    } else {
        puts("Surprise found, but the arg is not the right one!");
    }
}
 
void secret(int a){
    if (a == 0x12345678) {
		puts("Nice! Now, can you find the surprise?\n");
	} else {
		puts("Secret accessed, but the arg is not the right one!");
	}
}
 
void run(){
    char buf[32];
 
    printf("Tell me your name: ");
    fflush(stdout);
    fgets(buf, 128, stdin);
    printf("Hello, %s\n", buf);
 
}
 
int main(){
    run();
    return 0;
}