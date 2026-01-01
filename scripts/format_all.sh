#!/bin/bash

# Script to format all solution files in the repository
# This script formats code in multiple programming languages using their respective formatters

# Note: We don't use 'set -e' here because we want to continue even if some formatters fail
# But we do want to catch undefined variables
set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

hr() {
    printf '%s\n' "==================================="
}

ts() {
    date '+%H:%M:%S'
}

log() {
    printf '[%s] %s\n' "$(ts)" "$1"
}

ok() {
    printf '[%s] [OK] %s\n' "$(ts)" "$1"
}

warn() {
    printf '[%s] [WARN] %s\n' "$(ts)" "$1"
}

section() {
    hr
    log "$1"
    hr
    printf '\n'
}

section "Formatting all solution files"

# Change to repository root
cd "$REPO_ROOT"

# Summary counters
total_files=0
total_skipped=0
summary=""

count_files() {
    local dir="$1"
    shift
    local count
    if [ ! -d "$dir" ]; then
        printf '0'
        return
    fi
    count=$(find "$dir" -type f \( "$@" \) 2>/dev/null | wc -l | tr -d ' ')
    printf '%s' "$count"
}

append_summary() {
    local label="$1"
    local count="$2"
    local status="$3"
    summary="${summary}${label}: ${count} (${status})\n"
}

# Format Python files with black
py_count=$(count_files "src/python" -name "*.py")
total_files=$((total_files + py_count))
log "Formatting Python files (${py_count})..."
if [ "$py_count" -eq 0 ]; then
    warn "No Python files found, skipping"
    append_summary "Python" "$py_count" "empty"
elif command -v black &> /dev/null; then
    if find src/python -name "*.py" -type f -exec black {} +; then
        ok "Python files formatted with black"
        append_summary "Python" "$py_count" "formatted"
    else
        warn "Some Python files may have formatting errors"
        append_summary "Python" "$py_count" "partial"
    fi
else
    warn "black not found, skipping Python formatting"
    total_skipped=$((total_skipped + py_count))
    append_summary "Python" "$py_count" "skipped"
fi
printf '\n'

# Format C++ files with clang-format
cpp_count=$(count_files "src/cpp" -name "*.cpp" -o -name "*.hpp" -o -name "*.c" -o -name "*.h")
total_files=$((total_files + cpp_count))
log "Formatting C++ files (${cpp_count})..."
if [ "$cpp_count" -eq 0 ]; then
    warn "No C++ files found, skipping"
    append_summary "C++" "$cpp_count" "empty"
elif command -v clang-format &> /dev/null; then
    # Determine clang-format style
    if [ -f "$REPO_ROOT/.clang-format" ]; then
        CLANG_STYLE="file"
    else
        CLANG_STYLE="Google"
    fi
    # Format all C++ files
    find src/cpp -type f \( -name "*.cpp" -o -name "*.hpp" -o -name "*.c" -o -name "*.h" \) \
        -exec clang-format -i -style="$CLANG_STYLE" {} + 2>/dev/null || \
        warn "Some C++ files may have formatting errors"
    ok "C++ files formatted with clang-format"
    append_summary "C++" "$cpp_count" "formatted"
else
    warn "clang-format not found, skipping C++ formatting"
    total_skipped=$((total_skipped + cpp_count))
    append_summary "C++" "$cpp_count" "skipped"
fi
printf '\n'

# Format Java files with google-java-format
java_count=$(count_files "src/java" -name "*.java")
total_files=$((total_files + java_count))
log "Formatting Java files (${java_count})..."
if [ "$java_count" -eq 0 ]; then
    warn "No Java files found, skipping"
    append_summary "Java" "$java_count" "empty"
elif command -v google-java-format &> /dev/null; then
    find src/java -name "*.java" -type f -exec google-java-format -i {} +
    ok "Java files formatted with google-java-format"
    append_summary "Java" "$java_count" "formatted"
else
    warn "google-java-format not found, skipping Java formatting"
    total_skipped=$((total_skipped + java_count))
    append_summary "Java" "$java_count" "skipped"
fi
printf '\n'

