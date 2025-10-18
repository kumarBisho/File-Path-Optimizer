# Simplify Unix-Style Absolute Path

## Live Demo
[Open the live App here](https://file-path-optimizer-1.onrender.com)

## Problem Description
Given a string `A` representing an absolute path for a file (Unix-style).
return the string after simplifying the absolute path.

## Problem Osutput
Simplified absolute path of given large input file path.

### Notes
- In Unix-style file systems:
  - A period `.` refers to the current directory.
  - A double period `..` refers to the directory up a level.
  - Any multiple consecutive slashes `//` are treated as a single slash `/`.
- In the simplified absolute path:
  - The path starts with a single slash `/`.
  - Any two directories are separated by a single slash `/`.
  - The path doesn't end with trailing slashes `/`.
  - The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period `.` or double period `..`).
  - The path will not have whitespace characters.


## Input Format
- The only argument given is string `A`.

## Output Format
- Return a string denoting the simplified absolute path for a file (Unix-style).

## Example
```
Input:  "/a/./b/../../c/"
Output: "/c"
```

## How to Run
1. Implement your solution in `main.cpp`.
2. Compile the code using a C++ compiler:
   ```
   g++ main.cpp -o simplify_path
   ```
3. Run the executable:
   ```
   ./simplify_path
   ```

## License
This project is for educational purposes.
