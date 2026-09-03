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
languages: "D'ziriak, [[srd/pf2e/compendium/rules-elements/languages#Shadowtongue|Shadowtongue]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +8"
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
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]]) 20 feet. The colorful runes that decorate a d'ziriak's body create [[srd/pf2e/books/player-core/chapter-8-playing-the-game/perception-and-detection#Dim Light|dim light]]. The natural bioluminescence is specially adapted to [[srd/pf2e/compendium/gm/planes#The Netherworld|the Netherworld]], able to overcome magical darkness as if it were magical light with a rank equal to half the d'ziriak's level rounded up."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 1d10+4 piercing"
abilities_bot:
  - name: "Dazzling Burst"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/light|Light]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]]) The d'ziriak causes their body to flare with intense colorful light. Non-d'ziriaks in a 20-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] must attempt a DC 20 Fortitude save. After using this ability during this time they can't use Dazzling Burst again. A creature that attempts this save is immune to all Dazzling Bursts for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] for 1 round."
  - name: "Failure"
    desc: "The creature is dazzled for 1 minute."
  - name: "Critical Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] for 1 round and dazzled for 1 minute."
  - name: "Double Claw"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The d'ziriak makes two claw Strikes. If both hit the same creature, combine their damage for the purpose of resistances and weaknesses. This counts as two attacks for the d'ziriak's multiple attack penalty, and the penalty doesn't increase until after both attacks. Light Weavers The masters of d'ziriak light-weaving craft are occult practitioners, almost always [[srd/pf2e/compendium/character/classes/sorcerer|sorcerers]] of the aberrant bloodline. Light weavers prefer spells that provide light or create magical writing. In their hive cities, light weavers create art, lighting, signage, and magic wards. They also use their light weaving for entertainment and education."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 19 - __7th__ [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] (self only; to [[srd/pf2e/compendium/gm/planes#The Netherworld|Netherworld]] only)"
sourcebook: "_Monster Core 2_, page 142."
```

```encounter-table
name: D'ziriak
creatures:
  - 1: D'ziriak
```
