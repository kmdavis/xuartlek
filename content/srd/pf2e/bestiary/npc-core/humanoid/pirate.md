---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pirate"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Pirate"
level: 2
source: "NPC Core"
aon_id: "creature-3599"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3599"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Pirate"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +6, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +6, [[srd/pf2e/compendium/rules-elements/skills/lore|Sailing Lore]] +8"
abilityMods: [2, 3, 1, 0, 2, 2]
abilities_top:
  - name: "Items"
    desc: "cutlass (functions as a [[srd/pf2e/compendium/equipment/weapons/sword/scimitar|scimitar]]), Dagger, Padded Armor"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +8; __Will__: +6"
hp: 32
health:
  - name: "HP"
    desc: "32"
abilities_mid:
  - name: "Bravery"
    desc: "When the pirate rolls a success on a Will save against a [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]] effect, they get a critical success instead. In addition, anytime they gain the [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] condition, reduce its value by 1."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ cutlass +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d6+5 slashing"
  - name: "Melee"
    desc: "⬻ dagger +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+5 piercing"
  - name: "Melee"
    desc: "⬻ fist +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+5 piercing"
abilities_bot:
  - name: "Boarding Action"
    desc: "⬺ The pirate swings on a rope or Strides, moving up to double their Speed. If the pirate boarded or disembarked a boat during this movement, they can make a melee Strike at the end of their movement that deals one extra damage die on a hit."
sourcebook: "_NPC Core_, page 147."
```

```encounter-table
name: Pirate
creatures:
  - 1: Pirate
```
