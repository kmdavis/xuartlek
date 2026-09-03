---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ghoul Soldier"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/ghoul
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Ghoul Soldier"
level: 2
source: "Monster Core"
aon_id: "creature-3010"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3010"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ghoul Soldier"
level: "Creature 2"
size: "Medium"
trait_01: "Ghoul"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +6"
abilityMods: [3, 2, 2, 1, 2, 3]
abilities_top:
  - name: "Items"
    desc: "Bastard Sword, Breastplate"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +8; __Ref__: +8; __Will__: +6"
hp: 28
health:
  - name: "HP"
    desc: "28 (void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Stench"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|olfactory]]) 10 feet, DC 15"
speed: "25 feet, burrow 5 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 __Damage__ 1d10+3 piercing"
  - name: "Melee"
    desc: "⬻ bastard sword +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d12]]) __Damage__ 1d8+3 slashing"
  - name: "Melee"
    desc: "⬻ claw +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d8+3 slashing plus Grab"
abilities_bot:
  - name: "Consume Flesh"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) 2d6 HP"
  - name: "Ghoul Whispers"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) DC 18"
  - name: "Grave Knowledge"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) +8 skill modifier"
  - name: "Swift Leap"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]])"
sourcebook: "_Monster Core_, page 163."
```

```encounter-table
name: Ghoul Soldier
creatures:
  - 1: Ghoul Soldier
```
