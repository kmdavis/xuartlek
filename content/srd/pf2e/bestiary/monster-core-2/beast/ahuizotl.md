---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ahuizotl"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Ahuizotl"
level: 6
source: "Monster Core 2"
aon_id: "creature-4022"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4022"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ahuizotl"
level: "Creature 6"
size: "Large"
trait_01: "Amphibious"
trait_02: "Beast"
trait_03: "Uncommon"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15"
abilityMods: [5, 3, 5, -1, 3, 3]
abilities_top:
  - name: "Voice Imitation"
    desc: "An ahuizotl can mimic the sounds of a person in distress by attempting a [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Lie|Lie]]. The ahuizotl has a +4 circumstance bonus to this check."
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +17; __Ref__: +13; __Will__: +13"
hp: 105
health:
  - name: "HP"
    desc: "105"
speed: "25 feet, swim 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +17 __Damage__ 2d8+8 piercing"
  - name: "Melee"
    desc: "⬻ claw +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+8 slashing"
  - name: "Melee"
    desc: "⬻ tail claw +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d4+8 slashing plus Improved Grab"
abilities_bot:
  - name: "Tail Drag"
    desc: "⬻"
  - name: "Requirements"
    desc: "The ahuizotl has a Medium or smaller creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] with their tail claw"
  - name: "Effect"
    desc: "The ahuizotl attempts an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check against the creature's Fortitude DC."
  - name: "Critical Success"
    desc: "If the creature is 10 feet away from the ahuizotl, it's dragged into a square adjacent to the ahuizotl. The ahuizotl can make a jaws Strike against the creature."
  - name: "Success"
    desc: "If the creature is 10 feet away from the ahuizotl, it's dragged into a square adjacent to the ahuizotl."
  - name: "Failure"
    desc: "The creature isn't dragged."
  - name: "Critical Failure"
    desc: "The creature isn't dragged, and the ahuizotl no longer has the creature grabbed. Ahuizotl Allies An ahuizotl is unexpectedly canny in how they handle potential competitors in their territory, and when presented with fellow predators capable of conversation, they sometimes broker alliances. Will-o'-wisps are particular favorites as allies, as they can lure prey into the ahuizotl's clutches and feast on the anguish later when the mutilated corpse is discovered."
sourcebook: "_Monster Core 2_, page 20."
```

```encounter-table
name: Ahuizotl
creatures:
  - 1: Ahuizotl
```
