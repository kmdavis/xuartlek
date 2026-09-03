---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zoaem"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/archon
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/small
statblock: inline
name: "Zoaem"
level: 1
source: "Monster Core"
aon_id: "creature-2832"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2832"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Zoaem"
level: "Creature 1"
size: "Small"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "Diabolic, Draconic, Empyrean, Utopian"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Intimidation +6, Religion +6"
abilityMods: [-5, 3, 1, -1, 1, 1]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +6; __Ref__: +10; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20 (all-around vision); __Immunities__ fear; __Resistances__ fire 3; __Weaknesses__ unholy 3"
abilities_mid:
  - name: "Archon's Protection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages the archon's ally and both are within 15 feet of the archon"
  - name: "Effect"
    desc: "The ally gains resistance 3 to all damage against the triggering damage and the archon can make a Strike against the enemy."
speed: "fly 40 feet"
attacks:
  - name: "Ranged"
    desc: "⬻ eye ray +8 (Agile, Fire, Holy, Magical, range 30 feet) __Damage__ 1d8 fire"
abilities_bot:
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "The zoaem's rings and wings move in a complex pattern, mesmerizing creatures in the zoaem's choice of a 10-foot emanation or a 5-foot burst within 60 feet. Each creature must succeed at a DC 17 Will save or be fascinated with the zoaem for 1 minute and stunned 1 (or stunned for 1 round on a critical failure)."
  - name: "Light of Truth"
    desc: "⬻ (Concentrate, Divine, Light) The zoaem shines an intense light of truth, as _revealing light_ but in a 60-foot line. Against creatures affected by this light, the zoaem and their allies gain a +1 status bonus to damage rolls and Recall Knowledge checks. The zoaem can't use Light of Truth again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ Light - __1st__ Heal - __4th__ Read Omens __Behold!__ ⬺ (Concentrate, Illusion, Incapacitation, Visual)"
sourcebook: "_Monster Core_, page 26."
```

```encounter-table
name: Zoaem
creatures:
  - 1: Zoaem
```
