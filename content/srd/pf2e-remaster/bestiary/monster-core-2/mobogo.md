---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mobogo"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/huge
statblock: inline
name: "Mobogo"
level: 10
source: "Monster Core 2"
aon_id: "creature-4476"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4476"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Mobogo"
level: "Creature 10"
size: "Huge"
trait_01: "Amphibious"
trait_02: "Beast"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
languages: "Boggard; _speak with animals_"
skills:
  - name: "Skills"
    desc: "Acrobatics +19, Athletics +19, Nature +21, Stealth +19"
abilityMods: [7, 5, 6, -2, 5, 7]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +22; __Ref__: +17; __Will__: +19"
hp: 160
health:
  - name: "HP"
    desc: "160 , regeneration 30 (deactivated by acid^ cold^ or fire)"
speed: "25 feet, fly 20 feet, swim 30 feet; swamp passage"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +23 (reach 10 feet) __Damage__ 2d12+13 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ tongue +23 (Agile, reach 30 feet) __Damage__ 2d6+13 bludgeoning plus tongue grab"
abilities_bot:
  - name: "Song of the Swamp"
    desc: "⬻ (Auditory, emotion, mental, primal)"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Effect"
    desc: "The mobogo unleashes a booming croak. All boggards and mobogos within 50 feet gain a +2 status bonus to damage rolls and saves against fear for 1 round. Other creatures in the area of effect must attempt a DC 27 Will save."
  - name: "Success"
    desc: "The creature is unaffected and is temporarily immune for 24 hours."
  - name: "Failure"
    desc: "The creature is slowed 1 for 1d4 rounds."
  - name: "Critical Failure"
    desc: "The creature is slowed 2 for 1d4 rounds."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Large, 2d12+6 bludgeoning, Rupture 19"
  - name: "Swamp Passage"
    desc: "A mobogo ignores difficult terrain caused by swamp terrain features."
  - name: "Tongue Grab"
    desc: "A creature hit by the mobogo's tongue becomes grabbed by the mobogo. The creature isn't immobilized, but it can't move beyond the reach of the mobogo's tongue. A creature can sever the tongue with a Strike against AC 27 that deals at least 10 slashing damage. This deals no damage to the mobogo but prevents them from using their tongue Strike until they regrow their tongue, which takes 1 round. The mobogo can move without ending the tongue grab as long as the creature remains within the tongue's reach."
  - name: "Tongue Reposition"
    desc: "When a mobogo successfully Repositions a creature grabbed by their tongue, they increase the distance they can move that creature by 10 feet (a total of 15 feet on a success or 20 feet on a critical success); the creature must remain within the tongue's reach. Alternatively, the mobogo can transfer the grabbed creature to being grabbed by the mobogo's jaws. Children Of Gogunta Boggards of Golarion believe mobogos to have hatched from the first clutch of eggs laid by their demon goddess Gogunta, following her awakening at the dawn of creation. Boggards, hatched millennia later from the second clutch, have been charged with serving and aiding their elder siblings in keeping her sacred swamplands untainted by the presence of outsiders."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 27 - __4th__ Create Water (at will), Entangling Flora, Mist, Noise Blast (at will) - __5th__ Control Water - __Constant (2nd)__ Speak with Animals, Vanishing Tracks"
  - name: "Rituals"
    desc: "DC 27 - __4th__ Plant Growth"
sourcebook: "_Monster Core 2_, page 224."
```

```encounter-table
name: Mobogo
creatures:
  - 1: Mobogo
```
