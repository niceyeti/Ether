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
	char line[256];
    FILE *file = NULL;

	if(argc > 2){
		printf("Host received update %s: ",argv[0]);
		for(i = 2; i < argc; i++){
			printf("%s",argv[i]);
		}
		printf("\n");
	}

   file = fopen ("old.txt", "r" );
   if ( file != NULL )
   {
      while ( fgets ( line, sizeof line, file ) != NULL ){ /* read a line */
         fputs ( line, stdout ); /* write the line */
      }
      fclose ( file );
   }
	return 0;
}

