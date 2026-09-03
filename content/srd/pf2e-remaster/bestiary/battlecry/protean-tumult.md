---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Protean Tumult"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/protean
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Protean Tumult"
level: 12
source: "Battlecry!"
aon_id: "creature-3932"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3932"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Protean Tumult"
level: "Creature 12"
size: "Gargantuan"
trait_01: "Monitor"
trait_02: "Protean"
trait_03: "Troop"
trait_04: "Uncommon"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision, entropy sense (imprecise) 30 feet"
languages: "Chthonian, Empyrean, Protean"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Athletics +22, Intimidation +22, Survival +20"
abilityMods: [4, 6, 4, 0, 2, 4]
abilities_top:
  - name: "Entropy Sense"
    desc: "(divine, prediction) A protean tumult can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants it the ability to sense creatures within the listed range. Veil of privacy prevents a creature from being detected via entropy sense automatically (without a counteract check)."
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +22; __Ref__: +25; __Will__: +19 +1 status to all saves vs. magic"
hp: 210
health:
  - name: "HP"
    desc: "210 (4 segments, fast healing 8); __Resistances__ precision 8, protean anatomy 12; __Weaknesses__ area damage 10, splash damage 10"
abilities_mid:
  - name: "Protean Anatomy"
    desc: "(divine) The vital organs of each individual protean in the troop shift and change shape and position constantly. Immediately after the protean tumult takes acid, electricity, or sonic damage, it gains the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the tumult takes damage of one of the other types (in which case its resistance changes to match that type), whichever comes first. The tumult is immune to polymorph effects unless it is a willing target. If blinded or deafened, the tumult automatically recovers at the end of its next turn as new sensory organs grow to replace the compromised ones."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet, fly 30 feet, swim 25 feet; troop movement , unfettered movement"
abilities_bot:
  - name: "Chaos Strike"
    desc: "⭓ (Divine, Morph)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The protean tumult chooses adamantine, cold iron, or silver; the damage dealt by its Claws, Jaws, and Tails is treated as that material for 1 minute or until it uses Chaos Strike again."
  - name: "Chaos Flux"
    desc: "A protean tumult is less organized and more vicious than most troops. It can move into other creatures' spaces, and other creatures can move into its spaces. Its spaces are difficult terrain to non-protean creatures. A creature that willingly moves into a protean tumult's space takes 1d12+1 bludgeoning, piercing, or slashing damage (DC 29 basic Reflex save); a creature takes this damage only once per round. __Claws, Jaws, and Tails__"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The tumult viciously attacks each enemy within a 5-foot emanation (DC 29 basic Reflex save). The damage depends on the number of actions. ⬻ 1d12+1 bludgeoning, piercing, or slashing damage ⬺ 2d12+10 bludgeoning, piercing, or slashing damage ⬽ 3d12+11 bludgeoning, piercing, or slashing damage"
  - name: "Stupefying Swipe"
    desc: "⬺ (Divine, Emotion, Mental) The protean tumult makes their way across the battlefield. It Strides. At the end of this movement, they lash out at the enemy with tentacles and other blunt body parts, dealing 2d12+10 bludgeoning damage in a 5-foot emanation (DC 29 basic Reflex save). A creature who fails this save is also stupefied 2 for 2 rounds (stupefied 3 on a critical failure)."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29 - __Constant (4th)__ Unfettered Movement"
sourcebook: "_Battlecry!_, page 188."
```

```encounter-table
name: Protean Tumult
creatures:
  - 1: Protean Tumult
```
