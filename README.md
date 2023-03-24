# DFA Password Validator

Created by Bhaskar Rijal.

This is a practice project for CSC257 Theory of Computation subject in my course.

## Description

This project is a password validator implemented using a deterministic finite automaton (DFA). A DFA is a mathematical model of computation that recognizes a regular language. In this project, we use a DFA to validate passwords based on certain rules.

The DFA password validator checks if a given password satisfies the following rules:

-   The password must be at least 8 characters long
-   The password must contain at least one uppercase letter, one lowercase letter, and one digit

## How it works

The password validator uses a DFA with several states to check if a given password satisfies the rules above. When given a password, the DFA reads each character of the password and transitions between states depending on the type of character. If the DFA reaches an accepting state at the end of the password, it means the password is valid according to the rules.

## How to use

To use the password validator, you can run the `main.c` file and input a password when prompted. The program will then check if the password is valid and output a message accordingly.

## References

-   [Deterministic Finite Automaton (DFA) - GeeksforGeeks](https://www.geeksforgeeks.org/deterministic-finite-automata-dfa/)
-   [Regular Expressions - Wikipedia](https://en.wikipedia.org/wiki/Regular_expression)