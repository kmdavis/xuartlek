---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Scorpion"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Giant Scorpion"
level: 3
source: "Monster Core"
aon_id: "creature-3175"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3175"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Scorpion"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, tremorsense (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [4, 2, 3, -5, 2, -4]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +12; __Ref__: +9; __Will__: +7"
hp: 45
health:
  - name: "HP"
    desc: "45"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲ Stinger only."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pincer +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d8+6 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ stinger +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d6+6 piercing plus giant scorpion venom"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d6+4 bludgeoning, DC 20"
  - name: "Giant Scorpion Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 18 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d10 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 round)"
  - name: "Stage 2"
    desc: "2d10 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 3"
    desc: "2d10 poison damage and enfeebled 2 (1 round)"
sourcebook: "_Monster Core_, page 298."
```

```encounter-table
name: Giant Scorpion
creatures:
  - 1: Giant Scorpion
```
