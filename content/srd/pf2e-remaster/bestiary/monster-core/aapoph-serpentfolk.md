---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Aapoph Serpentfolk"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/mutant
  - pf2e/creature/trait/serpentfolk
  - pf2e/creature/trait/medium
statblock: inline
name: "Aapoph Serpentfolk"
level: 3
source: "Monster Core"
aon_id: "creature-3182"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3182"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Aapoph Serpentfolk"
level: "Creature 3"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Mutant"
trait_03: "Serpentfolk"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision, scent (imprecise) 30 feet"
languages: "Aklo, Sakvroth; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +11, Intimidation +6"
abilityMods: [4, 2, 3, -1, 1, -1]
abilities_top:
  - name: "Items"
    desc: "Scimitar"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +10; __Ref__: +7; __Will__: +6 (+2 status vs. mental)"
hp: 60
health:
  - name: "HP"
    desc: "60; __Resistances__ poison 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ scimitar +11 (Forceful, Sweep) __Damage__ 1d6+6 slashing"
  - name: "Melee"
    desc: "⬻ fangs +11 __Damage__ 1d8+6 piercing plus serpentfolk venom"
  - name: "Melee"
    desc: "⬻ tail +11 (Agile) __Damage__ 1d6+6 bludgeoning plus Knockdown"
abilities_bot:
  - name: "Serpentfolk Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 20 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "2d4 poison damage and enfeebled 1 (1 round)"
  - name: "Slithering Attack"
    desc: "⬻ The aapoph serpentfolk makes one scimitar or fangs Strike and one tail Strike, each targeting a different creature. These attacks both count toward the aapoph's multiple attack penalty, but the penalty doesn't increase until after the aapoph makes both attacks. Aapoph Mutations Aapophs are prone to mutations, which you can choose or roll using a d%. 1–45No mutation 46–56 Dual tail 57–66 Additional fangs 67–84 Hooded neck 85–91 Horns 92–96 Additional, vestigial head 97–100 Spiny scales"
sourcebook: "_Monster Core_, page 303."
```

```encounter-table
name: Aapoph Serpentfolk
creatures:
  - 1: Aapoph Serpentfolk
```
