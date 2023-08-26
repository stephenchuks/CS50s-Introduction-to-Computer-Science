#include "shell.h"

int main()
{
    char *line;
    char **args;
    int status;

    do
    {
        prompt();
        line = read_line();
        args = split_line(line);
        status = execute(args);

        free(line);
        free(args);
    }
    while (status);

    return 0;
}
