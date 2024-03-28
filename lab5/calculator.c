#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define TEST_MODE_FILE "/tmp/.TEST_MODE_ENABLED"


int main(int argc, char **argv) {
    if (argc < 2) {
        puts("Please supply a Python expression as argument!\n");
        return 1;
    }
    setreuid(geteuid(), geteuid());
    char expr[1024];
    snprintf(expr, sizeof(expr), "import math; print(%s);", argv[1]);
    if (access(TEST_MODE_FILE, F_OK) == 0) {
        snprintf(expr, sizeof(expr), "import math; print(\"TEST MODE! Here's a PI:\", math.pi);");
    }
    char *const exec_args[] = {"python3", "-c", expr, 0};
    return execv("/usr/bin/python3", exec_args);
}

