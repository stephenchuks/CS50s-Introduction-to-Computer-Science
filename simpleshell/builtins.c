#include "shell.h"

int shell_exit(char **args) {
    if (args[1] != NULL) {
        int status = atoi(args[1]);
        exit(status);
    }
    return 0;
}

int shell_env(char **args) {
    extern char **environ;

    for (int i = 0; environ[i] != NULL; i++) {
        printf("%s\n", environ[i]);
    }

    return 1;
}

int shell_setenv(char **args) {
    if (args[1] == NULL || args[2] == NULL) {
        fprintf(stderr, "Usage: setenv VARIABLE VALUE\n");
    } else if (setenv(args[1], args[2], 1) != 0) {
        perror("setenv");
    }

    return 1;
}

int shell_unsetenv(char **args) {
    if (args[1] == NULL) {
        fprintf(stderr, "Usage: unsetenv VARIABLE\n");
    } else if (unsetenv(args[1]) != 0) {
        perror("unsetenv");
    }

    return 1;
}

int shell_cd(char **args) {
    if (args[1] == NULL || strcmp(args[1], "~") == 0) {
        if (chdir(getenv("HOME")) != 0) {
            perror("cd");
        }
    } else if (strcmp(args[1], "-") == 0) {
        if (chdir(getenv("OLDPWD")) != 0) {
            perror("cd");
        }
    } else {
        if (chdir(args[1]) != 0) {
            perror("cd");
        }
    }
    return 1;
}

const char *builtin_str[] = {
    "exit",
    "env",
    "setenv",
    "unsetenv",
    "cd"
};

int (*builtin_func[])(char **) = {
    &shell_exit,
    &shell_env,
    &shell_setenv,
    &shell_unsetenv,
    &shell_cd
};

int num_builtins() {
    return sizeof(builtin_str) / sizeof(char *);
}