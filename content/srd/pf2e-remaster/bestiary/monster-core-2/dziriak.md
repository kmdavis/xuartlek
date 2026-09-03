---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "D'ziriak"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/medium
statblock: inline
name: "D'ziriak"
level: 3
source: "Monster Core 2"
aon_id: "creature-4376"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4376"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "D'ziriak"
level: "Creature 3"
size: "Medium"
trait_01: "Aberration"
trait_02: "Shadow"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "D'ziriak, Shadowtongue; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Arcana +8, Athletics +6, Occultism +10, Stealth +10, Survival +8"
abilityMods: [1, 3, 1, 1, 3, 4]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +12; __Will__: +10"
hp: 45
health:
  - name: "HP"
    desc: "45"
abilities_mid:
  - name: "Glow"
    desc: "(aura, light) 20 feet. The colorful runes that decorate a d'ziriak's body create dim light. The natural bioluminescence is specially adapted to the Netherworld, able to overcome magical darkness as if it were magical light with a rank equal to half the d'ziriak's level rounded up."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +12 (Agile, finesse) __Damage__ 1d10+4 piercing"
abilities_bot:
  - name: "Dazzling Burst"
    desc: "⬺ (Light, Visual) The d'ziriak causes their body to flare with intense colorful light. Non-d'ziriaks in a 20-foot emanation must attempt a DC 20 Fortitude save. After using this ability during this time they can't use Dazzling Burst again. A creature that attempts this save is immune to all Dazzling Bursts for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is dazzled for 1 round."
  - name: "Failure"
    desc: "The creature is dazzled for 1 minute."
  - name: "Critical Failure"
    desc: "The creature is blinded for 1 round and dazzled for 1 minute."
  - name: "Double Claw"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The d'ziriak makes two claw Strikes. If both hit the same creature, combine their damage for the purpose of resistances and weaknesses. This counts as two attacks for the d'ziriak's multiple attack penalty, and the penalty doesn't increase until after both attacks. Light Weavers The masters of d'ziriak light-weaving craft are occult practitioners, almost always sorcerers of the aberrant bloodline. Light weavers prefer spells that provide light or create magical writing. In their hive cities, light weavers create art, lighting, signage, and magic wards. They also use their light weaving for entertainment and education."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 19 - __7th__ Interplanar Teleport (self only; to Netherworld only)"
sourcebook: "_Monster Core 2_, page 142."
```

```encounter-table
name: D'ziriak
creatures:
  - 1: D'ziriak
```
