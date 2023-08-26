#include "shell.h"

void prompt()
{
    printf(":) ");
    fflush(stdout);
}

char **split_line(char *line)
{
    char **args = NULL;
    char *arg = strtok(line, " \t\n");
    int i = 0;

    while (arg != NULL)
    {
        args = realloc(args, (i + 1) * sizeof(char *));
        if (args == NULL)
        {
            perror("Allocation error");
            exit(EXIT_FAILURE);
        }
        args[i] = arg;
        i++;
        arg = strtok(NULL, " \t\n");
    }

    args = realloc(args, (i + 1) * sizeof(char *));
    if (args == NULL)
    {
        perror("Allocation error");
        exit(EXIT_FAILURE);
    }
    args[i] = NULL;

    return args;
}

int execute(char **args)
{
    if (args[0] == NULL)
    {
        return 1;
    }

    for (int i = 0; i < num_builtins(); i++)
    {
        if (strcmp(args[0], builtin_str[i]) == 0)
        {
            return (*builtin_func[i])(args);
        }
    }

    pid_t pid, wpid;
    int status;

    pid = fork();
    if (pid == 0)
    {
        // Child process
        if (execvp(args[0], args) == -1)
        {
            perror("shell");
        }
        exit(EXIT_FAILURE);
    }
    else if (pid < 0)
    {
        perror("shell");
    }
    else
    {
        // Parent process
        do
        {
            wpid = waitpid(pid, &status, WUNTRACED);
        }
        while (!WIFEXITED(status) && !WIFSIGNALED(status));
    }

    return 1;
}
