# Calculator Project with Bazel

This is a simple C project built with Bazel.

## Project Structure

```
bazel-for-build/
├── WORKSPACE          # Bazel workspace configuration
├── BUILD              # Root BUILD file
├── src/
│   ├── main.c         # Main calculator program
│   └── BUILD          # Build rules for calculator
└── build_executor.py  # Python script to execute the build
```

## Project Description

A simple calculator program that demonstrates:
- Basic C programming with functions
- Bazel build system setup
- Python automation of the build process

## Building the Project

### Method 1: Using Python Build Executor (Recommended)

```bash
cd /home/littlestarmalli/repo/bazel-for-build
python3 build_executor.py
```

This script will:
1. Check for Bazel installation
2. Build the calculator binary using Bazel
3. Execute the compiled binary
4. Display results with status messages

### Method 2: Manual Bazel Commands

```bash
# Build
bazel build //src:calculator

# Run
./bazel-bin/src/calculator

# Clean
bazel clean
```

## What the Program Does

The calculator program performs basic arithmetic operations:
- Adds numbers: 5 + 3 = 8
- Multiplies numbers: 5 * 3 = 15
- Additional test cases included

## Prerequisites

- Bazel (latest stable version)
- GCC/Clang compiler
- Python 3.x
