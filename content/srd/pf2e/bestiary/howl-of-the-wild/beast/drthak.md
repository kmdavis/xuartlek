---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Drthak"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/large
statblock: inline
name: "Drthak"
level: 6
source: "Howl of the Wild"
aon_id: "creature-3268"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3268"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Drthak"
level: "Creature 6"
size: "Large"
trait_01: "Beast"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; no vision, sensitive echolocation (precise) 120 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +13"
abilityMods: [4, 5, 4, -3, 3, -1]
abilities_top:
  - name: "Deep Breath"
    desc: "The drthak can [[srd/pf2e/books/player-core/chapter-8-playing-the-game/encounter-mode#Mounted Defenses|hold its breath]] for about 2 hours."
  - name: "Sensitive Echolocation"
    desc: "The drthak can use its hearing as a precise sense with the listed range. If the drthak takes sonic damage beyond its resistance, its senses are overloaded and all creatures are [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] from it for 1 round."
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +14; __Ref__: +17; __Will__: +11"
hp: 110
health:
  - name: "HP"
    desc: "110; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]"
abilities_mid:
  - name: "Auditory Hunter"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 15 feet uses an [[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]] action"
  - name: "Effect"
    desc: "The drthak Strides or [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swims]] towards the creature."
speed: "20 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +16 __Damage__ 2d8+4 piercing plus Grab"
  - name: "Ranged"
    desc: "⬻ screech +17 (range 60 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|Sonic]]) __Damage__ 4d6 sonic plus resonant jaws"
abilities_bot:
  - name: "Bubble Burst"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|Sonic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|Water]])"
  - name: "Requirement"
    desc: "The drthak is underwater"
  - name: "Effect"
    desc: "The drthak uses sonic power to push aside water in a 30-foot emanation, which then collapses in a crushing torrent. All creatures in the area, other than the drthak, take 3d10 bludgeoning damage (DC 24 basic Fortitude save)."
  - name: "Pull Under"
    desc: "The drthak can [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swim]] at half Speed while it has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] in its jaws, carrying the creature along with it."
  - name: "Resonant Jaws"
    desc: "When the drthak misses a screech Strike against a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] in its jaws, it deals that creature 2d6 sonic damage."
sourcebook: "_Howl of the Wild_, page 140."
```

```encounter-table
name: Drthak
creatures:
  - 1: Drthak
```
