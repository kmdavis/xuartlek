---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wyvern"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/large
statblock: inline
name: "Wyvern"
level: 6
source: "Monster Core"
aon_id: "creature-2961"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2961"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Wyvern"
level: "Creature 6"
size: "Large"
trait_01: "Dragon"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12"
abilityMods: [5, 2, 4, -2, 3, 0]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +16; __Ref__: +12; __Will__: +13"
hp: 95
health:
  - name: "HP"
    desc: "95; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Savage"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] by the wyvern critically fails a skill check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]]"
  - name: "Effect"
    desc: "The wyvern makes a stinger Strike against the triggering creature."
speed: "20 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +17 __Damage__ 2d12+5 piercing"
  - name: "Melee"
    desc: "⬻ claw +17 __Damage__ 2d8+5 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ stinger +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+5 piercing plus wyvern venom"
abilities_bot:
  - name: "Powerful Dive"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]]) The wyvern Flies up to their fly Speed and must both move forward at least 20 feet and descend at least 10 feet. If they end the movement within melee reach of at least one enemy their size or smaller, they can make a claw Strike against that enemy. If the claw hits, as a free action, the wyvern can either automatically Grab the target or knock it [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
  - name: "Punishing Momentum"
    desc: "⬻"
  - name: "Requirements"
    desc: "The wyvern grabbed a creature this turn using Powerful Dive"
  - name: "Effect"
    desc: "The wyvern can [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]] at half Speed while holding the creature in their claws, carrying that creature along with them and dropping it at the end of their movement. Alternatively, the wyvern can Strike the creature with their stinger with a +2 circumstance bonus."
  - name: "Wyvern Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 22 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d6 poison damage (1 round)"
  - name: "Stage 2"
    desc: "3d6 poison damage (1 round)"
  - name: "Stage 3"
    desc: "4d6 poison damage (1 round) Are Wyverns Drakes? Although commonly classified as drakes, wyverns exhibit significant differences from most other types of drakes. While scholars debate the precise relationship between them, none dispute that they exhibit collegial behavior and general deference to one another."
sourcebook: "_Monster Core_, page 131."
```

```encounter-table
name: Wyvern
creatures:
  - 1: Wyvern
```
