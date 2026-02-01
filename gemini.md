# ♊ Project Gemini Constitution

## 1. Data Schema

### Input (`JavaSource`)
```json
{
  "raw_code": "string",  // The raw Selenium Java code (TestNG)
  "metadata": {
    "source_file_name": "string (optional)",
    "package_name": "string (optional)"
  }
}
```

### Output (`PlaywrightResult`)
```json
{
  "ts_code": "string",   // The converted Playwright TypeScript code
  "file_structure": [    // Virtual file system output
    {
      "path": "string",
      "content": "string"
    }
  ],
  "conversion_log": [   // Warnings or notes about non-1:1 mappings
    "string"
  ]
}
```

## 2. Behavioral Rules
- **Readability First:** Do not aim for strict line-by-line synthesis. Produce idiomatic Playwright/TypeScript code (e.g., use `await expect()` instead of strict TestNG assertions if cleaner).
- **Structure:** Use the standard Playwright test structure (`test`, `expect` from `@playwright/test`).
- **UI Interaction:** The tool must expose a UI for input/output.

## 3. Architectural Invariants
- **Core Logic:** Python scripts in `tools/` handle the parsing and conversion logic (using regex or AST processing).
- **Interface:** A lightweight web UI (HTML/CSS + Python Backend) to accept input and render output.
- **State:** No persistent database required for now; ephemeral session state.
