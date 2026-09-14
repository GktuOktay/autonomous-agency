# Autonomous Agency

[🇹🇷 Türkçe](README.tr.md)

Multi-IDE enterprise-grade multi-agent skill sistemi.
Single Source of Truth: `src/skills/` → Cursor, Windsurf, Roo Code, Aider/Copilot, Antigravity.

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
├── src/skills/              # Single Source of Truth — tüm skill'ler buradan derlenir
│   ├── 01_orchestrators/    # Orkestratörler
│   ├── 02_specialists/      # Domain uzmanları
│   ├── 03_quality_gates/    # Kalite kapıları
│   ├── 04_meta/             # Meta skill'ler
│   └── _TEMPLATE/           # Yeni skill şablonu
├── .agents/skills/          # Antigravity / agent-runner formatı
├── rules/                   # Cursor .mdc çıktısı (build sonrası oluşur)
├── docs/
│   ├── en/                  # İngilizce dokümantasyon
│   └── tr/                  # Türkçe dokümantasyon
└── setup.py                 # Build scripti
```

---

## Skill Şablonu

Yeni skill için `src/skills/_TEMPLATE/SKILL.md`'yi kopyala:

```bash
cp -r src/skills/_TEMPLATE src/skills/04_meta/yeni-skill
# SKILL.md'yi düzenle
python setup.py
```

---

## Dokümantasyon

| Döküman | İçerik |
|---|---|
| [Architecture](docs/en/core/ARCHITECTURE.md) | Sistem mimarisi |
| [Hierarchy Protocol](docs/en/core/HIERARCHY_PROTOCOL.md) | Agent hiyerarşisi |
| [Skills Catalog](docs/en/catalogs/SKILLS_CATALOG.md) | Tüm skill listesi |
| [Installation](docs/en/core/INSTALLATION.md) | Kurulum detayları |
| [Principles](docs/en/core/PRINCIPLES.md) | Mühendislik prensipleri |

---

## Fark: autonomous-agency vs claude-agency

| | `autonomous-agency` | `claude-agency` |
|---|---|---|
| **Hedef** | Cursor, Windsurf, Cline, Aider | Yalnızca Claude Code |
| **Build** | `setup.py` compile pipeline | Direkt, compile yok |
| **Subagent** | Yok | 5 native agent |
| **Hooks** | Yok | 4 tool-call hook |
| **MCP** | Yok | 4 server |
| **CLAUDE.md** | Yok | Var (4KB) |
