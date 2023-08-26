#include "shell.h"

#define BUFFER_SIZE 1024

static char buffer[BUFFER_SIZE];
static size_t buffer_pos = 0;
static size_t buffer_size = 0;

char *read_line()
{
    if (buffer_pos >= buffer_size)
    {
        buffer_size = read(STDIN_FILENO, buffer, BUFFER_SIZE);
        if (buffer_size <= 0)
        {
            return NULL;
        }
        buffer_pos = 0;
    }

    char *line = NULL;
    size_t line_size = 0;
    char *newline = memchr(buffer + buffer_pos, '\n', buffer_size - buffer_pos);
    if (newline != NULL)
    {
        line_size = newline - (buffer + buffer_pos) + 1;
    }
    else
    {
        line_size = buffer_size - buffer_pos;
    }

    line = (char *) malloc(line_size + 1);
    if (line == NULL)
    {
        perror("Allocation error");
        exit(EXIT_FAILURE);
    }

    strncpy(line, buffer + buffer_pos, line_size);
    line[line_size] = '\0';
    buffer_pos += line_size;

    return line;
}