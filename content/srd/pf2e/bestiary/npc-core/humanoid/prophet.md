---
noteType: pf2eMonster
aliases: "Prophet"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Prophet"
level: 2
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3442"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Prophet"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "+10"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +8, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +7, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +7"
abilityMods: [2, 1, 0, 1, 3, 4]
abilities_top:
  - name: "Items"
    desc: "Flail, manifesto (functions as a [[srd/pf2e/compendium/equipment/adventuring-gear/Religious Text|religious text]]), pouch of rocks, robes"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +8; __Ref__: +7; __Will__: +11"
hp: 25
health:
  - name: "HP"
    desc: "25"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ flail +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|Trip]]) __Damage__ 1d6+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ rock +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]]) __Damage__ 1d4+2 bludgeoning"
abilities_bot:
  - name: "Cleric Domain Spells"
    desc: "DC 18, 1 Focus Point - __1st__ [[srd/pf2e/compendium/spells/focus/Read Fate|Read Fate]]"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 18, attack +10 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/Know the Way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Bless|Bless]], [[srd/pf2e/compendium/spells/rank-1/Enfeeble|Enfeeble]], [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]], [[srd/pf2e/compendium/spells/rank-1/Sanctuary|Sanctuary]] (4 slots)"
sourcebook: "_NPC Core_, page 30."
```

```encounter-table
name: Prophet
creatures:
  - 1: Prophet
```
