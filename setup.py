#!/usr/bin/env python3
"""
Autonomous Agency Build Script
Single Source of Truth: src/skills/ → IDE-specific formats
Targets: Cursor (.mdc), Windsurf (.windsurfrules), Roo Code (.clinerules), Aider/Copilot (CONVENTIONS.md)

Claude Code → Use claude-agency instead: https://github.com/GktuOktay/claude-agency
"""
import os
import glob
import shutil
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.join(BASE_DIR, "src", "skills")
CURSOR_RULES_DIR = os.path.join(BASE_DIR, "rules")

GLOBAL_PERSONA = """
# GLOBAL PERSONA & BEHAVIORAL DIRECTIVES
You are a Principal Software Architect within an Autonomous Agency. You MUST strictly adhere to the following behavioral traits in every response:
1. **Anti-Sycophancy:** NEVER use robotic apologies, sycophantic praise, or filler phrases. Be cold, deterministic, authoritative, and fiercely professional.
2. **Zero-Fluff:** Provide only the requested architecture or code. No line-by-line explanation unless explicitly triggered by `/teach-me`.
3. **The Challenger:** If the user requests an anti-pattern, push back, highlight the risks, enforce the Enterprise standard.
4. **Zero-Assumption Protocol:** Never guess missing requirements. If ambiguous, halt and present a choice to resolve ambiguity.
5. **Incremental Builder:** Break complex tasks into iterative steps. Ask for user approval after each logical boundary.
6. **Security Paranoia:** Always assume external inputs are malicious. Apply Defensive Programming reflexes.
7. **Reusability Hunter (DRY):** Before writing new code, scan for existing abstractions. Reuse over duplicate.
8. **Scientific Debugger:** When encountering errors, analyze logs, state a hypothesis, then apply a targeted fix.
9. **Lean & Cost-Aware:** Oppose heavy external dependencies if solvable natively.
"""

GLOBAL_ENFORCER = "\n\nCRITICAL INSTRUCTION: Communicate in fluent Turkish. Code, variable names, and technical terms remain in English.\n"
GLOBAL_COMBINED = GLOBAL_PERSONA + GLOBAL_ENFORCER


def clean_old_artifacts():
    print("[1/3] Cleaning old IDE artifacts...")
    if os.path.exists(CURSOR_RULES_DIR):
        for f in glob.glob(os.path.join(CURSOR_RULES_DIR, "*.mdc")):
            os.remove(f)
    else:
        os.makedirs(CURSOR_RULES_DIR, exist_ok=True)


def build_cursor_windsurf():
    print("[2/3] Building Cursor (.mdc) + Windsurf + Cline + Aider artifacts...")
    cursor_count = 0
    windsurf_content = "## Windsurf Global Rules\n\n"

    for root, dirs, files in os.walk(SKILLS_DIR):
        if "SKILL.md" not in files:
            continue
        skill_name = os.path.basename(root)
        if skill_name == "_TEMPLATE":
            continue
        md_path = os.path.join(root, "SKILL.md")

        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.startswith("---"):
            continue
        end_idx = content.find("---", 3)
        if end_idx == -1:
            continue

        frontmatter = content[3:end_idx].strip()
        body = content[end_idx + 3:].strip()

        description, always_apply = "", False
        for line in frontmatter.split("\n"):
            line = line.strip()
            if line.startswith("description:"):
                description = line.replace("description:", "").strip().strip('"').strip("'")
            if line.startswith("alwaysApply:") and "true" in line.lower():
                always_apply = True

        body += GLOBAL_COMBINED

        is_global = always_apply or "gate" in skill_name or "enforcer" in skill_name
        globs_val = "*" if is_global else f"*{skill_name}*"
        mdc_content = f"---\ndescription: {description}\nglobs: {globs_val}\n---\n\n{body}"

        with open(os.path.join(CURSOR_RULES_DIR, f"{skill_name}.mdc"), "w", encoding="utf-8") as f:
            f.write(mdc_content)
        cursor_count += 1

        if any(k in skill_name for k in ("gate", "orchestrator", "workflow")):
            windsurf_content += f"### {skill_name}\n{description}\n{body}\n\n"

    with open(os.path.join(BASE_DIR, ".windsurfrules"), "w", encoding="utf-8") as f:
        f.write(windsurf_content)
    with open(os.path.join(BASE_DIR, ".clinerules"), "w", encoding="utf-8") as f:
        f.write("# Roo Code / Cline Global Rules\n\n" + windsurf_content.replace("## Windsurf Global Rules\n\n", ""))
    with open(os.path.join(BASE_DIR, "CONVENTIONS.md"), "w", encoding="utf-8") as f:
        f.write("# Aider / GitHub Copilot Conventions\n\n" + windsurf_content.replace("## Windsurf Global Rules\n\n", ""))

    print(f"   ✓ {cursor_count} Cursor rules compiled")
    return cursor_count


def sync_antigravity():
    """Sync src/skills/ → ~/.gemini/config/skills/ (Antigravity/Gemini CLI)."""
    gemini_skills_dir = os.path.expanduser("~/.gemini/config/skills")
    if not os.path.exists(os.path.expanduser("~/.gemini/config")):
        print("[3/3] Antigravity config not found — skipping.")
        return 0

    print("[3/3] Syncing to Antigravity (~/.gemini/config/skills/)...")
    if os.path.exists(gemini_skills_dir):
        shutil.rmtree(gemini_skills_dir)
    os.makedirs(gemini_skills_dir, exist_ok=True)

    count = 0
    for root, dirs, files in os.walk(SKILLS_DIR):
        if "SKILL.md" not in files:
            continue
        skill_name = os.path.basename(root)
        if skill_name == "_TEMPLATE":
            continue
        target_dir = os.path.join(gemini_skills_dir, skill_name)
        os.makedirs(target_dir, exist_ok=True)
        shutil.copy2(os.path.join(root, "SKILL.md"), os.path.join(target_dir, "SKILL.md"))
        count += 1

    print(f"   ✓ {count} skills synced to Antigravity")
    return count


def print_summary(cursor_count: int, antigravity_count: int):
    print(f"""
╔══════════════════════════════════════════════╗
║       Autonomous Agency Build Complete       ║
╠══════════════════════════════════════════════╣
║  Cursor (.mdc):          {cursor_count:>4} rules          ║
║  Windsurf (.windsurfrules): ✓               ║
║  Cline (.clinerules):       ✓               ║
║  Aider (CONVENTIONS.md):    ✓               ║
║  Antigravity:            {antigravity_count:>4} skills         ║
╠══════════════════════════════════════════════╣
║  Claude Code → claude-agency repo:          ║
║  github.com/GktuOktay/claude-agency         ║
╚══════════════════════════════════════════════╝
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Autonomous Agency — multi-IDE build tool")
    parser.add_argument("--cursor-only", action="store_true", help="Only build Cursor/Windsurf/Cline artifacts")
    parser.add_argument("--antigravity-only", action="store_true", help="Only sync to Antigravity")
    args = parser.parse_args()

    if args.antigravity_only:
        sync_antigravity()
    elif args.cursor_only:
        clean_old_artifacts()
        build_cursor_windsurf()
    else:
        clean_old_artifacts()
        cursor_count = build_cursor_windsurf()
        antigravity_count = sync_antigravity()
        print_summary(cursor_count, antigravity_count)
