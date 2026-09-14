---
name: skill-name
description: "Bir cümle açıklama — Claude'un bu skill'i ne zaman tetikleyeceğini belirler. Spesifik ve eylem odaklı yaz."
alwaysApply: false
---

<role>Role Name</role>
<trigger>WHEN [objective, measurable condition — avoid vague terms like "needed" or "appropriate"]</trigger>

<rules>
- RULE 1: Zorunlu davranış (FORCE / REQUIRE / REJECT formatı)
- RULE 2: Yasak davranış
- RULE 3: Çıktı formatı veya kalite standardı
</rules>

<!--
SKILL YAZMA KURALLARI (bu yorum bloğunu sil):

1. name       → kebab-case, dizin adıyla birebir eşleşmeli
2. description → tek cümle, trigger için yeterli bağlam içermeli
3. alwaysApply → true: her zaman aktif (gate'ler için), false: talep üzerine
4. trigger     → ölçülebilir koşul — "WHEN adding DB entity", "WHEN writing unit test"
5. rules       → FORCE / REQUIRE / REJECT / WARN prefix'i kullan
6. Kategori rehberi:
     01_orchestrators/  → birden fazla skill'i koordine eden orkestratörler
     02_specialists/    → domain uzmanları (backend, security, devops…)
     03_gates/          → kalite kapıları, alwaysApply: true
     04_meta/           → Claude Code davranışını etkileyen meta skill'ler
-->
