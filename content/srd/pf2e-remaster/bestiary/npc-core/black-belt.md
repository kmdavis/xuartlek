---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Black Belt"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Black Belt"
level: 12
source: "NPC Core"
aon_id: "creature-3504"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3504"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Black Belt"
level: "Creature 12"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Athletics +25, Martial Arts Lore +22, Stealth +20"
abilityMods: [5, 4, 3, 1, 3, 0]
abilities_top:
  - name: "Items"
    desc: "_+1 striking handwraps of mighty blows_, _+1 striking bo staff_, _bands of force_"
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +23; __Ref__: +23; __Will__: +20"
hp: 220
health:
  - name: "HP"
    desc: "220"
abilities_mid:
  - name: "Blocking Counterattack"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within the black belt's reach targets them with a melee attack"
  - name: "Effect"
    desc: "The black belt blocks, gaining a +2 circumstance bonus to their AC against the triggering attack. If the attack misses, the black belt retaliates with a Strike. This Strike doesn't count toward the black belt's multiple attack penalty, and the multiple attack penalty doesn't apply to this Strike."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _bo staff_ +25 (Magical, Parry, Reach, Trip) __Damage__ 2d8+9 bludgeoning"
  - name: "Melee"
    desc: "⬻ _fist_ +25 (Agile, Magical, Nonlethal, Unarmed) __Damage__ 2d8+9 bludgeoning"
abilities_bot:
  - name: "Flurry of Blows"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The black belt makes two fist Strikes. If both hit the same creature, combine their damage for the purpose of resistances and weaknesses. The black belt can substitute any number of the attacks with bo staff Strikes or attempts to Grapple, Reposition, Shove, or Trip."
  - name: "Powerful Fists"
    desc: "The martial artist's fist Strikes don't take penalties when making lethal attacks, and their fist Strikes are treated as cold iron and silver."
  - name: "Rapid Barrage"
    desc: "⬺ (Incapacitation) The black belt pummels their fists in a fast onslaught. They make three fist Strikes against one target. If more than one Strike hits, combine damage for the purpose of resistances and weaknesses. Regardless of whether any Strikes hit, the target must succeed at a DC 32 Fortitude save or be clumsy 1 until the end of their next turn and stunned 1 (clumsy 2 and stunned 2 on a critical failure)."
spellcasting:
  - name: "Monk Focus Spells"
    desc: "DC 32, attack +23, 2 Focus Points - __6th__ Inner Upheaval, Qi Rush"
sourcebook: "_NPC Core_, page 73."
```

```encounter-table
name: Black Belt
creatures:
  - 1: Black Belt
```
