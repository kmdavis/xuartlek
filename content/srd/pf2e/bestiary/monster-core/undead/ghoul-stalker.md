---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ghoul Stalker"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/ghoul
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Ghoul Stalker"
level: 1
source: "Monster Core"
aon_id: "creature-3009"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3009"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ghoul Stalker"
level: "Creature 1"
size: "Medium"
trait_01: "Ghoul"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +5"
abilityMods: [1, 4, 1, 1, 2, 2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +4; __Ref__: +9; __Will__: +5"
hp: 16
health:
  - name: "HP"
    desc: "16 (void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]"
abilities_mid:
  - name: "Stench"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|olfactory]]) 10 feet, DC 14"
speed: "25 feet, burrow 5 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d8+1 piercing"
  - name: "Melee"
    desc: "⬻ claw +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+1 slashing plus Grab"
abilities_bot:
  - name: "Consume Flesh"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) 1d6 HP"
  - name: "Ghoul Whispers"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) DC 17"
  - name: "Grave Knowledge"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) +7 skill modifier"
  - name: "Swift Leap"
    desc: "⬻ (move)"
sourcebook: "_Monster Core_, page 163."
```

```encounter-table
name: Ghoul Stalker
creatures:
  - 1: Ghoul Stalker
```