# Format JavaScript files with prettier (preferred) or eslint
js_count=$(count_files "src/js" -name "*.js")
total_files=$((total_files + js_count))
log "Formatting JavaScript files (${js_count})..."
if [ "$js_count" -eq 0 ]; then
    warn "No JavaScript files found, skipping"
    append_summary "JavaScript" "$js_count" "empty"
elif command -v prettier &> /dev/null; then
    if find src/js -name "*.js" -type f -print0 | xargs -0 -r prettier --write; then
        ok "JavaScript files formatted with prettier"
        append_summary "JavaScript" "$js_count" "formatted"
    else
        warn "Some JavaScript files may have formatting errors"
        append_summary "JavaScript" "$js_count" "partial"
    fi
elif command -v eslint &> /dev/null; then
    if find src/js -name "*.js" -type f -print0 | xargs -0 -r eslint --fix; then
        ok "JavaScript files formatted with eslint"
        append_summary "JavaScript" "$js_count" "formatted"
    else
        warn "eslint failed (missing config?)"
        append_summary "JavaScript" "$js_count" "partial"
    fi
else
    warn "neither prettier nor eslint found, skipping JavaScript formatting"
    total_skipped=$((total_skipped + js_count))
    append_summary "JavaScript" "$js_count" "skipped"
fi
printf '\n'

# Format Rust files with rustfmt
rust_count=$(count_files "src/rust" -name "*.rs")
total_files=$((total_files + rust_count))
log "Formatting Rust files (${rust_count})..."
if [ "$rust_count" -eq 0 ]; then
    warn "No Rust files found, skipping"
    append_summary "Rust" "$rust_count" "empty"
elif command -v rustfmt &> /dev/null; then
    # Check if rustfmt.toml exists for configuration
    if [ -f "$REPO_ROOT/rustfmt.toml" ]; then
        find src/rust -name "*.rs" -type f -exec rustfmt --config-path "$REPO_ROOT/rustfmt.toml" --edition 2021 {} +
    else
        find src/rust -name "*.rs" -type f -exec rustfmt --edition 2021 {} +
    fi
    ok "Rust files formatted with rustfmt"
    append_summary "Rust" "$rust_count" "formatted"
else
    warn "rustfmt not found, skipping Rust formatting"
    total_skipped=$((total_skipped + rust_count))
    append_summary "Rust" "$rust_count" "skipped"
fi
printf '\n'

# Format Haskell files with ormolu
haskell_count=$(count_files "src/haskell" -name "*.hs")
total_files=$((total_files + haskell_count))
log "Formatting Haskell files (${haskell_count})..."
if [ "$haskell_count" -eq 0 ]; then
    warn "No Haskell files found, skipping"
    append_summary "Haskell" "$haskell_count" "empty"
elif command -v ormolu &> /dev/null; then
    find src/haskell -name "*.hs" -type f -exec ormolu --mode inplace {} +
    ok "Haskell files formatted with ormolu"
    append_summary "Haskell" "$haskell_count" "formatted"
else
    warn "ormolu not found, skipping Haskell formatting"
    total_skipped=$((total_skipped + haskell_count))
    append_summary "Haskell" "$haskell_count" "skipped"
fi
printf '\n'

# Format Bash files with shfmt (optional)
bash_count=$(count_files "src/bash" -name "*.sh")
total_files=$((total_files + bash_count))
log "Formatting Bash files (${bash_count})..."
if [ "$bash_count" -eq 0 ]; then
    warn "No Bash files found, skipping"
    append_summary "Bash" "$bash_count" "empty"
elif command -v shfmt &> /dev/null; then
    find src/bash -name "*.sh" -type f -exec shfmt -w -i 4 {} +
    ok "Bash files formatted with shfmt"
    append_summary "Bash" "$bash_count" "formatted"
else
    warn "shfmt not found, skipping Bash formatting"
    total_skipped=$((total_skipped + bash_count))
    append_summary "Bash" "$bash_count" "skipped"
fi
printf '\n'

section "Formatting complete!"
printf "Total files: %s\n" "$total_files"
printf "Skipped files: %s\n" "$total_skipped"
printf "\nBreakdown:\n"
printf "%b" "$summary"
