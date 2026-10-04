// Uruchamia rozwiązania wzorcowe z src/python w Pyodide (Python skompilowany do WebAssembly),
// czyli w tym samym środowisku, w którym kurs na stronie ocenia rozwiązania uczniów.
// Uzupełnia scripts/run_tests.py (CPython): oba muszą dawać identyczne wyniki.
//
//   npm install --no-save pyodide@0.29.5
//   node scripts/run_tests_pyodide.mjs
//
// Wersja pyodide powinna odpowiadać wersji używanej przez stronę kursu.

import { readFileSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { loadPyodide } from "pyodide";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const jsonDir = join(root, "zbior_zadan_json");

const toCase = (c) => {
  const job = { input: c.input, expected: c.output };
  if (c.files) job.files = c.files;
  if (c.expected_files) job.expected_files = c.expected_files;
  return job;
};

const pyodide = await loadPyodide();
pyodide.runPython(readFileSync(join(root, "scripts", "judge_harness.py"), "utf8"));
const run = pyodide.globals.get("_pyk_run");

let total = 0;
const failures = [];
for (const file of readdirSync(jsonDir).sort()) {
  const chapter = JSON.parse(readFileSync(join(jsonDir, file), "utf8"));
  const stem = file.replace(/\.json$/, "");
  for (const exercise of chapter.exercises) {
    total += 1;
    const id = exercise.id.slice(4, 6) + exercise.id.slice(6).toLowerCase();
    const code = readFileSync(join(root, "src", "python", stem, `zad${id}.py`), "utf8");
    const cases = [...exercise.examples, ...exercise.testcases].map(toCase);
    if (!exercise.testcases.length) cases.forEach((c) => (c.expected = null));
    const result = JSON.parse(run(code, JSON.stringify(cases)));
    if (result.compile_error) {
      failures.push(`${exercise.slug}: ${result.compile_error.type}: ${result.compile_error.message}`);
      continue;
    }
    result.results.forEach((r, n) => {
      if (r.ok === false || (r.ok === undefined && r.error)) {
        failures.push(`${exercise.slug} — przypadek ${n + 1}: ${r.error ? r.error.type : "złe wyjście"}`);
      }
    });
  }
}

failures.forEach((line) => console.error("✗ " + line));
console.log(`Pyodide ${pyodide.version}: ${total - new Set(failures.map((f) => f.split(/[: ]/)[0])).size}/${total} zadań zaliczonych.`);
process.exit(failures.length ? 1 : 0);
