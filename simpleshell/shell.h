#ifndef SHELL_H
#define SHELL_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

// Function declarations for shell.c
void prompt();
char *read_line();
char **split_line(char *line);
int execute(char **args);

// Function declarations for builtins.c
int shell_exit(char **args);
int shell_env(char **args);
int shell_setenv(char **args);
int shell_unsetenv(char **args);
int shell_cd(char **args);

// Array of built-in function names
extern const char *builtin_str[];
// Array of function pointers to built-in functions
extern int (*builtin_func[])(char **);
int num_builtins();

#endif /* SHELL_H */