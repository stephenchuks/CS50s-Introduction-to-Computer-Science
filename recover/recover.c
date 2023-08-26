#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // Check for correct command-line arguments
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s IMAGE\n", argv[0]);
        return 1;
    }

    // Open the forensic image file
    FILE *input_file = fopen(argv[1], "r");
    if (input_file == NULL)
    {
        fprintf(stderr, "Could not open %s for reading\n", argv[1]);
        return 1;
    }

    // Initialize variables
    unsigned char buffer[BLOCK_SIZE];
    int image_count = 0;
    FILE *output_file = NULL;

    // Read blocks and search for JPEG signatures
    while (fread(buffer, 1, BLOCK_SIZE, input_file) == BLOCK_SIZE)
    {
        // Check for JPEG signature
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close previous output file if open
            if (output_file != NULL)
            {
                fclose(output_file);
            }

            // Generate filename for new output file
            char filename[8]; // ###.jpg\0
            sprintf(filename, "%03d.jpg", image_count);
            image_count++;

            // Open new output file
            output_file = fopen(filename, "w");
            if (output_file == NULL)
            {
                fprintf(stderr, "Could not create %s\n", filename);
                fclose(input_file);
                return 1;
            }
        }

        // Write data to output file if open
        if (output_file != NULL)
        {
            fwrite(buffer, 1, BLOCK_SIZE, output_file);
        }
    }

    // Close files
    if (output_file != NULL)
    {
        fclose(output_file);
    }
    fclose(input_file);

    return 0;
}
