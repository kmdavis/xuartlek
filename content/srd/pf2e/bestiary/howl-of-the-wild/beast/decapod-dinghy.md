---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Decapod Dinghy"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Decapod Dinghy"
level: 8
source: "Howl of the Wild"
aon_id: "creature-3259"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3259"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Decapod Dinghy"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Amphibious"
trait_02: "Beast"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; tremorsense (imprecise) 30 feet, wavesense (imprecise) 30 feet"
languages: "Thalassic; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Athletics +18, Nature +17, Stealth +15"
abilityMods: [7, 3, 4, -2, 3, 0]
abilities_top:
  - name: "All Aboard"
    desc: "A decapod dinghy can carry up to 30 Bulk of creatures or unattended items on their back, such as five Medium creatures. The anemones' gentle hold on the passengers is sufficient in most situations, but while in combat, those passengers are slowed 1 if they want to take other actions while remaining on the decapod dinghy's back."
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +18; __Ref__: +15; __Will__: +15"
hp: 145
health:
  - name: "HP"
    desc: "145; __Immunities__ poison; __Weaknesses__ bludgeoning 5"
abilities_mid:
  - name: "Protect Passenger"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy within 20 feet damages one of the decapod dinghy's passengers"
  - name: "Effect"
    desc: "The decapod dinghy's anemones lash out for a tentacle Strike against the triggering creature."
speed: "30 feet, climb 25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +19 (reach 10 feet) __Damage__ 2d8+7 slashing plus 2d6 poison"
  - name: "Melee"
    desc: "⬻ tentacle +19 (Poison, reach 20 feet) __Damage__ 5d6 poison plus Grab"
abilities_bot:
  - name: "Anemone Transport"
    desc: "⬽ (Primal, Teleportation) The decapod dinghy and all their willing passengers teleport to a patch of anemones within 10 miles large enough for the decapod dinghy to stand among them. Although the decapod dinghy doesn't need to see the location, they must have been there before. All creatures transported are temporarily immune to this ability for 24 hours."
  - name: "Inflate Anemones"
    desc: "⬻ The anemones on the decapod dinghy's back inflate, enveloping all passengers and giving each passenger a +2 circumstance bonus to AC until the beginning of the decapod dinghy's next turn."
  - name: "Stinging Anemones"
    desc: "⬻ (Poison) The decapod dinghy's anemones sting any number of creatures they choose among passengers and those the decapod dinghy has grabbed or restrained. The stings deal 5d6 poison damage (DC 26 basic Fortitude save). On a failed save, that creature is also enfeebled 2 for 1 hour."
sourcebook: "_Howl of the Wild_, page 135."
```

```encounter-table
name: Decapod Dinghy
creatures:
  - 1: Decapod Dinghy
```
