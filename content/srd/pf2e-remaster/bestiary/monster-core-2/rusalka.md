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
languages: "Common, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +21, Athletics +24, Deception +25, Diplomacy +21, Nature +21, Performance +23, Stealth +25"
abilityMods: [4, 5, 3, 1, 3, 7]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +21; __Ref__: +25; __Will__: +21"
hp: 230
health:
  - name: "HP"
    desc: "230; __Resistances__ fire 10; __Weaknesses__ cold iron 15"
abilities_mid:
  - name: "Blurred Form"
    desc: "A rusalka is concealed while underwater."
speed: "25 feet, swim 50 feet; water walk"
attacks:
  - name: "Melee"
    desc: "⬻ tresses +24 (Agile, finesse, reach 15 feet) __Damage__ 3d8+10 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Beckoning Call"
    desc: "⬻ (Auditory, concentrate, incapacitation, mental, primal) The rusalka cries out a compelling invitation. Each non-fey creature within a 300-foot emanation must attempt a DC 29 Will save. The effect lasts for 1 round, but if the rusalka uses Beckoning Call again on subsequent rounds, the duration extends by 1 round for all affected creatures. Once a creature succeeds at any save against Beckoning Call, that creature is temporarily immune for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is fascinated and must spend each of its actions to move closer to the rusalka, avoiding obvious dangers. If a beckoned creature is adjacent to the rusalka, it stays still and doesn't act. If attacked by the rusalka, the creature is freed from captivation at the end of the rusalka's turn."
  - name: "Critical Failure"
    desc: "As failure, but if attacked by the rusalka, the creature can attempt a new save only at the start of its next turn, rather than being freed at the end of the rusalka's turn."
  - name: "Constrict"
    desc: "⬻ 2d8+10 bludgeoning, DC 32"
  - name: "Entangling Tresses"
    desc: "A rusalka can have up to eight creatures grabbed or restrained within their tresses at a time."
  - name: "Flowing Hair"
    desc: "⬻ The rusalka attempts an Athletics check against the Fortitude save of each creature they have grabbed or restrained by their tresses. The rusalka moves each creature they succeed against up to 10 feet and each creature they critically succeed against up to 20 feet. This movement must all be within reach of its tresses."
  - name: "Shameful Touch"
    desc: "⬻ (Emotion, mental, primal) The rusalka touches a creature within 5 feet using their hand, stirring up memories of regret and shame. The target must attempt a DC 35 Will save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is sickened 1."
  - name: "Failure"
    desc: "The creature is sickened 1 and stunned 1."
  - name: "Critical Failure"
    desc: "The creature is sickened 1, stunned 1, and it must use its first action on its next turn to Strike itself, automatically hitting. Blue Week Those living in areas where rusalkas dwell know well to avoid the water during the week-long period in early Sarenith when the fey become particularly active, a time known in many regions as Blue Week. Most villages prohibit swimming and fishing during this time, though the prohibition is difficult to enforce, as it takes place during the height of good weather. Particularly superstitious folk take care to lock their doors from both within and without."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 35 - __2nd__ Invisibility (at will), Mist (at will) - __5th__ Charm (at will), Control Water (at will) - __Constant (6th)__ Water Walk"
sourcebook: "_Monster Core 2_, page 272."
```

```encounter-table
name: Rusalka
creatures:
  - 1: Rusalka
```
