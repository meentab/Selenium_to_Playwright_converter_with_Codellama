# 🔎 Project Findings & Research

## Phase 0: Initialization
- [x] Answer Discovery Questions
    - **Goal:** Selenium Java -> Playwright TS Converter
    - **Source:** User Input via UI
    - **Output:** UI Display + Directory generation
    - **Priority:** Readability > Strict 1:1

## Research Logs
- **Challenge:** Java and TS have different sync/async models. Selenium is sync (mostly), Playwright is async.
- **Strategy:** The converter must wrap interactions in `await`.
- **Mapping:**
    - `driver.findElement(By.id("foo")).click()` -> `await page.locator('#foo').click()`
    - `Assert.assertEquals(a, b)` -> `expect(a).toBe(b)`
