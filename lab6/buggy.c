#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void wanted(int a) {
	if (a == 0xcafebabe) {
		puts("well done, you're cool!");
	} else {
		puts("at least you tried");
	}
}

void copy() {
	char name[12];

	printf("what's ur last name?\n");
	gets(name);

	printf("bye\n");
}

int main(int argc, char **argv) {
  if (argc == 1) {
    puts("Usage: %s <name>\n");
    return 1;
  }
	char buf[] = "hey";

	printf("%s, %s\n", buf, argv[1]);
	copy();

  exit(0);
}