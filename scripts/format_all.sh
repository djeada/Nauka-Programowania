#!/bin/bash

# Script to format all solution files in the repository
# This script formats code in multiple programming languages using their respective formatters

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "==================================="
echo "Formatting all solution files"
echo "==================================="
echo ""

# Change to repository root
cd "$REPO_ROOT"

# Format Python files with black
echo "Formatting Python files..."
if command -v black &> /dev/null; then
    find src/python -name "*.py" -type f -exec black {} +
    echo "✓ Python files formatted with black"
else
    echo "⚠ Warning: black not found, skipping Python formatting"
fi
echo ""

# Format C++ files with clang-format
echo "Formatting C++ files..."
if command -v clang-format &> /dev/null; then
    find src/cpp -type f \( -name "*.cpp" -o -name "*.hpp" -o -name "*.c" -o -name "*.h" \) -exec clang-format -i -style=file {} +
    echo "✓ C++ files formatted with clang-format"
else
    echo "⚠ Warning: clang-format not found, skipping C++ formatting"
fi
echo ""

# Format Java files with google-java-format
echo "Formatting Java files..."
if command -v google-java-format &> /dev/null; then
    find src/java -name "*.java" -type f -exec google-java-format -i {} +
    echo "✓ Java files formatted with google-java-format"
else
    echo "⚠ Warning: google-java-format not found, skipping Java formatting"
fi
echo ""

# Format JavaScript files with prettier (preferred) or eslint
echo "Formatting JavaScript files..."
if command -v prettier &> /dev/null; then
    find src/js -name "*.js" -type f -exec prettier --write {} +
    echo "✓ JavaScript files formatted with prettier"
elif command -v eslint &> /dev/null; then
    find src/js -name "*.js" -type f -exec eslint --fix {} + 2>/dev/null || true
    echo "✓ JavaScript files formatted with eslint"
else
    echo "⚠ Warning: neither prettier nor eslint found, skipping JavaScript formatting"
fi
echo ""

# Format Rust files with rustfmt
echo "Formatting Rust files..."
if command -v rustfmt &> /dev/null; then
    find src/rust -name "*.rs" -type f -exec rustfmt {} +
    echo "✓ Rust files formatted with rustfmt"
else
    echo "⚠ Warning: rustfmt not found, skipping Rust formatting"
fi
echo ""

# Format Haskell files with ormolu
echo "Formatting Haskell files..."
if command -v ormolu &> /dev/null; then
    find src/haskell -name "*.hs" -type f -exec ormolu --mode inplace {} +
    echo "✓ Haskell files formatted with ormolu"
else
    echo "⚠ Warning: ormolu not found, skipping Haskell formatting"
fi
echo ""

# Format Bash files with shfmt (optional)
echo "Formatting Bash files..."
if command -v shfmt &> /dev/null; then
    find src/bash -name "*.sh" -type f -exec shfmt -w -i 4 {} +
    echo "✓ Bash files formatted with shfmt"
else
    echo "⚠ Warning: shfmt not found, skipping Bash formatting"
fi
echo ""

echo "==================================="
echo "Formatting complete!"
echo "==================================="
