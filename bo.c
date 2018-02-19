// Secure Coding
// Author: Robert Edstrom

// Description: Simple program that is vulnerable to a buffer overflow

#include <stdio.h>

int main(){
	char buff[20];

	printf("[*] Enter something: ");
	// Problem here... No bounds checking of user input
	scanf("%s", buff);
}
