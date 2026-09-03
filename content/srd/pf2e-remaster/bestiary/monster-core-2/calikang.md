---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Calikang"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Calikang"
level: 12
source: "Monster Core 2"
other_sources: "Pathfinder #149: Against the Scarlet Triad"
aon_id: "creature-4290"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4290"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Calikang"
level: "Creature 12"
size: "Large"
trait_01: "Humanoid"
trait_02: "Uncommon"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision, _truesight_"
languages: "Common, Jotun"
skills:
  - name: "Skills"
    desc: "Athletics +25, Intimidation +24"
abilityMods: [7, 4, 5, -2, 2, 4]
abilities_top:
  - name: "Suspended Animation"
    desc: "(concentrate) By concentrating for 5 minutes, the calikang can enter a state of suspended animation, freezing in place and becoming motionless but remaining aware of their surroundings. While in this state, the calikang gains a +4 status bonus to Fortitude saves, doesn't age, and is immune to disease, inhaled toxins, poison, starvation, and thirst. A calikang can exit suspended animation as a free action. If they exit this state to attack, the calikang gains a +2 circumstance bonus to their initiative roll."
  - name: "Items"
    desc: "_+1 striking longsword_ (2)"
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +23; __Ref__: +22; __Will__: +20 +1 status to all saves vs. magic"
hp: 235
health:
  - name: "HP"
    desc: "235; __Immunities__ electricity"
abilities_mid:
  - name: "Energy Conversion"
    desc: "(arcane) Whenever the calikang is hit by an electricity spell's attack roll or rolls a successful save against a spell that deals electricity damage, they absorb the energy. This heals the calikang for an amount of HP equal to quadruple the spell's rank and recharges their Energy Breath. A calikang can't absorb their own spells this way."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ longsword +28 (Magical, reach 10 feet, versatile P) __Damage__ 2d8+15 slashing"
  - name: "Melee"
    desc: "⬻ fist +25 (Agile, nonlethal, reach 10 feet) __Damage__ 3d8+13 bludgeoning"
abilities_bot:
  - name: "Energy Breath"
    desc: "⬺ (Arcane)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The calikang exhales a blast of energy that deals 13d6 energy damage to creatures in a 60-foot line (DC 28 basic Reflex save). The calikang can choose the damage type each time: acid, cold, electricity, fire, or sonic. This ability gains the trait of the chosen damage type. Increase the die size to d8 if the calikang chooses electricity."
  - name: "Sixfold Flurry"
    desc: "⬺ The calikang makes up to two longsword Strikes and up to four fist Strikes. Each Strike must be against a different target. These attacks count toward the calikang's multiple attack penalty, which doesn't increase until after all the attacks are complete. For 1 round, the calikang gains a circumstance bonus to their AC equal to the number of Strikes they choose not to take to a maximum of +4 for taking only two Strikes. Calikang Origins Legend holds that an ancient Vudrani god failed to protect an important treasury from a raid by asuras. In shame, he severed his fingers and cast them down upon the world. Calikangs arose from the fingers, and, as penance, they've sought to protect worldly holdings from robberies or invasions ever since."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 28 - __1st__ Runic Weapon (at will) - __6th__ Chain Lightning - __Constant (6th)__ Truesight"
sourcebook: "_Monster Core 2_, page 66."
```

```encounter-table
name: Calikang
creatures:
  - 1: Calikang
```
