---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Aapoph Granitescale"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/mutant
  - pf2e/creature/trait/serpentfolk
  - pf2e/creature/trait/medium
statblock: inline
name: "Aapoph Granitescale"
level: 6
source: "Monster Core"
aon_id: "creature-3184"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3184"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Aapoph Granitescale"
level: "Creature 6"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Mutant"
trait_03: "Serpentfolk"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +15"
abilityMods: [5, 4, 4, -1, 1, 1]
abilities_top:
  - name: "Items"
    desc: "Javelin (5), Longspear"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +16; __Ref__: +14; __Will__: +11 (+2 status vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
hp: 120
health:
  - name: "HP"
    desc: "120; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 5"
abilities_mid:
  - name: "Chipping Scales"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The granitescale is about to take piercing or slashing damage"
  - name: "Effect"
    desc: "The granitescale twists to take the blow on their hardest scales, which they shed to reduce the incoming force. The granitescale gains resistance 15 to the damage, but their AC is reduced by 2 for 1 day, when the shed scales regrow."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ longspear +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d8+11 piercing"
  - name: "Melee"
    desc: "⬻ fangs +17 __Damage__ 1d8+11 piercing plus serpentfolk venom"
  - name: "Ranged"
    desc: "⬻ javelin +16 (range increment 30 feet) __Damage__ 1d6+11 piercing"
abilities_bot:
  - name: "Rattling Spear"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
  - name: "Requirements"
    desc: "The granitescale's last action was a successful longspear Strike"
  - name: "Effect"
    desc: "The granitescale rattles the base of their spear, attempting an [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] all enemies within 30 feet (compare the check result to the targets' Will DCs individually)."
  - name: "Serpentfolk Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 22 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 round)"
  - name: "Stage 2"
    desc: "2d4 poison damage and enfeebled 1 (1 round)"
sourcebook: "_Monster Core_, page 304."
```

```encounter-table
name: Aapoph Granitescale
creatures:
  - 1: Aapoph Granitescale
```
