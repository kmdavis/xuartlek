---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cassisian"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/angel
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Cassisian"
level: 1
source: "Monster Core"
aon_id: "creature-2814"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2814"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Cassisian"
level: "Creature 1"
size: "Tiny"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "Common, Diabolic, Draconic, Empyrean"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Diplomacy +6, Religion +6, Stealth +6"
abilityMods: [-1, 1, 2, -1, 1, 1]
abilities_top:
  - name: "Repository of Lore"
    desc: "While the cassisian isn't particularly intelligent, they have perfect memory and can remember everything they see or hear. This allows them to attempt Lore checks on any topic with a +10 modifier, provided (at the GM's discretion) they've encountered the topic in question before. The cassisian's limited intellect often prevents them from acting upon their knowledge, making them a better resource than agent in using information."
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +6; __Will__: +4 +1 status to all saves vs. unholy creatures"
hp: 20
health:
  - name: "HP"
    desc: "20; __Resistances__ cold 3, fire 3; __Weaknesses__ unholy 3"
abilities_mid:
  - name: "Transfer Protection"
    desc: "(holy) A creature can wear a willing cassisian as a helmet. While it does, the cassisian can't act, but the cassisian extends their +1 status bonus to AC and saves against unholy creatures to their wearer. At any time, the cassisian can detach themself from their wearer as a single action."
speed: "fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ headbutt +6 (Agile, Finesse, Holy, Magical, reach 0 feet) __Damage__ 1d6–1 bludgeoning"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) A cassisian can take the appearance of a dove, a winged humanoid, a dog, or a fish. Normally, this doesn't change their Speed or the attack and damage bonuses for their Strikes, but it might change the damage type Strikes deal (typically to bludgeoning). Any further changes for specific forms are noted below."
  - name: "Dog"
    desc: "size Small scent (imprecise) 30 feet, Speed 40 feet; Skills Athletics +6; Melee ⬻ jaws +7, Damage 1d6+2 piercing plus Knockdown"
  - name: "Fish"
    desc: "swim Speed 30 feet"
  - name: "Eye Beams"
    desc: "⬺ (Concentrate, Divine, Cold) The cassisian releases beams of heat or cold from their eyes, dealing 2d6 cold or fire damage (DC 17 basic Reflex save) to all creatures in a 15-foot line. They can’t use Eye Beams again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 16 - __Cantrips (1st)__ Know the Way, Light - __1st__ Heal - __4th__ Read Omens"
sourcebook: "_Monster Core_, page 14."
```

```encounter-table
name: Cassisian
creatures:
  - 1: Cassisian
```
