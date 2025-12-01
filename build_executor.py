#!/usr/bin/env python3
"""
Bazel Build Executor for Calculator Project
Compiles and runs the calculator binary using Bazel
"""

import subprocess
import sys
import os


def run_command(cmd, description):
    """Execute a command and return success status"""
    print(f"\n{'='*60}")
    print(f">>> {description}")
    print(f"{'='*60}")
    print(f"Running: {' '.join(cmd)}\n")
    
    try:
        result = subprocess.run(cmd, cwd="/home/littlestarmalli/repo/bazel-for-build")
        if result.returncode == 0:
            print(f"\n✓ {description} - SUCCESS")
            return True
        else:
            print(f"\n✗ {description} - FAILED")
            return False
    except Exception as e:
        print(f"\n✗ Error executing command: {e}")
        return False


def main():
    """Main build orchestration function"""
    print("\n" + "="*60)
    print("BAZEL BUILD EXECUTOR - Calculator Project")
    print("="*60)
    
    # Check if Bazel is installed
    print("\nChecking Bazel installation...")
    result = subprocess.run(["bazel", "--version"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✓ {result.stdout.strip()}")
    else:
        print("✗ Bazel not found. Please install Bazel first.")
        sys.exit(1)
    
    # Run Bazel build
    build_cmd = ["bazel", "build", "//src:calculator"]
    if not run_command(build_cmd, "Building calculator binary"):
        sys.exit(1)
    
    # Run the compiled binary
    print(f"\n{'='*60}")
    print(">>> Running the compiled calculator")
    print(f"{'='*60}\n")
    
    binary_path = "/home/littlestarmalli/repo/bazel-for-build/bazel-bin/src/calculator"
    try:
        result = subprocess.run([binary_path], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
    except Exception as e:
        print(f"Error running binary: {e}")
        sys.exit(1)
    
    print(f"\n{'='*60}")
    print("✓ BUILD COMPLETE - All operations successful!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
