---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Draxie"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/sprite
  - pf2e/creature/trait/tiny
statblock: inline
name: "Draxie"
level: 3
source: "Monster Core"
aon_id: "creature-3211"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3211"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Draxie"
level: "Creature 3"
size: "Tiny"
trait_01: "Fey"
trait_02: "Sprite"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; low-light vision"
languages: "Common, Fey; telepathy (touch)"
skills:
  - name: "Skills"
    desc: "Acrobatics +9, Deception +10, Diplomacy +8, Nature +6, Stealth +11"
abilityMods: [-1, 4, 1, 3, 1, 3]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +6; __Ref__: +11; __Will__: +8"
hp: 45
health:
  - name: "HP"
    desc: "45; __Weaknesses__ cold iron 5"
speed: "15 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 (Agile, Finesse, Magical, reach 0 feet) __Damage__ 1d8+3 piercing"
  - name: "Ranged"
    desc: "⬻ euphoric spark +7 (Magical, range 20 feet) __Damage__ 2d4+3 mental"
abilities_bot:
  - name: "Draxie Dust"
    desc: "(Emotion, Incapacitation, Mental, Primal) The draxie breathes magical dust in a 15-foot cone. Roll 1d4 to determine the effect. Each creature in the area must succeed at a DC 17 Will save or be affected. The draxie can't use Draxie Dust again for 1d4 rounds. The target takes the effects of the _charm_ spell.The target loses its last 5 minutes of memory.The target takes the effects of a _sleep_ spell.For 1 minute, the target is in a state of euphoria that makes it stupefied 2 and slowed 1."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 20 - __Cantrips (1st)__ Light, Figment, Prestidigitation - __1st__ Illusory Disguise (×3) - __2nd__ Invisibility, Revealing Light"
sourcebook: "_Monster Core_, page 322."
```

```encounter-table
name: Draxie
creatures:
  - 1: Draxie
```
