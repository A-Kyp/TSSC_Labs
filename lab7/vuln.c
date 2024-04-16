#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
 
void func(char *name)
{
    char buf[100];
    strcpy(buf, name);
    printf("Welcome %s\n", buf);
}
 
int main(int argc, char *argv[])
{
    setreuid(geteuid(), geteuid());
    func(argv[1]);
    return 0;
}