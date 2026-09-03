---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Reefclaw"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/small
statblock: inline
name: "Reefclaw"
level: 1
source: "Monster Core"
aon_id: "creature-3166"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3166"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Reefclaw"
level: "Creature 1"
size: "Small"
trait_01: "Aberration"
trait_02: "Aquatic"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "Common; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +4"
abilityMods: [1, 4, 2, -3, 1, 1]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +7; __Ref__: +9; __Will__: +4"
hp: 17
health:
  - name: "HP"
    desc: "17"
abilities_mid:
  - name: "Death Frenzy"
    desc: "⬲"
  - name: "Trigger"
    desc: "The reefclaw is reduced to 0 Hit Points"
  - name: "Effect"
    desc: "The reefclaw makes a claw Strike before dying."
speed: "5 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +9 (Finesse) __Damage__ 1d6+1 slashing plus reefclaw venom and Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d6 bludgeoning, DC 17"
  - name: "Reefclaw Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 17 Fortitude"
  - name: "Maximum Duration"
    desc: "4 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage and enfeebled 2 (1 round). Eating Reefclaws Reefclaws amass no treasure, but their meat—if kept fresh—can be sold in the right markets. However, in an increasing number of places, the practice of eating reefclaws has fallen out of favor—which means, of course, that the reefclaw market has simply shifted to black-market butchers, where all manner of meat gathered from dubious sources is available for purchase, and the value has increased accordingly."
sourcebook: "_Monster Core_, page 291."
```

```encounter-table
name: Reefclaw
creatures:
  - 1: Reefclaw
```
