| How to | Think | Like | a Computer | Scientist |
| ------ | ----- | ---- | ---------- | --------- |
C Version
Thomas Scheffler
|     |     | based | on previous work | by Allen B. Downey |
| --- | --- | ----- | ---------------- | ------------------ |
Version 1.10
June 27th, 2019

2
| Copyright | (C) 1999 Allen  | B. Downey |     |
| --------- | --------------- | --------- | --- |
| Copyright | (C) 2009 Thomas | Scheffler |     |
Permission is granted to copy, distribute, transmit and adapt this work un-
der the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 Inter-
| national License: | https://creativecommons.org/licenses/by-nc/4.0/. |     |     |
| ----------------- | ------------------------------------------------ | --- | --- |
If you are interested in distributing a commercial version of this work, please
| contact the | author(s).      |               |                    |
| ----------- | --------------- | ------------- | ------------------ |
| The LATEX   | source and code | for this book | is available from: |
https://github.com/tscheffl/ThinkC

Contents
| 1 The | way | of the | program |     |     |     |     |     |     | 1   |
| ----- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
1.1 What is a programming language? . . . . . . . . . . . . . . . . . 1
1.2 What is a program? . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 What is debugging? . . . . . . . . . . . . . . . . . . . . . . . . . 3
|     | 1.3.1 | Compile-time |        | errors        | . .     | . . . . . . | . . . . | . . . . | . . . | . . 4 |
| --- | ----- | ------------ | ------ | ------------- | ------- | ----------- | ------- | ------- | ----- | ----- |
|     | 1.3.2 | Run-time     |        | errors .      | . . . . | . . . . . . | . . . . | . . . . | . . . | . . 4 |
|     | 1.3.3 | Logic        | errors | and semantics |         | . . . .     | . . . . | . . . . | . . . | . . 4 |
|     | 1.3.4 | Experimental |        | debugging     |         | . . . . . . | . . . . | . . . . | . . . | . . 5 |
1.4 Formal and natural languages . . . . . . . . . . . . . . . . . . . . 5
1.5 The first program . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.6 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.7 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
| 2 Variables |     | and | types |     |     |     |     |     |     | 13  |
| ----------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
2.1 More output. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.2 Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.3 Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.4 Assignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.5 Outputting variables . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.6 Keywords . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.7 Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.8 Order of operations . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.9 Operators for characters . . . . . . . . . . . . . . . . . . . . . . . 20

ii Contents
2.10 Composition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.11 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.12 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3 Function 25
3.1 Floating-point. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.2 Constants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.3 Converting from double to int . . . . . . . . . . . . . . . . . . . 27
3.4 Math functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.5 Composition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.6 Adding new functions . . . . . . . . . . . . . . . . . . . . . . . . 29
3.7 Definitions and uses . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.8 Programs with multiple functions . . . . . . . . . . . . . . . . . . 31
3.9 Parameters and arguments . . . . . . . . . . . . . . . . . . . . . 32
3.10 Parameters and variables are local . . . . . . . . . . . . . . . . . 33
3.11 Functions with multiple parameters. . . . . . . . . . . . . . . . . 34
3.12 Functions with results . . . . . . . . . . . . . . . . . . . . . . . . 34
3.13 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.14 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4 Conditionals and recursion 39
4.1 Conditional execution . . . . . . . . . . . . . . . . . . . . . . . . 39
4.2 The modulus operator . . . . . . . . . . . . . . . . . . . . . . . . 40
4.3 Alternative execution. . . . . . . . . . . . . . . . . . . . . . . . . 40
4.4 Chained conditionals . . . . . . . . . . . . . . . . . . . . . . . . . 41
4.5 Nested conditionals . . . . . . . . . . . . . . . . . . . . . . . . . . 41
4.6 The return statement . . . . . . . . . . . . . . . . . . . . . . . . 42
4.7 Recursion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
4.8 Infinite recursion . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.9 Stack diagrams for recursive functions . . . . . . . . . . . . . . . 45
4.10 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
4.11 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

Contents iii
5 Fruitful functions 49
5.1 Return values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
5.2 Program development . . . . . . . . . . . . . . . . . . . . . . . . 51
5.3 Composition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
5.4 Boolean values . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
5.5 Boolean variables . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
5.6 Logical operators . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
5.7 Bool functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
5.8 Returning from main() . . . . . . . . . . . . . . . . . . . . . . . 57
5.9 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
5.10 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
6 Iteration 63
6.1 Multiple assignment . . . . . . . . . . . . . . . . . . . . . . . . . 63
6.2 Iteration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
6.3 The while statement . . . . . . . . . . . . . . . . . . . . . . . . . 64
6.4 Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
6.5 Two-dimensional tables . . . . . . . . . . . . . . . . . . . . . . . 68
6.6 Encapsulation and generalization . . . . . . . . . . . . . . . . . . 68
6.7 Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
6.8 More encapsulation . . . . . . . . . . . . . . . . . . . . . . . . . . 70
6.9 Local variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
6.10 More generalization . . . . . . . . . . . . . . . . . . . . . . . . . 71
6.11 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
6.12 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
7 Arrays 77
7.1 Increment and decrement operators . . . . . . . . . . . . . . . . . 78
7.2 Accessing elements . . . . . . . . . . . . . . . . . . . . . . . . . . 78
7.3 Copying arrays . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
7.4 for loops . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80

iv Contents
7.5 Array length . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
7.6 Random numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
7.7 Statistics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
7.8 Array of random numbers . . . . . . . . . . . . . . . . . . . . . . 83
7.9 Passing an array to a function . . . . . . . . . . . . . . . . . . . . 84
7.10 Counting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
7.11 Checking the other values . . . . . . . . . . . . . . . . . . . . . . 85
7.12 A histogram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
7.13 A single-pass solution . . . . . . . . . . . . . . . . . . . . . . . . 87
7.14 Random seeds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
7.15 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
7.16 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
8 Strings and things 91
8.1 Containers for strings . . . . . . . . . . . . . . . . . . . . . . . . 91
8.2 String variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
8.3 Extracting characters from a string . . . . . . . . . . . . . . . . . 92
8.4 Length . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
8.5 Traversal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
8.6 Finding a character in a string . . . . . . . . . . . . . . . . . . 94
8.7 Pointers and Addresses. . . . . . . . . . . . . . . . . . . . . . . . 95
8.8 String concatenation . . . . . . . . . . . . . . . . . . . . . . . . . 96
8.9 Assigning new values to string variables . . . . . . . . . . . . . 96
8.10 strings are not comparable . . . . . . . . . . . . . . . . . . . . . 97
8.11 Character classification. . . . . . . . . . . . . . . . . . . . . . . . 98
8.12 Getting user input . . . . . . . . . . . . . . . . . . . . . . . . . . 99
8.13 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
8.14 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101

| Contents     |     | v   |
| ------------ | --- | --- |
| 9 Structures |     | 103 |
9.1 Compound values . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
9.2 Point objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
9.3 Accessing member variables . . . . . . . . . . . . . . . . . . . . . 104
9.4 Operations on structures . . . . . . . . . . . . . . . . . . . . . . . 105
9.5 Structures as parameters . . . . . . . . . . . . . . . . . . . . . . . 105
9.6 Call by value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
9.7 Call by reference . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
9.8 Rectangles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
9.9 Structures as return types . . . . . . . . . . . . . . . . . . . . . . 109
9.10 Passing other types by reference . . . . . . . . . . . . . . . . . . 110
9.11 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
9.12 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
| A Coding | Style | 113 |
| -------- | ----- | --- |
A.1 A short guide on style . . . . . . . . . . . . . . . . . . . . . . . . 113
A.2 Naming conventions and capitalization rules . . . . . . . . . . . . 114
A.3 Bracing style . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
A.4 Layout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
| B ASCII-Table |     | 117 |
| ------------- | --- | --- |

vi Contents

| Chapter | 1   |        |         |
| ------- | --- | ------ | ------- |
| The     | way | of the | program |
The goal of this book, and this class, is to teach you to think like a computer
scientist. Ilikethewaycomputerscientiststhinkbecausetheycombinesomeof
thebestfeaturesofMathematics,Engineering,andNaturalScience. Likemath-
ematicians, computer scientists use formal languages to denote ideas (specifi-
callycomputations). Likeengineers,theydesignthings,assemblingcomponents
into systems and evaluating tradeoffs among alternatives. Like scientists, they
observethebehaviorofcomplexsystems,formhypotheses,andtestpredictions.
The single most important skill for a computer scientist is problem-solving.
By that I mean the ability to formulate problems, think creatively about solu-
tions,andexpressasolutionclearlyandaccurately. Asitturnsout,theprocess
of learning to program is an excellent opportunity to practice problem-solving
| skills. That’s | why this | chapter is called | “The way of the program.” |
| -------------- | -------- | ----------------- | ------------------------- |
On one level, you will be learning to program, which is a useful skill by itself.
On another level you will use programming as a means to an end. As we go
| along, that | end will become | clearer.      |           |
| ----------- | --------------- | ------------- | --------- |
| 1.1         | What is         | a programming | language? |
The programming language you will be learning is C, which was developed in
the early 1970s by Dennis M. Ritchie at the Bell Laboratories. C is an example
of a high-level language; other high-level languages you might have heard of
| are Pascal, | C++ and | Java. |     |
| ----------- | ------- | ----- | --- |
Asyoumightinferfromthename“high-levellanguage,”therearealsolow-level
languages, sometimes referred to as machine language or assembly language.
Loosely-speaking, computers can only execute programs written in low-level
languages. Thus, programs written in a high-level language have to be trans-
lated before they can run. This translation takes some time, which is a small
| disadvantage | of high-level | languages. |     |
| ------------ | ------------- | ---------- | --- |

| 2   |     |     |     |     |     | The | way of the program |
| --- | --- | --- | --- | --- | --- | --- | ------------------ |
Buttheadvantagesareenormous. First, itismucheasiertoprograminahigh-
levellanguage;by“easier”Imeanthattheprogramtakeslesstimetowrite,it’s
shorter and easier to read, and it’s more likely to be correct. Secondly, high-
level languages are portable, meaning that they can run on different kinds of
computers with few or no modifications. Low-level programs can only run on
| one kind | of computer, |     | and have | to be rewritten |     | to run | on another. |
| -------- | ------------ | --- | -------- | --------------- | --- | ------ | ----------- |
Duetotheseadvantages,almostallprogramsarewritteninhigh-levellanguages.
| Low-level | languages | are | only used | for a | few special | applications. |     |
| --------- | --------- | --- | --------- | ----- | ----------- | ------------- | --- |
There are two ways to translate a program; interpreting or compiling. An
interpreter is a program that reads a high-level program and does what it says.
In effect, it translates the program line-by-line, alternately reading lines and
| carrying | out commands. |     |     |     |     |     |     |
| -------- | ------------- | --- | --- | --- | --- | --- | --- |
Source
Interpreter
Code
|     |     | The interpreter reads  |     |     |     | … and the result appears  |     |
| --- | --- | ---------------------- | --- | --- | --- | ------------------------- | --- |
|     |     | the source code        |     |     |     | on the screen.            |     |
A compiler is a program that reads a high-level program and translates it all at
once, before executing any of the commands. Often you compile the program
as a separate step, and then execute the compiled code later. In this case, the
high-level program is called the source code, and the translated program is
| called the | object | code | or the | executable. |     |     |     |
| ---------- | ------ | ---- | ------ | ----------- | --- | --- | --- |
Asanexample,supposeyouwriteaprograminC.Youmightuseatexteditorto
writetheprogram(atexteditorisasimplewordprocessor). Whentheprogram
is finished, you might save it in a file named program.c, where “program” is an
arbitrary name you make up, and the suffix .c is a convention that indicates
| that the | file contains | C   | source | code. |     |     |     |
| -------- | ------------- | --- | ------ | ----- | --- | --- | --- |
Then, depending on what your programming environment is like, you might
leave the text editor and run the compiler. The compiler would read your
sourcecode, translateit, andcreateanewfilenamedprogram.otocontainthe
| object code,        | or  | program.exe     | to  | contain                  | the executable. |          |                   |
| ------------------- | --- | --------------- | --- | ------------------------ | --------------- | -------- | ----------------- |
| Source              |     |                 |     | Object                   |                 |          |                   |
|                     |     | Compiler        |     |                          |                 | Executor |                   |
| Code                |     |                 |     | Code                     |                 |          |                   |
| The compiler reads  |     | … and generates |     | You execute the program  |                 |          | … and the result  |
the source code object code. (one way or another) appears on the screen.
Thenextstepistoruntheprogram,whichrequiressomekindofexecutor. The
roleoftheexecutoristoloadtheprogram(copyitfromdiskintomemory)and
| make the | computer | start | executing | the program. |     |     |     |
| -------- | -------- | ----- | --------- | ------------ | --- | --- | --- |

| 1.2 What | is a | program? |     |     |     | 3   |
| -------- | ---- | -------- | --- | --- | --- | --- |
Although this process may seem complicated, in most programming environ-
ments(sometimescalleddevelopmentenvironments),thesestepsareautomated
for you. Usually you will only have to write a program and press a button or
type a single command to compile and run it. On the other hand, it is useful
to know what the steps are that are happening in the background, so that if
| something | goes | wrong you | can figure | out what it is. |     |     |
| --------- | ---- | --------- | ---------- | --------------- | --- | --- |
| 1.2       | What | is a      | program?   |                 |     |     |
A program is a sequence of instructions that specifies how to perform a com-
putation. The computation might be something mathematical, like solving a
system of equations or finding the roots of a polynomial, but it can also be
a symbolic computation, like searching and replacing text in a document or
| (strangely | enough) | compiling | a program. |     |     |     |
| ---------- | ------- | --------- | ---------- | --- | --- | --- |
The instructions, which we will call statements, look different in different
programming languages, but there are a few basic operations most languages
can perform:
| input:  | Get data | from the | keyboard,  | or a file, or some | other device.           |     |
| ------- | -------- | -------- | ---------- | ------------------ | ----------------------- | --- |
| output: | Display  | data on  | the screen | or send data to    | a file or other device. |     |
math: Performbasicmathematicaloperationslikeadditionandmultiplication.
testing: Check for certain conditions and execute the appropriate sequence of
statements.
| repetition: | Perform | some | action repeatedly, | usually | with some variation. |     |
| ----------- | ------- | ---- | ------------------ | ------- | -------------------- | --- |
That’sprettymuchallthereistoit. Everyprogramyou’veeverused,nomatter
howcomplicated,ismadeupofstatementsthatperformtheseoperations. Thus,
onewaytodescribeprogrammingistheprocessofbreakingalarge,complextask
up into smaller and smaller subtasks until eventually the subtasks are simple
| enough | to be performed |               | with one of | these basic operations. |     |     |
| ------ | --------------- | ------------- | ----------- | ----------------------- | --- | --- |
| 1.3    | What            | is debugging? |             |                         |     |     |
Programmingisacomplexprocess,andsinceitisdonebyhumanbeings,itoften
leadstoerrors. Forwhimsicalreasons,programmingerrorsarecalledbugsand
the process of tracking them down and correcting them is called debugging.
There are a few different kinds of errors that can occur in a program, and it is
useful to distinguish between them in order to track them down more quickly.

| 4     |              |     |        |     | The way | of the program |
| ----- | ------------ | --- | ------ | --- | ------- | -------------- |
| 1.3.1 | Compile-time |     | errors |     |         |                |
The compiler can only translate a program if the program is syntactically cor-
rect; otherwise, the compilation fails and you will not be able to run your
program. Syntax refers to the structure of your program and the rules about
that structure.
For example, in English, a sentence must begin with a capital letter and end
| with a | period. this sentence |     | contains a | syntax | error. So does | this one |
| ------ | --------------------- | --- | ---------- | ------ | -------------- | -------- |
Formostreaders,afewsyntaxerrorsarenotasignificantproblem,whichiswhy
we can read the poetry of E. E. Cummings without spewing error messages.
Compilers are not so forgiving. If there is a single syntax error anywhere in
your program, the compiler will print an error message and quit, and you will
| not be | able to run your | program. |     |     |     |     |
| ------ | ---------------- | -------- | --- | --- | --- | --- |
To make matters worse, there are more syntax rules in C than there are in
English, and the error messages you get from the compiler are often not very
helpful. During the first few weeks of your programming career, you will prob-
ably spend a lot of time tracking down syntax errors. As you gain experience,
| though, | you will make | fewer  | errors and | find them | faster. |     |
| ------- | ------------- | ------ | ---------- | --------- | ------- | --- |
| 1.3.2   | Run-time      | errors |            |           |         |     |
The second type of error is a run-time error, so-called because the error does
| not appear | until you | run the | program. |     |     |     |
| ---------- | --------- | ------- | -------- | --- | --- | --- |
Cisnotasafelanguage,suchasJava,whererun-timeerrorsarerare. Program-
ming in C allows you to get very close to the actual computing hardware. Most
run-time errors C occur because the language provides no protection against
| the accessing | or overwriting |     | of data in | memory. |     |     |
| ------------- | -------------- | --- | ---------- | ------- | --- | --- |
For the simple sorts of programs we will be writing for the next few weeks,
run-time errors are rare, so it might be a little while before you encounter one.
| 1.3.3 | Logic errors | and | semantics |     |     |     |
| ----- | ------------ | --- | --------- | --- | --- | --- |
The third type of error is the logical or semantic error. If there is a logical
error in your program, it will compile and run successfully, in the sense that
the computer will not generate any error messages, but it will not do the right
thing. It will do something else. Specifically, it will do what you told it to do.
The problem is that the program you wrote is not the program you wanted to
write. Themeaning oftheprogram(itssemantics)iswrong. Identifyinglogical
errors can be tricky, since it requires you to work backwards by looking at the
| output | of the program | and trying | to figure | out | what it is | doing. |
| ------ | -------------- | ---------- | --------- | --- | ---------- | ------ |

| 1.4 Formal | and          | natural | languages |     |     |     | 5   |
| ---------- | ------------ | ------- | --------- | --- | --- | --- | --- |
| 1.3.4      | Experimental |         | debugging |     |     |     |     |
One of the most important skills you will acquire in this class is debugging.
Although it can be frustrating, debugging is one of the most intellectually rich,
| challenging, | and | interesting | parts | of programming. |     |     |     |
| ------------ | --- | ----------- | ----- | --------------- | --- | --- | --- |
In some ways debugging is like detective work. You are confronted with clues
and you have to infer the processes and events that lead to the results you see.
Debugging is also like an experimental science. Once you have an idea what
is going wrong, you modify your program and try again. If your hypothesis
was correct, then you can predict the result of the modification, and you take
a step closer to a working program. If your hypothesis was wrong, you have to
come up with a new one. As Sherlock Holmes pointed out, “When you have
eliminated the impossible, whatever remains, however improbable, must be the
| truth.” | (from A. | Conan | Doyle’s | The Sign | of Four). |     |     |
| ------- | -------- | ----- | ------- | -------- | --------- | --- | --- |
For some people, programming and debugging are the same thing. That is,
programmingistheprocessofgraduallydebuggingaprogramuntilitdoeswhat
you want. The idea is that you should always start with a working program
that does something, and make small modifications, debugging them as you go,
| so that | you always | have | a working | program. |     |     |     |
| ------- | ---------- | ---- | --------- | -------- | --- | --- | --- |
For example, Linux is an operating system that contains thousands of lines of
code, but it started out as a simple program Linus Torvalds used to explore
the Intel 80386 chip. According to Larry Greenfield, “One of Linus’s earlier
projects was a program that would switch between printing AAAA and BBBB.
This later evolved to Linux” (from The Linux Users’ Guide Beta Version 1).
In later chapters I will make more suggestions about debugging and other pro-
| gramming | practices. |     |         |     |           |     |     |
| -------- | ---------- | --- | ------- | --- | --------- | --- | --- |
| 1.4      | Formal     | and | natural |     | languages |     |     |
Natural languagesarethelanguagesthatpeoplespeak,likeEnglish,Spanish,
and French. They were not designed by people (although people try to impose
| some order | on them); | they | evolved | naturally. |     |     |     |
| ---------- | --------- | ---- | ------- | ---------- | --- | --- | --- |
Formal languagesarelanguagesthataredesignedbypeopleforspecificappli-
cations. Forexample,thenotationthatmathematiciansuseisaformallanguage
thatisparticularlygoodatdenotingrelationshipsamongnumbersandsymbols.
Chemistsuseaformallanguagetorepresentthechemicalstructureofmolecules.
| And most    | importantly: |     |           |               |                  |           |     |
| ----------- | ------------ | --- | --------- | ------------- | ---------------- | --------- | --- |
| Programming |              |     | languages | are           | formal languages | that have |     |
| been        | designed     | to  | express   | computations. |                  |           |     |
As I mentioned before, formal languages tend to have strict rules about syntax.
For example, 3+3 = 6 is a syntactically correct mathematical statement, but

| 6   |     |     |     |     |     |     | The way | of the | program |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ------- |
3=+6$ is not. Also, H O is a syntactically correct chemical name, but Zz is
|     |     |     | 2   |     |     |     |     |     | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
not.
Syntax rules come in two flavors, pertaining to tokens and structure. Tokens
are the basic elements of the language, like words and numbers and chemical
elements. One of the problems with 3=+6$ is that $ is not a legal token in
mathematics (at least as far as I know). Similarly, 2 Zz is not legal because
| there is no | element | with | the | abbreviation | Zz. |     |     |     |     |
| ----------- | ------- | ---- | --- | ------------ | --- | --- | --- | --- | --- |
Thesecondtypeofsyntaxrulepertainstothestructureofastatement; thatis,
the way the tokens are arranged. The statement 3=+6$ is structurally illegal,
because you can’t have a plus sign immediately after an equals sign. Similarly,
molecular formulas have to have subscripts after the element name, not before.
When you read a sentence in English or a statement in a formal language, you
have to figure out what the structure of the sentence is (although in a natural
| language | you do | this unconsciously). |     |     | This | process | is called parsing. |     |     |
| -------- | ------ | -------------------- | --- | --- | ---- | ------- | ------------------ | --- | --- |
Forexample,whenyouhearthesentence,“Theothershoefell,”youunderstand
that“theothershoe”isthesubjectand“fell”istheverb. Onceyouhaveparsed
a sentence, you can figure out what it means, that is, the semantics of the
sentence. Assuming that you know what a shoe is, and what it means to fall,
| you will understand |     | the | general | implication |     | of this | sentence. |     |     |
| ------------------- | --- | --- | ------- | ----------- | --- | ------- | --------- | --- | --- |
Althoughformalandnaturallanguageshavemanyfeaturesincommon—tokens,
| structure, | syntax | and | semantics—there |     | are | many differences. |     |     |     |
| ---------- | ------ | --- | --------------- | --- | --- | ----------------- | --- | --- | --- |
ambiguity: Natural languages are full of ambiguity, which people deal with
| by using  |     | contextual  | clues | and           | other        | information. | Formal      | languages | are      |
| --------- | --- | ----------- | ----- | ------------- | ------------ | ------------ | ----------- | --------- | -------- |
| designed  | to  | be nearly   |       | or completely | unambiguous, |              | which       | means     | that any |
| statement |     | has exactly |       | one meaning,  | regardless   |              | of context. |           |          |
redundancy: In order to make up for ambiguity and reduce misunderstand-
| ings, | natural  | languages |     | employ    | lots of  | redundancy. | As  | a result, | they are |
| ----- | -------- | --------- | --- | --------- | -------- | ----------- | --- | --------- | -------- |
| often | verbose. | Formal    |     | languages | are less | redundant   | and | more      | concise. |
literalness: Natural languages are full of idiom and metaphor. If I say, “The
| other     | shoe | fell,” | there   | is probably | no        | shoe and | nothing | falling. | Formal |
| --------- | ---- | ------ | ------- | ----------- | --------- | -------- | ------- | -------- | ------ |
| languages |      | mean   | exactly | what        | they say. |          |         |          |        |
People who grow up speaking a natural language (everyone) often have a hard
timeadjustingtoformallanguages. Insomewaysthedifferencebetweenformal
and natural language is like the difference between poetry and prose, but more
so:
Poetry: Words are used for their sounds as well as for their meaning, and the
| whole  | poem | together | creates |       | an effect   | or emotional | response. |     | Ambiguity |
| ------ | ---- | -------- | ------- | ----- | ----------- | ------------ | --------- | --- | --------- |
| is not | only | common   | but     | often | deliberate. |              |           |     |           |
Prose: The literal meaning of words is more important and the structure con-
| tributes | more        | meaning.   |     | Prose | is more | amenable | to analysis |     | than poetry, |
| -------- | ----------- | ---------- | --- | ----- | ------- | -------- | ----------- | --- | ------------ |
| but      | still often | ambiguous. |     |       |         |          |             |     |              |

| 1.5 The | first program |     |     |     |     | 7   |
| ------- | ------------- | --- | --- | --- | --- | --- |
Programs: The meaning of a computer program is unambiguous and literal,
| and | can be understood | entirely | by analysis | of the tokens | and structure. |     |
| --- | ----------------- | -------- | ----------- | ------------- | -------------- | --- |
Here are some suggestions for reading programs (and other formal languages).
First, remember that formal languages are much more dense than natural lan-
guages,soittakeslongertoreadthem. Also,thestructureisveryimportant,so
it is usually not a good idea to read from top to bottom, left to right. Instead,
learn to parse the program in your head, identifying the tokens and interpret-
ing the structure. Finally, remember that the details matter. Little things like
spelling errors and bad punctuation, which you can get away with in natural
| languages, | can make  | a big difference | in a formal | language. |     |     |
| ---------- | --------- | ---------------- | ----------- | --------- | --- | --- |
| 1.5        | The first | program          |             |           |     |     |
Traditionally the first program people write in a new language is called “Hello,
World.” because all it does is display the words “Hello, World.” In C, this
| program  | looks like this: |             |        |     |     |     |
| -------- | ---------------- | ----------- | ------ | --- | --- | --- |
| #include | <stdio.h>        |             |        |     |     |     |
| #include | <stdlib.h>       |             |        |     |     |     |
| /* main: | generate         | some simple | output | */  |     |     |
int main(void)
{
|     | printf("Hello, | World.\n"); |     |     |     |     |
| --- | -------------- | ----------- | --- | --- | --- | --- |
return(EXIT_SUCCESS);
}
Some people judge the quality of a programming language by the simplicity of
the “Hello, World.” program. By this standard, C does reasonably well. Even
so, this simple program contains several features that are hard to explain to
beginning programmers. For now, we will ignore some of them, like the first
two lines.
The third line begins with /* and ends with */, which indicates that it is a
comment. A comment is a bit of English text that you can put in the middle
of a program, usually to explain what the program does. When the compiler
sees a /*, it ignores everything from there until it finds the corresponding */.
Intheforthline,younoticethewordmain. mainisaspecialnamethatindicates
the place in the program where execution begins. When the program runs, it
starts by executing the first statement in main() and it continues, in order,
| until it gets | to the last | statement, | and then | it quits. |     |     |
| ------------- | ----------- | ---------- | -------- | --------- | --- | --- |
There is no limit to the number of statements that can be in main(), but the
example contains only two. The first is an output statement, meaning that

| 8   |     |     |     |     | The way | of the | program |
| --- | --- | --- | --- | --- | ------- | ------ | ------- |
it displays or prints a message on the screen. The second statement tells the
| operating | system that our | program | executed | successfully. |     |     |     |
| --------- | --------------- | ------- | -------- | ------------- | --- | --- | --- |
The statement that prints things on the screen is printf(), and the characters
between the quotation marks will get printed. Notice the \n after the last
character. This is a special character called newline that is appended at the
endofalineoftextandcausesthecursortomovetothenextlineofthedisplay.
Thenexttimeyououtputsomething,thenewtextappearsonthenextline. At
the end of the statement there is a semicolon (;), which is required at the end
of every statement.
Thereareafewotherthingsyoushouldnoticeaboutthesyntaxofthisprogram.
First,Cusescurly-brackets({and})togroupthingstogether. Inthiscase,the
output statement is enclosed in curly-brackets, indicating that it is inside the
definition of main(). Also, notice that the statement is indented, which helps
| to show visually | which | lines are | inside | the definition. |     |     |     |
| ---------------- | ----- | --------- | ------ | --------------- | --- | --- | --- |
At this point it would be a good idea to sit down in front of a computer and
compile and run this program. The details of how to do that depend on your
| programming | environment, | this | book assumes |     | that you know | how | to do it. |
| ----------- | ------------ | ---- | ------------ | --- | ------------- | --- | --------- |
As I mentioned, the C compiler is very pedantic with syntax. If you make
any errors when you type in the program, chances are that it will not compile
successfully. For example, if you misspell stdio.h, you might get an error
| message like        | the following: |        |          |     |              |     |           |
| ------------------- | -------------- | ------ | -------- | --- | ------------ | --- | --------- |
| hello_world.c:1:19: |                | error: | sdtio.h: |     | No such file | or  | directory |
There is a lot of information on this line, but it is presented in a dense format
that is not easy to interpret. A more friendly compiler might say something
like:
| “On                             | line 1 of the   | source code    | file | named                       | hello_world.c, | you       | tried to |
| ------------------------------- | --------------- | -------------- | ---- | --------------------------- | -------------- | --------- | -------- |
| includeaheaderfilenamedsdtio.h. |                 |                |      | Ididn’tfindanythingwiththat |                |           |          |
| name,                           | but I did       | find something |      | named                       | stdio.h. Is    | that what | you      |
| meant,                          | by any chance?” |                |      |                             |                |           |          |
Unfortunately, few compilers are so accommodating. The compiler is not really
very smart, and in most cases the error message you get will be only a hint
about what is wrong. It will take some time for you to learn to interpret
| different compiler | messages. |     |     |     |     |     |     |
| ------------------ | --------- | --- | --- | --- | --- | --- | --- |
Nevertheless, the compiler can be a useful tool for learning the syntax rules
of a language. Starting with a working program (like hello_world.c), modify
it in various ways and see what happens. If you get an error message, try to
remember what the message says and what caused it, so if you see it again in
| the future | you will know | what | it means. |     |     |     |     |
| ---------- | ------------- | ---- | --------- | --- | --- | --- | --- |
1.6 Glossary
problem-solving: The process of formulating a problem, finding a solution,
| and | expressing the | solution. |     |     |     |     |     |
| --- | -------------- | --------- | --- | --- | --- | --- | --- |

| 1.6 Glossary |     |     |     |     |     |     |     |     | 9   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
high-level language: A programming language like C that is designed to be
| easy | for | humans | to read | and | write. |     |     |     |     |
| ---- | --- | ------ | ------- | --- | ------ | --- | --- | --- | --- |
low-level language: A programming language that is designed to be easy for
| a computer |     | to  | execute. | Also | called | “machine | language” | or “assembly |     |
| ---------- | --- | --- | -------- | ---- | ------ | -------- | --------- | ------------ | --- |
language.”
formal language: Any of the languages people have designed for specific pur-
| poses,      | like | representing |     | mathematical |     | ideas or   | computer | programs. | All |
| ----------- | ---- | ------------ | --- | ------------ | --- | ---------- | -------- | --------- | --- |
| programming |      | languages    |     | are formal   |     | languages. |          |           |     |
natural language: Any of the languages people speak that have evolved nat-
urally.
portability: A property of a program that can run on more than one kind of
computer.
interpret: To execute a program in a high-level language by translating it one
| line | at a | time. |     |     |     |     |     |     |     |
| ---- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
compile: To translate a program in a high-level language into a low-level lan-
| guage,       | all     | at once,   | in   | preparation      | for  | later execution.  |              |              |     |
| ------------ | ------- | ---------- | ---- | ---------------- | ---- | ----------------- | ------------ | ------------ | --- |
| source code: |         | A program  |      | in a high-level  |      | language,         | before being | compiled.    |     |
| object code: |         | The output |      | of the compiler, |      | after translating |              | the program. |     |
| executable:  | Another |            | name | for object       | code | that is           | ready to     | be executed. |     |
statement: Apartofaprogramthatspecifiesanactionthatwillbeperformed
| when | the         | program | runs. | A print | statement | causes | output | to be displayed |     |
| ---- | ----------- | ------- | ----- | ------- | --------- | ------ | ------ | --------------- | --- |
| on   | the screen. |         |       |         |           |        |        |                 |     |
comment: A part of a program that contains information about the program,
| but        | that          | has no        | effect    | when the      | program | runs.         |              |     |     |
| ---------- | ------------- | ------------- | --------- | ------------- | ------- | ------------- | ------------ | --- | --- |
| algorithm: | A             | general       | process   | for           | solving | a category    | of problems. |     |     |
| bug: An    | error         | in a program. |           |               |         |               |              |     |     |
| syntax:    | The structure |               | of a      | program.      |         |               |              |     |     |
| semantics: | The           | meaning       |           | of a program. |         |               |              |     |     |
| parse: To  | examine       |               | a program | and           | analyze | the syntactic | structure.   |     |     |
syntax error: An error in a program that makes it impossible to parse (and
| therefore |     | impossible | to  | compile). |     |     |     |     |     |
| --------- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- |
logical error: An error in a program that makes it do something other than
| what | the | programmer |     | intended. |     |     |     |     |     |
| ---- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- |
debugging: The process of finding and removing any of the three kinds of
errors.

