#!/usr/bin/env bash

# Checks that every solution file under src/ parses / compiles.
#
# Each language is checked with its own toolchain; languages whose toolchain
# is not installed are skipped with a notice. Exits non-zero if any file fails.
#
#   python   python3 compile() with SyntaxWarning/DeprecationWarning as errors
#   js       node --check
#   bash     bash -n (+ shellcheck -S error when shellcheck is installed)
#   cpp      g++ -std=c++20 -fsyntax-only -Wall   (only errors fail)
#   java     javac -d <tmp> zadN/*.java           (javac, or java -m jdk.compiler)
#   rust     rustc --edition 2021 --emit=metadata
#   haskell  ghc -fno-code
#
# Usage: scripts/check_sources.sh [options] [PATH...]
#
#   -l, --lang NAME   only check this language (repeatable, or comma-separated)
#   -j, --jobs N      number of parallel jobs (default: number of CPUs)
#   -v, --verbose     print the full compiler output of failing files
#   --no-shellcheck   only run bash -n for bash files, even if shellcheck exists
#   -h, --help        show this help
#   PATH...           only check files under these paths (default: src/)

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ALL_LANGS=(python js bash cpp java rust haskell)

usage() {
    sed -n '/^# Usage:/,/^[^#]/{/^#/s/^# \{0,1\}//p}' "${BASH_SOURCE[0]}"
}

die() {
    printf 'check_sources: %s\n' "$1" >&2
    exit 2
}

# ---------------------------------------------------------------------------
# Per-file check, run in parallel by xargs. Prints "ok<TAB>file" or
# "fail<TAB>file"; compiler output of failures goes to $CHECK_LOG_DIR.
# ---------------------------------------------------------------------------
check_one() {
    local lang=$1 file=$2
    local log tmp status=0
    log="$CHECK_LOG_DIR/$lang/$(printf '%s' "$file" | tr '/' '_').log"
    tmp="$(mktemp -d "$CHECK_WORK_DIR/$lang.XXXXXX")"

    case "$lang" in
        python)
            python3 -W error::SyntaxWarning -W error::DeprecationWarning -c '
import sys
with open(sys.argv[1], "rb") as f:
    compile(f.read(), sys.argv[1], "exec", dont_inherit=True)
