#include <stdio.h>

/*
The evil, malicious hello file.

Note changing/re-compiling this file will screw up its hash on disk, if already stored.
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

   file = fopen ("evil.txt", "r" );
   if ( file != NULL )
   {
      while ( fgets ( line, sizeof line, file ) != NULL ){ /* read a line */
         fputs ( line, stdout ); /* write the line */
      }
      fclose ( file );
   }

	return 0;
}

