---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Frost Drake"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/cold
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/large
statblock: inline
name: "Frost Drake"
level: 7
source: "Monster Core"
aon_id: "creature-2962"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2962"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Frost Drake"
level: "Creature 7"
size: "Large"
trait_01: "Cold"
trait_02: "Dragon"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision, scent (imprecise) 30 feet, snow vision"
languages: "Draconic"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Athletics +17, Intimidation +14, Stealth +15"
abilityMods: [6, 2, 4, -1, 3, 1]
abilities_top:
  - name: "Snow Vision"
    desc: "Snow doesn't impair a frost drake's vision; they ignore concealment from snowfall."
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +17; __Ref__: +15; __Will__: +14"
hp: 115
health:
  - name: "HP"
    desc: "115; __Immunities__ cold, paralyzed, sleep; __Weaknesses__ fire 10"
abilities_mid:
  - name: "Retaliatory Strike"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the frost drake's tail successfully damages the frost drake with a Strike"
  - name: "Effect"
    desc: "The frost drake attempts to Strike with their tail. If the Strike hits, it deals an additional 1d6 damage."
speed: "20 feet; burrow 20 feet (snow only), climb 20 feet (ice only), fly 50 feet; ice stride"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +17 __Damage__ 2d12+8 piercing plus 1d6 cold"
  - name: "Melee"
    desc: "⬻ tail +17 (reach 10 feet) __Damage__ 2d10+8 bludgeoning"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The frost drake makes two fangs Strikes and one tail Strike in any order."
  - name: "Freezing Mist Breath"
    desc: "⬺ (Cold, Primal) The frost drake spits a ball of liquid up to 60 feet that explodes into a 20-foot-burst cloud of freezing mist. Those in the burst take 8d6 cold damage (DC 25 basic Reflex save). The frost drake can't use Freezing Mist Breath again for 1d6 rounds, during which the mist cakes all surfaces in the area with a sheet of slippery ice that turns the area into difficult terrain."
  - name: "Ice Stride"
    desc: "A frost drake isn't impeded by difficult terrain caused by snow or ice, nor do they need to attempt Acrobatics checks to keep from falling on slippery ice."
  - name: "Speed Surge"
    desc: "⬻ (Move)"
  - name: "Frequency"
    desc: "three times per day"
  - name: "Effect"
    desc: "The frost drake Strides or Flies twice."
sourcebook: "_Monster Core_, page 132."
```

```encounter-table
name: Frost Drake
creatures:
  - 1: Frost Drake
```
