## Author
Mahesh Swaminathan

## Stevens Login
mswamina@stevens.edu

## GitHub Repo
https://github.com/maheshs85/Test-Harness

## Hours Spent
I estimate that I spent approximately 5-6 hours on this project.

## Testing
- Manual testing with various inputs to cover edge cases.
- Data files for common tests to cover most functionality.
- Test harness uses the same format given in canvas.

## Unresolved Issues
- Instead of directly executing {PROGRAM_NAME} in the command line, I am prefixing it with 'python3'.

## Difficult Issue and Resolution
The built-in 'wc' program displayed one less in the word count compared to my program, which correctly showed the accurate count. The discrepancy was caused due to the absence of a newline character at the end of the file. Once I added it, my program produced the same output as the built-in program.

## Implemented Extensions

### Extension 1: More advanced wc: multiple files
- Evaluation:
  - The CA can test this extension by appending multiple test files as given in canvas.

### Extension 2: More advanced wc: flags to control output
- Evaluation:
  - The CA can test this extension by adding different flag combinations as in canvas.

### Extension 3: More advanced gron: control the base-object name
- Evaluation:
  - The CA can test this extension by giving a different base name as in canvas.
