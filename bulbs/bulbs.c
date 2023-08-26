#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    string message = get_string("Message: ");
    int message_length = strlen(message);

    for (int i = 0; i < message_length; i++)
    {

        int ascii_value = (int) message[i];

        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            int bit = (ascii_value >> j) & 1; // Extract jth bit
            print_bulb(bit);
        }

        // Print a newline after each byte
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
