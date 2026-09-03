---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Xulgath Leader"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/xulgath
  - pf2e/creature/trait/medium
statblock: inline
name: "Xulgath Leader"
level: 3
source: "Monster Core"
aon_id: "creature-3246"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3246"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Xulgath Leader"
level: "Creature 3"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Xulgath"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [4, 1, 2, -1, 2, 1]
abilities_top:
  - name: "Items"
    desc: "Breastplate, Greataxe, Javelin (4)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +6; __Will__: +9"
hp: 44
health:
  - name: "HP"
    desc: "44"
abilities_mid:
  - name: "Stench"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|olfactory]]) 30 feet, DC 19"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greataxe +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d10+6 slashing"
  - name: "Melee"
    desc: "⬻ jaws +11 __Damage__ 1d6+6 piercing plus weakening strike"
  - name: "Melee"
    desc: "⬻ claw +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d4+6 slashing plus weakening strike"
  - name: "Ranged"
    desc: "⬻ javelin +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 30 feet]]) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Weakening Strike"
    desc: "A creature hit by a xulgath leader's jaws or claw Strike is [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (or enfeebled 2 on a critical hit) for 1 round."
sourcebook: "_Monster Core_, page 353."
```

```encounter-table
name: Xulgath Leader
creatures:
  - 1: Xulgath Leader
```
