---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pairaka"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/div
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Pairaka"
level: 7
source: "Monster Core 2"
aon_id: "creature-4341"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4341"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Pairaka"
level: "Creature 7"
size: "Medium"
trait_01: "Div"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; greater darkvision"
languages: "Common, Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Arcana +13, Deception +20, Diplomacy +20, Intimidation +16, Religion +13, Society +13, Stealth +16"
abilityMods: [3, 5, 3, 2, 4, 7]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +12; __Ref__: +16; __Will__: +17 +1 status to all saves vs. magic"
hp: 105
health:
  - name: "HP"
    desc: "105; __Immunities__ disease; __Weaknesses__ cold iron 5, holy 5"
abilities_mid:
  - name: "Hatred of Red"
    desc: "Pairakas hate the color red. They won't wear the color or willingly enter any place painted in a shade of red. Given a choice, they'll attack a creature wearing red before others, seeing their choice to do so as a personal affront. If barred from expressing their displeasure toward the color by force or some magical effect, they take 2d6 mental damage at the end of their turn."
speed: "25 feet, fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +16 (Agile, finesse, magical, unholy) __Damage__ 2d8+9 slashing plus bubonic plague"
abilities_bot:
  - name: "Bubonic Plague"
    desc: "(Disease) A creature can't remove the fatigued condition while infected"
  - name: "Saving Throw"
    desc: "DC 23 Fortitude; Onset 1 day"
  - name: "Stage 1"
    desc: "fatigued (1 day)"
  - name: "Stage 2"
    desc: "enfeebled 2 and fatigued (1 day)"
  - name: "Stage 3"
    desc: "enfeebled 3, fatigued, and takes 1d6 persistent bleed damage every 1d20 minutes (1 day)"
  - name: "Change Shape"
    desc: "⬻ (divine, polymorph) The pairaka can take the appearance of any Small or Medium humanoid or animal. This doesn't change their Speed or their attack and damage modifiers with their Strikes, but it might change the damage type their strikes deal."
  - name: "Tormenting Dreams"
    desc: "⬺ (Divine, emotion, mental)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The pairaka torments a sleeping creature within 100 feet with visions of betrayals by loved ones and friends. The target must attempt a DC 25 Will save, with the effects of the _nightmare_ spell."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25 - __Cantrips (4th)__ Detect Magic - __4th__ Charm (at will), Outcast's Curse (at will), Suggestion (at will), Translocate (at will)"
  - name: "Rituals"
    desc: "DC 25 - __1st__ Div Pact"
sourcebook: "_Monster Core 2_, page 112."
```

```encounter-table
name: Pairaka
creatures:
  - 1: Pairaka
```
