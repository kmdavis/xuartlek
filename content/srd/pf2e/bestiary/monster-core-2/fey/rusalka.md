---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rusalka"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/water
  - pf2e/creature/trait/medium
statblock: inline
name: "Rusalka"
level: 12
source: "Monster Core 2"
other_sources: "Pathfinder #147: Tomorrow Must Burn"
aon_id: "creature-4531"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4531"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Rusalka"
level: "Creature 12"
size: "Medium"
trait_01: "Aquatic"
trait_02: "Fey"
trait_03: "Water"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +21, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +25, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +21, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +21, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +23, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +25"
abilityMods: [4, 5, 3, 1, 3, 7]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +21; __Ref__: +25; __Will__: +21"
hp: 230
health:
  - name: "HP"
    desc: "230; __Resistances__ fire 10; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 15"
abilities_mid:
  - name: "Blurred Form"
    desc: "A rusalka is [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] while underwater."
speed: "25 feet, swim 50 feet; water walk"
attacks:
  - name: "Melee"
    desc: "⬻ tresses +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d8+10 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Beckoning Call"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The rusalka cries out a compelling invitation. Each non-fey creature within a 300-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] must attempt a DC 29 Will save. The effect lasts for 1 round, but if the rusalka uses Beckoning Call again on subsequent rounds, the duration extends by 1 round for all affected creatures. Once a creature succeeds at any save against Beckoning Call, that creature is temporarily immune for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] and must spend each of its actions to move closer to the rusalka, avoiding obvious dangers. If a beckoned creature is adjacent to the rusalka, it stays still and doesn't act. If attacked by the rusalka, the creature is freed from captivation at the end of the rusalka's turn."
  - name: "Critical Failure"
    desc: "As failure, but if attacked by the rusalka, the creature can attempt a new save only at the start of its next turn, rather than being freed at the end of the rusalka's turn."
  - name: "Constrict"
    desc: "⬻ 2d8+10 bludgeoning, DC 32"
  - name: "Entangling Tresses"
    desc: "A rusalka can have up to eight creatures [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] within their tresses at a time."
  - name: "Flowing Hair"
    desc: "⬻ The rusalka attempts an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check against the Fortitude save of each creature they have [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] by their tresses. The rusalka moves each creature they succeed against up to 10 feet and each creature they critically succeed against up to 20 feet. This movement must all be within reach of its tresses."
  - name: "Shameful Touch"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The rusalka touches a creature within 5 feet using their hand, stirring up memories of regret and shame. The target must attempt a DC 35 Will save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1."
  - name: "Failure"
    desc: "The creature is sickened 1 and [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] 1."
  - name: "Critical Failure"
    desc: "The creature is sickened 1, stunned 1, and it must use its first action on its next turn to Strike itself, automatically hitting. Blue Week Those living in areas where rusalkas dwell know well to avoid the water during the week-long period in early Sarenith when the fey become particularly active, a time known in many regions as Blue Week. Most villages prohibit swimming and fishing during this time, though the prohibition is difficult to enforce, as it takes place during the height of good weather. Particularly superstitious folk take care to lock their doors from both within and without."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 35 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (at will), [[srd/pf2e/compendium/spells/rank-2/mist|Mist]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-1/charm|Charm]] (at will), [[srd/pf2e/compendium/spells/rank-5/control-water|Control Water]] (at will) - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-2/water-walk|Water Walk]]"
sourcebook: "_Monster Core 2_, page 272."
```

```encounter-table
name: Rusalka
creatures:
  - 1: Rusalka
```
