---
obsidianUIMode: preview
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
aon_id: "creature-3153"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3153"
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
    desc: "Perception +17; low-light vision"
languages: "Common, Elven, Fey, Gnomish"
skills:
  - name: "Skills"
    desc: "Crafting +15, Deception +14, Medicine +15, Nature +17, Stealth +17, Thievery +15"
abilityMods: [4, 6, 3, 4, 6, 3]
abilities_top:
  - name: "Items"
    desc: "_+1 hatchet_, Shortbow"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +12; __Ref__: +15; __Will__: +17"
hp: 100
health:
  - name: "HP"
    desc: "100; __Resistances__ poison 5; __Weaknesses__ cold iron 10"
abilities_mid:
  - name: "Defensive Quills"
    desc: "A creature that hits a pukwudgie with an unarmed Strike or a non-reach melee Strike takes 3d8 piercing damage (basic Reflex save). On a critical failure, the creature also takes 1d6 persistent poison damage from the poisoned quills."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _hatchet_ +17 (Agile, Magical, Sweep) __Damage__ 1d6+10 slashing plus pukwudgie poison"
  - name: "Ranged"
    desc: "⬻ _hatchet_ +19 (Magical, thrown 10 feet) __Damage__ 1d6+10 slashing plus pukwudgie poison"
  - name: "Ranged"
    desc: "⬻ shortbow +18 (deadly d10, range increment 60 feet) __Damage__ 1d6+6 piercing plus pukwudgie poison"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Polymorph, Primal) The pukwudgie takes on the physical form of a giant porcupine or resumes their natural form. In porcupine form, their size changes to Medium, they lose their weapon Strikes, and they gain a quill Strike (+18 for 2d8+6 piercing plus 1d8 persistent poison)."
  - name: "Pukwudgie Poison"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and stupefied 1 (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage and stupefied 2 (1 round)"
  - name: "Stage 3"
    desc: "1d6 poison damage, confused, and stupefied 2 (1 round). Trepidatious Trade Pukwudgies rely heavily on their knowledge of local plants, which they use for food, medicine, magical weapons, and their signature poison. If shown proper respect, pukwudgies trade their crafts for items they deem valuable. They have little use for coin but accept unique foods, items of beauty, and even interesting stories as payment. The slightest transgression, however, can quickly turn pukwudgie encounters hostile."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 25, attack +17 - __2nd__ Invisibility (at will; self only) - __3rd__ Wall of Thorns - __4th__ Mirage, Unfettered Movement"
sourcebook: "_Monster Core_, page 279."
```

```encounter-table
name: Pukwudgie
creatures:
  - 1: Pukwudgie
```
