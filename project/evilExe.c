#include <stdio.h>

/*
The evil, malicious hello file.

Note changing/re-compiling this file will screw up its hash on disk, if already stored.
*/
int main(int argc, char** argv)
{
	int i;

	printf("\tEvil executable running...\n");

	if(argc > 2){
		printf("Host received update %s: ",argv[0]);
		for(i = 2; i < argc; i++){
			printf("%s",argv[i]);
		}
		printf("\n");
	}

	return 0;
}

