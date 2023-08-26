#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for start size
    int start_size;
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);

    // Prompt for end size
    int end_size;
    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < start_size);

    // Calculate long it takes to reach threshhold - in years
    int years = 0;
    int population = start_size;
    while (population < end_size)
    {
        int born = population / 3;
        int passedAway = population / 4;
        population = population + born - passedAway;
        years++;
    }

    // Print number of years
    printf("Years: %i\n", years);

    // Return 0 to show it executed successfully
    return 0;
}
