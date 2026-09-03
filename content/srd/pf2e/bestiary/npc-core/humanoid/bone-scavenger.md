---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bone Scavenger"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kholo
  - pf2e/creature/trait/small
  - pf2e/creature/trait/gnoll
statblock: inline
name: "Bone Scavenger"
level: 0
source: "NPC Core"
aon_id: "creature-3651"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3651"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Bone Scavenger"
level: "Creature 0"
size: "Small"
trait_01: "Humanoid"
trait_02: "Kholo"
trait_03: "Gnoll"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Kholo|Kholo]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +2, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +4"
abilityMods: [2, 3, 1, -1, 1, 0]
abilities_top:
  - name: "Items"
    desc: "Dagger (2)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +3; __Ref__: +6; __Will__: +3"
hp: 16
health:
  - name: "HP"
    desc: "16"
abilities_mid:
  - name: "Bone Armor"
    desc: "⬲"
  - name: "Trigger"
    desc: "The bone scavenger takes bludgeoning damage"
  - name: "Effect"
    desc: "The bone scavenger angles their makeshift armor to absorb some of the blow, causing shards of bone to splinter outward. All adjacent creatures take 2d4 piercing damage (DC 16 basic Reflex save)."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+2 piercing"
  - name: "Melee"
    desc: "⬻ jaws +5 __Damage__ 1d6+2 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+2 piercing"
abilities_bot:
  - name: "Rugged Travel"
    desc: "A kholo ignores the first square of difficult terrain they move into each time they Step or Stride. Ant Kholos The bone scavenger belongs to the ant kholo heritage, smaller and with larger ears than other kholos. You can change this NPC to a different kholo heritage by making it Medium, and you can conversely change a different kholo NPC to an ant kholo by making their size Small."
sourcebook: "_NPC Core_, page 196."
```

```encounter-table
name: Bone Scavenger
creatures:
  - 1: Bone Scavenger
```
