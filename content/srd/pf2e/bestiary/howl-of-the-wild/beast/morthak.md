---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Morthak"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/medium
statblock: inline
name: "Morthak"
level: 4
source: "Howl of the Wild"
aon_id: "creature-3267"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3267"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Morthak"
level: "Creature 4"
size: "Medium"
trait_01: "Beast"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; no vision, sensitive echolocation (precise) 90 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12"
abilityMods: [5, 2, 4, -3, 2, 1]
abilities_top:
  - name: "Sensitive Echolocation"
    desc: "The morthak can use its hearing as a precise sense with the listed range. If the morthak takes sonic damage beyond its resistance, its senses are overloaded and all creatures are [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] from it for 1 round."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +14; __Ref__: +10; __Will__: +10"
hp: 70
health:
  - name: "HP"
    desc: "70; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]; __Resistances__ sonic 5"
abilities_mid:
  - name: "Auditory Swipe"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within the morthak's reach uses an [[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]] __action__"
  - name: "Effect"
    desc: "The morthak makes a claw Strike against the triggering creature."
speed: "20 feet, burrow 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +13 __Damage__ 2d8+5 piercing"
  - name: "Melee"
    desc: "⬻ claw +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d6+5 slashing plus 1d6 sonic"
  - name: "Ranged"
    desc: "⬻ screech +10 (range 60 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|Sonic]]) __Damage__ 4d6 sonic"
abilities_bot:
  - name: "Shattering Scrape"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|Sonic]]) The morthak makes a claw Strike against a creature wearing stone or metal armor. If the Strike hits and the armor's Hardness is 12 or lower, that armor is [[srd/pf2e/compendium/rules-elements/conditions#Broken|broken]]."
sourcebook: "_Howl of the Wild_, page 140."
```

```encounter-table
name: Morthak
creatures:
  - 1: Morthak
```
