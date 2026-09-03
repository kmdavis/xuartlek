---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Quatoid"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/small
statblock: inline
name: "Quatoid"
level: 7
source: "Monster Core"
aon_id: "creature-2991"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2991"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Quatoid"
level: "Creature 7"
size: "Small"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Water"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +12, Elemental Lore +17, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +17, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +17, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13"
abilityMods: [4, 2, 0, 4, 3, 1]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +13; __Ref__: +15; __Will__: +18"
hp: 120
health:
  - name: "HP"
    desc: "120; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ bludgeoning 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 5"
abilities_mid:
  - name: "Calming Bioluminescence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 30 feet. The aura sheds dim light. Creatures in the emanation gain a +2 circumstance bonus to saving throws against [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]] effects. The quatoid can activate or deactivate this aura using a Sustain action."
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d12+6 bludgeoning plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d12+6 bludgeoning, DC 25"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 27, attack +17 - __2nd__ [[srd/pf2e/compendium/spells/rank-1/hydraulic-push|Hydraulic Push]] (at will)"
sourcebook: "_Monster Core_, page 148."
```

```encounter-table
name: Quatoid
creatures:
  - 1: Quatoid
```
