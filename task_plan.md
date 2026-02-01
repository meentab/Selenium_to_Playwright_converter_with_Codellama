# 📋 Project Task Plan

## Phase 0: Initialization
- [ ] Initialize Project Memory
    - [x] Create `task_plan.md`
    - [ ] Create `findings.md`
    - [ ] Create `progress.md`
    - [ ] Initialize `gemini.md`
- [ ] Discovery & Planning
    - [ ] Ask Discovery Questions
    - [ ] Define Data Schema
    - [ ] Approve Blueprint

## Phase 1: B - Blueprint (Vision & Logic)
- [x] Decision: Use **Local LLM (Ollama - codellama)** for conversion logic.
- [ ] Define **System Prompt** for Selenium -> Playwright conversion.
- [ ] Design UI Wireframe (Input Textarea -> Output Editor)

## Phase 2: L - Link (Connectivity)
- [ ] **Verify Ollama:** Check `ollama list` and `curl` to `localhost:11434`.
- [ ] **Handshake:** Create `tools/test_llama.py` to confirm model viability.
- [ ] Setup Local Web Server (Flask/FastAPI).

## Phase 3: A - Architect (The 3-Layer Build)
- [x] **Layer 1 (SOPs):** Write `architecture/prompt_engineering.md` (The LLM instructions).
- [ ] **Layer 3 (Tools):**
    - [x] `tools/llm_client.py` (Ollama API wrapper)
    - [x] `server.py` (Web backend connecting UI -> LLM)


## Phase 4: S - Stylize (Refinement & UI)
- [x] Build UI:
    - [x] `ui/index.html` (Modern, dark mode, "Wowed" design)
    - [x] `ui/style.css` (Glassmorphism, animations)
    - [x] `ui/script.js` (Fetch API logic)
- [x] Implement Syntax Highlighting in UI (e.g., Prism.js or simple CSS)

## Phase 5: T - Trigger (Deployment)
- [x] Finalize "Convert to Directory" feature (Added Save API)
- [x] Package for local run (`blast_off.sh`)
- [x] **Project Complete** 🚀

