---
noteType: pf2eMonster
aliases: "Bandit"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Bandit"
level: 2
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3425"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Bandit"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "+6"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +5, [[srd/pf2e/compendium/rules-elements/skills/Lore|Forest Lore]] +4, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +6, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +6, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +8"
abilityMods: [3, 3, 1, 0, 2, 1]
abilities_top:
  - name: "Bandit's Ambush"
    desc: "When the bandit rolls initiative using [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] or [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]], they can attempt to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] one creature as a free action."
  - name: "Items"
    desc: "Dagger, Machete, Sling (10 bullets), studded leather"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +7; __Ref__: +9; __Will__: +6"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet; forest passage"
attacks:
  - name: "Melee"
    desc: "⬻ machete +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]]) __Damage__ 1d6+5 slashing"
  - name: "Melee"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+5 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ sling +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], range increment 50 feet, reload 1) __Damage__ 1d6+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+5 piercing"
abilities_bot:
  - name: "Dread Striker"
    desc: "[[srd/pf2e/compendium/rules-elements/Conditions#Frightened|Frightened]] creatures are [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] to the bandit."
  - name: "Forest Passage"
    desc: "The bandit ignores any difficult terrain caused by plants, such as bushes, vines, and undergrowth."
sourcebook: "_NPC Core_, page 18."
```

```encounter-table
name: Bandit
creatures:
  - 1: Bandit
```
