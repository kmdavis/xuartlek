---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Olobigonde"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/large
statblock: inline
name: "Olobigonde"
level: 2
source: "Rage of Elements"
aon_id: "creature-2664"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2664"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Olobigonde"
level: "Creature 2"
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: "Elemental"
trait_04: "Water"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +7"
abilityMods: [3, 1, 4, -4, 1, -5]
abilities_top:
  - name: "Camouflage"
    desc: "An olobigonde can Hide in aquatic environments even if it doesn't have cover. However, there must be plants, debris, a seabed, or other objects for it to camouflage itself, not just open water."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +10; __Ref__: +7; __Will__: +5"
hp: 38
health:
  - name: "HP"
    desc: "38"
abilities_mid:
  - name: "Ambush"
    desc: "⬲"
  - name: "Trigger"
    desc: "A target creature passes within 20 feet of the olobigonde's hiding place and has not detected the olobigonde"
  - name: "Effect"
    desc: "The olobigonde lunges out of its hiding place, Swims directly toward the triggering creature, and makes a jaws Strike against it. The target creature is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to this attack."
  - name: "Reactive Grab"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within the olobigonde's reach leaves a square during a [[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]] action it's using"
  - name: "Requirements"
    desc: "The olobigonde doesn't have a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The olobigonde attempts to Grapple the triggering creature with its jaws. On a success, the target also takes 3 piercing damage (doubled on a critical success)."
speed: "5 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 __Damage__ 1d8+3 piercing plus decomposing toxin"
abilities_bot:
  - name: "Decomposing Toxin"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) A living creature struck by an olobigonde's jaws Strike must succeed at a DC 15 Fortitude save or become enfeebled 1 and take 1d6 persistent poison damage (or enfeebled 2 with 2d6 persistent poison damage on a critical failure). The enfeebled condition ends when the persistent damage does. A creature currently affected by decomposing toxin doesn't need to save again. Olobigonde Toxin Alchemists who travel the planes have discovered how readily an olobigonde's toxin can decompose flesh, and some have discovered ways to incorporate it into their creations. An olobigonde's corpse yields approximately 1 gp worth of raw materials when harvested with a successful DC 16 [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] or [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] check (2 gp worth on a critical success). This material can be used only to craft alchemical bombs with the [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] trait."
sourcebook: "_Rage of Elements_, page 184."
```

```encounter-table
name: Olobigonde
creatures:
  - 1: Olobigonde
```
