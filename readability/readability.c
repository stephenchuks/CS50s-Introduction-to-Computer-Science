#include <cs50.h>
#include <stdio.h>

int num_letters(string text);
int num_words(string text);
int num_sentences(string text);

int main(void)
{
    // Prompt the user for input text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences
    int letters = num_letters(text);
    int words = num_words(text);
    int sentences = num_sentences(text);

    // Calculate L and S for the Coleman-Liau index formula
    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;

    // Calculate the Coleman-Liau index
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // Round the index to the nearest integer
    int grade_level = (int) (index + 0.5);

    // Print the grade level result
    if (grade_level >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade_level < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade_level);
    }
}

int num_letters(string text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            count++;
        }
    }
    return count;
}

int num_words(string text)
{
    int count = 1; // Start with 1 because the first word is counted
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == ' ')
        {
            count++;
        }
    }
    return count;
}

int num_sentences(string text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    return count;
}
