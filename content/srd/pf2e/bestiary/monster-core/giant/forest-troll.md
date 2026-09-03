---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Forest Troll"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troll
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/large
statblock: inline
name: "Forest Troll"
level: 5
source: "Monster Core"
aon_id: "creature-3219"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3219"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Forest Troll"
level: "Creature 5"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Troll"
trait_04: "Wood"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +12"
abilityMods: [5, 2, 6, -2, 0, -2]
abilities_top:
  - name: "Easily Misled"
    desc: "The forest troll gets a –4 circumstance penalty to their Perception DC against [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +17; __Ref__: +11; __Will__: +7"
hp: 125
health:
  - name: "HP"
    desc: "125 , regeneration 20 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]); __Weaknesses__ electricity 10, fire 10"
abilities_mid:
  - name: "Furious Flailing"
    desc: "⬲"
  - name: "Trigger"
    desc: "The forest troll takes electricity or fire damage"
  - name: "Effect"
    desc: "The troll makes a claw Strike against a random creature within its reach. If the troll has persistent fire damage, they attempt a DC 15 flat check to remove it."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+5 piercing"
  - name: "Melee"
    desc: "⬻ claw +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+5 slashing"
abilities_bot:
  - name: "Chase Prey"
    desc: "⬺ The forest troll rushes forward on all fours, Striding and then making two claw Strikes."
  - name: "Rend"
    desc: "⬻ claw"
sourcebook: "_Monster Core_, page 330."
```

```encounter-table
name: Forest Troll
creatures:
  - 1: Forest Troll
```
