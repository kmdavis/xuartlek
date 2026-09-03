---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mountaineer"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Mountaineer"
level: 5
source: "NPC Core"
aon_id: "creature-3473"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3473"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Mountaineer"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]], [[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/lore|Mountain Lore]] +15, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +12, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +12"
abilityMods: [4, 3, 2, 0, 3, 0]
abilities_top:
  - name: "Experienced Steps"
    desc: "A mountaineer isn't impeded by difficult terrain caused by snow or ice. They gain a +2 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Balance|Balance]] on slippery ice."
  - name: "Professional Climber"
    desc: "While climbing, the mountaineer can have up to five allies [[srd/pf2e/compendium/rules-elements/actions/player-core#Follow the Expert|Following the Expert]] and grants a +3 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Climb|Climb]]."
  - name: "Items"
    desc: "Chalk (10), extreme climbing kit, Compass, Hatchet (2), Hide Armor, Pick, Spyglass, Survey Map"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +14; __Ref__: +12; __Will__: +9"
hp: 80
health:
  - name: "HP"
    desc: "80"
abilities_mid:
  - name: "Lost My Footing"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The mountaineer critically fails a check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Balance|Balance]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Climb|Climb]]"
  - name: "Effect"
    desc: "Training kicks in, and the mountaineer catches themself, improving the check from a critical failure to a failure."
  - name: "Tuck and Roll"
    desc: "During an [[srd/pf2e/books/gm-core/chapter-2-building-games/environment#Avalanches|avalanche]], the mountaineer gains a +2 circumstance bonus to their Reflex save against bludgeoning damage and natural disasters."
speed: "25 feet; arctic passage"
attacks:
  - name: "Melee"
    desc: "⬻ pick +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d10]]) __Damage__ 1d6+10 piercing"
  - name: "Melee"
    desc: "⬻ hatchet +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d6+10 slashing"
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hatchet +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d6+10 slashing"
abilities_bot:
  - name: "Arctic Passage"
    desc: "The mountaineer ignores difficult terrain caused by ice or snow."
  - name: "Team Awareness"
    desc: "⬻"
  - name: "Requirements"
    desc: "A creature is [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] by one or more of the mountaineer's allies but is [[srd/pf2e/compendium/rules-elements/conditions#Observed|observed]] by the mountaineer"
  - name: "Effect"
    desc: "The mountaineer [[srd/pf2e/compendium/rules-elements/actions/player-core#Point Out|Points Out]] an enemy and makes a Strike against them."
  - name: "Chasm Crossing"
    desc: "⬺ The mountaineer Strides twice and [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]] up to 20 feet horizontally."
  - name: "Quick Draw"
    desc: "⬻ The mountaineer Interacts to draw their hatchet or pick, then Strikes with the weapon."
sourcebook: "_NPC Core_, page 55."
```

```encounter-table
name: Mountaineer
creatures:
  - 1: Mountaineer
```
