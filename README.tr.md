# Autonomous Agency

[🇺🇸 English](README.md)

Multi-IDE enterprise-grade multi-agent skill sistemi.
Tek kaynak: `src/skills/` → Cursor, Windsurf, Roo Code, Aider/Copilot, Antigravity.

> **Claude Code kullanıyorsan:** → [claude-agency](https://github.com/GktuOktay/claude-agency)
> Native subagent, hooks ve MCP entegrasyonu olan Claude Code'a özel repo.

---

## Desteklenen IDE'ler

| IDE | Format | Çıktı |
|---|---|---|
| Cursor | `.mdc` | `rules/*.mdc` |
| Windsurf | `.windsurfrules` | `.windsurfrules` |
| Roo Code / Cline | `.clinerules` | `.clinerules` |
| Aider / GitHub Copilot | `CONVENTIONS.md` | `CONVENTIONS.md` |
| Antigravity (Gemini CLI) | flat skills | `~/.gemini/config/skills/` |

---

## Kurulum

```bash
git clone https://github.com/GktuOktay/autonomous-agency.git
cd autonomous-agency
python setup.py
```

Sadece Cursor/Windsurf için:
```bash
python setup.py --cursor-only
```

Sadece Antigravity için:
```bash
python setup.py --antigravity-only
```

---

## Yapı

```
autonomous-agency/
├── src/skills/              # Tek kaynak — tüm skill'ler buradan derlenir
│   ├── 01_orchestrators/
│   ├── 02_specialists/
│   ├── 03_quality_gates/
│   ├── 04_meta/
│   └── _TEMPLATE/
├── .agents/skills/          # Antigravity / agent-runner formatı
├── rules/                   # Cursor .mdc çıktısı (build sonrası oluşur)
├── docs/en/                 # İngilizce dokümantasyon
├── docs/tr/                 # Türkçe dokümantasyon
└── setup.py                 # Build scripti
```

---

## Yeni Skill Ekle

```bash
cp -r src/skills/_TEMPLATE src/skills/02_specialists/yeni-skill
# SKILL.md düzenle
python setup.py
```

---

## Fark: autonomous-agency vs claude-agency

| | `autonomous-agency` | `claude-agency` |
|---|---|---|
| **Hedef** | Cursor, Windsurf, Cline, Aider | Yalnızca Claude Code |
| **Build** | `setup.py` compile pipeline | Direkt, compile yok |
| **Subagent** | Yok | 5 native agent |
| **Hooks** | Yok | 4 tool-call hook |
| **MCP** | Yok | 4 server |
