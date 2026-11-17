# SignalVsNoise Python Lab

A learning project for building Python foundations through small,
tested components for SignalVsNoise, a citizen issue-reporting system.

This repository contains exercises and early building blocks.
It is not a complete application.

## Current functionality

- Filter open reports by category.
- Summarize affected counts while distinguishing unknown values from zero.
- Identify missing fields.
- Validate affected counts.
- Detect duplicate report IDs.
- Combine uniqueness checks with affected-count validation.

## Project structure

- `func/`: Functions developed through incremental exercises.
- `sample_data/`: Example data.
- `test/`: Tests using Python assertions.

## Running the tests

Open a terminal in the repository root and run:

```powershell
py -m test.test01_func04
py -m test.test02_func05
py -m test.test03_func06
py -m test.test04_func07
py -m test.test05_func08
py -m test.test06_func09
py -m test.test07_func11
```

The tests use Python's built-in `assert` statements.
A successful run may produce no output.

## Learning approach

I implement the exercises myself, with AI-assisted explanations,
feedback, and code review. The numbered modules reflect the AIs understanding of my learning
progress. I intent to build the whole SignalVsNoise program in cooperation with AI, but want to make sure, that I understand every step of the way. This enables me to alter needed structures as I see fit, to keep security a priority and not be reliant on AI in the end for understanding what is going on.