| 10  |     |     |     |     |     | The | way | of the | program |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- |
1.7 Exercises
| Exercise | 1.1 |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ComputerscientistshavetheannoyinghabitofusingcommonEnglishwordstomean
something different from their common English meaning. For example, in English, a
statement and a comment are pretty much the same thing, but when we are talking
| about a | program, they | are very | different. |     |     |     |     |     |     |
| ------- | ------------- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
The glossary at the end of each chapter is intended to highlight words and phrases
that have special meanings in computer science. When you see familiar words, don’t
| assume | that you know | what | they mean! |     |     |     |     |     |     |
| ------ | ------------- | ---- | ---------- | --- | --- | --- | --- | --- | --- |
a. Incomputerjargon,what’sthedifferencebetweenastatementandacomment?
| b. What  | does it mean      | to  | say that | a program | is  | portable? |     |     |     |
| -------- | ----------------- | --- | -------- | --------- | --- | --------- | --- | --- | --- |
| c. What  | is an executable? |     |          |           |     |           |     |     |     |
| Exercise | 1.2               |     |          |           |     |           |     |     |     |
Before you do anything else, find out how to compile and run a C program in your
environment. Some environments provide sample programs similar to the example in
Section 1.5.
| a. Type | in the “Hello | World” | program, | then | compile |     | and run | it. |     |
| ------- | ------------- | ------ | -------- | ---- | ------- | --- | ------- | --- | --- |
b. Add a second print statement that prints a second message after the “Hello
| World.”. | Something | witty | like, | “How | are you?” | Compile | and | run | the program |
| -------- | --------- | ----- | ----- | ---- | --------- | ------- | --- | --- | ----------- |
again.
c. Addacommentlinetotheprogram(anywhere)andrecompileit. Runthepro-
| gram | again. Thenew |     | commentshould |     | not affect | the | executionof |     | the program. |
| ---- | ------------- | --- | ------------- | --- | ---------- | --- | ----------- | --- | ------------ |
This exercise may seem trivial, but it is the starting place for many of the programs
we will work with. In order to debug with confidence, you have to have confidence
in your programming environment. In some environments, it is easy to lose track of
whichprogramisexecuting,andyoumightfindyourselftryingtodebugoneprogram
whileyouareaccidentallyexecutinganother. Adding(andchanging)printstatements
is a simple way to establish the connection between the program you are looking at
| and the  | output when | the program | runs. |     |     |     |     |     |     |
| -------- | ----------- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
| Exercise | 1.3         |             |       |     |     |     |     |     |     |
It is a good idea to commit as many errors as you can think of, so that you see what
error messages the compiler produces. Sometimes the compiler will tell you exactly
what is wrong, and all you have to do is fix it. Sometimes, though, the compiler will
produce wildly misleading messages. You will develop a sense for when you can trust
| the compiler | and when    | you           | have to | figure things | out | yourself. |     |     |     |
| ------------ | ----------- | ------------- | ------- | ------------- | --- | --------- | --- | --- | --- |
| a. Remove    | the closing | curly-bracket |         | (}).          |     |           |     |     |     |
| b. Remove    | the opening | curly-bracket |         | ({).          |     |           |     |     |     |
| c. Remove    | the int     | before        | main.   |               |     |           |     |     |     |

1.7 Exercises 11
| d. Instead | of main, write          | mian.           |                   |
| ---------- | ----------------------- | --------------- | ----------------- |
| e. Remove  | the closing */          | from a comment. |                   |
| f. Replace | printf with pintf.      |                 |                   |
| g. Delete  | one of the parentheses: | ( or ).         | Add an extra one. |
| h. Delete  | the semicolon after     | the             | statement.        |
return

| 12  | The way | of the program |
| --- | ------- | -------------- |

| Chapter   |             | 2   |       |     |     |     |
| --------- | ----------- | --- | ----- | --- | --- | --- |
| Variables |             | and | types |     |     |     |
| 2.1       | More output |     |       |     |     |     |
AsImentionedinthelastchapter,youcanputasmanystatementsasyouwant
| in main(). | For example,   | to output   | more than | one line: |     |     |
| ---------- | -------------- | ----------- | --------- | --------- | --- | --- |
| #include   | <stdio.h>      |             |           |           |     |     |
| #include   | <stdlib.h>     |             |           |           |     |     |
| /*         | main: generate | some simple | output    | */        |     |     |
| int        | main (void)    |             |           |           |     |     |
{
|     | printf ("Hello | World.\n");   |     | /* output | one line */  |     |
| --- | -------------- | ------------- | --- | --------- | ------------ | --- |
|     | printf ("How   | are you?\n"); |     | /* output | another line | */  |
return (EXIT_SUCCESS);
}
As you can see, it is legal to put comments at the end of a line, as well as on a
line by themselves.
The phrases that appear in quotation marks are called strings, because they
are made up of a sequence (string) of letters. Actually, strings can contain any
combination of letters, numbers, punctuation marks, and other special charac-
ters.
Often it is useful to display the output from multiple output statements all on
| one line. | You can do  | this by leaving | out the | \n from the | first printf: |     |
| --------- | ----------- | --------------- | ------- | ----------- | ------------- | --- |
| int       | main (void) |                 |         |             |               |     |
{
|     | printf ("Goodbye, | ");         |     |     |     |     |
| --- | ----------------- | ----------- | --- | --- | --- | --- |
|     | printf ("cruel    | world!\n"); |     |     |     |     |

| 14  |     |     |     | Variables and | types |
| --- | --- | --- | --- | ------------- | ----- |
return (EXIT_SUCCESS);
}
In this case the output appears on a single line as Goodbye, cruel world!.
Notice that there is a space between the word “Goodbye,” and the second quo-
tation mark. This space appears in the output, so it affects the behavior of the
program.
Spaces that appear outside of quotation marks generally do not affect the be-
| havior of | the program. | For example, | I could have written: |     |     |
| --------- | ------------ | ------------ | --------------------- | --- | --- |
int main(void)
{
| printf("Goodbye, |             | "); |     |     |     |
| ---------------- | ----------- | --- | --- | --- | --- |
| printf("cruel    | world!\n"); |     |     |     |     |
return(EXIT_SUCCESS);
}
This program would compile and run just as well as the original. The breaks
at the ends of lines (newlines) do not affect the program’s behavior either, so I
| could have                      | written: |     |                  |             |     |
| ------------------------------- | -------- | --- | ---------------- | ----------- | --- |
| int main(void){printf("Goodbye, |          |     | ");printf("cruel | world!\n"); |     |
return(EXIT_SUCCESS);}
That would work, too, although you have probably noticed that the program is
gettingharderandhardertoread. Newlinesandspacesareusefulfororganizing
your program visually, making it easier to read the program and locate syntax
errors.
2.2 Values
Computer programs operate on values stored in computer memory. A value
—like a letter or a number— is one of the fundamental things that a program
manipulates. Theonlyvalueswehavemanipulatedsofararethestringswehave
been outputting, like "Hello, world.". You (and the compiler) can identify
| these string | values because | they are | enclosed in quotation | marks. |     |
| ------------ | -------------- | -------- | --------------------- | ------ | --- |
There are different kinds of values, including integers and characters. It is im-
portant for the program to know exactly what kind of value is manipulated
because not all manipulations will make sense on all values. We therefore dis-
| tinguish | between different | types of values. |     |     |     |
| -------- | ----------------- | ---------------- | --- | --- | --- |
An integer is a whole number like 1 or 17. You can output integer values in a
| similar way    | as you output | strings: |     |     |     |
| -------------- | ------------- | -------- | --- | --- | --- |
| printf("%i\n", | 17);          |          |     |     |     |
When we look at the printf() statement more closely, we notice that the
value we are outputting no longer appears inside the quotes, but behind them
separated by comma. The string is still there, but now contains a %i instead
of any text. The %i a placeholder that tells the printf() command to print

| 2.3 Variables |     |     |     |     |     |     |     | 15  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
an integer value. Several such placeholders exist for different data types and
| formatting | options | of  | the output. | We  | will see the | next | one just now. |     |
| ---------- | ------- | --- | ----------- | --- | ------------ | ---- | ------------- | --- |
A character value is a letter or digit or punctuation mark enclosed in single
| quotes,        | like ’a’ | or ’5’. | You   | can output | character | values | in a similar | way: |
| -------------- | -------- | ------- | ----- | ---------- | --------- | ------ | ------------ | ---- |
| printf("%c\n", |          |         | ’}’); |            |           |        |              |      |
This example outputs a single closing curly-bracket on a line by itself. It uses
| the %c | placeholder | to  | signify | the output | of a character |     | value. |     |
| ------ | ----------- | --- | ------- | ---------- | -------------- | --- | ------ | --- |
Itiseasytoconfusedifferenttypesofvalues,like"5",’5’and5,butifyoupay
attention to the punctuation, it should be clear that the first is a string, the
second is a character and the third is an integer. The reason this distinction is
| important | should | become | clear | soon. |     |     |     |     |
| --------- | ------ | ------ | ----- | ----- | --- | --- | --- | --- |
2.3 Variables
One of the most powerful features of a programming language is the ability to
manipulatevaluesthroughtheuseofvariables. Sofarthevaluesthatwehave
used in our statements where fixed to what was written in the statement. Now
| we will | use a | variable | as a named | location | that | stores | a value. |     |
| ------- | ----- | -------- | ---------- | -------- | ---- | ------ | -------- | --- |
Just as there are different types of values (integer, character, etc.), there are
differenttypesofvariables. Whenyoucreateanewvariable,youhavetodeclare
what type it is. For example, the character type in C is called char. The
following statement creates a new variable named fred that has type char.
| char      | fred;        |     |           |                |     |     |     |     |
| --------- | ------------ | --- | --------- | -------------- | --- | --- | --- | --- |
| This kind | of statement |     | is called | a declaration. |     |     |     |     |
The type of a variable determines what kind of values it can store. A char
variable can contain characters, and it should come as no surprise that int
| variables | can | store integers. |     |     |     |     |     |     |
| --------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
Contrarytootherprogramminglanguages,Cdoesnothaveadedicatedvariable
type for the storage of string values. We will see in a later chapter how string
| values are | stored     | in  | C.        |            |     |     |     |     |
| ---------- | ---------- | --- | --------- | ---------- | --- | --- | --- | --- |
| To create  | an integer |     | variable, | the syntax | is  |     |     |     |
| int        | bob;       |     |           |            |     |     |     |     |
where bob is the arbitrary name you choose to identify the variable. In general,
youwillwanttomakeupvariablenamesthatindicatewhatyouplantodowith
| the variable. | For           | example, | if  | you saw | these variable | declarations: |     |     |
| ------------- | ------------- | -------- | --- | ------- | -------------- | ------------- | --- | --- |
| char          | first_letter; |          |     |         |                |               |     |     |
| char          | last_letter;  |          |     |         |                |               |     |     |
| int           | hour,         | minute;  |     |         |                |               |     |     |
you could probably make a good guess at what values would be stored in them.
Thisexamplealsodemonstratesthesyntaxfordeclaringmultiplevariableswith
| the same | type: | hour | and minute | are | both integers | (int | type). |     |
| -------- | ----- | ---- | ---------- | --- | ------------- | ---- | ------ | --- |

| 16  |     |     |     |     |     | Variables |     | and types |
| --- | --- | --- | --- | --- | --- | --------- | --- | --------- |
ATTENTION: The older C89 standard allows variable declarations only at the
beginningofablockofcode. Itisthereforenecessarytoputvariabledeclarations
beforeanyotherstatements,evenifthevariableitselfisonlyneededmuchlater
in your program.
2.4 Assignment
Nowthatwehavecreatedsomevariables,wewouldliketostorevaluesinthem.
| We do that   | with  | an assignment |      | statement. |              |          |         |        |
| ------------ | ----- | ------------- | ---- | ---------- | ------------ | -------- | ------- | ------ |
| first_letter |       | =             | ’a’; | /* give    | first_letter | the      | value   | ’a’ */ |
| hour         | = 11; |               |      | /* assign  | the          | value 11 | to hour | */     |
| minute       | =     | 59;           |      | /* set     | minute       | to 59 */ |         |        |
This example shows three assignments, and the comments show three different
ways people sometimes talk about assignment statements. The vocabulary can
| be confusing | here, | but     | the idea      | is straightforward: |             |               |           |        |
| ------------ | ----- | ------- | ------------- | ------------------- | ----------- | ------------- | --------- | ------ |
| • When       | you   | declare | a variable,   | you                 | create a    | named storage | location. |        |
| • When       | you   | make    | an assignment | to                  | a variable, | you give      | it a      | value. |
Acommonwaytorepresentvariablesonpaperistodrawaboxwiththenameof
thevariableontheoutsideandthevalueofthevariableontheinside. Thiskind
of figure is called a state diagram because is shows what state each variable
isin(youcanthinkofitasthevariable’s“stateofmind”). Thisdiagramshows
| the effect   | of the | three | assignment | statements: |     |        |     |     |
| ------------ | ------ | ----- | ---------- | ----------- | --- | ------ | --- | --- |
| first_letter |        |       |            | hour        |     | minute |     |     |
a
|     |     |     |     | 11  |     | 59  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
When we assign values to variables, we have to make sure that the assigned
value correspondents to the type of the variable. In C a variable has to have
the same type as the value you assign. For example, you cannot store a string
| in an int | variable.   | The | following | statement | generates | a compiler |     | warning: |
| --------- | ----------- | --- | --------- | --------- | --------- | ---------- | --- | -------- |
| int       | hour;       |     |           |           |           |            |     |          |
| hour      | = "Hello."; |     |           | /* WRONG  | !! */     |            |     |          |
This rule is sometimes a source of confusion, because there are many ways that
you can convert values from one type to another, and C sometimes converts
things automatically. But for now you should remember that as a general rule
variablesandvalueshavethesametype,andwe’lltalkaboutspecialcaseslater.
Another source of confusion is that some strings look like integers, but they are
not. Forexample,thestring"123",whichismadeupofthecharacters1,2and
| 3, is not | the same | thing | as the | number     | 123. This | assignment | is  | illegal: |
| --------- | -------- | ----- | ------ | ---------- | --------- | ---------- | --- | -------- |
| minute    | =        | "59"; |        | /* WRONG!! | */        |            |     |          |

| 2.5 Outputting | variables |           |     |     | 17  |
| -------------- | --------- | --------- | --- | --- | --- |
| 2.5 Outputting |           | variables |     |     |     |
You can output the value of a variable using the same commands we used to
| output simple | values.         |      |        |     |     |
| ------------- | --------------- | ---- | ------ | --- | --- |
| int           | hour, minute;   |      |        |     |     |
| char          | colon;          |      |        |     |     |
| hour          | = 11;           |      |        |     |     |
| minute        | = 59;           |      |        |     |     |
| colon         | = ’:’;          |      |        |     |     |
| printf        | ("The current   | time | is "); |     |     |
| printf        | ("%i", hour);   |      |        |     |     |
| printf        | ("%c", colon);  |      |        |     |     |
| printf        | ("%i", minute); |      |        |     |     |
| printf        | ("\n");         |      |        |     |     |
This program creates two integer variables named hour and minute, and a
character variable named colon. It assigns appropriate values to each of the
variables and then uses a series of output statements to generate the following:
| The | current time | is 11:59 |     |     |     |
| --- | ------------ | -------- | --- | --- | --- |
When we talk about “outputting a variable,” we mean outputting the value of
the variable. The name of a variable only has significance for the programmer.
The compiled program no longer contains a human readable reference to the
| variable | name in your program. |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- |
The printf() command is capable of outputting several variables in a single
statement. To do this, we need to put placeholders in the so called format
string, that indicate the position where the variable value will be put. The
variables will be inserted in the order of their appearance in the statement. It
| is important | to observe | the right order | and type | for the variables. |     |
| ------------ | ---------- | --------------- | -------- | ------------------ | --- |
By using a single output statement, we can make the previous program more
concise:
| int    | hour, minute; |      |               |              |          |
| ------ | ------------- | ---- | ------------- | ------------ | -------- |
| char   | colon;        |      |               |              |          |
| hour   | = 11;         |      |               |              |          |
| minute | = 59;         |      |               |              |          |
| colon  | = ’:’;        |      |               |              |          |
| printf | ("The current | time | is %i%c%i\n", | hour, colon, | minute); |
On one line, this program outputs a string, two integers and a character. Very
impressive!

| 18  |     |     |     |     |     | Variables | and | types |
| --- | --- | --- | --- | --- | --- | --------- | --- | ----- |
2.6 Keywords
A few sections ago, I said that you can make up any name you want for your
variables,butthat’snotquitetrue. Therearecertainwordsthatarereservedin
Cbecausetheyareusedbythecompilertoparsethestructureofyourprogram,
andifyouusethemasvariablenames, itwillgetconfused. Thesewords, called
| keywords, | include | int,   | char,    | void and | many more. |          |            |     |
| --------- | ------- | ------ | -------- | -------- | ---------- | -------- | ---------- | --- |
|           |         |        | Reserved | keywords | in the C   | language |            |     |
| auto      |         | double |          | inline   | sizeof     |          | volatile   |     |
| break     |         | else   |          | int      | static     |          | while      |     |
| case      |         | enum   |          | long     | struct     |          | _Bool      |     |
| char      |         | extern |          | register | switch     |          | _Complex   |     |
| const     |         | float  |          | restrict | typedef    |          | _Imaginary |     |
| continue  |         | for    |          | return   | union      |          |            |     |
| default   |         | goto   |          | short    | unsigned   |          |            |     |
| do        |         | if     |          | signed   | void       |          |            |     |
ThecompletelistofkeywordsisincludedintheCStandard,whichistheofficial
languagedefinitionadoptedbythetheInternationalOrganizationforStandard-
| ization | (ISO) | on September | 1,  | 1998. |     |     |     |     |
| ------- | ----- | ------------ | --- | ----- | --- | --- | --- | --- |
Rather than memorize the list, I would suggest that you take advantage of a
feature provided in many development environments: code highlighting. As
you type, different parts of your program should appear in different colors. For
example, keywords might be blue, strings red, and other code black. If you
type a variable name and it turns blue, watch out! You might get some strange
| behavior | from | the compiler. |     |     |     |     |     |     |
| -------- | ---- | ------------- | --- | --- | --- | --- | --- | --- |
2.7 Operators
Operators are special symbols that are used to represent simple computations
like addition and multiplication. Most of the operators in C do exactly what
youwouldexpectthemtodo,becausetheyarecommonmathematicalsymbols.
| For example, |     | the operator | for | adding | two integers | is +. |     |     |
| ------------ | --- | ------------ | --- | ------ | ------------ | ----- | --- | --- |
ThefollowingarealllegalCexpressionswhosemeaningismoreorlessobvious:
| 1+1 |     | hour-1 |     | hour*60+minute |     | minute/60 |     |     |
| --- | --- | ------ | --- | -------------- | --- | --------- | --- | --- |
Expressions can contain both variables names and values. In each case the
name of the variable is replaced with its value before the computation is per-
formed.
Addition,subtractionandmultiplicationalldowhatyouexpect,butyoumight
| be surprised | by  | division. | For | example, | the following | program: |     |     |
| ------------ | --- | --------- | --- | -------- | ------------- | -------- | --- | --- |

| 2.8 Order | of    | operations |     |     |     |     |     |     |     | 19  |
| --------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| int hour, |       | minute;    |     |     |     |     |     |     |     |     |
| hour      | = 11; |            |     |     |     |     |     |     |     |     |
| minute    | = 59; |            |     |     |     |     |     |     |     |     |
printf ("Number of minutes since midnight: %i\n", hour*60 + minute);
printf ("Fraction of the hour that has passed: %i\n", minute/60);
| would generate |     | the     | following | output:   |             |     |     |     |     |     |
| -------------- | --- | ------- | --------- | --------- | ----------- | --- | --- | --- | --- | --- |
| Number         | of  | minutes | since     | midnight: |             | 719 |     |     |     |     |
| Fraction       |     | of the  | hour      | that      | has passed: |     | 0   |     |     |     |
The first line is what we expected, but the second line is odd. The value of the
variable minute is 59, and 59 divided by 60 is 0.98333, not 0. The reason for
| the discrepancy |     | is that | C is | performing | integer |     | division. |     |     |     |
| --------------- | --- | ------- | ---- | ---------- | ------- | --- | --------- | --- | --- | --- |
When both of the operands are integers (operands are the things operators
operateon),theresultmustalsobeaninteger,andbydefinitionintegerdivision
always rounds down, even in cases like this where the next integer is so close.
A possible alternative in this case is to calculate a percentage rather than a
fraction:
| printf     | ("Percentage |     |                 | of the | hour | that    | has passed: |     | "); |     |
| ---------- | ------------ | --- | --------------- | ------ | ---- | ------- | ----------- | --- | --- | --- |
| printf     | ("%i\n",     |     | minute*100/60); |        |      |         |             |     |     |     |
| The result | is:          |     |                 |        |      |         |             |     |     |     |
| Percentage |              | of  | the hour        | that   | has  | passed: | 98          |     |     |     |
Againtheresultisroundeddown, butatleastnowtheanswerisapproximately
correct. In order to get an even more accurate answer, we could use a different
typeofvariable,calledfloating-point,thatiscapableofstoringfractionalvalues.
| We’ll get | to that | in  | the next   | chapter. |     |     |     |     |     |     |
| --------- | ------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
| 2.8       | Order   | of  | operations |          |     |     |     |     |     |     |
When more than one operator appears in an expression the order of evaluation
depends on the rules of precedence. A complete explanation of precedence
| can get | complicated, |     | but just | to get | you started: |     |     |     |     |     |
| ------- | ------------ | --- | -------- | ------ | ------------ | --- | --- | --- | --- | --- |
• Multiplication and division happen before addition and subtraction. So
| 2*3-1 | yields | 5,  | not 4, | and 2/3-1 | yields | -1, | not 1. |     |     |     |
| ----- | ------ | --- | ------ | --------- | ------ | --- | ------ | --- | --- | --- |
• If the operators have the same precedence they are evaluated from left
| toright.                                   |       | Sointheexpressionminute*100/60, |           |              |     |      | themultiplicationhappens |              |           |     |
| ------------------------------------------ | ----- | ------------------------------- | --------- | ------------ | --- | ---- | ------------------------ | ------------ | --------- | --- |
| first,yielding5900/60,whichinturnyields98. |       |                                 |           |              |     |      | Iftheoperationshadgone   |              |           |     |
| from                                       | right | to                              | left, the | result would | be  | 59*1 | which                    | is 59, which | is wrong. |     |
• Anytimeyouwanttooverridetherulesofprecedence(oryouarenotsure
| what       | they | are)    | you can    | use parentheses. |                  | Expressions |                 | in          | parentheses | are     |
| ---------- | ---- | ------- | ---------- | ---------------- | ---------------- | ----------- | --------------- | ----------- | ----------- | ------- |
| evaluated  |      | first,  | so 2*(3-1) | is               | 4. You           | can also    | use parentheses |             | to make     | an      |
| expression |      | easier  | to read,   | as in            | (minute*100)/60, |             |                 | even though | it          | doesn’t |
| change     | the  | result. |            |                  |                  |             |                 |             |             |         |

| 20  |           |                |     | Variables and | types |
| --- | --------- | -------------- | --- | ------------- | ----- |
| 2.9 | Operators | for characters |     |               |       |
Interestingly,thesamemathematicaloperationsthatworkonintegersalsowork
| on characters. | For example, |          |     |     |     |
| -------------- | ------------ | -------- | --- | --- | --- |
| char           | letter;      |          |     |     |     |
| letter         | = ’a’ +      | 1;       |     |     |     |
| printf         | ("%c\n",     | letter); |     |     |     |
outputs the letter b. Although it is syntactically legal to multiply characters, it
| is almost | never useful | to do it. |     |     |     |
| --------- | ------------ | --------- | --- | --- | --- |
Earlier I said that you can only assign integer values to integer variables and
charactervaluestocharactervariables,butthatisnotcompletelytrue. Insome
cases, C converts automatically between types. For example, the following is
legal.
| int    | number;  |          |     |     |     |
| ------ | -------- | -------- | --- | --- | --- |
| number | = ’a’;   |          |     |     |     |
| printf | ("%i\n", | number); |     |     |     |
Theresultis97,whichisthenumberthatisusedinternallybyCtorepresentthe
letter’a’. However,itisgenerallyagoodideatotreatcharactersascharacters,
and integers as integers, and only convert from one to the other if there is a
good reason.
Automatic type conversion is an example of a common problem in designing a
programming language, which is that there is a conflict between formalism,
which is the requirement that formal languages should have simple rules with
few exceptions, and convenience, which is the requirement that programming
| languages | be easy to | use in practice. |     |     |     |
| --------- | ---------- | ---------------- | --- | --- | --- |
More often than not, convenience wins, which is usually good for expert pro-
grammers, who are spared from rigorous but unwieldy formalism, but bad for
beginning programmers, who are often baffled by the complexity of the rules
and the number of exceptions. In this book I have tried to simplify things by
| emphasizing | the rules   | and omitting many | of the exceptions. |     |     |
| ----------- | ----------- | ----------------- | ------------------ | --- | --- |
| 2.10        | Composition |                   |                    |     |     |
So far we have looked at the elements of a programming language—variables,
expressions,andstatements—inisolation,withouttalkingabouthowtocombine
them.
One of the most useful features of programming languages is their ability to
take small building blocks and compose them. For example, we know how to
multiply integers and we know how to output values; it turns out we can do
| both at the | same time: |          |     |     |     |
| ----------- | ---------- | -------- | --- | --- | --- |
| printf      | ("%i\n",   | 17 * 3); |     |     |     |

| 2.11 Glossary |     |     |     |     |     |     |     | 21  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Actually, I shouldn’t say “at the same time,” since in reality the multiplication
hastohappenbeforetheoutput,butthepointisthatanyexpression,involving
numbers, characters, and variables, can be used inside an output statement.
| We’ve already | seen     | one | example: |      |          |     |     |     |
| ------------- | -------- | --- | -------- | ---- | -------- | --- | --- | --- |
| printf        | ("%i\n", |     | hour *   | 60 + | minute); |     |     |     |
You can also put arbitrary expressions on the right-hand side of an assignment
statement:
| int percentage; |     |           |     |      |       |     |     |     |
| --------------- | --- | --------- | --- | ---- | ----- | --- | --- | --- |
| percentage      |     | = (minute | *   | 100) | / 60; |     |     |     |
This ability may not seem so impressive now, but we will see other examples
where composition makes it possible to express complex computations neatly
and concisely.
WARNING: There are limits on where you can use certain expressions; most
notably,theleft-handsideofanassignmentstatementhastobeavariablename,
not an expression. That’s because the left side indicates the storage location
where the result will go. Expressions do not represent storage locations, only
| values. So | the following |     | is illegal: | minute | +   | 1 = hour;. |     |     |
| ---------- | ------------- | --- | ----------- | ------ | --- | ---------- | --- | --- |
| 2.11       | Glossary      |     |             |        |     |            |     |     |
variable: Anamedstoragelocationforvalues. Allvariableshaveatype,which
| determines |     | which | values it | can store. |     |     |     |     |
| ---------- | --- | ----- | --------- | ---------- | --- | --- | --- | --- |
value: A letter, or number, or other thing that can be stored in a variable.
type: The meaning of values. The types we have seen so far are integers (int
| in C) | and | characters | (char | in C). |     |     |     |     |
| ----- | --- | ---------- | ----- | ------ | --- | --- | --- | --- |
keyword: A reserved word that is used by the compiler to parse programs.
| Examples |     | we have | seen include | int, | void | and | char. |     |
| -------- | --- | ------- | ------------ | ---- | ---- | --- | ----- | --- |
statement: A line of code that represents a command or action. So far, the
| statements |     | we have | seen are | declarations, |     | assignments, | and output | state- |
| ---------- | --- | ------- | -------- | ------------- | --- | ------------ | ---------- | ------ |
ments.
declaration: Astatementthatcreatesanewvariableanddeterminesitstype.
| assignment: | A   | statement | that | assigns | a value | to a | variable. |     |
| ----------- | --- | --------- | ---- | ------- | ------- | ---- | --------- | --- |
expression: A combination of variables, operators and values that represents
| a single  | result | value.        | Expressions |     | also | have types, | as determined | by their |
| --------- | ------ | ------------- | ----------- | --- | ---- | ----------- | ------------- | -------- |
| operators |        | and operands. |             |     |      |             |               |          |
operator: Aspecialsymbolthatrepresentsasimplecomputationlikeaddition
or multiplication.
| operand: | One | of the | values on | which | an operator | operates. |     |     |
| -------- | --- | ------ | --------- | ----- | ----------- | --------- | --- | --- |

| 22          |     |       |          |            |                | Variables |     | and types |
| ----------- | --- | ----- | -------- | ---------- | -------------- | --------- | --- | --------- |
| precedence: | The | order | in which | operations | are evaluated. |           |     |           |
composition: The ability to combine simple expressions and statements into
compoundstatementsandexpressionsinordertorepresentcomplexcom-
| putations    | concisely. |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
| 2.12         | Exercises  |     |     |     |     |     |     |     |
| Exercise 2.1 |            |     |     |     |     |     |     |     |
a. Create a new program named MyDate.c. Copy or type in something like the
| "Hello, | World" | program | and | make sure | you can compile | and | run it. |     |
| ------- | ------ | ------- | --- | --------- | --------------- | --- | ------- | --- |
b. Following the example in Section 2.5, write a program that creates variables
| named  | day,   | and      |           | What type | is each variable? |       |     |     |
| ------ | ------ | -------- | --------- | --------- | ----------------- | ----- | --- | --- |
|        |        | month    | year      |           |                   |       |     |     |
| Assign | values | to those | variables | that      | represent today’s | date. |     |     |
c. Print the value of each variable on a line by itself. This is an intermediate step
| that | is useful | for checking |     | that everything | is working | so far. |     |     |
| ---- | --------- | ------------ | --- | --------------- | ---------- | ------- | --- | --- |
d. Modify the program so that it prints the date in standard American form:
mm/dd/yyyy.
| e. Modify | the     | program | again | so that the | total output | is: |     |     |
| --------- | ------- | ------- | ----- | ----------- | ------------ | --- | --- | --- |
| American  | format: |         |       |             |              |     |     |     |
3/18/2009
| European | format: |     |     |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
18.3.2009
The point of this exercise is to use the output function printf to display values
with different types, and to practice developing programs gradually by adding a few
| statements   | at a time. |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
| Exercise 2.2 |            |     |     |     |     |     |     |     |
a. Create a new program called MyTime.c. From now on, I won’t remind you to
| start | with a | small, | working | program, | but you should. |     |     |     |
| ----- | ------ | ------ | ------- | -------- | --------------- | --- | --- | --- |
b. Following the example in Section 2.7, create variables named hour, minute and
| second,andassignthemvaluesthatareroughlythecurrenttime. |             |        |           |               |            |            | Usea24-hour |           |
| ------------------------------------------------------- | ----------- | ------ | --------- | ------------- | ---------- | ---------- | ----------- | --------- |
| clock,                                                  | so that     | at 2pm | the       | value of hour | is 14.     |            |             |           |
| c. Make                                                 | the program |        | calculate | and print     | the number | of seconds | since       | midnight. |
d. Make the program calculate and print the number of seconds remaining in the
day.
e. Maketheprogramcalculateandprintthepercentageofthedaythathaspassed.
f. Change the values of hour, minute and second to reflect the current time (I
| assume | that      | some time | has       | elapsed), | and check to | make sure | that | the program |
| ------ | --------- | --------- | --------- | --------- | ------------ | --------- | ---- | ----------- |
| works  | correctly | with      | different | values.   |              |           |      |             |

2.12 Exercises 23
The point of this exercise is to use some of the arithmetic operations, and to start
thinkingaboutcompoundentitieslikethetimeofdaythatarerepresentedwithmul-
tiple values. Also, you might run into problems computing percentages with ints,
| which is | the motivation | for floating point | numbers in | the next chapter. |
| -------- | -------------- | ------------------ | ---------- | ----------------- |
HINT:youmaywanttouseadditionalvariablestoholdvaluestemporarilyduringthe
computation. Variables like this, that are used in a computation but never printed,
| are sometimes | called intermediate | or  | temporary variables. |     |
| ------------- | ------------------- | --- | -------------------- | --- |

| 24  | Variables and | types |
| --- | ------------- | ----- |

| Chapter | 3   |     |     |
| ------- | --- | --- | --- |
Function
3.1 Floating-point
In the last chapter we had some problems dealing with numbers that were not
integers. We worked around the problem by measuring percentages instead of
fractions, but a more general solution is to use floating-point numbers, which
can represent fractions as well as integers. In C, there are two floating-point
types, called float and double. In this book we will use doubles exclusively.
Youcancreatefloating-pointvariablesandassignvaluestothemusingthesame
| syntax we used | for the other | types. For | example: |
| -------------- | ------------- | ---------- | -------- |
| double pi;     |               |            |          |
pi = 3.14159;
It is also legal to declare a variable and assign a value to it at the same time:
| int x =         | 1;         |     |     |
| --------------- | ---------- | --- | --- |
| char first_char | = "a";     |     |     |
| double pi       | = 3.14159; |     |     |
In fact, this syntax is quite common. A combined declaration and assignment
| is sometimes | called an initialization. |     |     |
| ------------ | ------------------------- | --- | --- |
Althoughfloating-pointnumbersareuseful,theyareoftenasourceofconfusion
because there seems to be an overlap between integers and floating-point num-
bers. For example, if you have the value 1, is that an integer, a floating-point
| number, or | both? |     |     |
| ---------- | ----- | --- | --- |
Strictly speaking, C distinguishes the integer value 1 from the floating-point
value 1.0, even though they seem to be the same number. They belong to
different types, and strictly speaking, you are not allowed to make assignments
| between types. | For example, | the following | is illegal: |
| -------------- | ------------ | ------------- | ----------- |
| int x          | = 1.1;       |               |             |

26 Function
Becausethevariableontheleftisanintandthevalueontherightisadouble.
But it is easy to forget this rule, especially because there are places where C
automatically converts from one type to another. For example,
double y = 1;
should technically not be legal, but C allows it by converting the int to a
double automatically. This is convenient for the programmer, but it can cause
problems; for example:
double y = 1 / 3;
Youmightexpectthevariableytobegiventhevalue0.333333,whichisalegal
floating-point value, but in fact it will get the value 0.0. The reason is that
the expression on the right appears to be the ratio of two integers, so C does
integer division, which yields the integer value 0. Converted to floating-point,
the result is 0.0.
One way to solve this problem (once you figure out what it is) is to make the
right-hand side a floating-point expression:
double y = 1.0 / 3.0;
This sets y to 0.333333, as expected.
All the operations we have seen—addition, subtraction, multiplication, and
division—work on floating-point values, although you might be interested to
know that the underlying mechanism is completely different. In fact, most pro-
cessors have special hardware just for performing floating-point operations.
3.2 Constants
In the previous section we have assigned the value 3.14159 to a floating point
variable. Animportantthingtorememberaboutvariablesis,thattheycanhold
– as their name implies – different values at different points in your program.
For example, we could assign the value 3.14159 to the variable pi now and
assign some other value to it later on:
double pi = 3.14159;
...
pi = 10.999; /* probably a logical error in your program */
The second value is probably not what you intended when you first created the
named storage location pi . The value for π is constant and does not change
overtime. Usingthestoragelocationpitoholdarbitraryothervaluescancause
some very hard to find bugs in your program.
C allows you to specify the static nature of storage locations through the use of
the keyword const. It must be used in conjunction with the required type of
theconstant. Avaluewillbeassignedatinitialisationbutcanneverbechanged
again during the runtime of the program.

| 3.3 Converting |        | from   | double     | to  | int |     |     |     | 27  |
| -------------- | ------ | ------ | ---------- | --- | --- | --- | --- | --- | --- |
| const          | double | PI     | = 3.14159; |     |     |     |     |     |     |
| printf         | ("Pi:  | %f\n", | PI);       |     |     |     |     |     |     |
...
| PI  | = 10.999; | /*  | wrong, | error | caught |     | by the compiler | */  |     |
| --- | --------- | --- | ------ | ----- | ------ | --- | --------------- | --- | --- |
It is no longer possible to change the value for PI once it has been initialised,
| but other | than this | we  | can use | it just | like | a variable. |     |     |     |
| --------- | --------- | --- | ------- | ------- | ---- | ----------- | --- | --- | --- |
In order to visually separate constants from variables we will use all uppercase
| letters in | their names. |     |      |     |        |     |     |     |     |
| ---------- | ------------ | --- | ---- | --- | ------ | --- | --- | --- | --- |
| 3.3        | Converting   |     | from |     | double | to  | int |     |     |
AsImentioned, Cconvertsintstodoublesautomaticallyifnecessary, because
noinformationislostinthetranslation. Ontheotherhand,goingfromadouble
toanintrequiresroundingoff. Cdoesn’tperformthisoperationautomatically,
in order to make sure that you, as the programmer, are aware of the loss of the
| fractional | part of | the number. |     |     |     |     |     |     |     |
| ---------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
The simplest way to convert a floating-point value to an integer is to use a
typecast. Typecasting is so called because it allows you to take a value that
belongs to one type and “cast” it into another type (in the sense of molding or
| reforming, | not throwing). |     |     |     |     |     |     |     |     |
| ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
The syntax for typecasting requires the explicit specification of the target type,
| set in parenthesis |         | before | the expression |     | (Type). |     | For example: |     |     |
| ------------------ | ------- | ------ | -------------- | --- | ------- | --- | ------------ | --- | --- |
| const              | double  | PI =   | 3.14159;       |     |         |     |              |     |     |
| int x              | = (int) | PI;    |                |     |         |     |              |     |     |
The (int) operator casts the value of PI into an integer, so x gets the value
3. Converting to an integer always rounds down, even if the fraction part is
0.99999999.
For every type in C, there is a corresponding operator that typecasts its argu-
| ment to | the appropriate |           | type. |     |     |     |     |     |     |
| ------- | --------------- | --------- | ----- | --- | --- | --- | --- | --- | --- |
| 3.4     | Math            | functions |       |     |     |     |     |     |     |
Inmathematics,youhaveprobablyseenfunctionslikesinandlog,andyouhave
learned to evaluate expressions like sin(π/2) and log(1/x). First, you evaluate
the expression in parentheses, which is called the argument of the function.
Forexample,π/2isapproximately1.571,and1/xis0.1(ifxhappenstobe10).
Then you can evaluate the function itself, either by looking it up in a table or
by performing various computations. The sin of 1.571 is 1, and the log of 0.1 is
| -1 (assuming | that | log indicates |     | the | logarithm | base | 10). |     |     |
| ------------ | ---- | ------------- | --- | --- | --------- | ---- | ---- | --- | --- |
Thisprocesscanbeappliedrepeatedlytoevaluatemorecomplicatedexpressions
likelog(1/sin(π/2)). Firstweevaluatetheargumentoftheinnermostfunction,
| then evaluate | the | function, | and | so on. |     |     |     |     |     |
| ------------- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- |

28 Function
C provides a set of built-in functions that includes most of the mathematical
operations you can think of. The math functions are invoked using a syntax
| that is similar | to     | mathematical |                | notation: |     |     |
| --------------- | ------ | ------------ | -------------- | --------- | --- | --- |
| double          | log    | = log        | (17.0);        |           |     |     |
| double          | angle  | =            | 1.5;           |           |     |     |
| double          | height |              | = sin (angle); |           |     |     |
Thefirstexamplesetslogtothelogarithmof17,basee. Thereisalsoafunction
| called log10 | that | takes | logarithms | base | 10. |     |
| ------------ | ---- | ----- | ---------- | ---- | --- | --- |
Thesecondexamplefindsthesineofthevalueofthevariableangle. Cassumes
that the values you use with sin and the other trigonometric functions (cos,
tan) are in radians. To convert from degrees to radians, you can divide by 360
| and multiply | by  | 2π. |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- |
If you don’t happen to know π to 15 digits, you can calculate it using the acos
function. The arccosine (or inverse cosine) of -1 is π, because the cosine of π is
-1.
| const  | double  | PI =      | acos(-1.0); |        |          |     |
| ------ | ------- | --------- | ----------- | ------ | -------- | --- |
| double | degrees | =         | 90;         |        |          |     |
| double | angle   | = degrees | *           | 2 * PI | / 360.0; |     |
Before you can use any of the math functions, you have to include the math
header file. Header files contain information the compiler needs about func-
tionsthataredefinedoutsideyourprogram. Forexample,inthe“Hello,world!”
programweincludedaheaderfilenamedstdio.husinganincludestatement:
| #include | <stdio.h> |     |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- | --- |
stdio.hcontainsinformationaboutinputandoutput(I/O)functionsavailable
in C.
Similarly, the math header file contains information about the math functions.
| You can  | include  | it at the | beginning | of  | your program | along with stdio.h: |
| -------- | -------- | --------- | --------- | --- | ------------ | ------------------- |
| #include | <math.h> |           |           |     |              |                     |
3.5 Composition
Just as with mathematical functions, C functions can be composed, meaning
that you use one expression as part of another. For example, you can use any
| expression | as an | argument | to a   | function: |     |     |
| ---------- | ----- | -------- | ------ | --------- | --- | --- |
| double     | x     | = cos    | (angle | + PI/2);  |     |     |
This statement takes the value of PI, divides it by two and adds the result to
thevalueofangle. Thesumisthenpassedasanargumenttothecosfunction.
You can also take the result of one function and pass it as an argument to
another:
| double | x   | = exp | (log (10.0)); |     |     |     |
| ------ | --- | ----- | ------------- | --- | --- | --- |
This statement finds the log base e of 10 and then raises e to that power. The
| result gets | assigned | to  | x; I hope | you know | what it | is. |
| ----------- | -------- | --- | --------- | -------- | ------- | --- |

