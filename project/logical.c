/*#include "shell.h"

// shell.c
#include "shell.h"

// ... (existing code)

int execute(char **args) {
    if (args[0] == NULL) {
        return 1;
    }

    int status = 1;  // Default status

    for (int i = 0; args[i] != NULL; i++) {
        if (strcmp(args[i], ";") == 0) {
            // Execute the current command
            if (status == 0) {
                status = 1; // Reset status
                continue;   // Skip command after unsuccessful command
            }
        } else if (strcmp(args[i], "&&") == 0) {
            // Execute the current command only if previous command was successful
            if (status == 1) {
                continue;   // Skip command after unsuccessful command
            }
        } else if (strcmp(args[i], "||") == 0) {
            // Execute the current command only if previous command was unsuccessful
            if (status == 0) {
                status = 1; // Reset status
                continue;   // Skip command after unsuccessful command
            }
        } else {
            // Execute regular command
            for (int j = 0; j < num_builtins(); j++) {
                if (strcmp(args[i], builtin_str[j]) == 0) {
                    status = (*builtin_func[j])(args + i);
                    break;
                }
            }
            if (status != 0) {
                status = execute_external_command(args + i);
            }
        }
    }

    return status;
}*/
