# Code Formatting Script

This script formats all solution files in the repository using language-specific formatters.

## Usage

```bash
./scripts/format_all.sh
```

## Supported Languages and Formatters

The script formats code in the following languages:

| Language   | Formatter            | Installation |
|------------|----------------------|--------------|
| Python     | black                | `pip install black` |
| C++        | clang-format         | System package manager |
| Java       | google-java-format   | Download from [releases](https://github.com/google/google-java-format/releases) |
| JavaScript | prettier or eslint   | `npm install -g prettier` or `npm install -g eslint` |
| Rust       | rustfmt              | Included with Rust (`rustup component add rustfmt`) |
| Haskell    | ormolu               | `cabal install ormolu` or `stack install ormolu` |
| Bash       | shfmt (optional)     | Download from [releases](https://github.com/mvdan/sh/releases) |

## Prerequisites

Before running the script, install the required formatters for the languages you want to format. The script will skip formatting for any language where the formatter is not installed.

## Configuration

- **C++**: Uses the `.clang-format` file in the repository root
- **Python**: Uses black's default configuration
- **JavaScript**: Prefers prettier over eslint if both are available
- **Rust**: Uses default rustfmt configuration
- **Haskell**: Uses default ormolu configuration

## Examples

Format all files:
```bash
./scripts/format_all.sh
```

Format only Python files:
```bash
find src/python -name "*.py" -exec black {} +
```

Format only C++ files:
```bash
find src/cpp -type f \( -name "*.cpp" -o -name "*.hpp" -o -name "*.c" -o -name "*.h" \) -exec clang-format -i -style=file {} +
```

## Notes

- The script will only format files in the `src/` directory
- Files are formatted in-place (original files are modified)
- The script continues even if a formatter is not installed
- All formatters respect their respective configuration files if present