| 3.6 Adding | new functions |           |     | 29  |
| ---------- | ------------- | --------- | --- | --- |
| 3.6        | Adding new    | functions |     |     |
So far we have only been using the functions that are built into C, but it is
also possible to add new functions. Actually, we have already seen one function
definition: main(). The function named is special because it indicates
main()
where the execution of the program begins, but the syntax for main() is the
| same as | for any other | function definition: |     |     |
| ------- | ------------- | -------------------- | --- | --- |
| void    | NAME ( LIST   | OF PARAMETERS        | )   |     |
{
STATEMENTS
}
You can make up any name you want for your function, except that you can’t
call it main or any other C keyword. The list of parameters specifies what
information,ifany,youhavetoprovideinordertouse(orcall)thenewfunction.
main()doesn’ttakeanyparameters,asindicatedbytheparenthesescontaining
thekeyword(void)init’sdefinition. Thefirstcoupleoffunctionswearegoing
| to write | also have no parameters, | so     | the syntax looks like this: |     |
| -------- | ------------------------ | ------ | --------------------------- | --- |
| void     | PrintNewLine             | (void) |                             |     |
{
| printf | ("\n"); |     |     |     |
| ------ | ------- | --- | --- | --- |
}
This function is named PrintNewLine(). It contains only a single statement,
which outputs a newline character. Notice that we start the function name
with an uppercase letter. The following words of the function name are also
capitalized. Wewillusethisconventionforthenamingoffunctionsconsistently
| throughout | the book. |     |     |     |
| ---------- | --------- | --- | --- | --- |
In main() we can call this new function using syntax that is similar to the way
| we call  | the built-in C | commands: |     |     |
| -------- | -------------- | --------- | --- | --- |
| int main | (void)         |           |     |     |
{
| printf       | ("First       | Line.\n"); |     |     |
| ------------ | ------------- | ---------- | --- | --- |
| PrintNewLine | ();           |            |     |     |
| printf       | ("Second      | Line.\n"); |     |     |
| return       | EXIT_SUCCESS; |            |     |     |
}
| The output | of this program | is: |     |     |
| ---------- | --------------- | --- | --- | --- |
| First      | line.           |     |     |     |
| Second     | line.           |     |     |     |
Notice the extra space between the two lines. What if we wanted more space
| between  | the lines? We | could call the | same function repeatedly: |     |
| -------- | ------------- | -------------- | ------------------------- | --- |
| int main | (void)        |                |                           |     |
{
| printf | ("First | Line.\n"); |     |     |
| ------ | ------- | ---------- | --- | --- |

| 30      |     |          |            |     |     |     |     |     | Function |
| ------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | -------- |
| NewLine |     | ();      |            |     |     |     |     |     |          |
| NewLine |     | ();      |            |     |     |     |     |     |          |
| NewLine |     | ();      |            |     |     |     |     |     |          |
| printf  |     | ("Second | Line.\n"); |     |     |     |     |     |          |
}
Orwecouldwriteanewfunction,namedPrintThreeLines(),thatprintsthree
new lines:
| void | PrintThreeLines |     | (void) |     |     |     |     |     |     |
| ---- | --------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
{
| PrintNewLine |     | (); | PrintNewLine |     | (); | PrintNewLine |     | (); |     |
| ------------ | --- | --- | ------------ | --- | --- | ------------ | --- | --- | --- |
}
| int main | (void) |     |     |     |     |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
{
| printf          |     | ("First       | Line.\n"); |     |     |     |     |     |     |
| --------------- | --- | ------------- | ---------- | --- | --- | --- | --- | --- | --- |
| PrintThreeLines |     |               | ();        |     |     |     |     |     |     |
| printf          |     | ("Second      | Line.\n"); |     |     |     |     |     |     |
| return          |     | EXIT_SUCCESS; |            |     |     |     |     |     |     |
}
| You should | notice | a few | things | about | this program: |     |     |     |     |
| ---------- | ------ | ----- | ------ | ----- | ------------- | --- | --- | --- | --- |
• You can call the same procedure repeatedly. In fact, it is quite common
| and | useful | to do so. |     |     |     |     |     |     |     |
| --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
• You can have one function call another function. In this case, main()
callsPrintThreeLines()andPrintThreeLines()callsPrintNewLine().
| Again, | this | is common | and | useful. |     |     |     |     |     |
| ------ | ---- | --------- | --- | ------- | --- | --- | --- | --- | --- |
• In PrintThreeLines() I wrote three statements all on the same line,
| which                             | is syntactically |     | legal | (remember |     | that spaces                 | and | new | lines usually |
| --------------------------------- | ---------------- | --- | ----- | --------- | --- | --------------------------- | --- | --- | ------------- |
| don’tchangethemeaningofaprogram). |                  |     |       |           |     | Ontheotherhand,itisusuallya |     |     |               |
betterideatoputeachstatementonalinebyitself,tomakeyourprogram
| easy | to read. | I sometimes |     | break | that | rule in this | book | to save | space. |
| ---- | -------- | ----------- | --- | ----- | ---- | ------------ | ---- | ------- | ------ |
So far, it may not be clear why it is worth the trouble to create all these new
functions. Actually, there are a lot of reasons, but this example only demon-
strates two:
1. Creatinganewfunctiongivesyouanopportunitytogiveanametoagroup
| of                 | statements. | Functions |                                              | can simplify |     | a program | by    | hiding  | a complex |
| ------------------ | ----------- | --------- | -------------------------------------------- | ------------ | --- | --------- | ----- | ------- | --------- |
| computation        |             | behind    | a single                                     | command,     |     | and by    | using | English | words in  |
| placeofarcanecode. |             |           | Whichisclearer,PrintNewLine()orprintf("\n")? |              |     |           |       |         |           |
2. Creatinganewfunctioncanmakeaprogramsmallerbyeliminatingrepet-
| itive | code.   | For example,      | a   | short | way    | to print nine | consecutive |     | new lines    |
| ----- | ------- | ----------------- | --- | ----- | ------ | ------------- | ----------- | --- | ------------ |
| is    | to call | PrintThreeLines() |     | three | times. | How           | would       | you | print 27 new |
lines?

| 3.7 Definitions | and         | uses |      |     |     | 31  |
| --------------- | ----------- | ---- | ---- | --- | --- | --- |
| 3.7             | Definitions | and  | uses |     |     |     |
Pulling together all the code fragments from the previous section, the whole
| program  | looks like   | this:  |     |     |     |     |
| -------- | ------------ | ------ | --- | --- | --- | --- |
| #include | <stdio.h>    |        |     |     |     |     |
| #include | <stdlib.h>   |        |     |     |     |     |
| void     | PrintNewLine | (void) |     |     |     |     |
{
| printf | ("\n"); |     |     |     |     |     |
| ------ | ------- | --- | --- | --- | --- | --- |
}
| void | PrintThreeLines | (void) |     |     |     |     |
| ---- | --------------- | ------ | --- | --- | --- | --- |
{
| PrintNewLine |     | (); PrintNewLine |     | (); PrintNewLine | (); |     |
| ------------ | --- | ---------------- | --- | ---------------- | --- | --- |
}
| int main | (void) |     |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- |
{
| printf          | ("First       | Line.\n"); |     |     |     |     |
| --------------- | ------------- | ---------- | --- | --- | --- | --- |
| PrintThreeLines |               | ();        |     |     |     |     |
| printf          | ("Second      | Line.\n"); |     |     |     |     |
| return          | EXIT_SUCCESS; |            |     |     |     |     |
}
This program contains three function definitions: PrintNewLine(),
| PrintThreeLine(), |     | and main(). |     |     |     |     |
| ----------------- | --- | ----------- | --- | --- | --- | --- |
Inside the definition of main(), there is a statement that uses or calls
PrintThreeLine(). Similarly, PrintThreeLine() calls PrintNewLine() three
times. Noticethatthedefinitionofeachfunctionappearsabovetheplacewhere
it is used.
This is necessary in C; the definition of a function must appear before (above)
the first use of the function. You should try compiling this program with the
| functions | in a different | order and | see what error | messages  | you get. |     |
| --------- | -------------- | --------- | -------------- | --------- | -------- | --- |
| 3.8       | Programs       | with      | multiple       | functions |          |     |
WhenyoulookattheCsourcecodethatcontainsseveralfunctions,itistempt-
ing to read it from top to bottom, but that is likely to be confusing, because
| that is not | the order | of execution | of the program. |     |     |     |
| ----------- | --------- | ------------ | --------------- | --- | --- | --- |
Executionalwaysbeginsat thefirst statementof main(), regardlessof whereit
is in the program (often it is at the bottom). Statements are executed one at a
time, in order, until you reach a function call. Function calls are like a detour
in the flow of execution. Instead of going to the next statement, you go to the

32 Function
first line of the called function, execute all the statements there, and then come
| back and | pick up again | where you left off. |     |
| -------- | ------------- | ------------------- | --- |
Thatsoundssimpleenough,exceptthatyouhavetorememberthatonefunction
can call another. Thus, while we are in the middle of main(), we might have
to go off and execute the statements in PrintThreeLines(). But while we are
executing PrintThreeLines(), we get interrupted three times to go off and
execute PrintNewLine().
Fortunately, C is adept at keeping track of where it is, so each time
PrintNewLine() completes, the program picks up where it left off in
PrintThreeLine(), and eventually gets back to main() so the program can
terminate.
What’s the moral of this sordid tale? When you read a program, don’t read
| from top | to bottom. Instead, | follow the flow | of execution. |
| -------- | ------------------- | --------------- | ------------- |
| 3.9      | Parameters          | and arguments   |               |
Someofthebuilt-infunctionswehaveusedhaveparameters,whicharevalues
that you provide to let the function do its job. For example, if you want to find
the sine of a number, you have to indicate what the number is. Thus, sin()
| takes a | value as | a parameter. |     |
| ------- | -------- | ------------ | --- |
double
Some functions take more than one parameter, like pow(), which takes two
| doubles, | the base and | the exponent. |     |
| -------- | ------------ | ------------- | --- |
Notice that in each of these cases we have to specify not only how many pa-
rameters there are, but also what type they are. So it shouldn’t surprise you
that when you write a function definition, the parameter list indicates the type
| of each | parameter. For   | example: |     |
| ------- | ---------------- | -------- | --- |
| void    | PrintTwice (char | phil)    |     |
{
| printf("%c%c\n", |     | phil, phil); |     |
| ---------------- | --- | ------------ | --- |
}
Thisfunctiontakesasingleparameter,namedphil,thathastypechar. What-
ever that parameter is (and at this point we have no idea what it is), it gets
printed twice, followed by a newline. I chose the name phil to suggest that
the name you give a parameter is up to you, but in general you want to choose
| something | more illustrative | than phil. |     |
| --------- | ----------------- | ---------- | --- |
Inordertocallthisfunction,wehavetoprovideachar. Forexample,wemight
| have a main() | function | like this: |     |
| ------------- | -------- | ---------- | --- |
| int main      | (void)   |            |     |
{
| PrintTwice | (’a’);        |     |     |
| ---------- | ------------- | --- | --- |
| return     | EXIT_SUCCESS; |     |     |
}

| 3.10 Parameters |     | and | variables | are | local |     |     |     | 33  |
| --------------- | --- | --- | --------- | --- | ----- | --- | --- | --- | --- |
The char value you provide is called an argument, and we say that the ar-
gument is passed to the function. In this case the value ’a’ is passed as an
| argument | to PrintTwice() |     | where | it  | will get | printed | twice. |     |     |
| -------- | --------------- | --- | ----- | --- | -------- | ------- | ------ | --- | --- |
Alternatively,ifwehadacharvariable,wecoulduseitasanargumentinstead:
| int main | ()  |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{
| char       | argument |               | = ’b’; |     |     |     |     |     |     |
| ---------- | -------- | ------------- | ------ | --- | --- | --- | --- | --- | --- |
| PrintTwice |          | (argument);   |        |     |     |     |     |     |     |
| return     |          | EXIT_SUCCESS; |        |     |     |     |     |     |     |
}
Notice something very important here: the name of the variable we pass as an
argument(argument)hasnothingtodowiththenameoftheparameter(phil).
| Let me say | that  | again:   |          |     |                |       |          |           |     |
| ---------- | ----- | -------- | -------- | --- | -------------- | ----- | -------- | --------- | --- |
| The        | name  | of the   | variable | we  | pass           | as an | argument | has noth- |     |
| ing        | to do | with the | name     | of  | the parameter. |       |          |           |     |
They can be the same or they can be different, but it is important to realize
that they are not the same thing, except that they happen to have the same
| value (in | this case | the character |     | ’b’). |     |     |     |     |     |
| --------- | --------- | ------------- | --- | ----- | --- | --- | --- | --- | --- |
The value you provide as an argument must have the same type as the pa-
rameter of the function you call. This rule is important, but it is sometimes
confusing because C sometimes converts arguments from one type to another
automatically. For now you should learn the general rule, and we will deal with
| exceptions | later.     |     |     |     |           |     |     |       |     |
| ---------- | ---------- | --- | --- | --- | --------- | --- | --- | ----- | --- |
| 3.10       | Parameters |     |     | and | variables |     | are | local |     |
Parameters and variables only exist inside their own functions. Within the
confines of main(), there is no such thing as phil. If you try to use it, the
compiler will complain. Similarly, inside PrintTwice() there is no such thing
as argument.
Variables like this are said to be local. In order to keep track of parameters
and local variables, it is useful to draw a stack diagram. Like state diagrams,
stack diagrams show the value of each variable, but the variables are contained
| in larger    | boxes | that indicate | which | function         |     | they | belong to. |       |     |
| ------------ | ----- | ------------- | ----- | ---------------- | --- | ---- | ---------- | ----- | --- |
| For example, | the   | stack diagram |       | for PrintTwice() |     |      | looks like | this: |     |
|              |       | PrintTwice()  |       |            phil  |     |      | 'B'        |       |     |
|              |       |               |       |   argument       |     |      | 'B'        |       |     |
main()

| 34  |     |     |     |     |     |     |     | Function |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- |
Wheneverafunctioniscalled,itcreatesanewinstanceofthatfunction. Each
instanceofafunctioncontainstheparametersandlocalvariablesforthatfunc-
tion. In the diagram an instance of a function is represented by a box with the
name of the function on the outside and the variables and parameters inside.
In the example, main() has one local variable, argument, and no parameters.
| PrintTwice() | has       | no local | variables |          | and one | parameter, | named | phil. |
| ------------ | --------- | -------- | --------- | -------- | ------- | ---------- | ----- | ----- |
| 3.11         | Functions |          | with      | multiple |         | parameters |       |       |
The syntax for declaring and invoking functions with multiple parameters is a
common source of errors. First, remember that you have to declare the type of
| every parameter. |     | For example |       |     |         |     |     |     |
| ---------------- | --- | ----------- | ----- | --- | ------- | --- | --- | --- |
| void PrintTime   |     | (int        | hour, | int | minute) |     |     |     |
{
| printf | ("%i", | hour);   |     |     |     |     |     |     |
| ------ | ------ | -------- | --- | --- | --- | --- | --- | --- |
| printf | (":"); |          |     |     |     |     |     |     |
| printf | ("%i", | minute); |     |     |     |     |     |     |
}
It might be tempting to write (int hour, minute), but that format is only
| legal for variable |     | declarations, |     | not for | parameters. |     |     |     |
| ------------------ | --- | ------------- | --- | ------- | ----------- | --- | --- | --- |
Another common source of confusion is that you do not have to declare the
| types of arguments. |     | The   | following | is           | wrong! |           |     |     |
| ------------------- | --- | ----- | --------- | ------------ | ------ | --------- | --- | --- |
| int hour            | =   | 11;   |           |              |        |           |     |     |
| int minute          |     | = 59; |           |              |        |           |     |     |
| PrintTime           |     | (int  | hour,     | int minute); |        | /* WRONG! |     | */  |
In this case, the compiler can tell the type of hour and minute by looking at
their declarations. It is unnecessary and illegal to include the type when you
pass them as arguments. The correct syntax is PrintTime (hour, minute);.
| 3.12 | Functions |     | with | results |     |     |     |     |
| ---- | --------- | --- | ---- | ------- | --- | --- | --- | --- |
You might have noticed by now that some of the functions we are using, like
the math functions, yield results. Other functions, like PrintNewLine, perform
| an action | but don’t | return | a   | value. That | raises | some | questions: |     |
| --------- | --------- | ------ | --- | ----------- | ------ | ---- | ---------- | --- |
• What happens if you call a function and you don’t do anything with the
| result | (i.e. | you don’t | assign | it  | to a variable | or  | use it | as part of a larger |
| ------ | ----- | --------- | ------ | --- | ------------- | --- | ------ | ------------------- |
expression)?
• What happens if you use a function without a result as part of an expres-
| sion, | like PrintNewLine() |     |     | + 7? |     |     |     |     |
| ----- | ------------------- | --- | --- | ---- | --- | --- | --- | --- |
• Can we write functions that yield results, or are we stuck with things like
| PrintNewLine() |     |     | and PrintTwice()? |     |     |     |     |     |
| -------------- | --- | --- | ----------------- | --- | --- | --- | --- | --- |

3.13 Glossary 35
The answer to the third question is “yes, you can write functions that return
values,”andwe’lldoitinacoupleofchapters. Iwillleaveituptoyoutoanswer
theothertwoquestionsbytryingthemout. Anytimeyouhaveaquestionabout
what is legal or illegal in C, a good way to find out is to ask the compiler.
3.13 Glossary
constant: A named storage location similar to a variable, that can not be
changed once it has been initialised.
floating-point: Atypeofvariable(orvalue)thatcancontainfractionsaswell
as integers. There are a few floating-point types in C; the one we use in
this book is double.
initialization: A statement that declares a new variable and assigns a value
to it at the same time.
function: Anamedsequenceofstatementsthatperformssomeusefulfunction.
Functions may or may not take parameters, and may or may not produce
a result.
parameter: A piece of information you provide in order to call a function.
Parameters are like variables in the sense that they contain values and
have types.
argument: Avaluethatyouprovidewhenyoucallafunction. Thisvaluemust
have the same type as the corresponding parameter.
call: Cause a function to be executed.
3.14 Exercises
Exercise 3.1
The point of this exercise is to practice reading code and to make sure that you
understand the flow of execution through a program with multiple functions.
a. Whatistheoutputofthefollowingprogram? Bepreciseaboutwherethereare
spaces and where there are newlines.
HINT: Start by describing in words what Ping() and Baffle() do when they
are invoked.
#include <stdio.h>
#include <stdlib.h>
void Ping ()
{
printf (".\n");
}

36 Function
| void | Baffle () |     |     |     |
| ---- | --------- | --- | --- | --- |
{
printf ("wug");
Ping ();
}
| void | Zoop () |     |     |     |
| ---- | ------- | --- | --- | --- |
{
Baffle ();
| printf | ("You | wugga "); |     |     |
| ------ | ----- | --------- | --- | --- |
Baffle ();
}
| int | main (void) |     |     |     |
| --- | ----------- | --- | --- | --- |
{
| printf | ("No, | I "); |     |     |
| ------ | ----- | ----- | --- | --- |
Zoop ();
printf ("I ");
Baffle ();
return EXIT_SUCCESS;
}
b. DrawastackdiagramthatshowsthestateoftheprogramthefirsttimePing()
is invoked.
Exercise 3.2 The point of this exercise is to make sure you understand how to
| write and invoke | functions | that take | parameters. |     |
| ---------------- | --------- | --------- | ----------- | --- |
a. WritethefirstlineofafunctionnamedZool()thattakesthreeparameters: an
| int and | two char. |     |     |     |
| ------- | --------- | --- | --- | --- |
b. WritealineofcodethatinvokesZool(),passingasargumentsthevalue11,the
| letter a,    | and the letter | z.  |     |     |
| ------------ | -------------- | --- | --- | --- |
| Exercise 3.3 |                |     |     |     |
The purpose of this exercise is to take code from a previous exercise and encapsulate
it in a function that takes parameters. You should start with a working solution to
exercise
a. Write a function called PrintDateAmerican() that takes the day, month and
| year as | parameters | and that prints | them in American | format. |
| ------- | ---------- | --------------- | ---------------- | ------- |
b. Test your function by invoking it from main() and passing appropriate argu-
| ments. | Theoutputshouldlooksomethinglikethis(exceptthatthedatemight |     |     |     |
| ------ | ----------------------------------------------------------- | --- | --- | --- |
be different):
3/29/2009
c. Once you have debugged PrintDateAmerican(), write another function called
| PrintDateEuropean() |     | that prints | the date in European | format. |
| ------------------- | --- | ----------- | -------------------- | ------- |

| 3.14 Exercises |     |     |     |     |     |     | 37  |
| -------------- | --- | --- | --- | --- | --- | --- | --- |
| Exercise       | 3.4 |     |     |     |     |     |     |
Manycomputationscanbeexpressedconciselyusingthe“multadd”operation,which
takesthreeoperandsandcomputesa*b + c. Someprocessorsevenprovideahardware
| implementation | of    | this operation | for floating-point |     | numbers. |     |     |
| -------------- | ----- | -------------- | ------------------ | --- | -------- | --- | --- |
| a. Create      | a new | program        | called Multadd.c.  |     |          |     |     |
b. Write a function called Multadd() that takes three doubles as parameters and
| that | prints | their multadditionization. |     |     |     |     |     |
| ---- | ------ | -------------------------- | --- | --- | --- | --- | --- |
c. Write a main() function that tests Multadd() by invoking it with a few simple
| parameters, |     | like | 3.0, | and then | prints the | result, which | should be |
| ----------- | --- | ---- | ---- | -------- | ---------- | ------------- | --------- |
|             |     | 1.0, | 2.0, |          |            |               |           |
5.0.
| d. Also | in main(), | use Multadd() | to  | compute | the following | value: |     |
| ------- | ---------- | ------------- | --- | ------- | ------------- | ------ | --- |
cosπ
|     |     |     |     | sinπ + | 4   |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- |
|     |     |     |     | 4      | 2   |     |     |
e. Write a function called Yikes() that takes a double as a parameter and that
| uses | Multadd() | to calculate | and | print |     |     |     |
| ---- | --------- | ------------ | --- | ----- | --- | --- | --- |
xe−x+ p
1−e−x
| HINT: | the | Math function | for raising | e   | to a power is double | exp(double | x);. |
| ----- | --- | ------------- | ----------- | --- | -------------------- | ---------- | ---- |
In the last part, you get a chance to write a function that invokes a function you
wrote. Whenever you do that, it is a good idea to test the first function carefully
beforeyoustartworkingonthesecond. Otherwise,youmightfindyourselfdebugging
| two functions | at the | same time, | which | can be | very difficult. |     |     |
| ------------- | ------ | ---------- | ----- | ------ | --------------- | --- | --- |
One of the purposes of this exercise is to practice pattern-matching: the ability to
| recognize | a specific | problem | as an instance | of  | a general category | of problems. |     |
| --------- | ---------- | ------- | -------------- | --- | ------------------ | ------------ | --- |

38 Function

| Chapter      | 4           |           |     |           |     |     |
| ------------ | ----------- | --------- | --- | --------- | --- | --- |
| Conditionals |             |           | and | recursion |     |     |
| 4.1          | Conditional | execution |     |           |     |     |
In order to write useful programs, we almost always need the ability to check
certainconditionsandchangethebehavioroftheprogramaccordingly. Condi-
tional statements give us this ability. The simplest form is the if statement:
| if (x | > 0) |     |     |     |     |     |
| ----- | ---- | --- | --- | --- | --- | --- |
{
| printf | ("x is | positive\n"); |     |     |     |     |
| ------ | ------ | ------------- | --- | --- | --- | --- |
}
The expression in parentheses is called the condition. If it is true, then the
statements in brackets get executed. If the condition is not true, nothing hap-
pens.
| The condition | can contain | any of | the comparison | operators: |          |         |
| ------------- | ----------- | ------ | -------------- | ---------- | -------- | ------- |
| x ==          | y           | /*     | x equals       | y */       |          |         |
| x !=          | y           | /*     | x is not       | equal to   | y */     |         |
| x >           | y           | /*     | x is greater   | than       | y */     |         |
| x <           | y           | /*     | x is less      | than y     | */       |         |
| x >=          | y           | /*     | x is greater   | than       | or equal | to y */ |
| x <=          | y           | /*     | x is less      | than or    | equal    | to y */ |
Although these operations are probably familiar to you, the syntax C uses is a
little different from mathematical symbols like =, 6= and ≤. A common error
is to use a single = instead of a double ==. Remember that = is the assignment
operator, and == is a comparison operator. Also, there is no such thing as =<
or =>.
The two sides of a condition operator have to be the same type. You can only
compare ints to ints and doubles to doubles. Unfortunately, at this point
you can’t compare strings at all! There is a way to compare strings, but we
| won’t get | to it for a couple | of chapters. |     |     |     |     |
| --------- | ------------------ | ------------ | --- | --- | --- | --- |

| 40  |             |          | Conditionals | and recursion |
| --- | ----------- | -------- | ------------ | ------------- |
| 4.2 | The modulus | operator |              |               |
Themodulusoperatorworksonintegers(andintegerexpressions)andyieldsthe
remainder when the first operand is divided by the second. In C, the modulus
operator is a percent sign, %. The syntax is exactly the same as for other
operators:
| int quotient  | = 7 / 3; |     |     |     |
| ------------- | -------- | --- | --- | --- |
| int remainder | = 7 %    | 3;  |     |     |
The first operator, integer division, yields 2. The second operator yields 1.
| Thus, 7 | divided by 3 is 2 | with 1 left over. |     |     |
| ------- | ----------------- | ----------------- | --- | --- |
The modulus operator turns out to be surprisingly useful. For example, you
can check whether one number is divisible by another: if x % y is zero, then x
| is divisible | by y. |     |     |     |
| ------------ | ----- | --- | --- | --- |
Also, you can use the modulus operator to extract the rightmost digit or digits
from a number. For example, x % 10 yields the rightmost digit of x (in base
| 10). Similarly | x % 100 yields | the last  | two digits. |     |
| -------------- | -------------- | --------- | ----------- | --- |
| 4.3            | Alternative    | execution |             |     |
A second form of conditional execution is alternative execution, in which there
aretwopossibilities,andtheconditiondetermineswhichonegetsexecuted. The
| syntax looks | like: |     |     |     |
| ------------ | ----- | --- | --- | --- |
| if (x%2      | == 0) |     |     |     |
{
| printf | ("x is even\n"); |     |     |     |
| ------ | ---------------- | --- | --- | --- |
}
else
{
| printf | ("x is odd\n"); |     |     |     |
| ------ | --------------- | --- | --- | --- |
}
If the remainder when x is divided by 2 is zero, then we know that x is even,
and this code displays a message to that effect. If the condition is false, the
second set of statements is executed. Since the condition must be true or false,
| exactly | one of the alternatives | will be | executed. |     |
| ------- | ----------------------- | ------- | --------- | --- |
As an aside, if you think you might want to check the parity (evenness or
oddness)ofnumbersoften,youmightwantto“wrap”thiscodeupinafunction,
as follows:
| void | PrintParity (int | x)  |     |     |
| ---- | ---------------- | --- | --- | --- |
{
| if  | (x%2 == 0) |     |     |     |
| --- | ---------- | --- | --- | --- |
{
|     | printf ("x is | even\n"); |     |     |
| --- | ------------- | --------- | --- | --- |
}

| 4.4 Chained | conditionals |     |     |     | 41  |
| ----------- | ------------ | --- | --- | --- | --- |
else
{
|     | printf ("x | is odd\n"); |     |     |     |
| --- | ---------- | ----------- | --- | --- | --- |
}
}
NowyouhaveafunctionnamedPrintParity()thatwilldisplayanappropriate
message for any integer you care to provide. In main() you would call this
| function    | as follows: |     |     |     |     |
| ----------- | ----------- | --- | --- | --- | --- |
| PrintParity | (17);       |     |     |     |     |
Alwaysrememberthatwhenyoucallafunction, youdonothavetodeclarethe
types of the arguments you provide. C can figure out what type they are. You
| should resist | the temptation | to write things | like:       |     |     |
| ------------- | -------------- | --------------- | ----------- | --- | --- |
| int number    | = 17;          |                 |             |     |     |
| PrintParity   | (int           | number);        | /* WRONG!!! | */  |     |
| 4.4 Chained   | conditionals   |                 |             |     |     |
Sometimesyouwanttocheckforanumberofrelatedconditionsandchooseone
of several actions. One way to do this is by chaining a series of ifs and elses:
| if (x | > 0) |     |     |     |     |
| ----- | ---- | --- | --- | --- | --- |
{
|     | printf ("x is | positive\n"); |     |     |     |
| --- | ------------- | ------------- | --- | --- | --- |
}
| else | if (x < 0) |     |     |     |     |
| ---- | ---------- | --- | --- | --- | --- |
{
|     | printf ("x is | negative\n"); |     |     |     |
| --- | ------------- | ------------- | --- | --- | --- |
}
else
{
|     | printf ("x is | zero\n"); |     |     |     |
| --- | ------------- | --------- | --- | --- | --- |
}
These chains can be as long as you want, although they can be difficult to read
iftheygetoutofhand. Onewaytomakethemeasiertoreadistousestandard
indentation, as demonstrated in these examples. If you keep all the statements
and squiggly-braces lined up, you are less likely to make syntax errors and you
| can find   | them more quickly | if you do. |     |     |     |
| ---------- | ----------------- | ---------- | --- | --- | --- |
| 4.5 Nested | conditionals      |            |     |     |     |
In addition to chaining, you can also nest one conditional within another. We
| could have | written the previous | example | as: |     |     |
| ---------- | -------------------- | ------- | --- | --- | --- |
| if (x      | == 0)                |         |     |     |     |
{

| 42  |     |        |                  |     | Conditionals | and recursion |
| --- | --- | ------ | ---------------- | --- | ------------ | ------------- |
|     |     | printf | ("x is zero\n"); |     |              |               |
}
else
{
|     |     | if (x > | 0)  |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- |
{
|     |     | printf | ("x | is positive\n"); |     |     |
| --- | --- | ------ | --- | ---------------- | --- | --- |
}
else
{
|     |     | printf | ("x | is negative\n"); |     |     |
| --- | --- | ------ | --- | ---------------- | --- | --- |
}
}
There is now an outer conditional that contains two branches. The first branch
contains a simple output statement, but the second branch contains another if
statement, which has two branches of its own. Fortunately, those two branches
are both output statements, although they could have been conditional state-
| ments | as  | well. |     |     |     |     |
| ----- | --- | ----- | --- | --- | --- | --- |
Noticeagainthatindentationhelpsmakethestructureapparent, butneverthe-
less, nested conditionals get difficult to read very quickly. In general, it is a
| good | idea | to avoid | them when | you can. |     |     |
| ---- | ---- | -------- | --------- | -------- | --- | --- |
On the other hand, this kind of nested structure is common, and we will see
| it  | again, | so you better | get used | to it.    |     |     |
| --- | ------ | ------------- | -------- | --------- | --- | --- |
| 4.6 |        | The return    |          | statement |     |     |
Thereturnstatementallowsyoutoterminatetheexecutionofafunctionbefore
| you | reach    | the end.       | One reason | to use it | is if you detect | an error condition: |
| --- | -------- | -------------- | ---------- | --------- | ---------------- | ------------------- |
|     | #include | <math.h>       |            |           |                  |                     |
|     | void     | PrintLogarithm | (double    | x)        |                  |                     |
{
|     | if  | (x <= | 0.0) |     |     |     |
| --- | --- | ----- | ---- | --- | --- | --- |
{
|     |     | printf | ("Positive | numbers | only, please.\n"); |     |
| --- | --- | ------ | ---------- | ------- | ------------------ | --- |
return;
}
|     | double | result | = log  | (x);        |          |     |
| --- | ------ | ------ | ------ | ----------- | -------- | --- |
|     | printf | ("The  | log of | x is %f\n", | result); |     |
}
This defines a function named PrintLogarithm() that takes a double named
xasaparameter. Thefirstthingitdoesischeckwhetherxislessthanorequal
to zero, in which case it displays an error message and then uses return to exit

4.7 Recursion 43
the function. The flow of execution immediately returns to the caller and the
| remaining | lines of | the function |     | are not | executed. |     |     |
| --------- | -------- | ------------ | --- | ------- | --------- | --- | --- |
I used a floating-point value on the right side of the condition because there is
| a floating-point | variable |     | on the | left. |     |     |     |
| ---------------- | -------- | --- | ------ | ----- | --- | --- | --- |
Rememberthatanytimeyouwanttouseoneafunctionfromthemathlibrary,
| you have | to include | the | header | file math.h. |     |     |     |
| -------- | ---------- | --- | ------ | ------------ | --- | --- | --- |
4.7 Recursion
I mentioned in the last chapter that it is legal for one function to call another,
and we have seen several examples of that. I neglected to mention that it is
also legal for a function to call itself. It may not be obvious why that is a good
thing, but it turns out to be one of the most magical and interesting things a
| program      | can do.   |        |           |           |     |     |     |
| ------------ | --------- | ------ | --------- | --------- | --- | --- | --- |
| For example, | look      | at the | following | function: |     |     |     |
| void         | Countdown | (int   | n)        |           |     |     |     |
{
| if  | (n == | 0)  |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- |
{
printf ("Blastoff!");
}
else
{
|     | printf    | ("%i", | n);    |     |     |     |     |
| --- | --------- | ------ | ------ | --- | --- | --- | --- |
|     | Countdown |        | (n-1); |     |     |     |     |
}
}
The name of the function is Countdown() and it takes a single integer as a
parameter. If the parameter is zero, it outputs the word “Blastoff.” Otherwise,
itoutputstheparameterandthencallsafunctionnamedCountdown()—itself—
| passing      | n-1 as an | argument. |               |     |            |     |     |
| ------------ | --------- | --------- | ------------- | --- | ---------- | --- | --- |
| What happens | if        | we call   | this function |     | like this: |     |     |
| int main     | (void)    |           |               |     |            |     |     |
{
|     | Countdown | (3);          |     |     |     |     |     |
| --- | --------- | ------------- | --- | --- | --- | --- | --- |
|     | return    | EXIT_SUCCESS; |     |     |     |     |     |
}
The execution of Countdown() begins with n=3, and since n is not zero, it
| outputs | the value  | 3, and | then        | calls itself... |            |                     |          |
| ------- | ---------- | ------ | ----------- | --------------- | ---------- | ------------------- | -------- |
| The     | execution  | of     | Countdown() | begins          |            | with n=2, and since | n is not |
| zero,   | it outputs | the    | value       | 2, and          | then calls | itself...           |          |

| 44  |                                         |     |                     |                |     | Conditionals          | and      | recursion |
| --- | --------------------------------------- | --- | ------------------- | -------------- | --- | --------------------- | -------- | --------- |
|     | TheexecutionofCountdown()beginswithn=1, |     |                     |                |     |                       | andsince |           |
|     | nisnotzero,                             |     | itoutputsthevalue1, |                |     | andthencallsitself... |          |           |
|     |                                         | The | execution           | of Countdown() |     | begins with           | n=0,     |           |
andsinceniszero,itoutputstheword“Blastoff!”
|               |               | and then  | returns. |                  |              |     |     |     |
| ------------- | ------------- | --------- | -------- | ---------------- | ------------ | --- | --- | --- |
|               | The           | Countdown |          | that got         | n=1 returns. |     |     |     |
|               | The Countdown |           | that     | got n=2 returns. |              |     |     |     |
| The Countdown |               | that      | got      | n=3 returns.     |              |     |     |     |
And then you’re back in main() (what a trip). So the total output looks like:
3
2
1
Blastoff!
As a second example, let’s look again at the functions PrintNewLine() and
PrintThreeLines().
| void | PrintNewLine |     | ()  |     |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
{
printf ("\n");
}
| void | PrintThreeLines |     |     | ()  |     |     |     |     |
| ---- | --------------- | --- | --- | --- | --- | --- | --- | --- |
{
|     | PrintNewLine |     | (); | PrintNewLine |     | (); PrintNewLine |     | (); |
| --- | ------------ | --- | --- | ------------ | --- | ---------------- | --- | --- |
}
Although these work, they would not be much help if I wanted to output 2
| newlines, | or         | 106. A | better | alternative | would | be  |     |     |
| --------- | ---------- | ------ | ------ | ----------- | ----- | --- | --- | --- |
| void      | PrintLines |        | (int   | n)          |       |     |     |     |
{
|     | if  | (n > 0) |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- |
{
|     |     | printf     | ("\n"); |        |     |     |     |     |
| --- | --- | ---------- | ------- | ------ | --- | --- | --- | --- |
|     |     | PrintLines |         | (n-1); |     |     |     |     |
}
}
This program is similar to Countdown; as long as n is greater than zero, it
outputs one newline, and then calls itself to output n-1 additional newlines.
Thus, the total number of newlines is 1 + (n-1), which usually comes out to
roughly n.
The process of a function calling itself is called recursion, and such functions
| are said | to be | recursive. |     |     |     |     |     |     |
| -------- | ----- | ---------- | --- | --- | --- | --- | --- | --- |

