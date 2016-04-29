#include <stdio.h>

/*
	The example update file. This need not do anything, except
	report some correspondence with the hosts receiving them,
	for testing purposes.

	Input: a host name, number.

	Note that changing or recompiling this file will mess up its hash...
*/
int main(int argc, char** argv)
{
	int i;

	printf("\tOld hello\n");

	if(argc > 2){
		printf("Host received update %s: ",argv[0]);
		for(i = 2; i < argc; i++){
			printf("%s",argv[i]);
		}
		printf("\n");
	}

	return 0;
}

