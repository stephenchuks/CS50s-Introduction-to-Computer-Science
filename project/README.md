
# Simple Shell Project

![Simple Shell]
##Presentation
https://youtu.be/UomTdsg7shg

##About
This simple shell implementation is a part of my journey through Harvard University's CS50 Introduction to Computer Programming course. As part of this comprehensive course, I've undertaken various assigned projects, with the freedom to select a personal project for its completion. For my final project, I embarked on creating a minimalist version of the Linux Shell, known as a command-line interpreter.

##Motivation
The decision to develop this simple shell was motivated by my desire to deepen my understanding of fundamental programming concepts and system-level interactions. By building a shell, I aimed to gain insights into process management, user interaction, and the intricacies of managing commands and environment variables.


##Design Choices
Throughout the development process, I carefully considered several design choices:

Breadth vs. Depth: While I could have pursued more complex features, I chose to prioritize depth of understanding over breadth of functionality. This decision allowed me to gain a thorough comprehension of fundamental concepts.
Built-in Commands: The selection of built-in commands was influenced by their utility and relevance to the shell's purpose. Each command serves as an educational experience, demonstrating interactions with the system.
Environment Variables: The inclusion of environment variable management enhanced the project's realism and provided insights into system-level configuration.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Built-in Commands](#built-in-commands)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

## Description

The Simple Shell Project is a minimalistic shell that allows users to interact with their operating system through a command-line interface. It supports executing external programs, built-in commands, and environment variable management. The shell provides a straightforward way to navigate directories, execute programs, and manage environment variables.

## Features

- Display a prompt and wait for user input.
- Execute external commands and programs.
- Implement built-in commands: `exit`, `env`, `setenv`, `unsetenv`, and `cd`.
- Handle command lines with arguments.
- Support the `PATH` environment variable to locate executable programs.
- Handle the "end of file" condition (Ctrl+D).
- Change the current directory using the `cd` command.
- Update the `PWD` environment variable when changing directories.
- Simple and intuitive user interface.

## Getting Started

### Prerequisites

To run the Simple Shell Project, you need:

- A Unix-like terminal environment.
- GCC (GNU Compiler Collection) installed to compile the C code.

### Installation

1. Clone this repository to your local machine:


   git clone https://github.com/stephenchuks/project.git


2. Navigate to the project directory:


   cd simple-shell


3. Compile the source files:


   gcc -o shell main.c shell.c input.c builtins.c
   `

## Usage

### Basic Usage

To start the shell, run the compiled executable:

```sh
./shell
```

Once the shell is running, you can enter commands at the prompt and press Enter to execute them.

### Built-in Commands

The following built-in commands are supported:

- `exit [status]`: Exit the shell. Optional status can be an integer used to exit the shell.
- `env`: Print the current environment variables.
- `setenv VARIABLE VALUE`: Initialize or modify an environment variable.
- `unsetenv VARIABLE`: Remove an environment variable.
- `cd [DIRECTORY]`: Change the current directory. Use `cd -` to change to the previous directory.

## Contributing

Contributions to the Simple Shell Project are welcome! If you find any issues or want to suggest improvements, please open an issue or submit a pull request.

## Authors

- [Chuks Stephen](https://github.com/your-username)

## License

This project is licensed under the [MIT License](LICENSE).