| 4.8 Infinite | recursion |     |           |     |     |     |     | 45  |
| ------------ | --------- | --- | --------- | --- | --- | --- | --- | --- |
| 4.8          | Infinite  |     | recursion |     |     |     |     |     |
In the examples in the previous section, notice that each time the functions
get called recursively, the argument gets smaller by one, so eventually it gets
to zero. When the argument is zero, the function returns immediately, without
making any recursive calls. This case—when the function completes without
| making | a recursive | call—is | called | the | base case. |     |     |     |
| ------ | ----------- | ------- | ------ | --- | ---------- | --- | --- | --- |
If a recursion never reaches a base case, it will go on making recursive calls
forever and the program will never terminate. This is known as infinite re-
| cursion, | and | it is generally | not | considered | a good | idea. |     |     |
| -------- | --- | --------------- | --- | ---------- | ------ | ----- | --- | --- |
In most programming environments, a program with an infinite recursion will
not really run forever. Eventually, something will break and the program will
report an error. This is the first example we have seen of a run-time error (an
| error that | does | not appear | until | you | run the program). |     |     |     |
| ---------- | ---- | ---------- | ----- | --- | ----------------- | --- | --- | --- |
You should write a small program that recurses forever and run it to see what
happens.
| 4.9 | Stack | diagrams |     | for | recursive | functions |     |     |
| --- | ----- | -------- | --- | --- | --------- | --------- | --- | --- |
In the previous chapter we used a stack diagram to represent the state of a
program during a function call. The same kind of diagram can make it easier
| to interpret | a   | recursive | function. |     |     |     |     |     |
| ------------ | --- | --------- | --------- | --- | --- | --- | --- | --- |
Remember that every time a function gets called it creates a new instance that
| contains    | the function’s |             | local variables |              | and parameters. |             |        |     |
| ----------- | -------------- | ----------- | --------------- | ------------ | --------------- | ----------- | ------ | --- |
| This figure | shows          | a stack     | diagram         | for          | Countdown,      | called with | n = 3: |     |
|             |                | Countdown() |                 |            n |                 | 0           |        |     |
|             |                | Countdown() |                 |            n |                 | 1           |        |     |
|             |                | Countdown() |                 |            n |                 | 2           |        |     |
|             |                | Countdown() |                 |            n |                 | 3           |        |     |
|             |                |             | main()          |              |                 |             |        |     |
There is one instance of main() and four instances of Countdown(), each with
a different value for the parameter n. The bottom of the stack, Countdown()

| 46  |     |     |     |     | Conditionals |     | and recursion |     |
| --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- |
with n=0 is the base case. It does not make a recursive call, so there are no
| more instances | of Countdown(). |     |     |     |     |     |     |     |
| -------------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Theinstanceof main()isemptybecause main()doesnothaveanyparameters
or local variables. As an exercise, draw a stack diagram for PrintLines(),
| invoked with | the parameter | n=4. |     |     |     |     |     |     |
| ------------ | ------------- | ---- | --- | --- | --- | --- | --- | --- |
| 4.10         | Glossary      |      |     |     |     |     |     |     |
modulus: An operator that works on integers and yields the remainder when
| one | number is divided | by  | another. | In C it | is denoted | with | a percent | sign |
| --- | ----------------- | --- | -------- | ------- | ---------- | ---- | --------- | ---- |
(%).
conditional: A block of statements that may or may not be executed depend-
| ing       | on some condition. |         |             |     |            |     |           |     |
| --------- | ------------------ | ------- | ----------- | --- | ---------- | --- | --------- | --- |
| chaining: | A way of joining   | several | conditional |     | statements | in  | sequence. |     |
nesting: Putting a conditional statement inside one or both branches of an-
| other | conditional statement. |     |     |     |     |     |     |     |
| ----- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
recursion: The process of calling the same function you are currently execut-
ing.
infinite recursion: Afunctionthatcallsitselfrecursivelywithouteveryreach-
| ing | the base case. | Eventually | an  | infinite | recursion | will | cause a run-time |     |
| --- | -------------- | ---------- | --- | -------- | --------- | ---- | ---------------- | --- |
error.
| 4.11 | Exercises |     |     |     |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
Exercise 4.1 This exercise reviews the flow of execution through a program with
| multiple methods. | Read the     | following | code   | and answer | the | questions | below. |     |
| ----------------- | ------------ | --------- | ------ | ---------- | --- | --------- | ------ | --- |
| #include          | <stdio.h>    |           |        |            |     |           |        |     |
| #include          | <stdlib.h>   |           |        |            |     |           |        |     |
| void Zippo        | (int quince, | int       | flag); |            |     |           |        |     |
| void Baffle       | (int output) |           |        |            |     |           |        |     |
{
| printf | ("%i\n",output); |     |     |     |     |     |     |     |
| ------ | ---------------- | --- | --- | --- | --- | --- | --- | --- |
| Zippo  | (12, -5);        |     |     |     |     |     |     |     |
}
| void | Zippo (int quince, | int | flag) |     |     |     |     |     |
| ---- | ------------------ | --- | ----- | --- | --- | --- | --- | --- |
{
| if  | (flag < 0) |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
{
|     | printf ("%i | zoop\n", | quince); |     |     |     |     |     |
| --- | ----------- | -------- | -------- | --- | --- | --- | --- | --- |

4.11 Exercises 47
}
else
{
printf ("rattle ");
Baffle (quince);
printf ("boo-wa-ha-ha\n");
}
}
int main (void)
{
Zippo (5, 13);
return EXIT_SUCCESS;
}
a. Write the number 1 next to the first statement of this program that will be
executed. Be careful to distinguish things that are statements from things that
are not.
b. Write the number 2 next to the second statement, and so on until the end of
the program. If a statement is executed more than once, it might end up with
more than one number next to it.
c. What is the value of the parameter blimp when baffle() gets invoked?
d. What is the output of this program?
Exercise 4.2 The first verse of the song “99 Bottles of Beer” is:
99 bottles of beer on the wall, 99 bottles of beer, ya’ take one down, ya’
pass it around, 98 bottles of beer on the wall.
Subsequentversesareidenticalexceptthatthenumberofbottlesgetssmallerbyone
in each verse, until the last verse:
Nobottlesofbeeronthewall,nobottlesofbeer,ya’can’ttakeonedown,
ya’ can’t pass it around, ’cause there are no more bottles of beer on the
wall!
And then the song (finally) ends.
Write a program that prints the entire lyrics of “99 Bottles of Beer.” Your program
should include a recursive method that does the hard part, but you also might want
to write additional methods to separate the major functions of the program.
Asyouaredevelopingyourcode,youwillprobablywanttotestitwithasmallnumber
of verses, like “3 Bottles of Beer.”
The purpose of this exercise is to take a problem and break it into smaller problems,
and to solve the smaller problems by writing simple, easily-debugged methods.
Exercise4.3 Youcanusethegetchar()functioninCtogetcharacterinputfrom
theuserthroughthekeyboard. Thisfunctionstopstheexecutionoftheprogramand
waits for the input from the user.

| 48  |     |     |     |     | Conditionals | and recursion |
| --- | --- | --- | --- | --- | ------------ | ------------- |
Thegetchar()functionhasthetypeintanddoesnotrequireanargument. Itreturns
the ASCII-Code (cf. Appendix B) of the key that has been pressed on the keyboard.
| a. Write | a program, |     | that asks | the user to | input a digit | between 0 and 9. |
| -------- | ---------- | --- | --------- | ----------- | ------------- | ---------------- |
b. Testtheinputfromtheuseranddisplayanerrormessageifthereturnedvalue
| isnotadigit. |         | Theprogramshouldthenbeterminated. |           |             |                 | Ifthetestissuccessful, |
| ------------ | ------- | --------------------------------- | --------- | ----------- | --------------- | ---------------------- |
| the          | program | should                            | print the | input value | on the computer | screen.                |
Exercise 4.4 Fermat’s Last Theorem says that there are no integers a, b, and c
such that
|           |          |      |      | an+bn | =cn |     |
| --------- | -------- | ---- | ---- | ----- | --- | --- |
| except in | the case | when | n=2. |       |     |     |
Write a function named checkFermat() that takes four integers as parameters—a, b,
c and n—and that checks to see if Fermat’s theorem holds. If n is greater than 2 and
|     |     |     | an+bn | cn, |     |     |
| --- | --- | --- | ----- | --- | --- | --- |
it turns out to be true that = the program should print “Holy smokes,
Fermat was wrong!” Otherwise the program should print “No, that doesn’t work.”
YoushouldassumethatthereisafunctionnamedraiseToPow()thattakestwointe-
gers as arguments and that raises the first argument to the power of the second. For
example:
| int          | x = raiseToPow |       | (2, 3);         |        |     |     |
| ------------ | -------------- | ----- | --------------- | ------ | --- | --- |
| would assign | the            | value | 8 to x, because | 23 =8. |     |     |

| Chapter    | 5         |     |
| ---------- | --------- | --- |
| Fruitful   | functions |     |
| 5.1 Return | values    |     |
Some of the built-in functions we have used, like the math functions, have
produced results. That is, the effect of calling the function is to generate a new
value, which we usually assign to a variable or use as part of an expression. For
example:
| double e =    | exp (1.0); |                |
| ------------- | ---------- | -------------- |
| double height | = radius   | * sin (angle); |
But so far all the functions we have written have been void functions; that is,
functions that return no value. When you call a void function, it is typically on
| a line by itself, with | no assignment: |     |
| ---------------------- | -------------- | --- |
| PrintLines             | (3);           |     |
| Countdown (n-1);       |                |     |
In this chapter, we are going to write functions that return things, which I will
refer to as fruitful functions, for want of a better name. The first example is
area,whichtakesadoubleasaparameter,andreturnstheareaofacirclewith
the given radius:
| double Area | (double radius) |     |
| ----------- | --------------- | --- |
{
| double pi    | = acos (-1.0); |                  |
| ------------ | -------------- | ---------------- |
| double area  | = pi *         | radius * radius; |
| return area; |                |                  |
}
Thefirstthingyoushouldnoticeisthatthebeginningofthefunctiondefinition
is different. Instead of void, which indicates a void function, we see double,
which indicates that the return value from this function will have type double.
Also, noticethatthelastlineisanalternateformofthereturnstatementthat
includes a return value. This statement means, “return immediately from this

50 Fruitful functions
functionandusethefollowingexpressionasareturnvalue.” Theexpressionyou
provide can be arbitrarily complicated, so we could have written this function
more concisely:
| double Area | (double | radius) |     |
| ----------- | ------- | ------- | --- |
{
| return | acos(-1.0) | * radius | * radius; |
| ------ | ---------- | -------- | --------- |
}
Ontheotherhand,temporaryvariableslikeareaoftenmakedebuggingeasier.
In either case, the type of the expression in the return statement must match
thereturntypeofthefunction. Inotherwords,whenyoudeclarethatthereturn
type is double, you are making a promise that this function will eventually
produce a double. If you try to return with no expression, or an expression
| with the wrong | type, the | compiler will | take you to task. |
| -------------- | --------- | ------------- | ----------------- |
Sometimes it is useful to have multiple return statements, one in each branch
of a conditional:
| double AbsoluteValue |     | (double x) |     |
| -------------------- | --- | ---------- | --- |
{
| if (x | < 0) |     |     |
| ----- | ---- | --- | --- |
{
return -x;
}
else
{
return x;
}
}
Since these returns statements are in an alternative conditional, only one will
be executed. Although it is legal to have more than one return statement in a
function, you should keep in mind that as soon as one is executed, the function
| terminates without | executing | any subsequent | statements. |
| ------------------ | --------- | -------------- | ----------- |
Code that appears after a return statement, or any place else where it can
never be executed, is called dead code. Some compilers warn you if part of
| your code is | dead. |     |     |
| ------------ | ----- | --- | --- |
If you put return statements inside a conditional, then you have to guarantee
that every possible path through the program hits a return statement. For
example:
| double AbsoluteValue |     | (double x) |     |
| -------------------- | --- | ---------- | --- |
{
| if (x | < 0) |     |     |
| ----- | ---- | --- | --- |
{
return -x;
}
| else | if (x > 0) |     |     |
| ---- | ---------- | --- | --- |
{

| 5.2 | Program | development |     |     |     |            |     |     | 51  |
| --- | ------- | ----------- | --- | --- | --- | ---------- | --- | --- | --- |
|     |         | return      | x;  |     |     |            |     |     |     |
|     | }       |             |     |     |     | /* WRONG!! |     | */  |     |
}
Thisprogramisnotcorrectbecauseifxhappenstobe0,thenneithercondition
will be true and the function will end without hitting a return statement. Un-
fortunately, manyCcompilersdonotcatchthiserror. Asaresult, theprogram
may compile and run, but the return value when x==0 could be anything, and
| will | probably | be  | different | in different |     | environments. |     |     |     |
| ---- | -------- | --- | --------- | ------------ | --- | ------------- | --- | --- | --- |
By now you are probably sick of seeing compiler errors, but as you gain more
experience, you will realize that the only thing worse than getting a compiler
| error | is not | getting | a compiler |     | error when | your | program | is wrong. |     |
| ----- | ------ | ------- | ---------- | --- | ---------- | ---- | ------- | --------- | --- |
Here’sthekindofthingthat’slikelytohappen: youtestAbsoluteValue()with
severalvaluesofxanditseemstoworkcorrectly. Thenyougiveyourprogramto
someoneelseandtheyrunitinanotherenvironment. Itfailsinsomemysterious
way, andittakesdaysofdebuggingtodiscoverthattheproblemisanincorrect
implementation of AbsoluteValue(). If only the compiler had warned you!
From now on, if the compiler points out an error in your program, you should
notblamethecompiler. Rather,youshouldthankthecompilerforfindingyour
error and sparing you days of debugging. Some compilers have an option that
tells them to be extra strict and report all the errors they can find. You should
| turn | this | option | on all | the time. |     |     |     |     |     |
| ---- | ---- | ------ | ------ | --------- | --- | --- | --- | --- | --- |
Asanaside, youshouldknowthatthereisafunctioninthemathlibrarycalled
| fabs() | that    | calculates |     | the absolute | value | of a | double | – correctly. |     |
| ------ | ------- | ---------- | --- | ------------ | ----- | ---- | ------ | ------------ | --- |
| 5.2    | Program |            |     | development  |       |      |        |              |     |
At this point you should be able to look at complete C functions and tell what
they do. But it may not be clear yet how to go about writing them. I am going
| to  | suggest | one technique |     | that I | call incremental |     | development. |     |     |
| --- | ------- | ------------- | --- | ------ | ---------------- | --- | ------------ | --- | --- |
Asanexample,imagineyouwanttofindthedistancebetweentwopoints,given
| by  | the coordinates |     | (x ,y | ) and | (x ,y | ). By the | usual | definition, |     |
| --- | --------------- | --- | ----- | ----- | ----- | --------- | ----- | ----------- | --- |
|     |                 |     | 1     | 1     | 2 2   |           |       |             |     |
p
|     |     |     | distance= |     | (x  | −x )2+(y | −y  | )2  | (5.1) |
| --- | --- | --- | --------- | --- | --- | -------- | --- | --- | ----- |
|     |     |     |           |     | 2   | 1        | 2   | 1   |       |
The first step is to consider what a Distance function should look like in C. In
other words, what are the inputs (parameters) and what is the output (return
value).
In this case, the two points are the parameters, and it is natural to represent
themusingfourdoubles. Thereturnvalueisthedistance,whichwillhavetype
double.
| Already | we  | can write | an  | outline | of the | function: |     |     |     |
| ------- | --- | --------- | --- | ------- | ------ | --------- | --- | --- | --- |

