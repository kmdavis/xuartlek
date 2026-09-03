---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Heliocoprion"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Heliocoprion"
level: 10
source: "Howl of the Wild"
aon_id: "creature-3308"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3308"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Heliocoprion"
level: "Creature 10"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: "Uncommon"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; blood scent, scent (imprecise) 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +15"
abilityMods: [8, 3, 6, -4, 3, -1]
abilities_top:
  - name: "Blood Scent"
    desc: "The shark can smell blood in the water from up to 1 mile away."
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +22; __Ref__: +19; __Will__: +16"
hp: 230
health:
  - name: "HP"
    desc: "230"
speed: "swim 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+12 slashing plus 1d8 persistent bleed and Improved Grab"
abilities_bot:
  - name: "Deshell"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]])"
  - name: "Requirement"
    desc: "A creature is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] in the helicoprion's jaws"
  - name: "Effect"
    desc: "The shark rips into the creature dealing 3d10 slashing damage (DC 26 basic Reflex save)."
  - name: "Swallow Whole"
    desc: "⬻ Huge, 2d10+10 bludgeoning, Rupture 22"
sourcebook: "_Howl of the Wild_, page 179."
```

```encounter-table
name: Heliocoprion
creatures:
  - 1: Heliocoprion
```