' "$file" >"$log" 2>&1 || status=1
            ;;
        js)
            node --check "$file" >"$log" 2>&1 || status=1
            ;;
        bash)
            bash -n "$file" >"$log" 2>&1 || status=1
            if [[ $status -eq 0 && -n "$CHECK_SHELLCHECK" ]]; then
                shellcheck -s bash -S error -f gcc "$file" >>"$log" 2>&1 || status=1
            fi
            ;;
        cpp)
            "$CHECK_CXX" -std=c++20 -fsyntax-only -Wall "$file" >"$log" 2>&1 || status=1
            ;;
        java)
            # Compile the whole task directory, so helper classes kept in
            # separate files next to Main.java are found.
            local -a javac_cmd
            read -ra javac_cmd <<<"$CHECK_JAVAC"
            "${javac_cmd[@]}" -encoding UTF-8 -nowarn -d "$tmp" \
                "$(dirname "$file")"/*.java >"$log" 2>&1 || status=1
            ;;
        rust)
            rustc --edition 2021 --crate-type bin --emit=metadata -A warnings \
                -o "$tmp/out.rmeta" "$file" >"$log" 2>&1 || status=1
            ;;
        haskell)
            ghc -fno-code -v0 -outputdir "$tmp" "$file" >"$log" 2>&1 || status=1
            ;;
    esac

    rm -rf "$tmp"
    if [[ $status -eq 0 ]]; then
        rm -f "$log"
        printf 'ok\t%s\n' "$file"
    else
        printf 'fail\t%s\n' "$file"
    fi
}

# ---------------------------------------------------------------------------
# Toolchain detection. On failure sets SKIP_REASON and returns 1.
# Must not run in a subshell: it sets CHECK_JAVAC for the java workers.
# ---------------------------------------------------------------------------
require_cmd() {
    command -v "$1" >/dev/null 2>&1 && return 0
    SKIP_REASON="$1 not found"
    return 1
}

detect_toolchain() {
    SKIP_REASON=""
    case "$1" in
        python) require_cmd python3 ;;
        js) require_cmd node ;;
        bash) require_cmd bash ;;
        cpp) require_cmd "$CHECK_CXX" ;;
        java)
            if command -v javac >/dev/null 2>&1; then
                CHECK_JAVAC="javac"
            elif command -v java >/dev/null 2>&1 &&
                java -m jdk.compiler/com.sun.tools.javac.Main -version >/dev/null 2>&1; then
                CHECK_JAVAC="java -m jdk.compiler/com.sun.tools.javac.Main"
            else
                SKIP_REASON="no JDK found (neither javac nor java -m jdk.compiler)"
                return 1
            fi
            ;;
        rust) require_cmd rustc ;;
        haskell) require_cmd ghc ;;
    esac
}

# Prints the files of a language found under the selected paths (NUL-separated).
list_files() {
    local -a pattern
    case "$1" in
        python) pattern=(-name '*.py') ;;
        js) pattern=(-name '*.js') ;;
        bash) pattern=(-name '*.sh') ;;
        cpp) pattern=(-name '*.cpp') ;;
        java) pattern=(-name 'Main.java') ;;
        rust) pattern=(-name '*.rs') ;;
        haskell) pattern=(-name '*.hs') ;;
    esac
    find "${PATHS[@]}" -type f "${pattern[@]}" -not -path '*/__pycache__/*' -print0 |
        sort -z
}

# Shows the relevant part of a failing file's compiler output.
show_log() {
    local log=$1
    [[ -s "$log" ]] || return 0
    if [[ $VERBOSE -eq 1 ]]; then
        sed 's/^/        | /' "$log"
    elif grep -qi 'error' "$log"; then
        grep -i -A 2 'error' "$log" | grep -v '^--$' | head -n 12 | sed 's/^/        | /'
    else
        head -n 12 "$log" | sed 's/^/        | /'
    fi
}

# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------
LANGS=()
PATHS=()
JOBS="$(nproc 2>/dev/null || getconf _NPROCESSORS_ONLN 2>/dev/null || echo 4)"
VERBOSE=0
USE_SHELLCHECK=1

add_langs() {
    local -a parts
    local l known
    IFS=',' read -ra parts <<<"$1"
    for l in "${parts[@]}"; do
        known=0
        for k in "${ALL_LANGS[@]}"; do [[ "$l" == "$k" ]] && known=1; done
        [[ $known -eq 1 ]] || die "unknown language '$l' (known: ${ALL_LANGS[*]})"
        LANGS+=("$l")
    done
}

while (($#)); do
    case "$1" in
        -l | --lang)
            [[ $# -ge 2 ]] || die "$1 requires an argument"
            add_langs "$2"
            shift 2
            ;;
        --lang=*)
            add_langs "${1#--lang=}"
            shift
            ;;
        -j | --jobs)
            [[ $# -ge 2 && "$2" =~ ^[1-9][0-9]*$ ]] || die "$1 requires a positive number"
            JOBS=$2
            shift 2
            ;;
        -v | --verbose)
            VERBOSE=1
            shift
            ;;
        --no-shellcheck)
            USE_SHELLCHECK=0
            shift
            ;;
        -h | --help)
            usage
            exit 0
            ;;
        --)
            shift
            PATHS+=("$@")
            break
            ;;
        -*) die "unknown option '$1' (see --help)" ;;
        *)
            PATHS+=("$1")
            shift
            ;;
    esac
done

[[ ${#LANGS[@]} -gt 0 ]] || LANGS=("${ALL_LANGS[@]}")

# Resolve paths relative to the caller's directory, then work from the repo
# root so reported file names are short and stable.
if [[ ${#PATHS[@]} -eq 0 ]]; then
    PATHS=(src)
else
    resolved=()
    for p in "${PATHS[@]}"; do
        [[ -e "$p" ]] || die "no such path: $p"
        abs="$(cd "$(dirname "$p")" && pwd)/$(basename "$p")"
        if [[ "$abs" == "$REPO_ROOT" ]]; then
            resolved+=(.)
        else
            resolved+=("${abs#"$REPO_ROOT"/}")
        fi
    done
    PATHS=("${resolved[@]}")
fi
cd "$REPO_ROOT" || die "cannot enter $REPO_ROOT"

CHECK_WORK_DIR="$(mktemp -d "${TMPDIR:-/tmp}/check_sources.XXXXXX")" || die "mktemp failed"
trap 'rm -rf "$CHECK_WORK_DIR"' EXIT
CHECK_LOG_DIR="$CHECK_WORK_DIR/logs"
CHECK_CXX="${CXX:-g++}"
CHECK_JAVAC=""
CHECK_SHELLCHECK=""
if [[ $USE_SHELLCHECK -eq 1 ]] && command -v shellcheck >/dev/null 2>&1; then
    CHECK_SHELLCHECK=1
fi

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
total_ok=0
total_failed=0
failed_langs=()
skipped_langs=()

for lang in "${LANGS[@]}"; do
    if ! detect_toolchain "$lang"; then
        printf '[%-7s] SKIPPED: %s\n' "$lang" "$SKIP_REASON"
        skipped_langs+=("$lang")
        continue
    fi

    mkdir -p "$CHECK_LOG_DIR/$lang"
    export CHECK_WORK_DIR CHECK_LOG_DIR CHECK_CXX CHECK_JAVAC CHECK_SHELLCHECK
    export -f check_one

    results="$(list_files "$lang" |
        xargs -0 -r -n 1 -P "$JOBS" bash -c 'check_one "$1" "$2"' _ "$lang")"

    ok=0
    failed_files=()
    while IFS=$'\t' read -r state file; do
        [[ -n "$state" ]] || continue
        if [[ "$state" == ok ]]; then
            ok=$((ok + 1))
        else
            failed_files+=("$file")
        fi
    done <<<"$results"

    if [[ $((ok + ${#failed_files[@]})) -eq 0 ]]; then
        printf '[%-7s] no files\n' "$lang"
        continue
    fi

    extra=""
    [[ "$lang" == bash && -n "$CHECK_SHELLCHECK" ]] && extra=" (with shellcheck)"
    printf '[%-7s] ok: %d  failed: %d%s\n' "$lang" "$ok" "${#failed_files[@]}" "$extra"

    if [[ ${#failed_files[@]} -gt 0 ]]; then
        failed_langs+=("$lang")
        mapfile -t failed_files < <(printf '%s\n' "${failed_files[@]}" | sort)
        for file in "${failed_files[@]}"; do
            printf '    FAIL %s\n' "$file"
            show_log "$CHECK_LOG_DIR/$lang/$(printf '%s' "$file" | tr '/' '_').log"
            if [[ "${GITHUB_ACTIONS:-}" == true ]]; then
                printf '::error file=%s::%s check failed\n' "$file" "$lang"
            fi
        done
    fi

    total_ok=$((total_ok + ok))
    total_failed=$((total_failed + ${#failed_files[@]}))
done

printf '\nTotal: %d ok, %d failed' "$total_ok" "$total_failed"
[[ ${#skipped_langs[@]} -gt 0 ]] && printf ', skipped: %s' "${skipped_langs[*]}"
printf '\n'

[[ $total_failed -eq 0 ]]
