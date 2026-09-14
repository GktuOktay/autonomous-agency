---
name: plan-mode
description: "3+ dosya veya mimari değişiklik içeren görevlerde önce plan üretir, onay alır, sonra kod yazar. Büyük görevlerde otomatik tetiklenir."
alwaysApply: false
---

<role>Plan Mode Activator</role>
<trigger>WHEN task involves ANY of: 3+ files changed, new service/module/layer added, DB schema change, breaking API change, security-sensitive refactor</trigger>

<rules>
- ENTER plan mode before writing any code
- PRODUCE a plan containing:
  1. Etkilenen dosyalar (tam path listesi)
  2. Değişiklik özeti (her dosya için 1 satır)
  3. Risk: hangi mevcut davranış değişecek
  4. Test stratejisi: hangi test'ler eklenmeli/güncellenmeli
- WAIT for explicit user approval ("devam", "ok", "evet")
- EXIT plan mode only after approval — then implement
- If user rejects plan: revise, do NOT implement rejected version
- NEVER skip plan mode by claiming task is "simple" — trigger conditions are objective
</rules>

<plan-template>
## Plan: {görev adı}

### Etkilenecek Dosyalar
| Dosya | Değişiklik |
|---|---|
| `path/to/file.cs` | Açıklama |

### Risk
- [ ] Breaking change var mı?
- [ ] Mevcut test'ler etkileniyor mu?
- [ ] DB migration gerekiyor mu?

### Test Stratejisi
- Unit: ...
- Integration: ...
- Manuel doğrulama: ...

**Onaylıyor musun?**
</plan-template>
