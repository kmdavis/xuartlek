---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sporeback Frog"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Sporeback Frog"
level: 5
source: "Howl of the Wild"
aon_id: "creature-3280"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3280"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Sporeback Frog"
level: "Creature 5"
size: "Large"
trait_01: "Animal"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13"
abilityMods: [4, 3, 5, -4, 2, 1]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +15; __Ref__: +12; __Will__: +9"
hp: 94
health:
  - name: "HP"
    desc: "94; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 8; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 4"
speed: "25 feet, burrow 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +13 __Damage__ 2d8+6 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ tongue +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ seed spores"
abilities_bot:
  - name: "Seed Spores"
    desc: "A creature hit by the sporeback frog's tongue Strike takes 1d6 persistent poison damage as fungal spores begin to grow."
  - name: "Soporific Spores"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) The sporeback frog shakes the plants and fungi on its back until they emit a cloud of spores in a 20-foot emanation. All creatures in the area must succeed a DC 22 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 2]] and [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 2]] for 1 minute (clumsy 3 and stupefied 3 on a critical failure). This ability can't be used again for 1d4 rounds."
sourcebook: "_Howl of the Wild_, page 151."
```

```encounter-table
name: Sporeback Frog
creatures:
  - 1: Sporeback Frog
```
