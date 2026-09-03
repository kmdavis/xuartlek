---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kappa"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/small
statblock: inline
name: "Kappa"
level: 2
source: "Monster Core 2"
aon_id: "creature-4457"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4457"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Kappa"
level: "Creature 2"
size: "Small"
trait_01: "Amphibious"
trait_02: "Beast"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "Common, Thalassic"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +7, Medicine +9, Survival +7"
abilityMods: [3, 4, 1, 1, 3, 1]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +10; __Will__: +7"
hp: 35
health:
  - name: "HP"
    desc: "35"
abilities_mid:
  - name: "Head Bowl"
    desc: "The depression atop a kappa's head is filled with water. Spilling, evaporating, or otherwise removing all the water from the top of a kappa's head reduces all their Speeds to 5 feet until the basin is again filled with water. A kappa who becomes prone must succeed at a DC 15 Reflex save or spill their water, and a kappa who becomes unconscious automatically spills their water. If a kappa is grappled, restrained, or stunned, another creature can attempt to spill the water from their bowl by spending a single action, which has the attack and manipulate traits, to attempt an Athletics check against the kappa's Fortitude DC. On a success, the creature spills the kappa's water."
speed: "15 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +11 (Agile) __Damage__ 1d10+3 slashing"
abilities_bot:
  - name: "Pull Arm"
    desc: "⬻ The kappa pulls one of their arms, gaining 10- foot reach with that arm. The opposing arm shrinks to little more than a hand extending from their shell. The kappa can still use their shortened hand to hold things, but they can't use that hand to wield a shield or weapon. By spending a single action to pull their opposing arm, the kappa can return their arms to their original length. A Sinister Side Kappas despise horses and gleefully kill and consume any that venture too close to the water's edge. Because of this, they're sometimes mistaken for strangely armored goblins. Some vile kappas have even developed a taste for human flesh and have been witnessed drowning people before tearing them apart for consumption."
sourcebook: "_Monster Core 2_, page 208."
```

```encounter-table
name: Kappa
creatures:
  - 1: Kappa
```