52 Fruitful functions
double Distance (double x1, double y1, double x2, double y2)
{
return 0.0;
}
The return statement is a placekeeper so that the function will compile and
return something, even though it is not the right answer. At this stage the
function doesn’t do anything useful, but it is worthwhile to try compiling it so
we can identify any syntax errors before we make it more complicated.
In order to test the new function, we have to call it with sample values. Some-
where in main() I would add:
double dist = Distance (1.0, 2.0, 4.0, 6.0);
printf ("%f\n" dist);
Ichosethesevaluessothatthehorizontaldistanceis3andtheverticaldistance
is 4; that way, the result will be 5 (the hypotenuse of a 3-4-5 triangle). When
you are testing a function, it is useful to know the right answer.
Oncewehavecheckedthesyntaxofthefunctiondefinition,wecanstartadding
lines of code one at a time. After each incremental change, we recompile and
runtheprogram. Thatway,atanypointweknowexactlywheretheerrormust
be—in the last line we added.
The next step in the computation is to find the differences x −x and y −y .
2 1 2 1
I will store those values in temporary variables named dx and dy.
double Distance (double x1, double y1, double x2, double y2)
{
double dx = x2 - x1;
double dy = y2 - y1;
printf ("dx is %f\n", dx);
printf ("dy is %f\n", dy;
return 0.0;
}
Iaddedoutputstatementsthatwillletmechecktheintermediatevaluesbefore
proceeding. As I mentioned, I already know that they should be 3.0 and 4.0.
When the function is finished I will remove the output statements. Code like
that is called scaffolding, because it is helpful for building the program, but
it is not part of the final product. Sometimes it is a good idea to keep the
scaffolding around, but comment it out, just in case you need it later.
The next step in the development is to square dx and dy. We could use the
pow() function, but it is simpler and faster to just multiply each term by itself.
double Distance (double x1, double y1, double x2, double y2)
{
double dx = x2 - x1;
double dy = y2 - y1;
double dsquared = dx*dx + dy*dy;
printf ("d_squared is %f\n", dsquared);

5.3 Composition 53
return 0.0;
}
Again, I would compile and run the program at this stage and check the inter-
mediate value (which should be 25.0).
Finally, we can use the sqrt() function to compute and return the result.
double Distance (double x1, double y1, double x2, double y2)
{
double dx = x2 - x1;
double dy = y2 - y1;
double dsquared = dx*dx + dy*dy;
double result = sqrt (dsquared);
return result;
}
Then in main(), we should output and check the value of the result.
As you gain more experience programming, you might find yourself writing
and debugging more than one line at a time. Nevertheless, this incremental
development process can save you a lot of debugging time.
The key aspects of the process are:
• Start with a working program and make small, incremental changes. At
any point, if there is an error, you will know exactly where it is.
• Use temporary variables to hold intermediate values so you can output
and check them.
• Once the program is working, you might want to remove some of the
scaffoldingorconsolidatemultiplestatementsintocompoundexpressions,
but only if it does not make the program difficult to read.
5.3 Composition
As you should expect by now, once you define a new function, you can use it as
partofanexpression, andyoucanbuildnewfunctionsusingexistingfunctions.
For example, what if someone gave you two points, the center of the circle and
a point on the perimeter, and asked for the area of the circle?
Let’ssaythecenterpointisstoredinthevariablesxcandyc,andtheperimeter
pointisinxpandyp. Thefirststepistofindtheradiusofthecircle,whichisthe
distance between the two points. Fortunately, we have a function, Distance(),
that does that.
double radius = Distance (xc, yc, xp, yp);
The second step is to find the area of a circle with that radius, and return it.
double result = Area (radius);
return result;

| 54       |     |          |         |           |         |     | Fruitful functions |
| -------- | --- | -------- | ------- | --------- | ------- | --- | ------------------ |
| Wrapping |     | that all | up in a | function, | we get: |     |                    |
double AreaFromPoints (double xc, double yc, double xp, double yp)
{
|     | double | radius  | =   | Distance | (xc, yc,  | xp, | yp); |
| --- | ------ | ------- | --- | -------- | --------- | --- | ---- |
|     | double | result  | =   | Area     | (radius); |     |      |
|     | return | result; |     |          |           |     |      |
}
The temporary variables radius and area are useful for development and de-
bugging, but once the program is working we can make it more concise by
| composing |     | the function | calls: |     |     |     |     |
| --------- | --- | ------------ | ------ | --- | --- | --- | --- |
double AreaFromPoints (double xc, double yc, double xp, double yp)
{
|     | return | Area | (Distance |     | (xc, yc, xp, | yp)); |     |
| --- | ------ | ---- | --------- | --- | ------------ | ----- | --- |
}
| 5.4 | Boolean |     | values |     |     |     |     |
| --- | ------- | --- | ------ | --- | --- | --- | --- |
The types we have seen so far can hold very large values. There are a lot of
integersintheworld,andevenmorefloating-pointnumbers. Bycomparison,the
set of characters is pretty small. Well, many computing languages implement
an even more fundamental type that is even smaller. It is called _Bool, and
| the | only values | in  | it are true | and | false. |     |     |
| --- | ----------- | --- | ----------- | --- | ------ | --- | --- |
Unfortunately, earlier versions of the C standard did not implement boolean
as a separate type, but instead used the integer values 0 and 1 to represent
truth values. By convention 0 represents false and 1 represents true. Strictly
speaking C interprets any integer value different from 0 as true. This can be a
source of error if you are testing a value to be true by comparing it with 1.
Without thinking about it, we have been using boolean values in the last of
chapter. The condition inside an if statement is a boolean expression. Also,
| the | result | of a comparison |     | operator | is a boolean | value. | For example: |
| --- | ------ | --------------- | --- | -------- | ------------ | ------ | ------------ |
| if  | (x     | == 5)           |     |          |              |        |              |
{
|     | /* do | something*/ |     |     |     |     |     |
| --- | ----- | ----------- | --- | --- | --- | --- | --- |
}
| The | operator | ==  | compares | two integers | and produces |     | a boolean value. |
| --- | -------- | --- | -------- | ------------ | ------------ | --- | ---------------- |
PreC99hasnokeywordsfortheexpressionoftrueorfalse. Alotofprograms
instead are using C preprocessor definitions anywhere a boolean expression is
| called  | for. | For example, |     |     |     |     |     |
| ------- | ---- | ------------ | --- | --- | --- | --- | --- |
| #define |      | FALSE        | 0   |     |     |     |     |
| #define |      | TRUE         | 1   |     |     |     |     |
...
if (TRUE)
{

| 5.5 | Boolean | variables |        |          |     |     |     |     | 55  |
| --- | ------- | --------- | ------ | -------- | --- | --- | --- | --- | --- |
|     | /* will | be        | always | executed |     | */  |     |     |     |
}
is a standard idiom for a loop that should run forever (or until it reaches a
| return | or  | break   | statement). |           |     |     |     |     |     |
| ------ | --- | ------- | ----------- | --------- | --- | --- | --- | --- | --- |
| 5.5    |     | Boolean |             | variables |     |     |     |     |     |
SincebooleanvaluesarenotsupporteddirectlyinC,wecannotdeclarevariables
of the type boolean. Instead, programmers typically use the short datatype in
| combination |     | with  | preprocessor |     | definitions |     | to store | truth values. |     |
| ----------- | --- | ----- | ------------ | --- | ----------- | --- | -------- | ------------- | --- |
| #define     |     | FALSE | 0            |     |             |     |          |               |     |
| #define     |     | TRUE  | 1            |     |             |     |          |               |     |
...
| short |     | fred;      |     |          |     |     |     |     |     |
| ----- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- |
| fred  | =   | TRUE;      |     |          |     |     |     |     |     |
| short |     | testResult |     | = FALSE; |     |     |     |     |     |
The first line is a simple variable declaration; the second line is an assignment,
and the third line is a combination of a declaration and as assignment, called
an initialization.
As I mentioned, the result of a comparison operator is a boolean, so you can
| store | it in | a variable   |         |      |             |           |         |                  |     |
| ----- | ----- | ------------ | ------- | ---- | ----------- | --------- | ------- | ---------------- | --- |
| short |       | evenFlag     | =       | (n%2 | == 0);      |           | /* true | if n is even */  |     |
| short |       | positiveFlag |         | =    | (x > 0);    |           | /* true | if x is positive | */  |
| and   | then  | use it       | as part | of a | conditional | statement | later   |                  |     |
if (evenFlag)
{
|     | printf("n |     | was | even | when | I checked | it"); |     |     |
| --- | --------- | --- | --- | ---- | ---- | --------- | ----- | --- | --- |
}
Avariableusedinthiswayiscalledaflag,sinceitflagsthepresenceorabsence
of some condition.
| 5.6 |     | Logical |     | operators |     |     |     |     |     |
| --- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- |
TherearethreelogicaloperatorsinC:AND,ORandNOT,whicharedenoted
by the symbols &&, || and !. The semantics (meaning) of these operators is
similartotheirmeaninginEnglish. Forexamplex > 0 && x < 10istrueonly
| if x | is greater | than | zero | AND | less | than 10. |     |     |     |
| ---- | ---------- | ---- | ---- | --- | ---- | -------- | --- | --- | --- |
evenFlag || n%3 == 0 is true if either of the conditions is true, that is, if
| evenFlag |     | is true | OR  | the number |     | is divisible | by 3. |     |     |
| -------- | --- | ------- | --- | ---------- | --- | ------------ | ----- | --- | --- |
Finally, the NOT operator has the effect of negating or inverting a bool ex-
pression, so !evenFlag is true if evenFlag is false; that is, if the number is
odd.

56 Fruitful functions
Logicaloperatorsoftenprovideawaytosimplifynestedconditionalstatements.
Forexample,howwouldyouwritethefollowingcodeusingasingleconditional?
| if  | (x > 0) |     |     |     |
| --- | ------- | --- | --- | --- |
{
|     | if (x < 10) |     |     |     |
| --- | ----------- | --- | --- | --- |
{
|     | printf | ("x | is a positive | single digit.\n"); |
| --- | ------ | --- | ------------- | ------------------ |
}
}
| 5.7 | Bool | functions |     |     |
| --- | ---- | --------- | --- | --- |
It is sometimes appropriate for functions to return boolean values just like any
other return type. This is is especially convenient for hiding complicated tests
| inside | functions.    | For example: |         |     |
| ------ | ------------- | ------------ | ------- | --- |
| int    | IsSingleDigit |              | (int x) |     |
{
|     | if (x >= | 0 && | x < 10) |     |
| --- | -------- | ---- | ------- | --- |
{
|     | return | TRUE; |     |     |
| --- | ------ | ----- | --- | --- |
}
else
{
|     | return | FALSE; |     |     |
| --- | ------ | ------ | --- | --- |
}
}
The name of this function is IsSingleDigit(). It is common to give such test
functionsnamesthatsoundlikeyes/noquestions. Thereturntypeisint,which
means that again we need to follow the agreement that 0 represents and
false
1 represents true. Every return statement has to follow this convention, again,
| we are | using preprocessor |     | definitions. |     |
| ------ | ------------------ | --- | ------------ | --- |
Thecodeitselfisstraightforward,althoughitisabitlongerthanitneedstobe.
Remember that the expression x >= 0 && x < 10 is evaluated to a boolean
value, so there is nothing wrong with returning it directly, and avoiding the
if
| statement | altogether:   |     |         |     |
| --------- | ------------- | --- | ------- | --- |
| int       | IsSingleDigit |     | (int x) |     |
{
|     | return | (x >= | 0 && x < | 10); |
| --- | ------ | ----- | -------- | ---- |
}
| In main()      | you can | call          | this function  | in the usual ways: |
| -------------- | ------- | ------------- | -------------- | ------------------ |
| printf("%i\n", |         | IsSingleDigit |                | (2));              |
| short          | bigFlag | =             | !IsSingleDigit | (17);              |

| 5.8 Returning |     | from | main() |     |     |     |     | 57  |
| ------------- | --- | ---- | ------ | --- | --- | --- | --- | --- |
The first line outputs the value true because 2 is a single-digit number. Unfor-
tunately, when C outputs boolean values, it does not display the words TRUE
| and FALSE, | but | rather | the integers | 1 and 0. |     |     |     |     |
| ---------- | --- | ------ | ------------ | -------- | --- | --- | --- | --- |
The second line assigns the value true to bigFlag only if 17 is not a positive
| single-digit | number. |     |     |     |     |     |     |     |
| ------------ | ------- | --- | --- | --- | --- | --- | --- | --- |
The most common use of boolean functions is inside conditional statements
| if  | (IsSingleDigit |     | (x)) |     |     |     |     |     |
| --- | -------------- | --- | ---- | --- | --- | --- | --- | --- |
{
|     | printf("x |     | is little\n"); |     |     |     |     |     |
| --- | --------- | --- | -------------- | --- | --- | --- | --- | --- |
}
else
{
|     | printf("x |     | is big\n"); |     |     |     |     |     |
| --- | --------- | --- | ----------- | --- | --- | --- | --- | --- |
}
| 5.8 | Returning |     | from |     |     |     |     |     |
| --- | --------- | --- | ---- | --- | --- | --- | --- | --- |
main()
Nowthatweknowfunctionsthatreturnvalues,wecanlookmorecloselyatthe
| return | value | of the main() | function. | It’s supposed |     | to return | an integer: |     |
| ------ | ----- | ------------- | --------- | ------------- | --- | --------- | ----------- | --- |
| int    | main  | (void)        |           |               |     |           |             |     |
The usual return value from main() is 0, which indicates that the program
succeeded at whatever it was supposed to to. If something goes wrong, it is
common to return -1, or some other value that indicates what kind of error
occurred.
The C standard library <stdlib.h> provides two predefined constants
EXIT_SUCCESS and EXIT_FAILURE. We can use these to return a descriptive
| result   | from our | return     | statement. |     |     |     |     |     |
| -------- | -------- | ---------- | ---------- | --- | --- | --- | --- | --- |
| #include |          | <stdlib.h> |            |     |     |     |     |     |
| int      | main     | (void)     |            |     |     |     |     |     |
{
|     | return | EXIT_SUCCESS; |     | /*program | terminated |     | successfully*/ |     |
| --- | ------ | ------------- | --- | --------- | ---------- | --- | -------------- | --- |
}
Of course, you might wonder who this value gets returned to, since we never
call main() ourselves. It turns out that when the operating system executes a
program,itstartsbycallingmain()inprettymuchthesamewayitcallsallthe
other functions. When the program terminates it passes a value back that tells
if the execution was successful or not. The operating system can use this value
| to create | error | reports | or even pass | this value | on  | to other | programs. |     |
| --------- | ----- | ------- | ------------ | ---------- | --- | -------- | --------- | --- |
There are even some parameters that can be passed to main() by the system,
but we are not going to deal with them for a little while, so we define main()
| as having | no  | parameters: | int main | (void). |     |     |     |     |
| --------- | --- | ----------- | -------- | ------- | --- | --- | --- | --- |

| 58  |     |     |     |     |     |     |     | Fruitful | functions |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- |
5.9 Glossary
| return | type:  | The | type  | of value | a function |     | returns.    |          |       |     |
| ------ | ------ | --- | ----- | -------- | ---------- | --- | ----------- | -------- | ----- | --- |
| return | value: | The | value | provided | as         | the | result of a | function | call. |     |
dead code: Part of a program that can never be executed, often because it
|     | appears | after | a return | statement. |     |     |     |     |     |     |
| --- | ------- | ----- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
scaffolding: Code that is used during program development but is not part of
|     | the final | version. |     |     |     |     |     |     |     |     |
| --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
void: A special return type that indicates a void function; that is, one that
|     | does | not return | a   | value. |     |     |     |     |     |     |
| --- | ---- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- |
boolean: A value or variable that can take on one of two states, often called
|       | true       | and false. |                  | In C, boolean |            | values | are mainly          | stored    | in variables | of  |
| ----- | ---------- | ---------- | ---------------- | ------------- | ---------- | ------ | ------------------- | --------- | ------------ | --- |
|       | type       | short      | and preprocessor |               | statements |        | are used            | to define | the states.  |     |
| flag: | A variable |            | that records     | a             | condition  | or     | status information. |           |              |     |
comparison operator: An operator that compares two values and produces
|     | a boolean | that | indicates |     | the relationship |     | between | the | operands. |     |
| --- | --------- | ---- | --------- | --- | ---------------- | --- | ------- | --- | --------- | --- |
logical operator: An operator that combines boolean values in order to test
|      | compound  |     | conditions. |     |     |     |     |     |     |     |
| ---- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| 5.10 | Exercises |     |             |     |     |     |     |     |     |     |
Exercise 5.1 Ifyouaregiventhreesticks,youmayormaynotbeabletoarrange
them in a triangle. For example, if one of the sticks is 12 inches long and the other
two are one inch long, it is clear that you will not be able to get the short sticks to
meetinthemiddle. Foranythreelengths,thereisasimpletesttoseeifitispossible
| to form | a triangle: |        |           |             |     |            |           |        |                |     |
| ------- | ----------- | ------ | --------- | ----------- | --- | ---------- | --------- | ------ | -------------- | --- |
|         | “If         | any of | the three | lengths     | is  | greater    | than the  | sum of | the other two, |     |
|         | then you    | cannot | form      | a triangle. |     | Otherwise, | you can.” |        |                |     |
Write a function named IsTriangle() that it takes three integers as arguments, and
that returns either TRUE or FALSE, depending on whether you can or cannot form a
| triangle | from | sticks | with | the given | lengths. |     |     |     |     |     |
| -------- | ---- | ------ | ---- | --------- | -------- | --- | --- | --- | --- | --- |
The point of this exercise is to use conditional statements to write a function that
returns a value.
| Exercise | 5.2 |     | What | is the output | of  | the following | program? |     |     |     |
| -------- | --- | --- | ---- | ------------- | --- | ------------- | -------- | --- | --- | --- |
Thepurposeofthisexerciseistomakesureyouunderstandlogicaloperatorsandthe
| flow | of execution | through |     | fruitful | methods. |     |     |     |     |     |
| ---- | ------------ | ------- | --- | -------- | -------- | --- | --- | --- | --- | --- |

5.10 Exercises 59
#define TRUE 1
#define FALSE 0
| short IsHoopy | (int x) |     |
| ------------- | ------- | --- |
{
short hoopyFlag;
| if (x%2 | == 0) |     |
| ------- | ----- | --- |
{
| hoopyFlag | = TRUE; |     |
| --------- | ------- | --- |
}
else
{
| hoopyFlag | = FALSE; |     |
| --------- | -------- | --- |
}
return hoopyFlag;
}
| short IsFrabjuous | (int x) |     |
| ----------------- | ------- | --- |
{
short frabjuousFlag;
if (x > 0)
{
| frabjuousFlag | = TRUE; |     |
| ------------- | ------- | --- |
}
else
{
| frabjuousFlag | = FALSE; |     |
| ------------- | -------- | --- |
}
return frabjuousFlag;
}
int main (void)
{
| short flag1     | = IsHoopy     | (202); |
| --------------- | ------------- | ------ |
| short flag2     | = IsFrabjuous | (202); |
| printf ("%i\n", | flag1);       |        |
| printf ("%i\n", | flag2);       |        |
| if (flag1       | && flag2)     |        |
{
| printf | ("ping!\n"); |     |
| ------ | ------------ | --- |
}
| if (flag1 | || flag2) |     |
| --------- | --------- | --- |
{
| printf | ("pong!\n"); |     |
| ------ | ------------ | --- |
}
return EXIT_SUCCESS;
}

60 Fruitful functions
Exercise 5.3
a. Create a new program called Sum.c, and type in the following two functions.
int FunctionOne (int m, int n)
{
if (m == n)
{
return n;
}
else
{
return m + FunctionOne (m+1, n);
}
}
int FunctionTwo (int m, int n)
{
if (m == n)
{
return n;
}
else
{
return n * FunctionTwo (m, n-1);
}
}
b. Write a few lines in main() to test these functions. Invoke them a couple of
times, with a few different values, and see what you get. By some combination
oftestingandexaminationofthecode,figureoutwhatthesefunctionsdo, and
give them more meaningful names. Add comments that describe their function
abstractly.
c. Addaprinfstatementtothebeginningofbothfunctionssothattheyprinttheir
argumentseachtimetheyareinvoked. Thisisausefultechniquefordebugging
recursive programs, since it demonstrates the flow of execution.
Exercise 5.4 WritearecursivefunctioncalledPower()thattakesadoublexand
an integer n and that returns xn.
Hint: arecursivedefinitionofthisoperationisPower (x, n) = x * Power (x, n-1).
Also, remember that anything raised to the zeroeth power is 1.
Exercise 5.5
(This exercise is based on page 44 of Ableson and Sussman’s Structure and Interpre-
tation of Computer Programs.)
ThefollowingalgorithmisknownasEuclid’sAlgorithmbecauseitappearsinEuclid’s
Elements (Book 7, ca. 300 B.C.). It may be the oldest nontrivial algorithm.

5.10 Exercises 61
Thealgorithmisbasedontheobservationthat,ifristheremainderwhenaisdivided
by b, then the common divisors of a and b are the same as the common divisors of b
| and r. Thus | we  | can use | the equation |     |     |     |     |
| ----------- | --- | ------- | ------------ | --- | --- | --- | --- |
gcd(a,b)=gcd(b,r)
tosuccessivelyreducetheproblemofcomputingaGCDtotheproblemofcomputing
| the GCD | of smaller | and | smaller | pairs of | integers. | For example, |     |
| ------- | ---------- | --- | ------- | -------- | --------- | ------------ | --- |
gcd(36,20)=gcd(20,16)=gcd(16,4)=gcd(4,0)=4
implies that the GCD of 36 and 20 is 4. It can be shown that for any two starting
numbers,thisrepeatedreductioneventuallyproducesapairwherethesecondnumber
| is 0. Then | the GCD | is the | other | number | in the pair. |     |     |
| ---------- | ------- | ------ | ----- | ------ | ------------ | --- | --- |
Write a function called gcd that takes two integer parameters and that uses Euclid’s
algorithmtocomputeandreturnthegreatestcommondivisorofthetwonumbers.
| Exercise | 5.6 | The distance |     | between | two points | (x 1 ,y 1 ) and (x | 2 ,y 2 ) is |
| -------- | --- | ------------ | --- | ------- | ---------- | ------------------ | ----------- |
p
|     |     |     | Distance= | (x  | 2 −x 1 )2+(y | 2 −y 1 )2 |     |
| --- | --- | --- | --------- | --- | ------------ | --------- | --- |
PleasewriteafunctionnamedDistance()thattakesfourdoublesasparameters—x1,
| y1, x2 and | y2—and | that | prints | the distance | between | the points. |     |
| ---------- | ------ | ---- | ------ | ------------ | ------- | ----------- | --- |
You should assume that there is a function named SumSquares() that calculates and
| returns      | the sum | of the squares |     | of its arguments. |     | For example: |     |
| ------------ | ------- | -------------- | --- | ----------------- | --- | ------------ | --- |
| double       | x =     | SumSquares     |     | (3.0, 4.0);       |     |              |     |
| would assign | the     | value 25.0     | to  | x.                |     |              |     |
The point of this exercise is to write a new function that uses an existing one. You
should write only one function: Distance(). You should not write SumSquares() or
| main() | and you | should | not invoke | Distance(). |     |     |     |
| ------ | ------- | ------ | ---------- | ----------- | --- | --- | --- |
Exercise5.7 Thepointofthisexerciseistopracticethesyntaxoffruitfulfunctions.
a. Use your existing solution to Exercise 3.4 and make sure you can still compile
| and | run it. |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- |
b. TransformMultadd()intoafruitfulfunction,sothatinsteadofprintingaresult,
| it  | returns | it. |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- |
c. EverywhereintheprogramthatMultadd()getsinvoked,changetheinvocation
| so           | that it | stores the | result | in a variable | and/or | prints the result. |     |
| ------------ | ------- | ---------- | ------ | ------------- | ------ | ------------------ | --- |
| d. Transform |         | Yikes()    | in the | same way.     |        |                    |     |

62 Fruitful functions

| Chapter |     | 6   |     |
| ------- | --- | --- | --- |
Iteration
| 6.1 | Multiple | assignment |     |
| --- | -------- | ---------- | --- |
I haven’t said much about it, but it is legal in C to make more than one assign-
menttothesamevariable. Theeffectofthesecondassignmentistoreplacethe
| old value | of the variable | with a new | value. |
| --------- | --------------- | ---------- | ------ |
| int       | fred = 5;       |            |        |
| printf    | ("%i", fred);   |            |        |
| fred      | = 7;            |            |        |
| printf    | ("%i", fred);   |            |        |
Theoutputofthisprogramis57, becausethefirsttimeweprintfredhisvalue
| is 5, and | the second | time his value | is 7. |
| --------- | ---------- | -------------- | ----- |
This kind of multiple assignment is the reason I described variables as a
container for values. When you assign a value to a variable, you change the
| contents | of the container, | as shown | in the figure: |
| -------- | ----------------- | -------- | -------------- |
int fred = 5; fred 5
fred = 7; fred 5 7
When there are multiple assignments to a variable, it is especially important to
distinguish between an assignment statement and a statement of equality. Be-
causeCusesthe=symbolforassignment,itistemptingtointerpretastatement
| like a = | b as a statement | of equality. | It is not! |
| -------- | ---------------- | ------------ | ---------- |
First of all, equality is commutative, and assignment is not. For example, in
mathematics if a = 7 then 7 = a. But in C the statement a = 7; is legal, and
| 7 = a; | is not. |     |     |
| ------ | ------- | --- | --- |

| 64  |     |     |     |     |     |     | Iteration |
| --- | --- | --- | --- | --- | --- | --- | --------- |
Furthermore, in mathematics, a statement of equality is true for all time. If
a=b now, then a will always equal b. In C, an assignment statement can make
| two variables | equal, | but | they  | don’t | have to stay | that way! |     |
| ------------- | ------ | --- | ----- | ----- | ------------ | --------- | --- |
| int a         | = 5;   |     |       |       |              |           |     |
| int b         | = a;   | /*  | a and | b are | now equal    | */        |     |
| a = 3;        |        | /*  | a and | b are | no longer    | equal     | */  |
The third line changes the value of a but it does not change the value of b,
and so they are no longer equal. In many programming languages an alternate
symbol is used for assignment, such as <- or :=, in order to avoid confusion.
Although multiple assignment is frequently useful, you should use it with cau-
tion. If the values of variables are changing constantly in different parts of the
| program, | it can | make | the code | difficult | to read | and debug. |     |
| -------- | ------ | ---- | -------- | --------- | ------- | ---------- | --- |
6.2 Iteration
One of the things computers are often used for is the automation of repetitive
tasks. Repeating identical or similar tasks without making errors is something
| that computers |     | do well | and people |     | do poorly. |     |     |
| -------------- | --- | ------- | ---------- | --- | ---------- | --- | --- |
Insection4.7wehaveseenprogramsthatuserecursiontoperformrepetition,
such as PrintLines() and Countdown(). I now want to introduce a new type
of repetition, that is called iteration, and C provides several language features
| that make | it easier | to  | write repetetive |     | programs. |     |     |
| --------- | --------- | --- | ---------------- | --- | --------- | --- | --- |
The two features we are going to look at are the while statement and the for
statement.
| 6.3     | The              | while | statement |             |              |     |     |
| ------- | ---------------- | ----- | --------- | ----------- | ------------ | --- | --- |
| Using a | while statement, |       | we        | can rewrite | Countdown(): |     |     |
| void    | Countdown        | (int  | n)        |             |              |     |     |
{
| while | (n  | > 0) |     |     |     |     |     |
| ----- | --- | ---- | --- | --- | --- | --- | --- |
{
|     | printf | ("%i\n", |     | n); |     |     |     |
| --- | ------ | -------- | --- | --- | --- | --- | --- |
n = n-1;
}
| printf | ("Blastoff!\n"); |     |     |     |     |     |     |
| ------ | ---------------- | --- | --- | --- | --- | --- | --- |
}
You can almost read a while statement as if it were English. What this means
is, “While n is greater than zero, continue displaying the value of n and then
reducingthevalueofnby1. Whenyougettozero,outputtheword‘Blastoff!”’
| More formally, | the | flow | of execution |     | for a while | statement | is as follows: |
| -------------- | --- | ---- | ------------ | --- | ----------- | --------- | -------------- |

| 6.3 The     | while | statement     |     |                 |     |               |           | 65  |
| ----------- | ----- | ------------- | --- | --------------- | --- | ------------- | --------- | --- |
| 1. Evaluate |       | the condition |     | in parentheses, |     | yielding true | or false. |     |
2. If the condition is false, exit the while statement and continue execution
| at  | the next | statement. |     |     |     |     |     |     |
| --- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
3. If the condition is true, execute each of the statements between the curly-
| brackets, |     | and then | go back | to  | step 1. |     |     |     |
| --------- | --- | -------- | ------- | --- | ------- | --- | --- | --- |
This type of flow is called a loop because the third step loops back around to
the top. Notice that if the condition is false the first time through the loop, the
statements inside the loop are never executed. The statements inside the loop
| are called | the body |     | of the loop. |     |     |     |     |     |
| ---------- | -------- | --- | ------------ | --- | --- | --- | --- | --- |
The body of the loop should change the value of one or more variables so that,
eventually, the condition becomes false and the loop terminates. Otherwise the
loop will repeat forever, which is called an infinite loop. An endless source
of amusement for computer scientists is the observation that the directions on
| shampoo, | “Lather, | rinse, | repeat,” | are | an infinite | loop. |     |     |
| -------- | -------- | ------ | -------- | --- | ----------- | ----- | --- | --- |
In the case of Countdown(), we can prove that the loop will terminate because
we know that the value of is finite, and we can see that the value of gets
|     |     |     | n   |     |     |     |     | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
smaller each time through the loop (each iteration), so eventually we have to
| get to zero. | In       | other | cases it | is not | so easy to | tell: |     |     |
| ------------ | -------- | ----- | -------- | ------ | ---------- | ----- | --- | --- |
| void         | Sequence | (int  | n)       |        |            |       |     |     |
{
| while | (n  | !=  | 1)  |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- |
{
|     | printf | ("%i\n", |       | n); |         |         |     |     |
| --- | ------ | -------- | ----- | --- | ------- | ------- | --- | --- |
|     | if     | (n%2     | == 0) |     | /* n is | even */ |     |     |
{
|     |     | n = | n / 2; |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- |
}
|     | else |     |     |     | /* n is | odd */ |     |     |
| --- | ---- | --- | --- | --- | ------- | ------ | --- | --- |
{
|     |     | n = | n*3 + | 1;  |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- |
}
}
}
The condition for this loop is n != 1, so the loop will continue until n is 1,
| which will | make | the | condition | false. |     |     |     |     |
| ---------- | ---- | --- | --------- | ------ | --- | --- | --- | --- |
At each iteration, the program outputs the value of n and then checks whether
it is even or odd. If it is even, the value of n is divided by two. If it is odd, the
value is replaced by 3n+1. For example, if the starting value (the argument
| passed to | Sequence) |     | is 3, the | resulting | sequence | is 3, 10, | 5, 16, 8, 4, 2, 1. |     |
| --------- | --------- | --- | --------- | --------- | -------- | --------- | ------------------ | --- |
Since n sometimes increases and sometimes decreases, there is no obvious proof
thatnwilleverreach1,orthattheprogramwillterminate. Forsomeparticular
values of n, we can prove termination. For example, if the starting value is a

| 66  |     |     |     | Iteration |
| --- | --- | --- | --- | --------- |
poweroftwo,thenthevalueofnwillbeeveneverytimethroughtheloop,until
we get to 1. The previous example ends with such a sequence, starting with 16.
Particular values aside, the interesting question is whether we can prove that
this program terminates for all values of n. So far, no one has been able to
| prove it | or disprove it! |     |     |     |
| -------- | --------------- | --- | --- | --- |
6.4 Tables
One of the things loops are good for is generating tabular data. For example,
before computers were readily available, people had to calculate logarithms,
sines and cosines, and other common mathematical functions by hand. To
make that easier, there were books containing long tables where you could find
the values of various functions. Creating these tables was slow and boring, and
| the result | tended to be full | of errors. |     |     |
| ---------- | ----------------- | ---------- | --- | --- |
When computers appeared on the scene, one of the initial reactions was, “This
is great! We can use the computers to generate the tables, so there will be no
errors.” That turned out to be true (mostly), but shortsighted. Soon thereafter
computers and calculators were so pervasive that the tables became obsolete.
Well, almost. It turns out that for some operations, computers use tables of
valuestogetanapproximateanswer,andthenperformcomputationstoimprove
the approximation. In some cases, there have been errors in the underlying
tables, most famously in the table the original Intel Pentium used to perform
| floating-point | division. |     |     |     |
| -------------- | --------- | --- | --- | --- |
Although a “log table” is not as useful as it once was, it still makes a good
exampleofiteration. Thefollowingprogramoutputsasequenceofvaluesinthe
| left column | and their logarithms | in the | right column: |     |
| ----------- | -------------------- | ------ | ------------- | --- |
| double      | x = 1.0;             |        |               |     |
| while       | (x < 10.0)           |        |               |     |
{
| printf | ("%.0f\t%f\n", | x ,log(x)); |     |     |
| ------ | -------------- | ----------- | --- | --- |
| x      | = x + 1.0;     |             |     |     |
}
The sequence \t represents a tab character. The sequence \n represents a
newlinecharacter. Theyaresocalledescapesequences whichareusedtoencode
non-printableASCII-characters. Escapesequencescanbeincludedanywherein
| a string, | although in these | examples the | sequence is the whole | string. |
| --------- | ----------------- | ------------ | --------------------- | ------- |
A tab character causes the cursor to shift to the right until it reaches one of
the tab stops, which are normally every eight characters. As we will see in a
minute, tabsareusefulformakingcolumnsoftextlineup. Anewlinecharacter
| causes the | cursor to move  | on to the next | line. |     |
| ---------- | --------------- | -------------- | ----- | --- |
| The output | of this program | is:            |       |     |

6.4 Tables 67
|     | 1   | 0.000000 |     |     |     |
| --- | --- | -------- | --- | --- | --- |
|     | 2   | 0.693147 |     |     |     |
|     | 3   | 1.098612 |     |     |     |
|     | 4   | 1.386294 |     |     |     |
|     | 5   | 1.609438 |     |     |     |
|     | 6   | 1.791759 |     |     |     |
|     | 7   | 1.945910 |     |     |     |
|     | 8   | 2.079442 |     |     |     |
|     | 9   | 2.197225 |     |     |     |
If these values seem odd, remember that the log() function uses base e. Since
powers of two are so important in computer science, we often want to find
logarithmswithrespecttobase2. Todothat,wecanusethefollowingformula:
|     |     |     |     |        | log e x |
| --- | --- | --- | --- | ------ | ------- |
|     |     |     |     | log x= |         |
|     |     |     |     | 2      | log 2   |
e
| Changing |        | the output     | statement | to        |              |
| -------- | ------ | -------------- | --------- | --------- | ------------ |
|          | printf | ("%.0f\t%f\n", |           | x, log(x) | / log(2.0)); |
yields:
|     | 1   | 0.000000 |     |     |     |
| --- | --- | -------- | --- | --- | --- |
|     | 2   | 1.000000 |     |     |     |
|     | 3   | 1.584963 |     |     |     |
|     | 4   | 2.000000 |     |     |     |
|     | 5   | 2.321928 |     |     |     |
|     | 6   | 2.584963 |     |     |     |
|     | 7   | 2.807355 |     |     |     |
|     | 8   | 3.000000 |     |     |     |
|     | 9   | 3.169925 |     |     |     |
We can see that 1, 2, 4 and 8 are powers of two, because their logarithms base
2 are round numbers. If we wanted to find the logarithms of other powers of
| two, | we could | modify      | the program | like this: |     |
| ---- | -------- | ----------- | ----------- | ---------- | --- |
|      | double   | x = 1.0;    |             |            |     |
|      | while    | (x < 100.0) |             |            |     |
{
|     | printf | ("%.0f\t%.0f\n", |     | x,  | log(x) / log(2.0)); |
| --- | ------ | ---------------- | --- | --- | ------------------- |
|     | x      | = x * 2.0;       |     |     |                     |
}
Now instead of adding something to x each time through the loop, which yields
an arithmetic sequence, we multiply by something, yielding a geometric
x
| sequence. |     | The result is: |     |     |     |
| --------- | --- | -------------- | --- | --- | --- |
|           | 1   | 0              |     |     |     |
|           | 2   | 1              |     |     |     |
|           | 4   | 2              |     |     |     |
|           | 8   | 3              |     |     |     |
|           | 16  | 4              |     |     |     |
|           | 32  | 5              |     |     |     |
|           | 64  | 6              |     |     |     |

| 68  |     |     |     |     |     |     | Iteration |
| --- | --- | --- | --- | --- | --- | --- | --------- |
Because we are using tab characters between the columns, the position of the
second column does not depend on the number of digits in the first column.
Log tables may not be useful any more, but for computer scientists, knowing
thepowersoftwois! Asanexercise,modifythisprogramsothatitoutputsthe
216).
| powers | of two          | up to 65536 | (that’s |     | Print  | it out and memorize | it. |
| ------ | --------------- | ----------- | ------- | --- | ------ | ------------------- | --- |
| 6.5    | Two-dimensional |             |         |     | tables |                     |     |
A two-dimensional table is a table where you choose a row and a column and
read the value at the intersection. A multiplication table is a good example.
Let’s say you wanted to print a multiplication table for the values from 1 to 6.
A good way to start is to write a simple loop that prints the multiples of 2, all
on one line.
| int   | i = | 1;    |     |     |     |     |     |
| ----- | --- | ----- | --- | --- | --- | --- | --- |
| while | (i  | <= 6) |     |     |     |     |     |
{
|     | printf("%i |     | ",  | i*2); |     |     |     |
| --- | ---------- | --- | --- | ----- | --- | --- | --- |
i = i + 1;
}
printf("\n");
The first line initializes a variable named i, which is going to act as a counter,
or loop variable. As the loop executes, the value of i increases from 1 to 6,
and then when i is 7, the loop terminates. Each time through the loop, we
print the value 2*i followed by three spaces. By omitting the \n from the first
| output     | statement,    | we get       | all  | the output | on a single    | line.           |     |
| ---------- | ------------- | ------------ | ---- | ---------- | -------------- | --------------- | --- |
| The output | of            | this program | is:  |            |                |                 |     |
| 2          | 4             | 6 8          | 10   | 12         |                |                 |     |
| So far,    | so good.      | The next     | step | is to      | encapsulate    | and generalize. |     |
| 6.6        | Encapsulation |              |      | and        | generalization |                 |     |
Encapsulation usually means taking a piece of code and wrapping it up in a
function,allowingyoutotakeadvantageofallthethingsfunctionsaregoodfor.
Wehaveseentwoexamplesofencapsulation,whenwewrotePrintParity()in
| Section | 4.3 and | IsSingleDigit() |     | in  | Section 5.7. |     |     |
| ------- | ------- | --------------- | --- | --- | ------------ | --- | --- |
Generalizationmeanstakingsomethingspecific,likeprintingmultiplesof2,and
| making | it more | general, | like | printing | the multiples | of any integer. |     |
| ------ | ------- | -------- | ---- | -------- | ------------- | --------------- | --- |
Here’s a function that encapsulates the loop from the previous section and
| generalizes | it to | print multiples |     | of n. |     |     |     |
| ----------- | ----- | --------------- | --- | ----- | --- | --- | --- |

| 6.6 Encapsulation |                | and | generalization |     |     | 69  |
| ----------------- | -------------- | --- | -------------- | --- | --- | --- |
| void              | PrintMultiples |     | (int n)        |     |     |     |
{
int i = 1;
|     | while | (i <= | 6)  |     |     |     |
| --- | ----- | ----- | --- | --- | --- | --- |
{
|     | printf("%i |       | ", i*n); |     |     |     |
| --- | ---------- | ----- | -------- | --- | --- | --- |
|     | i          | = i + | 1;       |     |     |     |
}
printf("\n");
}
To encapsulate, all I had to do was add the first line, which declares the name,
parameter, andreturntype. Togeneralize, allIhadtodowasreplacethevalue
| 2 with the | parameter | n.  |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- | --- |
If we call this function with the argument 2, we get the same output as before.
| With argument |          | 3, the output | is:       |     |     |     |
| ------------- | -------- | ------------- | --------- | --- | --- | --- |
| 3             | 6 9      | 12            | 15 18     |     |     |     |
| and with      | argument | 4, the        | output is |     |     |     |
| 4             | 8 12     | 16            | 20 24     |     |     |     |
Bynowyoucanprobablyguesshowwearegoingtoprintamultiplicationtable:
we’ll call PrintMultiples() repeatedly with different arguments. In fact, we
| are going | to use | another | loop to iterate | through | the rows. |     |
| --------- | ------ | ------- | --------------- | ------- | --------- | --- |
| int       | i = 1; |         |                 |         |           |     |
| while     | (i     | <= 6)   |                 |         |           |     |
{
|     | PrintMultiples |     | (i); |     |     |     |
| --- | -------------- | --- | ---- | --- | --- | --- |
i = i + 1;
}
Firstofall, noticehowsimilarthisloopistotheoneinsidePrintMultiples().
I only replaced the call of the printf() function with the call of the
| PrintMultiples() |      | function.    |       |     |     |     |
| ---------------- | ---- | ------------ | ----- | --- | --- | --- |
| The output       | of   | this program | is    |     |     |     |
| 1                | 2 3  | 4            | 5 6   |     |     |     |
| 2                | 4 6  | 8            | 10 12 |     |     |     |
| 3                | 6 9  | 12           | 15 18 |     |     |     |
| 4                | 8 12 | 16           | 20 24 |     |     |     |
| 5                | 10   | 15 20        | 25 30 |     |     |     |
| 6                | 12   | 18 24        | 30 36 |     |     |     |
which is a (slightly sloppy) multiplication table. If the sloppiness bothers you,
tryreplacingthespacesbetweencolumnswithtabcharactersandseewhatyou
get.

| 70  |     |     |     |     |     |     | Iteration |
| --- | --- | --- | --- | --- | --- | --- | --------- |
6.7 Functions
In the last section I mentioned “all the things functions are good for.” About
thistime,youmightbewonderingwhatexactlythosethingsare. Herearesome
| of the reasons | functions |     | are useful: |     |     |     |     |
| -------------- | --------- | --- | ----------- | --- | --- | --- | --- |
• By giving a name to a sequence of statements, you make your program
| easier | to read | and | debug. |     |     |     |     |
| ------ | ------- | --- | ------ | --- | --- | --- | --- |
• Dividingalongprogramintofunctionsallowsyoutoseparatepartsofthe
| program,    | debug      | them | in isolation,  | and | then compose   | them into | a whole. |
| ----------- | ---------- | ---- | -------------- | --- | -------------- | --------- | -------- |
| • Functions | facilitate |      | both recursion |     | and iteration. |           |          |
• Well-designed functions are often useful for many programs. Once you
| write    | and debug | one,          | you | can reuse | it. |     |     |
| -------- | --------- | ------------- | --- | --------- | --- | --- | --- |
| 6.8 More |           | encapsulation |     |           |     |     |     |
Todemonstrateencapsulationagain,I’lltakethecodefromtheprevioussection
| and wrap | it up in       | a function: |     |     |     |     |     |
| -------- | -------------- | ----------- | --- | --- | --- | --- | --- |
| void     | PrintMultTable |             | ()  |     |     |     |     |
{
int i = 1;
| while | (i  | <=  | 6)  |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- |
{
|     | PrintMultiples |     |     | (i); |     |     |     |
| --- | -------------- | --- | --- | ---- | --- | --- | --- |
|     | i =            | i + | 1;  |      |     |     |     |
}
}
The process I am demonstrating is a common development plan. You develop
code gradually by adding lines to main() or someplace else, and then when you
| get it working, | you | extract | it and | wrap it | up in a function. |     |     |
| --------------- | --- | ------- | ------ | ------- | ----------------- | --- | --- |
The reason this is useful is that you sometimes don’t know when you start
writing exactly how to divide the program into functions. This approach lets
| you design | as you | go along. |     |     |     |     |     |
| ---------- | ------ | --------- | --- | --- | --- | --- | --- |
| 6.9 Local  |        | variables |     |     |     |     |     |
About this time, you might be wondering how we can use the same variable i
in both PrintMultiples() and PrintMultTable(). Didn’t I say that you can
only declare a variable once? And doesn’t it cause problems when one of the
| functions changes |     | the value | of the | variable? |     |     |     |
| ----------------- | --- | --------- | ------ | --------- | --- | --- | --- |
The answer to both questions is “no,” because the i in PrintMultiples() and
the i in PrintMultTable() are not the same variable. They have the same

| 6.10 More | generalization |     |     |     | 71  |
| --------- | -------------- | --- | --- | --- | --- |
name, but they do not refer to the same storage location, and changing the
| value of | one of them | has no effect | on the other. |     |     |
| -------- | ----------- | ------------- | ------------- | --- | --- |
Rememberthatvariablesthataredeclaredinsideafunctiondefinitionarelocal.
You cannot access a local variable from outside its “home” function, and you
are free to have multiple variables with the same name, as long as they are not
| in the same | function. |     |     |     |     |
| ----------- | --------- | --- | --- | --- | --- |
The stack diagram for this program shows clearlythat the two variablesnamed
i are not in the same storage location. They can have different values, and
| changing | one does not     | affect the       | other.                 |     |     |
| -------- | ---------------- | ---------------- | ---------------------- | --- | --- |
|          |                  | PrintMultiples() |  n      1            i | 3   |     |
|          | PrintMultTable() |                  |                      i | 1   |     |
main()

Notice that the value of the parameter n in PrintMultiples() has to be the
same as the value of i in PrintMultTable(). On the other hand, the value of
i in PrintMultiples() goes from 1 up to 6. In the diagram, it happens to be
| 3. The next | time through | the loop | it will be 4. |     |     |
| ----------- | ------------ | -------- | ------------- | --- | --- |
It is often a good idea to use different variable names in different functions, to
avoid confusion, but there are good reasons to reuse names. For example, it is
common to use the names i, j and k as loop variables. If you avoid using them
in one function just because you used them somewhere else, you will probably
| make the | program harder      | to read. |     |     |     |
| -------- | ------------------- | -------- | --- | --- | --- |
| 6.10     | More generalization |          |     |     |     |
Asanotherexampleofgeneralization,imagineyouwantedaprogramthatwould
print a multiplication table of any size, not just the 6x6 table. You could add a
| parameter | to PrintMultTable(): |      |       |     |     |
| --------- | -------------------- | ---- | ----- | --- | --- |
| void      | PrintMultTable       | (int | high) |     |     |
{
int i = 1;
|     | while (i <= | high) |     |     |     |
| --- | ----------- | ----- | --- | --- | --- |
{
|     | PrintMultiples |      | (i); |     |     |
| --- | -------------- | ---- | ---- | --- | --- |
|     | i = i          | + 1; |      |     |     |
}
}

| 72  |     |     |     |     |     | Iteration |
| --- | --- | --- | --- | --- | --- | --------- |
I replaced the value 6 with the parameter high. If I call PrintMultTable()
| with the argument | 7,    | I get: |     |     |     |     |
| ----------------- | ----- | ------ | --- | --- | --- | --- |
| 1 2 3             | 4     | 5      | 6   |     |     |     |
| 2 4 6             | 8     | 10     | 12  |     |     |     |
| 3 6 9             | 12    | 15     | 18  |     |     |     |
| 4 8 12            | 16    | 20     | 24  |     |     |     |
| 5 10              | 15 20 | 25     | 30  |     |     |     |
| 6 12              | 18 24 | 30     | 36  |     |     |     |
| 7 14              | 21 28 | 35     | 42  |     |     |     |
which is fine, except that I probably want the table to be square (same num-
ber of rows and columns), which means I have to add another parameter to
| PrintMultiples(), | to  | specify | how many | columns | the table should | have. |
| ----------------- | --- | ------- | -------- | ------- | ---------------- | ----- |
Just to be annoying, I will also call this parameter high, demonstrating that
different functions can have parameters with the same name (just like local
variables):
| void PrintMultiples |     | (int | n, int | high) |     |     |
| ------------------- | --- | ---- | ------ | ----- | --- | --- |
{
| int i =  | 1;       |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- |
| while (i | <= high) |     |     |     |     |     |
{
| printf | ("%i |     | ", n*i); |     |     |     |
| ------ | ---- | --- | -------- | --- | --- | --- |
i = i + 1;
}
| printf | ("\n"); |     |     |     |     |     |
| ------ | ------- | --- | --- | --- | --- | --- |
}
| void PrintMultTable |     | (int | high) |     |     |     |
| ------------------- | --- | ---- | ----- | --- | --- | --- |
{
| int i =  | 1;       |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- |
| while (i | <= high) |     |     |     |     |     |
{
| PrintMultiples |     |     | (i, high); |     |     |     |
| -------------- | --- | --- | ---------- | --- | --- | --- |
i = i + 1;
}
}
Notice that when I added a new parameter, I had to change the first line of
the function, and I also had to change the place where the function is called in
PrintMultTable(). As expected, this program generates a square 7x7 table:
| 1 2 3  | 4     | 5   | 6 7   |     |     |     |
| ------ | ----- | --- | ----- | --- | --- | --- |
| 2 4 6  | 8     | 10  | 12 14 |     |     |     |
| 3 6 9  | 12    | 15  | 18    | 21  |     |     |
| 4 8 12 | 16    | 20  | 24    | 28  |     |     |
| 5 10   | 15 20 | 25  | 30    | 35  |     |     |
| 6 12   | 18 24 | 30  | 36    | 42  |     |     |
| 7 14   | 21 28 | 35  | 42    | 49  |     |     |

| 6.11 Glossary |     |     |     |     |     |     |     |     | 73  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
When you generalize a function appropriately, you often find that the resulting
program has capabilities you did not intend. For example, you might notice
thatthemultiplicationtableissymmetric, becauseab=ba, soalltheentriesin
the table appear twice. You could save ink by printing only half the table. To
| do that,       | you only | have | to change | one    | line of | PrintMultTable(). |     | Change |     |
| -------------- | -------- | ---- | --------- | ------ | ------- | ----------------- | --- | ------ | --- |
| PrintMultiples |          |      | (i,       | high); |         |                   |     |        |     |
to
| PrintMultiples |     |     | (i, | i); |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and you get:
1
| 2          | 4        |        |           |         |           |     |     |     |     |
| ---------- | -------- | ------ | --------- | ------- | --------- | --- | --- | --- | --- |
| 3          | 6        | 9      |           |         |           |     |     |     |     |
| 4          | 8        | 12 16  |           |         |           |     |     |     |     |
| 5          | 10       | 15     | 20 25     |         |           |     |     |     |     |
| 6          | 12       | 18     | 24 30     | 36      |           |     |     |     |     |
| 7          | 14       | 21     | 28 35     | 42      | 49        |     |     |     |     |
| I’ll leave | it up    | to you | to figure | out how | it works. |     |     |     |     |
| 6.11       | Glossary |        |           |         |           |     |     |     |     |
loop: A statement that executes repeatedly while a condition is true or until
| some      | condition  | is     | satisfied. |           |           |       |     |     |     |
| --------- | ---------- | ------ | ---------- | --------- | --------- | ----- | --- | --- | --- |
| infinite  | loop:      | A loop | whose      | condition | is always | true. |     |     |     |
| body: The | statements |        | inside     | the loop. |           |       |     |     |     |
iteration: Onepassthrough(executionof)thebodyoftheloop, includingthe
| evaluation |     | of the | condition. |     |     |     |     |     |     |
| ---------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- |
tab: A special character, written as \t in C, that causes the cursor to move to
| the | next | tab stop | on the | current | line. |     |     |     |     |
| --- | ---- | -------- | ------ | ------- | ----- | --- | --- | --- | --- |
encapsulate: To divide a large complex program into components (like func-
| tions) | and         | isolate | the components |     | from | each other | (for | example, | by using |
| ------ | ----------- | ------- | -------------- | --- | ---- | ---------- | ---- | -------- | -------- |
| local  | variables). |         |                |     |      |            |      |          |          |
local variable: A variable that is declared inside a function and that exists
| onlywithinthatfunction. |      |           |     | Localvariablescannotbeaccessedfromoutside |           |      |           |            |     |
| ----------------------- | ---- | --------- | --- | ----------------------------------------- | --------- | ---- | --------- | ---------- | --- |
| their                   | home | function, | and | do not                                    | interfere | with | any other | functions. |     |
generalize: To replace something unnecessarily specific (like a constant value)
| withsomethingappropriatelygeneral(likeavariableorparameter). |     |     |     |     |     |     |     |     | Gen- |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
eralizationmakescodemoreversatile,morelikelytobereused,andsome-
| times | even | easier | to write. |     |     |     |     |     |     |
| ----- | ---- | ------ | --------- | --- | --- | --- | --- | --- | --- |
development plan: A process for developing a program. In this chapter, I
| demonstrated |          | a       | style of | development        | based | on  | developing    | code | to do sim- |
| ------------ | -------- | ------- | -------- | ------------------ | ----- | --- | ------------- | ---- | ---------- |
| ple,         | specific | things, | and      | then encapsulating |       | and | generalizing. |      |            |

74 Iteration
| 6.12     | Exercises   |     |     |
| -------- | ----------- | --- | --- |
| Exercise | 6.1         |     |     |
| void     | Loop(int n) |     |     |
{
|     | int i = n;    |     |     |
| --- | ------------- | --- | --- |
|     | while (i > 1) |     |     |
{
printf ("%i\n",i);
|     | if (i%2 == | 0)  |     |
| --- | ---------- | --- | --- |
{
i = i/2;
}
else
{
i = i+1;
}
}
}
| int | main (void) |     |     |
| --- | ----------- | --- | --- |
{
Loop(10);
|     | return EXIT_SUCCESS; |     |     |
| --- | -------------------- | --- | --- |
}
a. Drawatablethatshowsthevalueofthevariablesiandnduringtheexecution
| oftheprogram. | Thetableshouldcontainonecolumnforeachvariableandone |                  |     |
| ------------- | --------------------------------------------------- | ---------------- | --- |
| line          | for each iteration.                                 |                  |     |
| b. What       | is the output                                       | of this program? |     |
Exercise 6.2 InExercise5.4wewrotearecursiveversionofPower(),whichtakes
adoublexandanintegernandreturnsxn. Nowwriteaniterativefunctiontoperform
the same calculation.
Exercise 6.3 Let’ssayyouaregivenanumber,a,andyouwanttofinditssquare
root. One way to do that is to start with a very rough guess about the answer, x ,
0
| and then | improve the guess | using the following | formula:     |
| -------- | ----------------- | ------------------- | ------------ |
|          |                   | x 1 =(x             | 0 +a/x 0 )/2 |
For example, if we want to find the square root of 9, and we start with x =6, then
0
| x 1 =(6+9/6)/2=15/4=3.75, |     | which | is closer. |
| ------------------------- | --- | ----- | ---------- |
We can repeat the procedure, using x to calculate x , and so on. In this case,
1 2
x =3.075 and x =3.00091. So that is converging very quickly on the right answer
| 2   | 3   |     |     |
| --- | --- | --- | --- |
(which is 3).
Write a function called SquareRoot that takes a double as a parameter and that
returns an approximation of the square root of the parameter, using this algorithm.
| You may | not use the sqrt() | function from | the math.h library. |
| ------- | ------------------ | ------------- | ------------------- |

6.12 Exercises 75
Asyourinitialguess,youshouldusea/2. Yourfunctionshoulditerateuntilitgetstwo
consecutiveestimatesthatdifferbylessthan0.0001;inotherwords,untiltheabsolute
valueofx −x islessthan0.0001. Youcanusethebuilt-infabs()functionfrom
| n                  | n−1          |                     |     |     |
| ------------------ | ------------ | ------------------- | --- | --- |
| the math.h library | to calculate | the absolute value. |     |     |
e−x2
| Exercise 6.4 | One way to evaluate | is to use | the infinite series | expansion |
| ------------ | ------------------- | --------- | ------------------- | --------- |
e−x2 =1−2x+3x2/2!−4x3/3!+5x4/4!−...
In other words, we need to add up a series of terms where the ith term is equal to
(−1)i(i+1)xi/i!. WriteafunctionnamedGauss()thattakesxandnasargumentsand
thatreturnsthesumofthefirstntermsoftheseries. Youshouldnotusefactorial()
or pow().

76 Iteration

| Chapter |     | 7   |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- |
Arrays
A array is a set of values where each value is identified and referenced by a
number(calledanindex). Thenicethingaboutarraysisthattheycanbemade
up of any type of element, including basic types like ints and doubles, but all
| the values | in an array | have | to  | have the same | type. |     |     |
| ---------- | ----------- | ---- | --- | ------------- | ----- | --- | --- |
When you declare an array, you have to determine the number of elements in
| the array. | Otherwise   | the | declaration | looks | similar | to other variable | types: |
| ---------- | ----------- | --- | ----------- | ----- | ------- | ----------------- | ------ |
| int        | c[4];       |     |             |       |         |                   |        |
| double     | values[10]; |     |             |       |         |                   |        |
Syntactically, array variables look like other C variables except that they are
followed by [NUMBER_OF_ELEMENTS], the number of elements in the array en-
closed in square brackets. The first line in our example, int c[4]; is of the
type"arrayofintegers"andcreatesaarrayoffourintegersnamedc. Thesecond
line, double values[10]; has the type "array of doubles" and creates an array
of 10 doubles.
C allows you to to initialize the element values of an array immediately after
you have declared it. The values for the individual elements must be enclosed
| in curly brakets | {}     | and | separated | by comma, |     | as in the following | example: |
| ---------------- | ------ | --- | --------- | --------- | --- | ------------------- | -------- |
| int              | c[4] = | {0, | 0, 0,     | 0};       |     |                     |          |
This statement creates an array of four elements and initializes all of them to
zero. Thissyntaxisonlylegalatinitialisationtime. Laterinyourprogramyou
| can only      | assign values |       | for the | array element  | by          | element. |           |
| ------------- | ------------- | ----- | ------- | -------------- | ----------- | -------- | --------- |
| The following | figure        | shows | how     | arrays are     | represented | in state | diagrams: |
|               |               |       | c 0     | 0 0            | 0           |          |           |
|               |               |       | c[0]    | c[1] c[2] c[3] |             |          |           |
The large numbers inside the boxes are the values of the elements in the
array. Thesmallnumbersoutsidetheboxesaretheindicesusedtoidentifyeach

78 Arrays
box. When you allocate a new array, without initializing, the arrays elements
typically contain arbitrary values and you must initialise them to a meaningful
| value before | using them. |               |     |           |
| ------------ | ----------- | ------------- | --- | --------- |
| 7.1          | Increment   | and decrement |     | operators |
Incrementing and decrementing are such common operations that C provides
specialoperatorsforthem. The++operatoraddsonetothecurrentvalueofan
| int, char | or double, | and -- subtracts | one. |     |
| --------- | ---------- | ---------------- | ---- | --- |
Technically, it is legal to increment a variable and use it in an expression at the
| same time. | For example, | you might | see something | like: |
| ---------- | ------------ | --------- | ------------- | ----- |
| printf     | ("%i\n       | ", i++);  |               |       |
Looking at this, it is not clear whether the increment will take effect before or
after the value is displayed. Because expressions like this tend to be confusing,
I would discourage you from using them. In fact, to discourage you even more,
I’mnotgoingtotellyouwhattheresultis. Ifyoureallywanttoknow, youcan
try it.
Using the increment operators, we can rewrite the PrintMultTable() from
Section 6.10:
| void | PrintMultTable(int | high) |     |     |
| ---- | ------------------ | ----- | --- | --- |
{
int i = 1;
|     | while (i <= | high) |     |     |
| --- | ----------- | ----- | --- | --- |
{
PrintMultiples(i);
i++;
}
}
| It is a common | error      | to write something | like:      |     |
| -------------- | ---------- | ------------------ | ---------- | --- |
| index          | = index++; |                    | /* WRONG!! | */  |
Unfortunately,thisissyntacticallylegal,sothecompilerwillnotwarnyou. The
effect of this statement is to leave the value of index unchanged. This is often
| a difficult | bug to track | down. |     |     |
| ----------- | ------------ | ----- | --- | --- |
Remember, you can write index = index + 1;, or you can write index++;,
| but you | shouldn’t mix | them.    |     |     |
| ------- | ------------- | -------- | --- | --- |
| 7.2     | Accessing     | elements |     |     |
The[]operatorallowsustoreadandwritetheindividualelementsofanarray.
The indices start at zero, so c[0] refers to the first element of the array, and
c[1] refers to the second element. You can use the [] operator anywhere in an
expression:

| 7.3 Copying |        | arrays |     |     |     |     |     |     | 79  |
| ----------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| c[0]        | = 7;   |        |     |     |     |     |     |     |     |
| c[1]        | = c[0] | *      | 2;  |     |     |     |     |     |     |
c[2]++;
| c[3] | -=  | 60; |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
All of these are legal assignment statements. Here is the effect of this code
fragment:
c
|     |     |     |      | 7 14 | 1 -60     |     |     |     |     |
| --- | --- | --- | ---- | ---- | --------- | --- | --- | --- | --- |
|     |     |     | c[0] | c[1] | c[2] c[3] |     |     |     |     |
By now you should have noticed that the four elements of this array are num-
| bered from | 0   | to 3, which | means | that | there | is no element | with | the index | 4.  |
| ---------- | --- | ----------- | ----- | ---- | ----- | ------------- | ---- | --------- | --- |
Nevertheless,itisacommonerrortogobeyondtheboundsofanarray. Insafer
languages such as Java, this will cause an error and most likely the program
quits. C does not check array boundaries, so your program can go on accessing
memory locations beyond the array itself, as if they where part of the array.
| This is | most likely  | wrong     | and  | can      | cause very       | severe      | bugs in your | program. |      |
| ------- | ------------ | --------- | ---- | -------- | ---------------- | ----------- | ------------ | -------- | ---- |
| It      | is necessary |           | that | you,     | as a programmer, |             | make         | sure     | that |
| your    | code         | correctly |      | observes | array            | boundaries! |              |          |      |
You can use any expression as an index, as long as it has type int. One of the
most common ways to index an array is with a loop variable. For example:
| int   | i = | 0;   |     |     |     |     |     |     |     |
| ----- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| while | (i  | < 4) |     |     |     |     |     |     |     |
{
|     | printf | ("%i\n", |     | c[i]); |     |     |     |     |     |
| --- | ------ | -------- | --- | ------ | --- | --- | --- | --- | --- |
i++;
}
This is a standard while loop that counts from 0 up to 4, and when the loop
variable i is 4, the condition fails and the loop terminates. Thus, the body of
| the loop | is only | executed | when | i   | is 0, 1, 2 | and 3. |     |     |     |
| -------- | ------- | -------- | ---- | --- | ---------- | ------ | --- | --- | --- |
Each time through the loop we use i as an index into the array, printing the
ith element. This type of array traversal is very common. Arrays and loops go
| together | like fava | beans | and    | a nice | Chianti. |     |     |     |     |
| -------- | --------- | ----- | ------ | ------ | -------- | --- | --- | --- | --- |
| 7.3      | Copying   |       | arrays |        |          |     |     |     |     |
Arrays can be a very convenient solution for a number of problems, like storing
| and processing |     | large | sets of | data. |     |     |     |     |     |
| -------------- | --- | ----- | ------- | ----- | --- | --- | --- | --- | --- |
However, there is very little that C does automatically for you. For example
you can not set all the elements of an array at the same time and you can not
assign one array to the other, even if they are identical in type and number of
elements.

| 80     |       |         |        |      |       |     | Arrays |
| ------ | ----- | ------- | ------ | ---- | ----- | --- | ------ |
| double | a[3]  | = {1.0, |        | 1.0, | 1.0}; |     |        |
| double | b[3]; |         |        |      |       |     |        |
| a =    | 0.0;  | /*      | Wrong! | */   |       |     |        |
| b =    | a;    | /*      | Wrong! | */   |       |     |        |
In order to set all of the elements of an array to some value, you must do so
element by element. To copy the contents of one array to another, you must
| again do | so, by | copying | each | element | from one | array to the | other. |
| -------- | ------ | ------- | ---- | ------- | -------- | ------------ | ------ |
| int      | i = 0; |         |      |         |          |              |        |
| while    | (i     | < 3)    |      |         |          |              |        |
{
b[i] = a[i];
i++;
}
| 7.4 | for | loops |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- |
The loops we have written so far have a number of elements in common. All of
themstartbyinitializingavariable;theyhaveatest,orcondition,thatdepends
on that variable; and inside the loop they do something to that variable, like
| increment | it. |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- |
Thistypeofloopissocommonthatthereisanalternateloopstatement,called
| for, that | expresses     | it  | more       | concisely. | The general  | syntax looks | like this: |
| --------- | ------------- | --- | ---------- | ---------- | ------------ | ------------ | ---------- |
| for       | (INITIALIZER; |     | CONDITION; |            | INCREMENTOR) |              |            |
{
BODY
}
| This statement |     | is exactly | equivalent |     | to  |     |     |
| -------------- | --- | ---------- | ---------- | --- | --- | --- | --- |
INITIALIZER;
| while | (CONDITION) |     |     |     |     |     |     |
| ----- | ----------- | --- | --- | --- | --- | --- | --- |
{
BODY
INCREMENTOR
}
except that it is more concise and, since it puts all the loop-related statements
| in one place, | it   | is easier | to read. | For | example: |     |     |
| ------------- | ---- | --------- | -------- | --- | -------- | --- | --- |
| int           | i;   |           |          |     |          |     |     |
| for           | (i = | 0; i <    | 4; i++)  |     |          |     |     |
{
|     | printf("%i\n", |     | c[i]); |     |     |     |     |
| --- | -------------- | --- | ------ | --- | --- | --- | --- |
}
| is equivalent | to  |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- |

| 7.5 Array | length  |     |     |     |     | 81  |
| --------- | ------- | --- | --- | --- | --- | --- |
| int       | i = 0;  |     |     |     |     |     |
| while     | (i < 4) |     |     |     |     |     |
{
|     | printf("%i\n", | c[i]); |     |     |     |     |
| --- | -------------- | ------ | --- | --- | --- | --- |
i++;
}
| 7.5 | Array length |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- |
C does not provide us with a convenient way to determine the actual length of
anarray. Knowingthesizeofanarraywouldbeconvenientwhenwearelooping
| through | all elements | of the array | and need to stop | with the | last element. |     |
| ------- | ------------ | ------------ | ---------------- | -------- | ------------- | --- |
In order to determine the array length we could use the sizeof() operator,
that calculates the size of data types in bytes. Most data types in C use more
than one byte tostore their values, therefore it becomes necessary todivide the
byte-count for the array by the byte-count for a single element to establish the
| number | of elements | in the array. |     |     |     |     |
| ------ | ----------- | ------------- | --- | --- | --- | --- |
sizeof(ARRAY)/sizeof(ARRAY_ELEMENT)
It is a good idea to use this value as the upper bound of a loop, rather than
a constant. That way, if the size of the array changes, you won’t have to go
through the program changing all the loops; they will work correctly for any
size array.
| int    | i, length; |             |                |     |     |     |
| ------ | ---------- | ----------- | -------------- | --- | --- | --- |
| length | = sizeof   | (c) /       | sizeof (c[0]); |     |     |     |
| for    | (i = 0;    | i < length; | i++)           |     |     |     |
{
|     | printf("%i\n", | c[i]); |     |     |     |     |
| --- | -------------- | ------ | --- | --- | --- | --- |
}
The last time the body of the loop gets executed, the value of i is length - 1,
whichistheindexofthelastelement. Wheniisequaltolength,thecondition
fails and the body is not executed, which is a good thing, since it would access
| a memory | location | that is not | part of the array. |     |     |     |
| -------- | -------- | ----------- | ------------------ | --- | --- | --- |
| 7.6      | Random   | numbers     |                    |     |     |     |
Most computer programs do the same thing every time they are executed, so
they are said to be deterministic. Usually, determinism is a good thing, since
we expect the same calculation to yield the same result. For some applications,
though,wewouldlikethecomputertobeunpredictable. Gamesareanobvious
example.
Making a program truly nondeterministic turns out to be not so easy, but
there are ways to make it at least seem nondeterministic. One of them is to

82 Arrays
generatepseudorandomnumbersandusethemtodeterminetheoutcomeofthe
program. Pseudorandom numbers are not truly random in the mathematical
| sense, but | for | our purposes, | they | will | do. |     |     |
| ---------- | --- | ------------- | ---- | ---- | --- | --- | --- |
C provides a function called rand() that generates pseudorandom numbers. It
is declared in the header file stdlib.h, which contains a variety of “standard
| library” | functions, | hence | the | name. |     |     |     |
| -------- | ---------- | ----- | --- | ----- | --- | --- | --- |
The return value from rand() is an integer between 0 and RAND_MAX, where
RAND_MAXisalargenumber(about2billiononmycomputer)alsodefinedinthe
header file. Each time you call rand() you get a different randomly-generated
| number. | To see | a sample, | run     | this loop: |     |     |     |
| ------- | ------ | --------- | ------- | ---------- | --- | --- | --- |
| for     | (i =   | 0; i <    | 4; i++) |            |     |     |     |
{
int x = rand();
|     | printf("%i\n", |     | x); |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- |
}
| On my machine |     | I got | the following | output: |     |     |     |
| ------------- | --- | ----- | ------------- | ------- | --- | --- | --- |
1804289383
846930886
1681692777
1714636915
| You will | probably | get | something | similar, | but different, |     | on yours. |
| -------- | -------- | --- | --------- | -------- | -------------- | --- | --------- |
Of course, we don’t always want to work with gigantic integers. More often we
want to generate integers between 0 and some upper bound. A simple way to
| do that | is with | the modulus     |     | operator. | For example: |     |     |
| ------- | ------- | --------------- | --- | --------- | ------------ | --- | --- |
| int     | x =     | rand ();        |     |           |              |     |     |
| int     | y =     | x % upperBound; |     |           |              |     |     |
Since y is the remainder when x is divided by upperBound, the only possible
values for y are between 0 and upperBound - 1, including both end points.
| Keep in | mind, | though, | that y | will never | be equal | to upperBound. |     |
| ------- | ----- | ------- | ------ | ---------- | -------- | -------------- | --- |
Itisalsofrequentlyusefultogeneraterandomfloating-pointvalues. Acommon
| way to do | that | is by dividing |     | by RAND_MAX.  | For | example: |     |
| --------- | ---- | -------------- | --- | ------------- | --- | -------- | --- |
| int       | x =  | rand ();       |     |               |     |          |     |
| double    | y    | = (double)     |     | x / RAND_MAX; |     |          |     |
This code sets y to a random value between 0.0 and 1.0, including both end
points. As an exercise, you might want to think about how to generate a
random floating-point value in a given range; for example, between 100.0 and
200.0.

7.7 Statistics 83
7.7 Statistics
The numbers generated by rand() are supposed to be distributed uniformly.
That means that each value in the range should be equally likely. If we count
the number of times each value appears, it should be roughly the same for all
values, provided that we generate a large number of values.
In the next few sections, we will write programs that generate a sequence of
random numbers and check whether this property holds true.
7.8 Array of random numbers
The first step is to generate a large number of random values and store them
in a array. By “large number,” of course, I mean 20. It’s always a good idea to
start with a manageable number, to help with debugging, and then increase it
later.
The following function takes three arguments, an array of integers, the size of
the array and an upper bound for the random values. It fills the array of ints
with random values between 0 and upperBound-1.
void RandomizeArray (int array[], int length, int upperBound)
{
int i;
for (i = 0; i < length; i++)
{
array[i] = rand() % upperBound;
}
}
The return type is void, which means that this function does not return any
value to the calling function. To test this function, it is convenient to have a
function that outputs the contents of a array.
void PrintArray (int array[], int length)
{
int i;
for (i = 0; i < length; i++)
{
printf ("%i ", array[i]);
}
}
Thefollowingcodegeneratesanarrayfilledwithrandomvaluesandoutputsit:
int r_array[20];
int upperBound = 10;
int length = sizeof(r_array) / sizeof(r_array[0]);
RandomizeArray (r_array, length, upperBound);
PrintArray (r_array, length);

| 84       |         |                 |     |         |             |         | Arrays |
| -------- | ------- | --------------- | --- | ------- | ----------- | ------- | ------ |
| On my    | machine | the output      |     | is:     |             |         |        |
| 3 6 7 5  | 3 5     | 6 2 9 1         | 2 7 | 0 9 3 6 | 0 6 2 6     |         |        |
| which is | pretty  | random-looking. |     | Your    | results may | differ. |        |
If these numbers are really random, we expect each digit to appear the same
number of times—twice each. In fact, the number 6 appears five times, and the
| numbers | 4 and | 8 never | appear | at all. |     |     |     |
| ------- | ----- | ------- | ------ | ------- | --- | --- | --- |
Dotheseresultsmeanthevaluesarenotreallyuniform? It’shardtotell. With
so few values, the chances are slim that we would get exactly what we expect.
Butasthenumberofvaluesincreases,theoutcomeshouldbemorepredictable.
To test this theory, we’ll write some programs that count the number of times
each value appears, and then see what happens when we increase the number
| of elements | in      | our array. |          |     |            |     |     |
| ----------- | ------- | ---------- | -------- | --- | ---------- | --- | --- |
| 7.9         | Passing |            | an array | to  | a function |     |     |
You probably have noticed that our RandomizeArray() function looked a bit
unusual. We pass an array to this function and expect to get a a random-
ized array back. Nevertheless, we have declared it to be a void function, and
| miraculously | the | function | appears | to have | altered | the array. |     |
| ------------ | --- | -------- | ------- | ------- | ------- | ---------- | --- |
This behaviour goes against everything what I have said about the use of vari-
ablesinfunctionssofar. Ctypicallyusesthesocalledcall-by-valueevaluation
of expressions. If you pass a value to a function it gets copied from the calling
function to a variable in the called function. The same is true if the function
returns a value. Changes to the internal variable in the called function do not
| affect the | external | values | of  | the calling | function. |     |     |
| ---------- | -------- | ------ | --- | ----------- | --------- | --- | --- |
Whenwepassanarraytoafunctionthisbehaviourchangestosomethingcalled
call-by-reference evaluation. C does not copy the array to an internal array
– it rather generates a reference to the original array and any operation in the
called function directly affects the original array. This is also the reason why
wedonothavetoreturnanythingfromourfunction. Thechangeshavealready
taken place.
Call by reference also makes it necessary to supply the length of the array to
the called function, since invoking the sizeof operator in the called function
| would determine |     | the size | of  | the reference | and not | the original | array. |
| --------------- | --- | -------- | --- | ------------- | ------- | ------------ | ------ |
We will further discuss call by reference and call by value in Section 8.7, Sec-
| tion 9.6 | and 9.7. |     |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- | --- |
| 7.10     | Counting |     |     |     |     |     |     |
A good approach to problems like this is to think of simple functions that are
easy to write, and that might turn out to be useful. Then you can combine
them into a solution. This approach is sometimes called bottom-up design.

| 7.11 | Checking | the | other | values |     |     |     |     | 85  |
| ---- | -------- | --- | ----- | ------ | --- | --- | --- | --- | --- |
Of course, it is not easy to know ahead of time which functions are likely to be
useful, but as you gain experience you will have a better idea. Also, it is not
always obvious what sort of things are easy to write, but a good approach is to
| look for | subproblems |     | that fit | a pattern | you | have seen | before. |     |     |
| -------- | ----------- | --- | -------- | --------- | --- | --------- | ------- | --- | --- |
In our current example we want to examine a potentially large set of elements
and count the number of times a certain value appears. You can think of this
program as an example of a pattern called “traverse and count.” The elements
| of this | pattern   | are:      |             |        |              |          |                |             |     |
| ------- | --------- | --------- | ----------- | ------ | ------------ | -------- | -------------- | ----------- | --- |
| •       | A set or  | container | that        | can be | traversed,   | like     | a string       | or a array. |     |
| •       | A test    | that you  | can apply   | to     | each element | in       | the container. |             |     |
| •       | A counter | that      | keeps track | of     | how many     | elements | pass           | the test.   |     |
Inthiscase,IhaveafunctioninmindcalledHowMany()thatcountsthenumber
of elements in a array that are equal to a given value. The parameters are the
array, the length of the array and the integer value we are looking for. The
| return | value   | is the number | of       | times | the value   | appears. |            |     |     |
| ------ | ------- | ------------- | -------- | ----- | ----------- | -------- | ---------- | --- | --- |
| int    | HowMany | (int          | array[], |       | int length, |          | int value) |     |     |
{
int i;
|     | int | count | = 0;        |     |      |     |     |     |     |
| --- | --- | ----- | ----------- | --- | ---- | --- | --- | --- | --- |
|     | for | (i=0; | i < length; |     | i++) |     |     |     |     |
{
|     |     | if  | (array[i] |     | == value) | count++; |     |     |     |
| --- | --- | --- | --------- | --- | --------- | -------- | --- | --- | --- |
}
return count;
}
| 7.11 | Checking |     | the | other |     | values |     |     |     |
| ---- | -------- | --- | --- | ----- | --- | ------ | --- | --- | --- |
HowMany() only counts the occurrences of a particular value, and we are inter-
ested in seeing how many times each value appears. We can solve that problem
with a loop:
| int                     | i;           |                       |                 |         |                       |              |     |     |     |
| ----------------------- | ------------ | --------------------- | --------------- | ------- | --------------------- | ------------ | --- | --- | --- |
| int                     | r_array[20]; |                       |                 |         |                       |              |     |     |     |
| int                     | upperBound   |                       | = 10;           |         |                       |              |     |     |     |
| int                     | length       | =                     | sizeof(r_array) |         | / sizeof(r_array[0]); |              |     |     |     |
| RandomizeArray(r_array, |              |                       |                 | length, |                       | upperBound); |     |     |     |
| printf                  |              | ("value\tHowMany\n"); |                 |         |                       |              |     |     |     |
| for                     | (i           | = 0; i                | < upperBound;   |         | i++)                  |              |     |     |     |
{

86 Arrays
|     | printf("%i\t%i\n", | i, HowMany(r_array, |     | length, i)); |
| --- | ------------------ | ------------------- | --- | ------------ |
}
ThiscodeusestheloopvariableasanargumenttoHowMany(),inordertocheck
| each value | between 0 and | 9, in order. | The result is: |     |
| ---------- | ------------- | ------------ | -------------- | --- |
| value      | HowMany       |              |                |     |
| 0          | 2             |              |                |     |
| 1          | 1             |              |                |     |
| 2          | 3             |              |                |     |
| 3          | 3             |              |                |     |
| 4          | 0             |              |                |     |
| 5          | 2             |              |                |     |
| 6          | 5             |              |                |     |
| 7          | 2             |              |                |     |
| 8          | 0             |              |                |     |
| 9          | 2             |              |                |     |
Again, it is hard to tell if the digits are really appearing equally often. If we
| increase | the size of the | array to 100,000 | we get the following: |     |
| -------- | --------------- | ---------------- | --------------------- | --- |
| value    | HowMany         |                  |                       |     |
| 0        | 10130           |                  |                       |     |
| 1        | 10072           |                  |                       |     |
| 2        | 9990            |                  |                       |     |
| 3        | 9842            |                  |                       |     |
| 4        | 10174           |                  |                       |     |
| 5        | 9930            |                  |                       |     |
| 6        | 10059           |                  |                       |     |
| 7        | 9954            |                  |                       |     |
| 8        | 9891            |                  |                       |     |
| 9        | 9958            |                  |                       |     |
In each case, the number of appearances is within about 1% of the expected
value (10,000), so we conclude that the random numbers are probably uniform.
| 7.12 | A histogram |     |     |     |
| ---- | ----------- | --- | --- | --- |
It is often useful to take the data from the previous tables and store them for
later access, rather than just print them. What we need is a way to store 10
integers. We could create 10 integer variables with names like howManyOnes,
howManyTwos, etc. But that would require a lot of typing, and it would be a
| real pain | later if we decided | to change | the range of values. |     |
| --------- | ------------------- | --------- | -------------------- | --- |
A better solution is to use a array with length 10. That way we can create all
ten storage locations at once and we can access them using indices, rather than
| ten different | names. Here’s    | how: |     |     |
| ------------- | ---------------- | ---- | --- | --- |
| int           | i;               |      |     |     |
| int           | upperBound =     | 10;  |     |     |
| int           | r_array[100000]; |      |     |     |

| 7.13                    | A single-pass          | solution |             |                 |     |                       |     | 87  |
| ----------------------- | ---------------------- | -------- | ----------- | --------------- | --- | --------------------- | --- | --- |
| int                     | histogram[upperBound]; |          |             |                 |     |                       |     |     |
| int                     | r_array_length         |          | =           | sizeof(r_array) |     | / sizeof(r_array[0]); |     |     |
| RandomizeArray(r_array, |                        |          |             | r_array_length, |     | upperBound);          |     |     |
| for                     | (i =                   | 0; i <   | upperBound; | i++)            |     |                       |     |     |
{
|     | int count    | =   | HowMany(r_array, |     | length, | i); |     |     |
| --- | ------------ | --- | ---------------- | --- | ------- | --- | --- | --- |
|     | histogram[i] |     | = count;         |     |         |     |     |     |
}
I called the array histogram because that’s a statistical term for a array of
| numbers | that counts | the | number | of appearances |     | of a range | of values. |     |
| ------- | ----------- | --- | ------ | -------------- | --- | ---------- | ---------- | --- |
The tricky thing here is that I am using the loop variable in two different ways.
First, it is an argument to HowMany(), specifying which value I am interested
in. Second, it is an index into the histogram, specifying which location I should
| store | the result    | in. |     |          |     |     |     |     |
| ----- | ------------- | --- | --- | -------- | --- | --- | --- | --- |
| 7.13  | A single-pass |     |     | solution |     |     |     |     |
Althoughthiscodeworks,itisnotasefficientasitcouldbe. Everytimeitcalls
HowMany(), it traverses the entire array. In this example we have to traverse
| the array | ten times! |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
It would be better to make a single pass through the array. For each value in
the array we could find the corresponding counter and increment it. In other
words, we can use the value from the array as an index into the histogram.
| Here’s | what that             | looks  | like:           |       |      |             |          |     |
| ------ | --------------------- | ------ | --------------- | ----- | ---- | ----------- | -------- | --- |
| int    | upperBound            | =      | 10;             |       |      |             |          |     |
| int    | histogram[upperBound] |        |                 | = {0, | 0,   | 0, 0, 0, 0, | 0, 0, 0, | 0}; |
| for    | (i =                  | 0; i < | r_array_length; |       | i++) |             |          |     |
{
|     | int index | =   | r_array[i]; |     |     |     |     |     |
| --- | --------- | --- | ----------- | --- | --- | --- | --- | --- |
histogram[index]++;
}
The second line initializes the elements of the histogram to zeroes. That way,
whenweusetheincrementoperator(++)insidetheloop,weknowwearestarting
| from | zero. Forgetting | to  | initialize | counters | is  | a common error. |     |     |
| ---- | ---------------- | --- | ---------- | -------- | --- | --------------- | --- | --- |
As an exercise, encapsulate this code in a function called Histogram() that
takes an array and the range of values in the array (in this case 0 through 10)
astwoparametersminandmax. Youshouldpassasecondarraytothefunction
| where | a histogram | of the | values | in the | array | can be stored. |     |     |
| ----- | ----------- | ------ | ------ | ------ | ----- | -------------- | --- | --- |

| 88   |        |       |     |     | Arrays |
| ---- | ------ | ----- | --- | --- | ------ |
| 7.14 | Random | seeds |     |     |        |
If you have run the code in this chapter a few times, you might have noticed
that you are getting the same “random” values every time. That’s not very
random!
One of the properties of pseudorandom number generators is that if they start
fromthesameplacetheywillgeneratethesamesequenceofvalues. Thestarting
place is called a seed; by default, C uses the same seed every time you run the
program.
While you are debugging, it is often helpful to see the same sequence over and
over. That way, when you make a change to the program you can compare the
| output before | and after | the change. |     |     |     |
| ------------- | --------- | ----------- | --- | --- | --- |
If you want to choose a different seed for the random number generator, you
can use the srand() function. It takes a single argument, which is an integer
| between 0 | and RAND_MAX. |     |     |     |     |
| --------- | ------------- | --- | --- | --- | --- |
Formanyapplications, likegames, youwanttoseeadifferentrandomsequence
every time the program runs. A common way to do that is to use a library
function like time() to generate something reasonably unpredictable and unre-
peatable,likethenumberofsecondssinceJanuary1970,andusethatnumberas
aseed. Thedetailsofhowtodothatdependonyourdevelopmentenvironment.
| 7.15 | Glossary |     |     |     |     |
| ---- | -------- | --- | --- | --- | --- |
array: A named collection of values, where all the values have the same type,
| and | each value is identified | by an | index. |     |     |
| --- | ------------------------ | ----- | ------ | --- | --- |
element: One of the values in a array. The [] operator selects elements of a
array.
index: An integer variable or value used to indicate an element of a array.
increment: Increasethevalueofavariablebyone. Theincrementoperatorin
| C is | ++. |     |     |     |     |
| ---- | --- | --- | --- | --- | --- |
decrement: Decrease the value of a variable by one. The decrement operator
| in C           | is --.    |           |          |                  |            |
| -------------- | --------- | --------- | -------- | ---------------- | ---------- |
| deterministic: | A program | that does | the same | thing every time | it is run. |
pseudorandom: Asequenceofnumbersthatappeartoberandom,butwhich
| are actually | the product | of a deterministic |     | computation. |     |
| ------------ | ----------- | ------------------ | --- | ------------ | --- |
seed: A value used to initialize a random number sequence. Using the same
| seed | should yield the | same sequence | of values. |     |     |
| ---- | ---------------- | ------------- | ---------- | --- | --- |
bottom-up design: Amethodofprogramdevelopmentthatstartsbywriting
| small, | useful functions | and then | assembling | them into larger | solutions. |
| ------ | ---------------- | -------- | ---------- | ---------------- | ---------- |
histogram: Aarrayofintegerswhereeachintegercountsthenumberofvalues
| that | fall into a certain | range. |     |     |     |
| ---- | ------------------- | ------ | --- | --- | --- |

7.16 Exercises 89
| 7.16     | Exercises |     |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- | --- |
| Exercise | 7.1       |     |     |     |     |     |
A friend of yours shows you the following method and explains that if number is any
two-digit number, the program will output the number backwards. He claims that if
| number is | 17, the method |     | will output | 71. |     |     |
| --------- | -------------- | --- | ----------- | --- | --- | --- |
Is he right? If not, explain what the program actually does and modify it so that it
| does the | right thing. |     |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- | --- |
| #include | <stdio.h>    |     |     |     |     |     |
#include<stdlib.h>
| int main | (void) |     |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- |
{
| int                   | number        | = 71;        |            |              |     |     |
| --------------------- | ------------- | ------------ | ---------- | ------------ | --- | --- |
| int                   | lastDigit     | = number%10; |            |              |     |     |
| int                   | firstDigit    | =            | number/10; |              |     |     |
| printf("%i",lastDigit |               |              | +          | firstDigit); |     |     |
| return                | EXIT_SUCCESS; |              |            |              |     |     |
}
Exercise 7.2 Write a function that takes an array of integers, the length of the
| array and | an integer | named | target | as arguments. |     |     |
| --------- | ---------- | ----- | ------ | ------------- | --- | --- |
The function should search through the provided array and should return the first
index where target appears in the array, if it does. If target is not in the array
the function should return an invalid index value to indicate an error condition (e.g.
-1).
| Exercise | 7.3 |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
Onenot-very-efficientwaytosorttheelementsofanarrayistofindthelargestelement
and swap it with the first element, then find the second-largest element and swap it
| with the | second, and | so on. |     |     |     |     |
| -------- | ----------- | ------ | --- | --- | --- | --- |
a. Write a function called IndexOfMaxInRange() that takes an array of integers,
| finds | the largest | element | in  | the given range, | and returns | its index. |
| ----- | ----------- | ------- | --- | ---------------- | ----------- | ---------- |
b. Write a function called that takes an array of integers and two
SwapElement()
| indices, | and | that swaps | the | elements at | the given indices. |     |
| -------- | --- | ---------- | --- | ----------- | ------------------ | --- |
c. Write a function called SortArray() that takes an array of integers and that
| uses | IndexOfMaxInRange() |     |     | and SwapElement() | to sort | the array from largest |
| ---- | ------------------- | --- | --- | ----------------- | ------- | ---------------------- |
to smallest.

90 Arrays

| Chapter        |     | 8   |     |         |     |     |     |
| -------------- | --- | --- | --- | ------- | --- | --- | --- |
| Strings        |     | and |     | things  |     |     |     |
| 8.1 Containers |     |     | for | strings |     |     |     |
We have seen four types of values—characters, integers, floating-point numbers
and strings—but only three types of variables—char, int and double. So far
we have no way to store a string in a variable or perform operations on strings.
ThischapterisgoingtorectifythissituationandIcannowtellyouthatstrings
| in C are stored | as  | an array | of  | characters | terminated | by the character | \0. |
| --------------- | --- | -------- | --- | ---------- | ---------- | ---------------- | --- |
Bynowthisexplanationshouldmakesensetoyouandyouprobablyunderstand
why we had to learn quite a bit about the working of the language before we
| could turn | our attention |     | towards | string | variables. |     |     |
| ---------- | ------------- | --- | ------- | ------ | ---------- | --- | --- |
In the previous chapter we have seen that operations on arrays have only mini-
mal support from the C language itself and we had to program extra functions
byourselves. Fortunatelythingsarealittlebiteasierwhenwemanipulatethese
special types of arrays - called strings. There exist a number of library func-
tions in string.h that make string handling a bit easier than operations on
pure arrays.
Nevertheless string operations in C are still a lot more cumbersome than their
equivalence in other programing languages and can be a potential source of
| errors in your | programs, |           | if not | handled | carefully. |     |     |
| -------------- | --------- | --------- | ------ | ------- | ---------- | --- | --- |
| 8.2 String     |           | variables |        |         |            |     |     |
You can create a string variable as an array of characters in the following way:
| char | first[]  | =   | "Hello,   | ";  |     |     |     |
| ---- | -------- | --- | --------- | --- | --- | --- | --- |
| char | second[] | =   | "world."; |     |     |     |     |

| 92  |     |     |     |     |     | Strings and | things |
| --- | --- | --- | --- | --- | --- | ----------- | ------ |
The first line creates an string and assigns it the string value "Hello." In
the second line we declare a second string variable. Remember, the combined
| declaration | and | assignment | is  | called initialization. |     |     |     |
| ----------- | --- | ---------- | --- | ---------------------- | --- | --- | --- |
Initialisation time is the only time you can assign a value to a string directly
(just as with arrays in general). The initialisation parameters are passed in the
| form of | a string | constant | enclosed | in quotation | marks | ("..."). |     |
| ------- | -------- | -------- | -------- | ------------ | ----- | -------- | --- |
Noticethedifferenceinsyntaxfortheinitialisationofarraysandstrings. Ifyou
like you can also initialize the string in the normal array syntax, although this
| looks a | little odd | and is | not very                   | convenient | to type. |          |     |
| ------- | ---------- | ------ | -------------------------- | ---------- | -------- | -------- | --- |
| char    | first[]    | =      | {’H’,’e’,’l’,’l’,’o’,’,’,’ |            |          | ’,’\0’}; |     |
There is no need to supply an array size when you are initialising the string
variable at declaration time. The compiler compute the necessary array size to
| store the | supplied | string. |     |     |     |     |     |
| --------- | -------- | ------- | --- | --- | --- | --- | --- |
Remember what we said about the nature of a string variable. It is an array
of characters plus a marker that shows where our string ends: the termination
| character | \0. |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- |
Normally you do not have to supply this termination character. The compiler
understands our code and insertes it automatically. However, in the example
above, we treated our string exactly like an array and in this case we have to
| insert the | termination |     | character | ourselves. |     |     |     |
| ---------- | ----------- | --- | --------- | ---------- | --- | --- | --- |
When we are using a string variable to store different sting values during the
lifetime of our program we have to declare a size big enough for the largest
sequence of characters that we are going to store. We also have to make our
string variable exactly one character longer than the text we are going to store,
| because      | of the necessary |         | termination  | character. |                    |           |     |
| ------------ | ---------------- | ------- | ------------ | ---------- | ------------------ | --------- | --- |
| We can       | output strings   |         | in the usual | way        | using the printf() | function: |     |
| printf("%s", |                  | first); |              |            |                    |           |     |
| 8.3          | Extracting       |         | characters   |            | from               | a string  |     |
Stringsarecalled“strings”becausetheyaremadeupofasequence,orstring,of
characters. Thefirstoperationwearegoingtoperformonastringistoextract
one of the characters. C uses an index in square brackets ([ and ]) for this
operation:
| char   | fruit[]  | =           | "banana"; |     |     |     |     |
| ------ | -------- | ----------- | --------- | --- | --- | --- | --- |
| char   | letter   | = fruit[1]; |           |     |     |     |     |
| printf | ("%c\n", |             | letter);  |     |     |     |     |
The expression fruit[1] indicates that I want character number 1 from the
string named fruit. The result is stored in a char named letter. When I
| output | the value | of letter, | I   | get a surprise: |     |     |     |
| ------ | --------- | ---------- | --- | --------------- | --- | --- | --- |
a

8.4 Length 93
a is not the first letter of "banana". Unless you are a computer scientist. For
perverse reasons, computer scientists always start counting from zero. The 0th
letter (“zeroeth”) of "banana" is b. The 1th letter (“oneth”) is a and the 2th
| (“twoeth”) | letter is n. |     |     |     |
| ---------- | ------------ | --- | --- | --- |
If you want the zereoth letter of a string, you have to put zero in the square
brackets:
| char | letter = fruit[0]; |     |     |     |
| ---- | ------------------ | --- | --- | --- |
8.4 Length
Tofindthelengthofastring(thenumberofcharactersthisstringcontains),we
can use the strlen() function. The function is called using the string variable
as an argument:
| #include       | <string.h> |     |     |     |
| -------------- | ---------- | --- | --- | --- |
| int main(void) |            |     |     |     |
{
| int    | length;          |             |     |     |
| ------ | ---------------- | ----------- | --- | --- |
| char   | fruit[]          | = "banana"; |     |     |
| length | = strlen(fruit); |             |     |     |
| return | EXIT_SUCCESS;    |             |     |     |
}
The return value of strlen() in this case is 6. We assign this value to the
| integer length | for further | use. |     |     |
| -------------- | ----------- | ---- | --- | --- |
In order to compile this code, you need to include the header file for the
string.h library. This library provides a number of useful functions for oper-
ations on strings. You should familiarize yourself with these functions because
| they can help | you to solve | your programming | problems | faster. |
| ------------- | ------------ | ---------------- | -------- | ------- |
To find the last letter of a string, you might be tempted to try something like
| int length | = strlen(fruit);      |     |            |     |
| ---------- | --------------------- | --- | ---------- | --- |
| char       | last = fruit[length]; |     | /* WRONG!! | */  |
That won’t work. The reason is that fruit is still an array and there is no
letter at the array index fruit[6] in "banana". Since we started counting at
0, the 6 letters are numbered from 0 to 5. To get the last character, you have
| to subtract | 1 from length.          |     |     |     |
| ----------- | ----------------------- | --- | --- | --- |
| int length  | = strlen(fruit);        |     |     |     |
| char        | last = fruit[length-1]; |     |     |     |
8.5 Traversal
A common thing to do with a string is start at the beginning, select each char-
acter in turn, do something to it, and continue until the end. This pattern of

| 94  |     |     |     |     | Strings and | things |
| --- | --- | --- | --- | --- | ----------- | ------ |
processing is called a traversal. A natural way to encode a traversal is with a
while statement:
| int   | index = | 0;               |     |     |     |     |
| ----- | ------- | ---------------- | --- | --- | --- | --- |
| while | (index  | < strlen(fruit)) |     |     |     |     |
{
|     | char letter   | = fruit[index]; |          |     |     |     |
| --- | ------------- | --------------- | -------- | --- | --- | --- |
|     | printf("%c\n" | ,               | letter); |     |     |     |
|     | index =       | index +         | 1;       |     |     |     |
}
This loop traverses the string and outputs each letter on a line by itself. Notice
that the condition is index < strlen(fruit), which means that when index
is equal to the length of the string, the condition is false and the body of the
loop is not executed. The last character we access is the one with the index
strlen(fruit)-1.
The name of the loop variable is index. An index is a variable or value used
tospecifyonememberofanorderedset,inthiscasethesetofcharactersinthe
string. The index indicates (hence the name) which one you want. The set has
to be ordered so that each letter has an index and each index refers to a single
character.
As an exercise, write a function that takes a string as an argument and that
| outputs | the letters | backwards,  | all on | one line.   |     |     |
| ------- | ----------- | ----------- | ------ | ----------- | --- | --- |
| 8.6     | Finding     | a character |        | in a string |     |     |
If we are looking for a letter in a string, we have to search through the string
and detect the position where this letter occurs in the string. Here is an imple-
| mentation | of this              | function: |     |         |     |     |
| --------- | -------------------- | --------- | --- | ------- | --- | --- |
| int       | LocateCharacter(char |           | *s, | char c) |     |     |
{
int i = 0;
|     | while (i | < strlen(s)) |     |     |     |     |
| --- | -------- | ------------ | --- | --- | --- | --- |
{
|     | if  | (s[i] == | c) return | i;  |     |     |
| --- | --- | -------- | --------- | --- | --- | --- |
|     | i = | i + 1;   |           |     |     |     |
}
return -1;
}
We have to pass the string as the first argument, the other argument is the
character we are looking for. Our function returns the index of the first occur-
| rence of | the letter, | or -1 if | the letter | is not contained | in the string. |     |
| -------- | ----------- | -------- | ---------- | ---------------- | -------------- | --- |

| 8.7 Pointers | and Addresses |               |     |     | 95  |
| ------------ | ------------- | ------------- | --- | --- | --- |
| 8.7          | Pointers      | and Addresses |     |     |     |
When we look at the definition of the LocateCharacter() function you may
| notice the | following construct | char | *s which looks | unfamiliar. |     |
| ---------- | ------------------- | ---- | -------------- | ----------- | --- |
Remember, when we discussed how we had to pass an array to a function, back
inSection7.9,wesaidthatinsteadofcopyingthearray,weonlypassareference
to the function. Back then, we did not say exactly what this reference was.
C is one of the very few high-level programming languages that let you directly
manipulate objects in the computer memory. In order to do this direct manip-
ulation, we need to know the location of the object in memory: it’s address.
Adressescanbestoredinvariablesofaspecialtype. Thesevariablesthatpoint
to other objects in memory (such as variables, arrays and strings) are therefore
| called pointer | variables. |     |     |     |     |
| -------------- | ---------- | --- | --- | --- | --- |
A pointer references the memory location of an object and can be defined like
this:
| int | *i_p; |     |     |     |     |
| --- | ----- | --- | --- | --- | --- |
This declaration looks similar to our earlier declarations, with one difference:
the asterisk infrontof thename. Wehavegiven this pointer thetype int. The
type specification has nothing to do with the pointer itself, but rather defines
which object this pointer is supposed to reference (in this case an integer).
This allows the compiler to do some type checking on, what would otherwise
| be, an anonymous | reference. |     |     |     |     |
| ---------------- | ---------- | --- | --- | --- | --- |
A pointer all by itself is rather meaningless, we also need an object that this
| pointer is | referencing: |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- |
| int        | number = 5;  |     |     |     |     |
| int        | *i_p;        |     |     |     |     |
This code-fragment defines an int variable and a pointer. We can use the
"address-of"operator&toassignthememorylocationoraddressofourvariable
to the pointer.
| i_p | = &number; |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- |
Pointer i_p now references integer variable number. We can verify this using
| the "content-of" | operator | *.     |     |     |     |
| ---------------- | -------- | ------ | --- | --- | --- |
| printf("%i\n",   |          | *i_p); |     |     |     |
This prints 5, which happens to be the content of the memory location at our
pointer reference.
| With pointers  | we can      | directly manipulate | memory | locations: |     |
| -------------- | ----------- | ------------------- | ------ | ---------- | --- |
| *i_p           | = *i_p + 2; |                     |        |            |     |
| printf("%i\n", |             | number);            |        |            |     |
Our variable number now has the value 7 and we begin to understand how our
LocateCharacter() function can directly access the values of string variables
| through | the use of a char | pointer. |     |     |     |
| ------- | ----------------- | -------- | --- | --- | --- |

| 96  |     |     |     |     |     | Strings | and things |
| --- | --- | --- | --- | --- | --- | ------- | ---------- |
Pointers are widely used in many C programs and we have only touched the
surface of the topic. They can be immensely useful and efficient, however they
canalsobeapotentialsourceofproblemswhennotusedappropriately. Forthis
reasonnotmanyprogramminglanguagessupportdirectmemorymanipulation.
| 8.8 | String | concatenation |     |     |     |     |     |
| --- | ------ | ------------- | --- | --- | --- | --- | --- |
InSection8.6wehaveseenhowwecouldimplementasearchfunctionthatfinds
| a character | in a string. |     |     |     |     |     |     |
| ----------- | ------------ | --- | --- | --- | --- | --- | --- |
Oneusefuloperationonstringsisstringconcatenation. Toconcatenatemeans
to join the two operands end to end. For example: and becomes
|     |     |     |     |     |     | shoe maker |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- |
shoemaker.
Fortunately, we do not have to program all the necessary functions in C our-
selves. The string.h library already provides several functions that we can
| invoke         | on strings.     |             |             |      |                |         |       |
| -------------- | --------------- | ----------- | ----------- | ---- | -------------- | ------- | ----- |
| We can         | use the library | function    | strncat()   |      | to concatenate | strings | in C. |
| char           | fruit[20]       | = "banana"; |             |      |                |         |       |
| char           | bakedGood[]     | = "         | nut bread"; |      |                |         |       |
| strncat(fruit, |                 | bakedGood,  |             | 10); |                |         |       |
| printf         | ("%s\n",        | fruit);     |             |      |                |         |       |
| The output     | of this         | program     | is banana   | nut  | bread.         |         |       |
Whenweareusinglibraryfunctionsitisimportanttocompletelyunderstandall
the necessary arguments and to have a complete understanding of the working
of the function.
Thestrncat()doesnottakethetwostrings,joinsthemtogetherandproduces
a new combined string. It rather copies the content from the second argument
into the first.
We therefore have to make sure that our first string is long enough to also hold
the second string. We do this by defining the maximum capacity for string
fruit to be 19 characters + 1 termination character (char fruit[20]). The
third argument of strncat() specifies the number of characters that will be
| copied | from the second | into | the first | string. |           |           |     |
| ------ | --------------- | ---- | --------- | ------- | --------- | --------- | --- |
| 8.9    | Assigning       | new  | values    |         | to string | variables |     |
So far we have seen how to initialise a string variable at declaration time. As
witharraysingeneral,itisnotlegaltoassignvaluesdirectlytostrings,because
| it is not | possible to | assign a | value to | an entire | array. |           |     |
| --------- | ----------- | -------- | -------- | --------- | ------ | --------- | --- |
| fruit     | = "orange"; | /*       | Wrong:   | Cannot    | assign | directly! | */  |
In order to assign a new value to an existing string variable we have to use the
| strncpy() | function. | For example, |     |     |     |     |     |
| --------- | --------- | ------------ | --- | --- | --- | --- | --- |

| 8.10 strings |               | are not | comparable |          |     |      |     |     | 97  |
| ------------ | ------------- | ------- | ---------- | -------- | --- | ---- | --- | --- | --- |
| char         | greeting[15]; |         |            |          |     |      |     |     |     |
| strncpy      | (greeting,    |         | "Hello,    | world!", |     | 13); |     |     |     |
copies13charactersfromtheofthesecondargumentstringtothefirstargument
string.
This works, but not quite as expected. The strncpy() function copies exactly
13 characters from the second argument string into the first argument string.
| And what | happens | to our | string | termination | character |     | \0? |     |     |
| -------- | ------- | ------ | ------ | ----------- | --------- | --- | --- | --- | --- |
It is not copied automatically. We need to change our copy statement to copy
| also the | invisible  | 14th character |         | at the end | of  | the string: |     |     |     |
| -------- | ---------- | -------------- | ------- | ---------- | --- | ----------- | --- | --- | --- |
| strncpy  | (greeting, |                | "Hello, | world!",   |     | 14);        |     |     |     |
However, if we only copy parts of the second string into the first we need to
explicitlysetthen+1thcharacterinthegreeting[15]stringto\0afterwards.
strncpy (greeting, "Hello, world!", 5); /*only Hello is copied*/
| greeting[5] |     | = ’\0’; |     |     |     |     |     |     |     |
| ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Attention! In the last two sections we have used the strncpy() and the
strncat() function that require you to explicitly supply the number of charac-
| ters that | will get | copied | or attached | to  | the first | argument | string. |     |     |
| --------- | -------- | ------ | ----------- | --- | --------- | -------- | ------- | --- | --- |
The string.h library also defines the strcpy() and the strcat() functions
| that have | no explicit | bound | on  | the number | of  | characters | that | are copied. |     |
| --------- | ----------- | ----- | --- | ---------- | --- | ---------- | ---- | ----------- | --- |
Theusageofthesefunctionsisstronglydiscouraged! Theirusehasleadtoavast
number of security problems with C programs. Remember, C does not check
array boundaries and will continue copying characters into computer memory
| even past | the length | of  | the variable. |            |     |     |     |     |     |
| --------- | ---------- | --- | ------------- | ---------- | --- | --- | --- | --- | --- |
| 8.10      | strings    |     | are not       | comparable |     |     |     |     |     |
All the comparison operators that work on ints and doubles do work on
strings. For example, if you write the following code to determine if two
| strings   | are equal:  |              |     |           |     |     |     |     |     |
| --------- | ----------- | ------------ | --- | --------- | --- | --- | --- | --- | --- |
| if        | (word       | == "banana") |     | /* Wrong! | */  |     |     |     |     |
| This test | will always | fail.        |     |           |     |     |     |     |     |
Youhavetousethestrcmp()functiontocomparetwostringswitheachother.
The function returns 0 if the two strings are identical, a negative value if the
first string is ’alphabetically less’ than the second (would be listed first in a
| dictionary) | or a | positive | value if | the second | string | is  | ’greater’. |     |     |
| ----------- | ---- | -------- | -------- | ---------- | ------ | --- | ---------- | --- | --- |
Please notice, this return value is not the standard true/false result, where the
| return value | 0   | is interpreted | as        | ’false’.    |       |     |              |        |     |
| ------------ | --- | -------------- | --------- | ----------- | ----- | --- | ------------ | ------ | --- |
| The strcmp() |     | function       | is useful | for putting | words | in  | alphabetical | order. |     |

98 Strings and things
if (strcmp(word, "banana") < 0)
{
printf( "Your word, %s, comes before banana.\n", word);
}
else if (strcmp(word, "banana") > 0)
{
printf( "Your word, %s, comes after banana.\n", word);
}
else
{
printf ("Yes, we have no bananas!\n");
}
Youshouldbeaware,though,thatthestrcmp()functiondoesnothandleupper
and lower case letters the same way that people do. All the upper case letters
come before all the lower case letters. As a result,
Your word, Zebra, comes before banana.
A common way to address this problem is to convert strings to a standard
format,likealllower-case,beforeperformingthecomparison. Thenextsections
explains how.
8.11 Character classification
It is often useful to examine a character and test whether it is upper or lower
case, or whether it is a character or a digit. C provides a library of functions
thatperformthiskindofcharacterclassification. Inordertousethesefunctions,
you have to include the header file ctype.h.
char letter = ’a’;
if (isalpha(letter))
{
printf("The character %c is a letter.", letter);
}
The return value from isalpha() is an integer that is 0 if the argument is not
a letter, and some non-zero value if it is.
It is legal to use this kind of integer in a conditional, as shown in the example.
The value 0 is treated as false, and all non-zero values are treated as true.
Other character classification functions include isdigit(), which identifies the
digits 0 through 9, and isspace(), which identifies all kinds of “white” space,
including spaces, tabs, newlines, and a few others. There are also isupper()
and islower(), which distinguish upper and lower case letters.
Finally, there are two functions that convert letters from one case to the other,
called toupper() and tolower(). Both take a single character as an argument
and return a (possibly converted) character.

| 8.12           | Getting | user         | input    |           |     |     |     |     | 99  |
| -------------- | ------- | ------------ | -------- | --------- | --- | --- | --- | --- | --- |
| char           | letter  | =            | ’a’;     |           |     |     |     |     |     |
| letter         |         | = toupper    |          | (letter); |     |     |     |     |     |
| printf("%c\n", |         |              | letter); |           |     |     |     |     |     |
| The output     |         | of this code | is       | A.        |     |     |     |     |     |
As an exercise, use the character classification and conversion library to write
functions named StringToUpper() and StringToLower() that take a single
string as a parameter, and that modify the string by converting all the letters
| to upper | or      | lower case. | The  | return | type  | should | be void. |     |     |
| -------- | ------- | ----------- | ---- | ------ | ----- | ------ | -------- | --- | --- |
| 8.12     | Getting |             | user |        | input |        |          |     |     |
The programs we have written so far are pretty predictable; they do the same
thing every time they run. Most of the time, though, we want programs that
| take input | from | the | user | and respond |     | accordingly. |     |     |     |
| ---------- | ---- | --- | ---- | ----------- | --- | ------------ | --- | --- | --- |
Therearemanywaystogetinput,includingkeyboardinput,mousemovements
and button clicks, as well as more exotic mechanisms like voice control and
| retinal | scanning. | In  | this text | we  | will consider |     | only keyboard | input. |     |
| ------- | --------- | --- | --------- | --- | ------------- | --- | ------------- | ------ | --- |
In the header file stdio.h, C defines a function named scanf() that handles
input in much the same way that printf() handles output. We can use the
| following   | code | to get | an integer |     | value | from | the user: |     |     |
| ----------- | ---- | ------ | ---------- | --- | ----- | ---- | --------- | --- | --- |
| int         | x;   |        |            |     |       |      |           |     |     |
| scanf("%i", |      | &x);   |            |     |       |      |           |     |     |
The scanf() function causes the program to stop executing and wait for the
user to type something. If the user types a valid integer, the program converts
| it into | an integer | value | and | stores | it in | x.  |     |     |     |
| ------- | ---------- | ----- | --- | ------ | ----- | --- | --- | --- | --- |
If the user types something other than an integer, C doesn’t report an error, or
anything sensible like that. Instead, the function returns and leaves
scanf()
| the value | in  | x unchanged. |     |     |     |     |     |     |     |
| --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Fortunately, there is a way to check and see if an input statement succeeds.
The scanf() function returns the number of items that have been successfully
read. This number will be 1 when the last input statement succeeded. If not,
we know that some previous operation failed, and also that the next operation
will fail.
| Getting | input | from   | the user | might | look | like | this: |     |     |
| ------- | ----- | ------ | -------- | ----- | ---- | ---- | ----- | --- | --- |
| int     | main  | (void) |          |       |      |      |       |     |     |
{
|     | int    | success,  |     | x;   |           |       |     |     |     |
| --- | ------ | --------- | --- | ---- | --------- | ----- | --- | --- | --- |
|     | /*     | prompt    | the | user | for input |       | */  |     |     |
|     | printf | ("Enter   |     | an   | integer:  | \n"); |     |     |     |
|     | /*     | get input |     | */   |           |       |     |     |     |

100 Strings and things
success = scanf("%i", &x);
/* check and see if the input statement succeeded */
if (success == 1)
{
/* print the value we got from the user */
printf ("Your input: %i\n", x);
return EXIT_SUCCESS;
}
printf("That was not an integer.\n");
return EXIT_FAILURE;
}
There is another potential pitfall connected with the scanf() function. Your
program code might want to insist that the user types a valid integer, because
this value is needed later on. In this case you might want to repeat the input
statement in order to get a valid user input:
if (success != 1)
{
while (success != 1)
{
printf("That was not a number. Please try again:\n");
success = scanf("%i", &x);
}
}
Unfortunately this code leads into an endless loop. You probably ask yourself,
why? The input from the keyboard is delivered to your program by the oper-
ating system, in something called an input buffer. A successful read operation
automaticallyemptiesthisbuffer. However,ifthescanf()functionfails,likein
our example, the buffer does not get emptied and the next scanf() operation
re-reads the old value - you see the problem?
Weneedtoemptytheinputbuffer,beforewecanattempttoreadthenextinput
from the user. Since there is no standard way to do this, we will introduce our
own code that reads and empties the buffer using the getchar() function. It
run through a while-loop until there are no more characters left in the buffer
(notice the construction of this loop, where all the operations are executed in
the test condition):
char ch; /* helper variable stores discarded chars*/
while (success != 1)
{
printf("That isn’t a number. Please try again:\n");
/* now we empty the input buffer*/
while ((ch = getchar()) != ’\n’ && ch != EOF);
success = scanf("%i", &x);
}

8.13 Glossary 101
| The scanf() | function  |        | can also      | be used | to input | a string: |     |
| ----------- | --------- | ------ | ------------- | ------- | -------- | --------- | --- |
| char        | name[80]; |        |               |         |          |           |     |
| printf      | ("What    | is     | your name?"); |         |          |           |     |
| scanf       | ("%s",    | name); |               |         |          |           |     |
| printf      | ("%s",    | name); |               |         |          |           |     |
Again, we have to make sure our string variable is large enough to contain
the complete user input. Notice the difference in the argument of the scanf()
function when we are reading an integer or a string. The function requires a
pointer to the variable where the input value will be stored. If we are reading
an integer we need to use the address operator & with the variable name. In
| the case | of a | we  | simply | provide | the variable | name. |     |
| -------- | ---- | --- | ------ | ------- | ------------ | ----- | --- |
string
Also notice, that the scanf() function only takes the first word of the input,
and leaves the rest for the next input statement. So, if you run this program
| and type | your full | name, | it will | only output | your | first name. |     |
| -------- | --------- | ----- | ------- | ----------- | ---- | ----------- | --- |
| 8.13     | Glossary  |       |         |             |      |             |     |
index: Avariableorvalueusedtoselectoneofthemembersofanorderedset,
| like | a character | from | a string. |     |     |     |     |
| ---- | ----------- | ---- | --------- | --- | --- | --- | --- |
traverse: To iterate through all the elements of a set performing a similar
| operation | on  | each. |     |     |     |     |     |
| --------- | --- | ----- | --- | --- | --- | --- | --- |
counter: A variable used to count something, usually initialized to zero and
| then         | incremented. |         |              |             |         |            |     |
| ------------ | ------------ | ------- | ------------ | ----------- | ------- | ---------- | --- |
| concatenate: | To           | join    | two operands | end-to-end. |         |            |     |
| pointer:     | A reference  | to      | an object    | in computer |         | memory.    |     |
| address:     | The exact    | storage | location     | of          | objects | in memory. |     |
| 8.14         | Exercises    |         |              |             |         |            |     |
Exercise 8.1 Awordissaidtobe“abecedarian”ifthelettersinthewordappear
in alphabetical order. For example, the following are all 6-letter English abecedarian
words.
| abdest, | acknow, | acorsy, | adempt, | adipsy, | agnosy, | befist, behint, | beknow, |
| ------- | ------- | ------- | ------- | ------- | ------- | --------------- | ------- |
| bijoux, | biopsy, | cestuy, | chintz, | deflux, | dehors, | dehort, deinos, | diluvy, |
dimpsy
a. Describeanalgorithmforcheckingwhetheragivenword(String)isabecedarian,
| assumingthatthewordcontainsonlylower-caseletters. |      |            |     |            |        | Youralgorithmcanbe |     |
| ------------------------------------------------- | ---- | ---------- | --- | ---------- | ------ | ------------------ | --- |
| iterative                                         | or   | recursive. |     |            |        |                    |     |
| b. Implement                                      | your | algorithm  | in  | a function | called | IsAbecedarian().   |     |

| 102 |     |     |     |     |     |     | Strings |     | and things |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ---------- |
Exercise 8.2 Write a function called LetterHist() that takes a String as a
parameter and that returns a histogram of the letters in the String. The zeroeth
element of the histogram should contain the number of a’s in the String (upper and
lower case); the 25th element should contain the number of z’s. Your solution should
| only traverse | the | String once. |     |     |     |     |     |     |     |
| ------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Exercise 8.3 Awordissaidtobea“doubloon”ifeveryletterthatappearsinthe
word appears exactly twice. For example, the following are all the doubloons I found
in my dictionary.
| Abba,     | Anna,     | appall,       | appearer, |         | appeases, | arraigning, | beriberi,           | bilabial, |     |
| --------- | --------- | ------------- | --------- | ------- | --------- | ----------- | ------------------- | --------- | --- |
| boob,     | Caucasus, | coco,         | Dada,     | deed,   | Emmett,   |             | Hannah, horseshoer, |           | in- |
| testines, | Isis,     | mama,         | Mimi,     | murmur, | noon,     | Otto,       | papa, peep,         | reappear, |     |
| redder,   | sees,     | Shanghaiings, |           | Toto    |           |             |                     |           |     |
WriteafunctioncalledIsDoubloon()thatreturnsTRUEifthegivenwordisadoubloon
| and FALSE | otherwise. |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Exercise  | 8.4        |     |     |     |     |     |     |     |     |
The Captain Crunch decoder ring works by taking each letter in a string and adding
13 to it. For example, ’a’ becomes ’n’ and ’b’ becomes ’o’. The letters “wrap around”
| at the end, | so ’z’ | becomes | ’m’. |     |     |     |     |     |     |
| ----------- | ------ | ------- | ---- | --- | --- | --- | --- | --- | --- |
a. WriteafunctionthattakesaStringandthatreturnsanewStringcontainingthe
| encoded        | version. | You         | should      | assume | that               | the   | String contains | upper | and lower      |
| -------------- | -------- | ----------- | ----------- | ------ | ------------------ | ----- | --------------- | ----- | -------------- |
| case           | letters, | and spaces, | but         | no     | other punctuation. |       | Lower           | case  | letters should |
| be transformed |          | into        | other lower | case   | letters;           | upper | into upper.     | You   | should not     |
| encode         | the      | spaces.     |             |        |                    |       |                 |       |                |
b. Generalize the Captain Crunch method so that instead of adding 13 to the
| letters, | it adds | any given  | amount. |           | Now  | you should | be able | to encode | things by |
| -------- | ------- | ---------- | ------- | --------- | ---- | ---------- | ------- | --------- | --------- |
| adding   | 13      | and decode | them    | by adding | -13. | Try        | it.     |           |           |
Exercise 8.5 In Scrabble each player has a set of tiles with letters on them, and
the object of the game is to use those letters to spell words. The scoring system is
complicated, but as a rough guide longer words are often worth more than shorter
words.
Imagine you are given your set of tiles as a String, like "qijibo" and you are given
anotherStringtotest,like"jib". WriteafunctioncalledTestWord()thattakesthese
twoStringsandreturnstrueifthesetoftilescanbeusedtospelltheword. Youmight
have more than one tile with the same letter, but you can only use each tile once.
Exercise 8.6 InrealScrabble,therearesomeblanktilesthatcanbeusedaswild
| cards; that | is, a | blank tile | can be | used | to represent | any | letter. |     |     |
| ----------- | ----- | ---------- | ------ | ---- | ------------ | --- | ------- | --- | --- |
Think of an algorithm for that deals with wild cards. Don’t get bogged
TestWord()
down in details of implementation like how to represent wild cards. Just describe the
| algorithm, | using | English, pseudocode, |     | or  | C.  |     |     |     |     |
| ---------- | ----- | -------------------- | --- | --- | --- | --- | --- | --- | --- |

| Chapter |     | 9   |
| ------- | --- | --- |
Structures
| 9.1 | Compound | values |
| --- | -------- | ------ |
Most of the data types we have been working with represent a single value—an
integer, a floating-point number, a character value. Strings are different in the
sense that they are made up of smaller pieces, the characters. Thus, strings are
| an example | of a compound | type. |
| ---------- | ------------- | ----- |
Depending on what we are doing, we may want to treat a compound type
as a single thing (or object), or we may want to access its parts (or member
| variables). | This ambiguity | is useful. |
| ----------- | -------------- | ---------- |
It is also useful to be able to create your own compound values. C provides a
| mechanism | for doing     | that: structures. |
| --------- | ------------- | ----------------- |
| 9.2       | Point objects |                   |
As a simple example of a compound structure, consider the concept of a math-
ematical point. At one level, a point is two numbers (coordinates) that we
treat collectively as a single object. In mathematical notation, points are often
writteninparentheses, withacommaseparatingthecoordinates. Forexample,
(0,0)indicatestheorigin,and(x,y)indicatesthepointxunitstotherightand
| y units | up from the | origin. |
| ------- | ----------- | ------- |
A natural way to represent a point in C is with two doubles. The question,
then, is how to group these two values into a compound object, or structure.
| The answer | is a struct | definition: |
| ---------- | ----------- | ----------- |
| typedef    | struct      |             |
{
double x;
double y;
} Point_t;

| 104 |     |     |     |     |     |     | Structures |
| --- | --- | --- | --- | --- | --- | --- | ---------- |
struct definitions appear outside of any function definition, usually at the be-
| ginning of | the program | (after | the | include | statements). |     |     |
| ---------- | ----------- | ------ | --- | ------- | ------------ | --- | --- |
This definition indicates that there are two elements in this structure, named
x
| and y. These | elements | are | called | the members | or  | fields | of a structure. |
| ------------ | -------- | --- | ------ | ----------- | --- | ------ | --------------- |
It is a common error to leave off the semi-colon at the end of a structure defini-
tion. It might seem odd to put a semi-colon after curly-brackets, but you’ll get
used to it.
Once you have defined the new structure, you can create variables with that
type:
| Point_t | blank; |     |     |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- | --- | --- |
| blank.x | = 3.0; |     |     |     |     |     |     |
| blank.y | = 4.0; |     |     |     |     |     |     |
The first line is a conventional variable declaration: blank has type Point_t.
Thenexttwolinesinitializethefieldsofthestructure. The“dotnotation”used
here is called the field selection operator and allows to access the structure
fields.
| The result | of these | assignments |     | is shown | in the following |     | state diagram: |
| ---------- | -------- | ----------- | --- | -------- | ---------------- | --- | -------------- |
x: 3
blank
y: 4
As usual, the name of the variable blank appears outside the box and its value
appears inside the box. In this case, that value is a compound object with two
| named member  | variables. |        |     |     |           |     |     |
| ------------- | ---------- | ------ | --- | --- | --------- | --- | --- |
| 9.3 Accessing |            | member |     |     | variables |     |     |
You can read the values of an member variable using the same syntax we used
to write them:
| double | x = blank.x; |     |     |     |     |     |     |
| ------ | ------------ | --- | --- | --- | --- | --- | --- |
Theexpressionblank.xmeans“gototheobjectnamedblankandgetthevalue
of x.” In this case we assign that value to a local variable named x. Notice that
thereisnoconflictbetweenthelocalvariablenamedxandthemembervariable
named x. The purpose of dot notation is to identify which variable you are
| referring | to unambiguously. |     |     |     |     |     |     |
| --------- | ----------------- | --- | --- | --- | --- | --- | --- |
YoucanusedotnotationaspartofanyCexpression, sothefollowingarelegal.
| printf    | ("%0.1f,     | %0.1f\n", |         | blank.x,  | blank.y);       |         |            |
| --------- | ------------ | --------- | ------- | --------- | --------------- | ------- | ---------- |
| double    | distance     | =         | blank.x | * blank.x | +               | blank.y | * blank.y; |
| The first | line outputs | 3,        | 4; the  | second    | line calculates | the     | value 25.  |

| 9.4 Operations |            | on structures |     |            |     |     | 105 |
| -------------- | ---------- | ------------- | --- | ---------- | --- | --- | --- |
| 9.4            | Operations |               | on  | structures |     |     |     |
Most of the operators we have been using on other types, like mathematical
operators ( +, %, etc.) and comparison operators (==, >, etc.), do not work on
structures.
On the other hand, the assignment operator does work for structures. It can be
used in two ways: to initialize the member variables of a structure or to copy
themembervariablesfromonestructuretoanother. Aninitializationlookslike
this:
| Point_t |     | blank = | { 3.0, | 4.0 | };  |     |     |
| ------- | --- | ------- | ------ | --- | --- | --- | --- |
Thevaluesinsquigglybracesgetassignedtothemembervariablesofthestruc-
ture one by one, in order. So in this case, x gets the first value and y gets the
second.
Unfortunately, this syntax can be used only in an initialization, not in an as-
| signment | statement. | So     | the following |     | is illegal: |       |     |
| -------- | ---------- | ------ | ------------- | --- | ----------- | ----- | --- |
| Point_t  |            | blank; |               |     |             |       |     |
| blank    | =          | { 3.0, | 4.0 };        |     | /* WRONG    | !! */ |     |
You might wonder why this perfectly reasonable statement should be illegal;
I’m not sure, but I think the problem is that the compiler doesn’t know what
typetherighthandsideshouldbe. Youmustspecifythetypeoftheassignment
| by adding | a   | typecast:  |      |     |     |     |     |
| --------- | --- | ---------- | ---- | --- | --- | --- | --- |
| Point_t   |     | blank;     |      |     |     |     |     |
| blank     | =   | (Point_t){ | 3.0, | 4.0 | };  |     |     |
That works.
| It is legal | to         | assign one   | structure     | to         | another. For | example:          |     |
| ----------- | ---------- | ------------ | ------------- | ---------- | ------------ | ----------------- | --- |
| Point_t     |            | p1 = {       | 3.0, 4.0      | };         |              |                   |     |
| Point_t     |            | p2 = p1;     |               |            |              |                   |     |
| printf      |            | ("%f, %f\n", | p2.x,         | p2.y);     |              |                   |     |
| The output  | of         | this program | is            | 3, 4.      |              |                   |     |
| 9.5         | Structures |              | as            | parameters |              |                   |     |
| You can     | pass       | structures   | as parameters |            | in the usual | way. For example, |     |
| void        | PrintPoint |              | (Point_t      | point)     |              |                   |     |
{
|     | printf | ("(%0.1f, |     | %0.1f)\n", | point.x, | point.y); |     |
| --- | ------ | --------- | --- | ---------- | -------- | --------- | --- |
}
PrintPoint() takes a point as an argument and outputs it in the standard
| format. | If you | call PrintPoint(blank), |     |     | it will | output (3.0, 4.0). |     |
| ------- | ------ | ----------------------- | --- | --- | ------- | ------------------ | --- |
As a second example, we can rewrite the ComputeDistance() function from
Section 5.2 so that it takes two Points as parameters instead of four doubles.

| 106    |                 |          |     |             | Structures |
| ------ | --------------- | -------- | --- | ----------- | ---------- |
| double | ComputeDistance | (Point_t | p1, | Point_t p2) |            |
{
| double | dx = | p2.x - p1.x;     |     |     |     |
| ------ | ---- | ---------------- | --- | --- | --- |
| double | dy = | p2.y - p1.y;     |     |     |     |
| return | sqrt | (dx*dx + dy*dy); |     |     |     |
}
| 9.6 Call | by value |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- |
When you pass a structure as an argument, remember that the argument and
the parameter are not the same variable. Instead, there are two variables (one
in the caller and one in the callee) that have the same value, at least initially.
For example, when we call PrintPoint(), the stack diagram looks like this:
x: 3
|     | PrintPoint() |       point |     |     |     |
| --- | ------------ | ----------- | --- | --- | --- |
y: 4
x: 3
      blank
main()
y: 4
If PrintPoint() happened to change one of the member variables of point, it
wouldhavenoeffectonblank. Ofcourse,thereisnoreasonforPrintPoint()to
modifyitsparameter,sothisisolationbetweenthetwofunctionsisappropriate.
This kind of parameter-passing is called “pass by value” because it is the value
| of the structure | (or other    | type) that | gets passed | to the function. |     |
| ---------------- | ------------ | ---------- | ----------- | ---------------- | --- |
| 9.7 Call         | by reference |            |             |                  |     |
An alternative parameter-passing mechanism that is available in C is called
“passbyreference.” BynowwealreadyknowthatCusespointersasreferences.
Thismechanismmakesitpossibletopassastructuretoaprocedureandmodify
it directly.
For example, you can reflect a point around the 45-degree line by swap-
ping the two coordinates. The most obvious (but incorrect) way to write a
| ReflectPoint()    | function | is something | like this: |             |          |
| ----------------- | -------- | ------------ | ---------- | ----------- | -------- |
| void ReflectPoint |          | (Point_t     | point)     | /* Does not | work! */ |
{
| double | temp | = point.x; |     |     |     |
| ------ | ---- | ---------- | --- | --- | --- |

| 9.7 Call | by reference |            |     |     | 107 |
| -------- | ------------ | ---------- | --- | --- | --- |
|          | point.x      | = point.y; |     |     |     |
|          | point.y      | = temp;    |     |     |     |
}
Thiswon’twork,becausethechangeswemakeinReflectPoint()willhaveno
| effect on | the caller. |     |     |     |     |
| --------- | ----------- | --- | --- | --- | --- |
Instead, we have to specify that we want to pass the parameter by reference.
| Our function | now          | has a | struct pointer argument | Point_t *ptr. |     |
| ------------ | ------------ | ----- | ----------------------- | ------------- | --- |
| void         | ReflectPoint |       | (Point_t *ptr)          |               |     |
{
|     | double | temp | = ptr->x; |     |     |
| --- | ------ | ---- | --------- | --- | --- |
ptr->x = ptr->y;
ptr->y = temp;
}
When we are accessing the struct member variables through a pointer we can
no longer use the "field-selection-operator" (.). Instead we need to use the
| "pointing-to" | operator | (->). |     |     |     |
| ------------- | -------- | ----- | --- | --- | --- |
Wepassareferenceofourstructparameterbyaddingthe"address-of"operator
| (&) to the   | structure | variable  | when we call    | the function:     |     |
| ------------ | --------- | --------- | --------------- | ----------------- | --- |
| PrintPoint   |           | (blank);  |                 |                   |     |
| ReflectPoint |           | (&blank); |                 |                   |     |
| PrintPoint   |           | (blank);  |                 |                   |     |
| The output   | of this   | program   | is as expected: |                   |     |
| (3.0,        | 4.0)      |           |                 |                   |     |
| (4.0,        | 3.0)      |           |                 |                   |     |
| Here’s how   | we would  | draw      | a stack diagram | for this program: |     |
ptr
|     |     | ReflectPoint() |        |     |     |
| --- | --- | -------------- | ------ | --- | --- |
x: 3  4
      blank
main()
y: 4  3
The parameter ptr is a reference to the structure named blank. The usual
representation for a reference is a dot with an arrow that points to whatever
| the reference | refers | to. |     |     |     |
| ------------- | ------ | --- | --- | --- | --- |
The important thing to see in this diagram is that any changes that
| ReflectPoint() |     | makes | through ptr will | also affect blank. |     |
| -------------- | --- | ----- | ---------------- | ------------------ | --- |
Passing structures by reference is more versatile than passing by value, because
thecalleecanmodifythestructure. Itisalsofaster,becausethesystemdoesnot

108 Structures
have to copy the whole structure. On the other hand, it is less safe, since it is
hardertokeeptrackofwhatgetsmodifiedwhere. Nevertheless, inCprograms,
almost all structures are passed by reference almost all the time. In this book
| I will follow | that | convention. |     |     |     |     |
| ------------- | ---- | ----------- | --- | --- | --- | --- |
9.8 Rectangles
Now let’s say that we want to create a structure to represent a rectangle. The
questionis,whatinformationdoIhavetoprovideinordertospecifyarectangle?
To keep things simple let’s assume that the rectangle will be oriented vertically
| or horizontally, |     | never at | an angle. |     |     |     |
| ---------------- | --- | -------- | --------- | --- | --- | --- |
There are a few possibilities: I could specify the center of the rectangle (two
coordinates)anditssize(widthandheight),orIcouldspecifyoneofthecorners
| and the size, | or  | I could | specify two | opposing | corners. |     |
| ------------- | --- | ------- | ----------- | -------- | -------- | --- |
Themostcommonchoiceinexistingprogramsistospecifytheupperleftcorner
of the rectangle and the size. To do that in C, we will define a structure that
| contains | a Point_t | and | two doubles. |     |     |     |
| -------- | --------- | --- | ------------ | --- | --- | --- |
| typedef  | struct    |     |              |     |     |     |
{
Point_t corner;
|     | double | width, | height; |     |     |     |
| --- | ------ | ------ | ------- | --- | --- | --- |
} Rectangle_t;
Noticethatonestructurecancontainanother. Infact,thissortofthingisquite
common. Ofcourse, thismeansthatinordertocreateaRectangle_t, wehave
| to create   | a Point_t | first: |             |        |       |     |
| ----------- | --------- | ------ | ----------- | ------ | ----- | --- |
| Point_t     | corner    | =      | { 0.0, 0.0  | };     |       |     |
| Rectangle_t |           | box    | = { corner, | 100.0, | 200.0 | };  |
This code creates a new Rectangle_t structure and initializes the member
| variables. | The | figure shows | the effect | of  | this assignment. |     |
| ---------- | --- | ------------ | ---------- | --- | ---------------- | --- |
x: 3
point
y: 4

box
|                |     |             | width      |     | 100       |      |
| -------------- | --- | ----------- | ---------- | --- | --------- | ---- |
|                |     |             | height     |     | 200       |      |
| We can access  |     | the width   | and height | in  | the usual | way: |
| box.width      |     | += 50.0;    |            |     |           |      |
| printf("%f\n", |     | box.width); |            |     |           |      |

| 9.9 Structures |     | as  | return | types |     |     |     |     | 109 |
| -------------- | --- | --- | ------ | ----- | --- | --- | --- | --- | --- |
In order to access the member variables of corner, we can use a temporary
variable:
| Point_t        |     | temp              | = box.corner; |     |                 |     |     |     |     |
| -------------- | --- | ----------------- | ------------- | --- | --------------- | --- | --- | --- | --- |
| double         |     | x = temp.x;       |               |     |                 |     |     |     |     |
| Alternatively, |     | we can            | compose       | the | two statements: |     |     |     |     |
| double         |     | x = box.corner.x; |               |     |                 |     |     |     |     |
It makes the most sense to read this statement from right to left: “Extract x
| from | the corner | of the | box, | and assign | it  | to the local | variable | x.” |     |
| ---- | ---------- | ------ | ---- | ---------- | --- | ------------ | -------- | --- | --- |
While we are on the subject of composition, I should point out that you can, in
| fact,       | create the | Point | and | the Rectangle |     | at the same | time: |     |     |
| ----------- | ---------- | ----- | --- | ------------- | --- | ----------- | ----- | --- | --- |
| Rectangle_t |            | box   | = { | { 0.0,        | 0.0 | }, 100.0,   | 200.0 | };  |     |
The innermost squiggly braces are the coordinates of the corner point; together
theymakeupthefirstofthethreevaluesthatgointothenewRectangle. This
| statement | is         | an example | of  | nested    | structure. |       |     |     |     |
| --------- | ---------- | ---------- | --- | --------- | ---------- | ----- | --- | --- | --- |
| 9.9       | Structures |            |     | as return |            | types |     |     |     |
Youcanwritefunctionsthatreturnstructures. Forexample,FindCenter()has
a Rectangle_t parameter and returns a Point_t that contains the coordinates
| of the  | center | of the rectangle: |     |              |     |      |     |     |     |
| ------- | ------ | ----------------- | --- | ------------ | --- | ---- | --- | --- | --- |
| Point_t |        | FindCenter        |     | (Rectangle_t |     | box) |     |     |     |
{
|     | double  | x      | = box.corner.x |       | + box.width/2;  |     |     |     |     |
| --- | ------- | ------ | -------------- | ----- | --------------- | --- | --- | --- | --- |
|     | double  | y      | = box.corner.y |       | + box.height/2; |     |     |     |     |
|     | Point_t | result |                | = {x, | y};             |     |     |     |     |
return result;
}
To call this function, we have to pass a Rectangle_t as an argument (notice
that it is being passed by value), and assign the return value to a Point_t
variable:
| Rectangle_t |     | box          | = {          | {0.0,   | 0.0},  | 100, 200 | };  |     |     |
| ----------- | --- | ------------ | ------------ | ------- | ------ | -------- | --- | --- | --- |
| Point_t     |     | center       | = FindCenter |         | (box); |          |     |     |     |
| PrintPoint  |     | (center);    |              |         |        |          |     |     |     |
| The output  | of  | this program |              | is (50, | 100).  |          |     |     |     |
We could have passed the structure as a reference to the function. In this case
| our function |     | would look | like | this:        |     |       |     |     |     |
| ------------ | --- | ---------- | ---- | ------------ | --- | ----- | --- | --- | --- |
| Point_t      |     | FindCenter |      | (Rectangle_t |     | *box) |     |     |     |
{
|     | double  | x      | = box->corner.x |       | +   | box->width/2;  |     |     |     |
| --- | ------- | ------ | --------------- | ----- | --- | -------------- | --- | --- | --- |
|     | double  | y      | = box->corner.y |       | +   | box->height/2; |     |     |     |
|     | Point_t | result |                 | = {x, | y}; |                |     |     |     |
return result;
}

110 Structures
Notice, how we had to change the access to the members of the structure,
since box is now a pointer. We would also have to change the function call for
FindCenter():
| Point_t | center  | = FindCenter |       | (&box); |              |
| ------- | ------- | ------------ | ----- | ------- | ------------ |
| 9.10    | Passing | other        | types |         | by reference |
It’snotjuststructuresthatcanbepassedbyreference. Alltheothertypeswe’ve
seencan,too. Forexample,toswaptwointegers,wecouldwritesomethinglike:
| void | Swap (int | *x, int | *y) |     |     |
| ---- | --------- | ------- | --- | --- | --- |
{
int temp = *x;
*x = *y;
*y = temp;
}
| We would | call this | function | in the | usual way: |     |
| -------- | --------- | -------- | ------ | ---------- | --- |
| int i    | = 7;      |          |        |            |     |
| int j    | = 9;      |          |        |            |     |
| printf   | (" i=%i,  | j=%i\n", |        | i, j);     |     |
| Swap     | (&i, &j); |          |        |            |     |
| printf   | (" i=%i,  | j=%i\n", |        | i, j);     |     |
The output of this program shows that the variable values have been swapped.
Draw a stack diagram for this program to convince yourself this is true. If the
parameters x and y were declared as regular integer variables (without the s),
Swap() would not work. It would modify x and y and have no effect on i and
j.
When people start passing things like integers by reference, they often try to
| use an expression | as          | a reference | argument. |            | For example: |
| ----------------- | ----------- | ----------- | --------- | ---------- | ------------ |
| int i             | = 7;        |             |           |            |              |
| int j             | = 9;        |             |           |            |              |
| Swap              | (&i, &j+1); |             |           | /* WRONG!! | */           |
Presumably the programmer wanted to increase the value of j by 1 before it is
passed to the function. This does not work as expected, because the expression
j+1nowisinterpretedapointervalueandinnowpointingtoamemorylocation
beyond the variable j. It is a little tricky to figure out exactly what kinds of
expressionsmakesensetobepassedbyreference. Fornowagoodruleofthumb
| is that reference | arguments |     | have to | be variables. |     |
| ----------------- | --------- | --- | ------- | ------------- | --- |
| 9.11              | Glossary  |     |         |               |     |
structure: Acollectionofdatagroupedtogetherandtreatedasasingleobject.
member variable: Oneofthenamedpiecesofdatathatmakeupastructure.

9.12 Exercises 111
reference: Avaluethatindicatesorreferstoavariableorstructure. Inastate
diagram, a reference appears as an arrow.
pass by value: Amethodofparameter-passinginwhichthevalueprovidedas
an argument is copied into the corresponding parameter, but the param-
eter and the argument occupy distinct locations.
pass by reference: Amethodofparameter-passinginwhichtheparameteris
areferencetotheargumentvariable. Changestotheparameteralsoaffect
the argument variable.
9.12 Exercises
Exercise 9.1
Section9.5definesthefunctionPrintPoint(). Theargumentofthisfunctionispassed
along as a value (call-by-value).
a. Change the definition of this function, so that it only passes a reference to the
structure to the function for printing (call-by-reference).
b. Test the new function with different values and document the results.
Exercise 9.2
Write a program, that defines a struct Person_t. This struct should contain two
members. The first member should be a string of sufficient length, to contain the
name of a person. The second member should be an integer value containing the
persons age.
a. Define two struct variables person1 and person2.
Initialize the two struct variables with suitable values. The first person should
be called Betsy. Betsy should be 42 years old.
The second person should be named after yourself and should also be as old as
yourself.
b. Write a function PrintPerson(). The function should take a struct variable
of type Person_t as an argument and print the name of the person and the
corresponding age.
c. WriteafunctionHappyBirthday(). Thefunctionshouldincreasetheageofthe
corresponding person by one year and print out a birthday greeting.
Hint: You need to passes a reference to the structure to the function (call-by-
reference). If your function uses call-by-value, the age only changes in the local
copy of the struct and the changes you have made are lost, once the function
terminates. Try it out, if you do not believe me!
Exercise 9.3
Most computer games can capture our interest only when their actions are non-
predictable,otherwisetheybecomeboringquickly. Section7.6tellsushowtogenerate
random numbers in in C.

112 Structures
Write a simple game, where the computer chooses an arbitrary number in the range
between1and20. YouwillthenbeaskedtoguessthenumberchosenbytheComputer.
To give you a hint the computer should answer your guess in the following way: in
case your guess was lower than the number of the computer, the output should be:
| My number | is larger! |     |     |     |
| --------- | ---------- | --- | --- | --- |
If you guess was higher than the number of the computer, the output should read:
| My number | is smaller! |     |     |     |
| --------- | ----------- | --- | --- | --- |
Itisnecessarytoseedtherandomnumbergeneratorwhenyoustartyourprogram(cf.
Section 7.14. You could use the time() function for this. It returns the actual time
| measured | in seconds since | 1971. |     |     |
| -------- | ---------------- | ----- | --- | --- |
srand(time(NULL)); /*Initialisation of the random number generator*/
Whenyoufoundtherightanswer,thecomputershouldcongratulateyou. Theprogram
shouldalsodisplaythenumberoftriesthatwhereneededinordertoguessthenumber.
Theprogramshouldalsokeepthea‘High-Score’,thatgetsupdatedonceournumberof
trialsislowerthananyprevioustry. TheHigh-Score(thenumberofminimalguesses)
| should be | stored in a | struct, together | with the name | of the player. |
| --------- | ----------- | ---------------- | ------------- | -------------- |
TheHigh-Score()functionshouldaskforyournameandstoreit,whenyourcurrent
| number | of tries is lower | than the previous | High-Score | value. |
| ------ | ----------------- | ----------------- | ---------- | ------ |
Theprogramthengivesyouthechancetoplayagainorstopthegamebypressing’q’
on the keyboard.

Appendix A
Coding Style
A.1 A short guide on style
Inthelastfewsections,Iusedthephrase“byconvention”severaltimestoindi-
catedesigndecisionsthatarearbitraryinthesensethattherearenosignificant
reasons to do things one way or another, but dictated by convention.
Inthesecases, itistoyouradvantagetobefamiliarwithconventionanduseit,
since it will make your programs easier for others to understand. At the same
time, it is important to distinguish between (at least) three kinds of rules:
Divine law: This is my phrase to indicate a rule that is true because of some
underlying principle of logic or mathematics, and that is true in any pro-
gramming language (or other formal system). For example, there is no
way to specify the location and size of a bounding box using fewer than
four pieces of information. Another example is that adding integers is
commutative. That’spartofthedefinitionofadditionandhasnothingto
do with C.
Rules of C: These are the syntactic and semantic rules of C that you cannot
violate, because the resulting program will not compile or run. Some are
arbitrary; for example, the fact that the = symbol represents assignment
and not equality. Others reflect underlying limitations of the compila-
tion or execution process. For example, you have to specify the types of
parameters, but not arguments.
Style and convention: There are a lot of rules that are not enforced by the
compiler,butthatareessentialforwritingprogramsthatarecorrect,that
you can debug and modify, and that others can read. Examples include
indentation and the placement of squiggly braces, as well as conventions
for naming variables, functions and types.

| 114 |     |     |     |     |     | Coding | Style |
| --- | --- | --- | --- | --- | --- | ------ | ----- |
InthissectionIwillbrieflysummarizethecodingstyleusedwithinthisbook. It
1
follows loosely the "Nasa C Style Guide" and its main intent is on readability
| rather than | saving | space | or typing | effort. |     |     |     |
| ----------- | ------ | ----- | --------- | ------- | --- | --- | --- |
SinceChassuchalonghistoryofusage,manydifferentcodingstyleshavebeen
developed and used. It is important that you can read them and follow one
particular scheme in all your code. This makes it much more accessible should
you find yourself in a position where you have to share your work with other
people or have to access code written by your younger self - many years ago...
| A.2 | Naming |     | conventions |     | and | capitalization |     |
| --- | ------ | --- | ----------- | --- | --- | -------------- | --- |
rules
As a general rule, you should always choose meaningful names for your identi-
fiers. Ideally the name of a variable or function already explains its behaviour
or use.
It may be more typing effort to use a function named FindSubString() rather
than FndSStr(). However, the former is almost self describing and might save
| you a lot | in debugging-time. |        |          |        |     |     |     |
| --------- | ------------------ | ------ | -------- | ------ | --- | --- | --- |
| Don’t     | use single         | letter | variable | names! |     |     |     |
Similarly to functions, you should give your variables names that speak for
themselves and make clear what values will be stored by this variable. There
are few noticeable exceptions to this rule: People use i, j and k as counter
variables in loops and for spacial coordinates people use x, y and z. Use these
conventionsiftheysuityou. Don’ttrytoinventnewconventionsallbyyourself.
Thefollowingcapitalizationstylesholdbeusedforthedifferentelementsinyour
program. The consistent use of one style gives the programmer and the reader
of the source code a quick way to determine the meaning of different items in
your program:
variableNames: variablenamesalwaysstartwithlower-case,multiplewords
| are | separated | by  | capitalizing | the first | letter. |     |     |
| --- | --------- | --- | ------------ | --------- | ------- | --- | --- |
CONSTANTS: use all upper case letters. In order to avoid name space
| collisions |     | it might | be necessary | to use | a prefix | such as MY_CONSTANT. |     |
| ---------- | --- | -------- | ------------ | ------ | -------- | -------------------- | --- |
FunctionNames: start always with upper case and should possibly contain a
| verb  | describing | the     | function. | Names for | functions | that test values | should |
| ----- | ---------- | ------- | --------- | --------- | --------- | ---------------- | ------ |
| start | with       | ’Is’ or | ’Are’.    |           |           |                  |        |
UserDefinedTypes_t: always end in ’_t’. Type names names must be capi-
| talised | in  | order to | avoid conflict | with | POSIX names. |     |     |
| ------- | --- | -------- | -------------- | ---- | ------------ | --- | --- |
pointerNames_p: in order to visually separate pointer variables from ordi-
| nary | variables | you | should | consider ending | pointers | with ’_p’. |     |
| ---- | --------- | --- | ------ | --------------- | -------- | ---------- | --- |
1www.scribd.com/doc/6878959/NASA-C-programming-guide

| A.3 Bracing | style   |       |     |     |     |     | 115 |
| ----------- | ------- | ----- | --- | --- | --- | --- | --- |
| A.3         | Bracing | style |     |     |     |     |     |
There exist different bracing or indent styles that serve the goal to make your
codemorereadablethroughtheuseofaconsistentindentationforcontrolblock
structures. The styles differ in the way the braces are indented with the rest
of the control block. This book uses the BSD/Allman Style because its is the
most readable of the four. It needs more horizontal space than the K&R Style
| but it makes | it very | easy to track | opening | and closing | braces. |     |     |
| ------------ | ------- | ------------- | ------- | ----------- | ------- | --- | --- |
When you are writing programs, make sure that you are using one style con-
sistently. In larger projects all contributors should agree on the style they are
using. ModernprogrammingenvironmentslikeEclipsesupportyouthroughthe
| automatic     | enforcement | of a single | style. |     |     |     |     |
| ------------- | ----------- | ----------- | ------ | --- | --- | --- | --- |
| /*Whitesmiths | Style*/     |             |        |     |     |     |     |
if (condition)
{
statement1;
statement2;
}
Is named after Whitesmiths C, an early commercial C compiler that used this
| style in its | examples. | Some people | refer | to it as the | One True | Brace Style. |     |
| ------------ | --------- | ----------- | ----- | ------------ | -------- | ------------ | --- |
/*GNU Style*/
if (condition)
{
statement1;
statement2;
}
Indents are always four spaces per level, with the braces halfway between the
| outer and      | inner indent | levels. |     |     |     |     |     |
| -------------- | ------------ | ------- | --- | --- | --- | --- | --- |
| /*K&R/Kernel   | Style*/      |         |     |     |     |     |     |
| if (condition) |              | {       |     |     |     |     |     |
statement1;
statement2;
}
ThisstyleisnamedaftertheprogrammingexamplesinthebookTheCProgram-
ming Language by Brian W. Kernighan and Dennis Ritchie (the C inventors).
The K&R style is the style that is hardest to read. The opening brace happens
to be at the far right side of the control statement and can be hard to find.
The braces therefore have different indentation levels. Nevertheless, many C
| programs     | use this | style. So you | should | be able to read | it. |     |     |
| ------------ | -------- | ------------- | ------ | --------------- | --- | --- | --- |
| /*BSD/Allman | Style*/  |               |        |                 |     |     |     |
if (condition)

116 Coding Style
{
statement1;
statement2;
}
| This style | is used | for all | the examples | in this book. |
| ---------- | ------- | ------- | ------------ | ------------- |
| A.4        | Layout  |         |              |               |
Blockcommentsshouldbeusedatthetopofyourfile,beforeallfunctiondecla-
rations, to explain the purpose of the program and give additional information.
Youshouldalsouseasimilardocumentationstylebeforeeveryrelevantfunction
in your program.
/*
| * File:   | test.c |            |      |     |
| --------- | ------ | ---------- | ---- | --- |
| * Author: | Peter  | Programmer |      |     |
| * Date:   | May,   | 29th,      | 2009 |     |
*
| * Purpose: | to       | demonstrate | good | programming |
| ---------- | -------- | ----------- | ---- | ----------- |
| *          | practise |             |      |             |
* /
| #include | <stdlib.h> |     |     |     |
| -------- | ---------- | --- | --- | --- |
/*
| * main | function, | does | not use | arguments |
| ------ | --------- | ---- | ------- | --------- |
*/
| int main | (void) |     |     |     |
| -------- | ------ | --- | --- | --- |
{
| return | EXIT_SUCCESS; |     |     |     |
| ------ | ------------- | --- | --- | --- |
}

| Appendix | B   |     |     |
| -------- | --- | --- | --- |
ASCII-Table
| Dec Hex | Oct Character | Dec Hex | Oct Character |
| ------- | ------------- | ------- | ------------- |
| 0 0x00  | 000 NUL       | 32 0x20 | 040 SP        |
| 1 0x01  | 001 SOH       | 33 0x21 | 041 !         |
| 2 0x02  | 002 STX       | 34 0x22 | 042 "’        |
| 3 0x03  | 003 ETX       | 35 0x23 | 043 #         |
| 4 0x04  | 004 EOT       | 36 0x24 | 044 $         |
| 5 0x05  | 005 ENQ       | 37 0x25 | 045 %         |
| 6 0x06  | 006 ACK       | 38 0x26 | 046 &         |
| 7 0x07  | 007 BEL       | 39 0x27 | 047 ’         |
| 8 0x08  | 010 BS        | 40 0x28 | 050 (         |
| 9 0x09  | 011 TAB       | 41 0x29 | 051 )         |
| 10 0x0A | 012 LF        | 42 0x2A | 052 *         |
| 11 0x0B | 013 VT        | 43 0x2B | 053 +         |
| 12 0x0C | 014 FF        | 44 0x2C | 054 ,         |
| 13 0x0D | 015 CR        | 45 0x2D | 055 -         |
| 14 0x0E | 016 SO        | 46 0x2E | 056 .         |
| 15 0x0F | 017 SI        | 47 0x2F | 057 /         |
| 16 0x10 | 020 DLE       | 48 0x30 | 060 0         |
| 17 0x11 | 021 DC1       | 49 0x31 | 061 1         |
| 18 0x12 | 022 DC2       | 50 0x32 | 062 2         |
| 19 0x13 | 023 DC3       | 51 0x33 | 063 3         |
| 20 0x14 | 024 DC4       | 52 0x34 | 064 4         |
| 21 0x15 | 025 NAK       | 53 0x35 | 065 5         |
| 22 0x16 | 026 SYN       | 54 0x36 | 066 6         |
| 23 0x17 | 027 ETB       | 55 0x37 | 067 7         |
| 24 0x18 | 030 CAN       | 56 0x38 | 070 8         |
| 25 0x19 | 031 EM        | 57 0x39 | 071 9         |
| 26 0x1A | 032 SUB       | 58 0x3A | 072 :         |
| 27 0x1B | 033 ESC       | 59 0x3B | 073 ;         |
| 28 0x1C | 034 FS        | 60 0x3C | 074 "<        |
| 29 0x1D | 035 GS        | 61 0x3D | 075 =         |
| 30 0x1E | 036 RS        | 62 0x3E | 076 ">        |
| 31 0x1F | 037 US        | 63 0x3F | 077 ?         |

| 118     |               |          | ASCII-Table   |
| ------- | ------------- | -------- | ------------- |
| Dec Hex | Oct Character | Dec Hex  | Oct Character |
| 64 0x40 | 100 @         | 96 0x60  | 140 ‘         |
| 65 0x41 | 101 A         | 97 0x61  | 141 a         |
| 66 0x42 | 102 B         | 98 0x62  | 142 b         |
| 67 0x43 | 103 C         | 99 0x63  | 143 c         |
| 68 0x44 | 104 D         | 100 0x64 | 144 d         |
| 69 0x45 | 105 E         | 101 0x65 | 145 e         |
| 70 0x46 | 106 F         | 102 0x66 | 146 f         |
| 71 0x47 | 107 G         | 103 0x67 | 147 g         |
| 72 0x48 | 110 H         | 104 0x68 | 150 h         |
| 73 0x49 | 111 I         | 105 0x69 | 151 i         |
| 74 0x4A | 112 J         | 106 0x6A | 152 j         |
| 75 0x4B | 113 K         | 107 0x6B | 153 k         |
| 76 0x4C | 114 L         | 108 0x6C | 154 l         |
| 77 0x4D | 115 M         | 109 0x6D | 155 m         |
| 78 0x4E | 116 N         | 110 0x6E | 156 n         |
| 79 0x4F | 117 O         | 111 0x6F | 157 o         |
| 80 0x50 | 120 P         | 112 0x70 | 160 p         |
| 81 0x51 | 121 Q         | 113 0x71 | 161 q         |
| 82 0x52 | 122 R         | 114 0x72 | 162 r         |
| 83 0x53 | 123 S         | 115 0x73 | 163 s         |
| 84 0x54 | 124 T         | 116 0x74 | 164 t         |
| 85 0x55 | 125 U         | 117 0x75 | 165 u         |
| 86 0x56 | 126 V         | 118 0x76 | 166 v         |
| 87 0x57 | 127 W         | 119 0x77 | 167 w         |
| 88 0x58 | 130 X         | 120 0x78 | 170 x         |
| 89 0x59 | 131 Y         | 121 0x79 | 171 y         |
| 90 0x5A | 132 Z         | 122 0x7A | 172 z         |
| 91 0x5B | 133 [         | 123 0x7B | 173 {         |
| 92 0x5C | 134 \         | 124 0x7C | 174 |         |
| 93 0x5D | 135 ]         | 125 0x7D | 175 }         |
| 94 0x5E | 136 ˆ         | 126 0x7E | 176 "         |
| 95 0x5F | 137 _         | 127 0x7F | 177 DEL       |

Index
| <ctype.h>,      | 98      |     | string,      | 97        |         |         |
| --------------- | ------- | --- | ------------ | --------- | ------- | ------- |
| <math.h>,       | 28      |     | comparison   | operator, |         | 54      |
| <stdio.h>,      | 28      |     | compile,     | 2, 9      |         |         |
| <stdlib.h>,     | 57,     | 82  | compile-time | error,    | 4,      | 51      |
| <string.h>,     | 91,     | 93  | composition, | 20,       | 22, 28, | 53, 109 |
|                 |         |     | concatenate, | 101       |         |         |
| absolute        | value,  | 51  | conditional, | 39,       | 46      |         |
| address,        | 95, 101 |     |              |           |         |         |
|                 |         |     | alternative, |           | 40      |         |
| ambiguity,      | 6       |     | chained,     | 41,       | 46      |         |
| argument,       | 27, 32, | 35  |              |           |         |         |
|                 |         |     | nested,      | 41,       | 46      |         |
| arithmetic      |         |     | constant     | values,   | 26      |         |
| floating-point, |         | 26  |              |           |         |         |
|                 |         |     | constants,   | 26        |         |         |
| integer,        | 19      |     |              |           |         |         |
|                 |         |     | counter,     | 84, 101   |         |         |
array, 88
| copying,          | 79  |     |              |       |     |     |
| ----------------- | --- | --- | ------------ | ----- | --- | --- |
|                   |     |     | dead code,   | 50,   | 58  |     |
| element,          | 78  |     |              |       |     |     |
|                   |     |     | debugging,   | 3, 9, | 51  |     |
| length,           | 81  |     |              |       |     |     |
|                   |     |     | declaration, | 15,   | 104 |     |
| array parameters, |     | 84  |              |       |     |     |
|                   |     |     | decrement,   | 78,   | 101 |     |
arrays, 77
|     |     |     | deterministic, |     | 81, 88 |     |
| --- | --- | --- | -------------- | --- | ------ | --- |
assigning
diagram
| string,     | 96  |        |               |     |     |     |
| ----------- | --- | ------ | ------------- | --- | --- | --- |
|             |     |        | stack,        | 45, | 71  |     |
| assignment, | 16, | 22, 63 |               |     |     |     |
|             |     |        | state,        | 45  |     |     |
|             |     |        | distribution, | 83  |     |     |
body, 73
| loop,     | 65      |     | division        |                   |        |     |
| --------- | ------- | --- | --------------- | ----------------- | ------ | --- |
|           |         |     | floating-point, |                   | 66     |     |
| bool, 56, | 58      |     |                 |                   |        |     |
| boolean,  | 54      |     | integer,        | 19                |        |     |
|           |         |     | double          | (floating-point), |        | 25  |
| bottom-up | design, | 85  |                 |                   |        |     |
|           |         |     | Doyle,          | Arthur            | Conan, | 5   |
bug, 3
| call, 35  |            |              | element,       | 78, 88 |         |     |
| --------- | ---------- | ------------ | -------------- | ------ | ------- | --- |
| call by   | reference, | 84, 106, 110 | encapsulation, |        | 68, 70, | 73  |
| call by   | value, 84, | 106          | error, 9       |        |         |     |
| character | operator,  | 20           | compile-time,  |        | 4, 51   |     |
|           |            |              | logic,         | 4      |         |     |
Chianti, 79
| coding     | style, 113 |     | run-time,     |     | 4       |            |
| ---------- | ---------- | --- | ------------- | --- | ------- | ---------- |
| comment,   | 7, 9       |     | EXIT_FAILURE, |     | 57      |            |
| comparison |            |     | EXIT_SUCCESS, |     | 57      |            |
| operator,  | 39         |     | expression,   | 18, | 20, 22, | 27, 28, 79 |

120 Index
| fava beans,     | 79         |        | high-level,       | 1      |     |
| --------------- | ---------- | ------ | ----------------- | ------ | --- |
| flag, 55        |            |        | low-level,        | 1      |     |
| floating-point, | 35         |        | natural,          | 5      |     |
|                 |            |        | programming,      |        | 1   |
| floating-point  | number,    | 25     |                   |        |     |
| for, 80         |            |        | safe,             | 4      |     |
| formal          | language,  | 5, 9   | length            |        |     |
| fruitful        | function,  | 34, 49 | array,            | 81     |     |
| function,       | 35, 70     |        | string,           | 93     |     |
| bool,           | 56         |        | Linux, 5          |        |     |
| definition,     | 29         |        | literalness,      | 6      |     |
| fruitful,       | 34,        | 49     | local variable,   | 71,    | 73  |
| main,           | 29         |        | logarithm,        | 66     |     |
|                 |            |        | logic error,      | 4      |     |
| math,           | 27         |        |                   |        |     |
| multiple        | parameter, | 34     | logical operator, |        | 55  |
| void,           | 49         |        | loop, 65,         | 73, 79 |     |
|                 |            |        | body,             | 65     |     |
| generalization, | 68,        | 71, 73 | counting,         | 84     |     |
for, 80
| header       | file, 28  |      | infinite,      | 65, 73    |            |
| ------------ | --------- | ---- | -------------- | --------- | ---------- |
| ctype.h,     | 98        |      |                |           |            |
|              |           |      | loop variable, | 68,       | 71, 79, 94 |
| math.h,      | 28        |      |                |           |            |
|              |           |      | low-level      | language, | 1, 9       |
| stdio.h,     | 28        |      |                |           |            |
| stdlib.h,    | 57,       | 82   | main, 29       |           |            |
| string.h,    | 91,       | 93   | math function, | 27        |            |
| hello world, | 7         |      | acos(),        | 49        |            |
| high-level   | language, | 1, 9 | exp(),         | 49        |            |
| histogram,   | 86–88     |      | fabs(),        | 51        |            |
| Holmes,      | Sherlock, | 5    | sin(),         | 49        |            |
mean, 83
| increment,      | 78, 101      |             | member            | variable,   | 111         |
| --------------- | ------------ | ----------- | ----------------- | ----------- | ----------- |
| incremental     | development, | 51          | modulus,          | 40, 46      |             |
| index, 79,      | 88, 94,      | 101         | multiple          | assignment, | 63          |
| infinite        | loop, 65,    | 73          |                   |             |             |
| infinite        | recursion,   | 45, 46      | natural           | language,   | 5, 9        |
| initialization, | 25,          | 35, 55      | nested structure, |             | 42, 55, 109 |
| input           |              |             | newline,          | 13, 44      |             |
| flushing        | the          | buffer, 100 | nondeterministic, |             | 81          |
| keyboard,       | 99           |             |                   |             |             |
|                 |              |             | operand,          | 19, 22      |             |
input buffer
|            |           |             | operator,    | 18, 22 |        |
| ---------- | --------- | ----------- | ------------ | ------ | ------ |
| flushing   | the       | buffer, 100 |              |        |        |
|            |           |             | character,   | 20     |        |
| integer    | division, | 19          |              |        |        |
| interpret, | 2, 9      |             | comparison,  |        | 39, 54 |
|            |           |             | conditional, |        | 58     |
| iteration, | 64, 73    |             |              |        |        |
|            |           |             | decrement,   | 78     |        |
| keyword,   | 18, 22    |             | increment,   | 78     |        |
|            |           |             | logical,     | 55, 58 |        |
| language   |           |             | modulus,     | 40     |        |
| formal,    | 5         |             | sizeof,      | 81     |        |

Index 121
| order of   | operations, | 19       | state, 104     |       |        |
| ---------- | ----------- | -------- | -------------- | ----- | ------ |
| output,    | 13          |          | state diagram, |       | 104    |
|            |             |          | statement,     | 3, 9, | 22     |
| parameter, | 32,         | 35, 105  |                |       |        |
|            |             |          | assignment,    |       | 16, 63 |
| multiple,  |             | 34       |                |       |        |
|            |             |          | comment,       |       | 7      |
| parameter  | passing,    | 106, 110 | conditional,   |       | 39     |
parse, 6, 9
|          |            |     | declaration,    |     | 15, 104 |
| -------- | ---------- | --- | --------------- | --- | ------- |
| pass by  | reference, | 111 | for,            | 80  |         |
| pass by  | value,     | 111 |                 |     |         |
|          |            |     | initialization, |     | 55      |
| pattern  |            |     | output,         | 13  |         |
| counter, | 85         |     |                 |     |         |
|          |            |     | printf,         | 7   |         |
| pi, 49   |            |     | return,         | 42, | 49, 109 |
poetry, 6
|     |     |     | while, | 64  |     |
| --- | --- | --- | ------ | --- | --- |
Point, 103
|          |         |     | statistics, | 83  |     |
| -------- | ------- | --- | ----------- | --- | --- |
| pointer, | 95, 101 |     |             |     |     |
String, 13
| portable,   | 1     |     |             |     |     |
| ----------- | ----- | --- | ----------- | --- | --- |
|             |       |     | string, 96, | 97  |     |
| precedence, | 19    |     |             |     |     |
|             |       |     | length,     | 93  |     |
| printf(),   | 7, 99 |     |             |     |     |
struct, 103
| problem-solving, |              | 9           |               |           |     |
| ---------------- | ------------ | ----------- | ------------- | --------- | --- |
|                  |              |             | as parameter, |           | 105 |
| program          | development, | 51, 73      |               |           |     |
|                  |              |             | as return     | type,     | 109 |
| bottom-up,       |              | 85          |               |           |     |
|                  |              |             | member        | variable, | 104 |
| encapsulation,   |              | 70          |               |           |     |
|                  |              |             | operations,   |           | 105 |
| programming      |              | language, 1 |               |           |     |
|                  |              |             | Point,        | 103       |     |
prose, 6
|               |     |     | Rectangle, |     | 108 |
| ------------- | --- | --- | ---------- | --- | --- |
| pseudorandom, |     | 88  |            |     |     |
|               |     |     | structure, | 111 |     |
style, 113
random, 88
|            |         |     | syntax, 4, | 9   |     |
| ---------- | ------- | --- | ---------- | --- | --- |
| random     | number, | 81  |            |     |     |
| Rectangle, | 108     |     |            |     |     |
tab, 73
| recursion,    | 43,     | 46            |                  |           |     |
| ------------- | ------- | ------------- | ---------------- | --------- | --- |
| infinite,     | 45,     | 46            | table, 66        |           |     |
|               |         |               | two-dimensional, |           | 68  |
| recursive,    | 44      |               |                  |           |     |
|               |         |               | temporary        | variable, | 50  |
| redundancy,   | 6       |               |                  |           |     |
|               |         |               | traverse,        | 93, 101   |     |
| reference,    | 104,    | 106, 110, 111 |                  |           |     |
|               |         |               | counting,        | 84        |     |
| return,       | 42, 49, | 109           |                  |           |     |
|               |         |               | type, 14,        | 22        |     |
| return type,  | 58      |               |                  |           |     |
|               |         |               | bool,            | 55        |     |
| return value, | 49,     | 58            |                  |           |     |
| rounding,     | 27      |               | array,           | 77        |     |
|               |         |               | double,          | 25        |     |
| run-time      | error,  | 4, 45, 79     |                  |           |     |
int, 19
| safe language, |     | 4   | String,      | 13  |     |
| -------------- | --- | --- | ------------ | --- | --- |
| scaffolding,   | 52, | 58  | typecasting, | 27, | 105 |
scanf(), 99
| seed, 88   |       |     | value, 14, | 15, 22 |     |
| ---------- | ----- | --- | ---------- | ------ | --- |
| semantics, | 4, 9, | 55  | boolean,   | 54     |     |
|            |       |     | variable,  | 15, 22 |     |
sizeof, 81
| stack, 45      |     |        | local, | 71, 73  |        |
| -------------- | --- | ------ | ------ | ------- | ------ |
| stack diagram, |     | 45, 71 | loop,  | 68, 71, | 79, 94 |

122 Index
temporary, 50
void, 49, 58
while statement, 64