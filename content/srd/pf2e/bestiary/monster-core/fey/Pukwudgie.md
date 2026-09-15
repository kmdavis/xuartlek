---
noteType: pf2eMonster
aliases: "Pukwudgie"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/small
statblock: inline
name: "Pukwudgie"
level: 7
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3153"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Pukwudgie"
level: "Creature 7"
size: "Small"
trait_01: "Fey"
modifier: 17
perception:
  - name: "Perception"
    desc: "+17; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/Languages#Gnomish|Gnomish]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +15, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +14, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +15, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +17, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +15"
abilityMods: [4, 6, 3, 4, 6, 3]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/weapons/axe/Hatchet|hatchet]]_, Shortbow"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +12; __Ref__: +15; __Will__: +17"
hp: 100
health:
  - name: "HP"
    desc: "100; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 5; __Weaknesses__ cold iron 10"
abilities_mid:
  - name: "Defensive Quills"
    desc: "A creature that hits a pukwudgie with an [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|unarmed]] Strike or a non-[[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach]] melee Strike takes 3d8 piercing damage (basic Reflex save). On a critical failure, the creature also takes 1d6 persistent poison damage from the poisoned quills."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _hatchet_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]]) __Damage__ 1d6+10 slashing plus pukwudgie poison"
  - name: "Ranged"
    desc: "⬻ _hatchet_ +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]]) __Damage__ 1d6+10 slashing plus pukwudgie poison"
  - name: "Ranged"
    desc: "⬻ shortbow +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], range increment 60 feet) __Damage__ 1d6+6 piercing plus pukwudgie poison"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]]) The pukwudgie takes on the physical form of a giant porcupine or resumes their natural form. In porcupine form, their size changes to Medium, they lose their weapon Strikes, and they gain a quill Strike (+18 for 2d8+6 piercing plus 1d8 persistent poison)."
  - name: "Pukwudgie Poison"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 1]] (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage and stupefied 2 (1 round)"
  - name: "Stage 3"
    desc: "1d6 poison damage, [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]], and stupefied 2 (1 round). Trepidatious Trade Pukwudgies rely heavily on their knowledge of local plants, which they use for food, medicine, magical weapons, and their signature poison. If shown proper respect, pukwudgies trade their crafts for items they deem valuable. They have little use for coin but accept unique foods, items of beauty, and even interesting stories as payment. The slightest transgression, however, can quickly turn pukwudgie encounters hostile."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 25, attack +17 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (at will; self only) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Wall of Thorns|Wall of Thorns]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Mirage|Mirage]], [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]]"
sourcebook: "_Monster Core_, page 279."
```

```encounter-table
name: Pukwudgie
creatures:
  - 1: Pukwudgie
```
