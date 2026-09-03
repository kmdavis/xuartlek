---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Earthen Destrier"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/large
statblock: inline
name: "Earthen Destrier"
level: 4
source: "Monster Core 2"
aon_id: "creature-4383"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4383"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Earthen Destrier"
level: "Creature 4"
size: "Large"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision, tremorsense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12"
abilityMods: [4, 1, 4, -1, 3, 0]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +14; __Ref__: +9; __Will__: +10"
hp: 75
health:
  - name: "HP"
    desc: "75; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
speed: "50 feet, burrow 30 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ lance arm +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+6 piercing and lancing charge"
  - name: "Melee"
    desc: "⬻ hoof +14 __Damage__ 2d6+6 bludgeoning"
abilities_bot:
  - name: "Earth Glide"
    desc: "A earthen destrier can [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrow]] through earthen matter, including rock. When it does so, it moves at its full burrow Speed, leaving no tunnels or signs of its passing."
  - name: "Lancing Charge"
    desc: "If the destrier moved at least 10 feet directly before its lance arm Strike, it gains a +2 circumstance bonus to its damage roll."
  - name: "Tilting Strike"
    desc: "⬲"
  - name: "Trigger"
    desc: "The earthen destrier tramples a creature"
  - name: "Effect"
    desc: "The earthen destrier makes a lance arm Strike against the creature it's Trampling with a –5 circumstance penalty."
  - name: "Trample"
    desc: "⬽ Medium or smaller, hoof, DC 20"
sourcebook: "_Monster Core 2_, page 146."
```

```encounter-table
name: Earthen Destrier
creatures:
  - 1: Earthen Destrier
```
