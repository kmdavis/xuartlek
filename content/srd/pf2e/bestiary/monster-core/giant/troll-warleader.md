---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Troll Warleader"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troll
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/large
statblock: inline
name: "Troll Warleader"
level: 10
source: "Monster Core"
aon_id: "creature-3220"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3220"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Troll Warleader"
level: "Creature 10"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Troll"
trait_04: "Wood"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +21, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +15, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +22, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +17, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +17"
abilityMods: [7, 3, 7, -1, 1, 4]
abilities_top:
  - name: "Easily Misled"
    desc: "The troll warleader gets a –4 circumstance penalty to their Perception DC against [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/axe/battle-axe|battle axe]]_ (2), Half Plate"
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +23; __Ref__: +17; __Will__: +15"
hp: 240
health:
  - name: "HP"
    desc: "240 , regeneration 20 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]); __Weaknesses__ electricity 10, fire 10"
abilities_mid:
  - name: "Furious Roar"
    desc: "⬲"
  - name: "Trigger"
    desc: "The troll warleader takes electricity or fire damage"
  - name: "Effect"
    desc: "The warleader uses their Primordial Roar and, if they're aware of the damage's source, can Stride toward it. If the warleader has persistent fire damage, they attempt a DC 15 flat check to remove it."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d12+13 piercing"
  - name: "Melee"
    desc: "⬻ battle axe +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 2d8+13 slashing"
  - name: "Melee"
    desc: "⬻ claw +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+13 slashing"
abilities_bot:
  - name: "Primordial Roar"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The troll warleader unleashes a bestial roar. Each non-troll creature in a 100-foot emanation must attempt a DC 29 Will save. The creature is then temporarily immune for 10 minutes."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 1]]."
  - name: "Failure"
    desc: "The creature is frightened 2."
  - name: "Critical Failure"
    desc: "The creature is frightened 3."
  - name: "Shed Armor"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The warleader cuts their armor loose from their flesh. They immediately heal 60 Hit Points in a surge of regeneration as they grow twisted limbs and malformed faces. Without their armor, the warleader's AC drops to 26 but they gain all-around vision from the new faces. Putting the armor back on takes 10 minutes, and this ability can't be used again until 1 hour has passed."
  - name: "Sweeping Axes"
    desc: "⬽"
  - name: "Requirements"
    desc: "The troll warleader is wielding two battle axes"
  - name: "Effect"
    desc: "The warleader makes a battle axe Strike against each creature in their reach and the bonus from [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|sweep]] applies to each attack. These attacks count against their multiple attack penalty, but the multiple attack penalty doesn't increase until after all the attacks."
sourcebook: "_Monster Core_, page 331."
```

```encounter-table
name: Troll Warleader
creatures:
  - 1: Troll Warleader
```
