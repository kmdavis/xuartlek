---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tomb Raider"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Tomb Raider"
level: 5
source: "NPC Core"
aon_id: "creature-3474"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3474"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tomb Raider"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/lore|Architecture Lore]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/lore|Engineering Lore]] +11, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +13"
abilityMods: [3, 4, 1, 2, 2, 0]
abilities_top:
  - name: "Hazard Spotter"
    desc: "Even if the tomb raider isn't [[srd/pf2e/compendium/rules-elements/actions/player-core#Search|Searching]], they get a check to find traps that normally require them to be Searching."
  - name: "Items"
    desc: "Climbing Kit, Hand Crossbow (20 bolts), Kukri"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +10; __Ref__: +15; __Will__: +11"
hp: 75
health:
  - name: "HP"
    desc: "75"
speed: "25 feet, climb 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ kukri +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d6+9 slashing"
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+9 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +15 (range increment 60 feet, reload 1) __Damage__ 1d6+6 piercing"
abilities_bot:
  - name: "Trick Attack"
    desc: "⬻ The tomb raider chooses one of their weapons. The next attack with that weapon this turn deals an additional 2d6 precision damage. In addition, the tomb raider can Interact to draw or reload the weapon."
sourcebook: "_NPC Core_, page 56."
```

```encounter-table
name: Tomb Raider
creatures:
  - 1: Tomb Raider
```
