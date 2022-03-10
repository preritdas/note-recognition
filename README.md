# Measuring Note Reading Accuracy

This program is a semi-automated method of creating and tracking a piano student's reading accuracy by note. Below, I explain the problem, the solution, and how to use this program. 

## The Problem

Not all notes are treated equally. When it comes to the treble and bass clef, there are certain notes that confuse students repeatedly causing slowness in sight reading or general learning. These tricky notes are _different for everyone_ (though there are some broad patterns which I discuss at the end). In a non musical context, the obvious solution to a problem like this is data. Simulations, analysis, and graphical distributions would allow us to identify areas of weakness and then target those areas to 'flatten the curve' while advancing the curve holistically. 

## The Solution

Tracking the accuracy of each individual note. There are approximately 4.5 octaves between the bottom ledger-lines of the bass clef and the upper ledger-lines of the treble clef. That leaves roughly 31 notes whose accuracy are of vital importance. I break these down by clef (the simulation is run clef-independently). 

We use a [tool](https://www.musictheory.net/exercises/note) to present a student with a random note and give them a few seconds to make an _educated guess_. This is vital: if the student calculates the note using a phonetic tool or counting method the purpose isn't achieved. We're testing their ability to sight-read. So, they should only have a few seconds to answer each question, and be instructed to try to 'recognize' it, and if they can't, trust their gut. 

The teacher (or individual) follows along with the programs prompts in conjunction with this website to enter in their note-by-note accuracy. The program then analyzes their results, compiles it into a CSV, and generates a distribution of their reading accuracy. 

## Instructions

Necessary files:

```
main.py
Students/Copy-Treble.csv
Students/Copy-Bass.csv
```

Download these files manually or clone the repository. If you're running this with a new individual, run the program with the following command: `python main.py create student_name treble`, or replace `treble` with `bass` to start with the bass clef. To run the program again, or using a student's pre-compiled data, use the command `python main.py student_name treble`. Or, of course, `bass`. 

Open the simulation website and follow along, entering the correct answer and whether it was inputted correctly. Once you have completed the number of questions you indicated in the program's prompt, it will automatically append the data to any preexisting files, create a new file if their file doesn't exist, and then create a distribution plot. The plot is saved to a `Graphs/` subdirectory with the format `student_name-Treble.png`. Or, of course, `Bass`. 