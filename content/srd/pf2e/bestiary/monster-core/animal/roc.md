---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Roc"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Roc"
level: 9
source: "Monster Core"
aon_id: "creature-3170"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3170"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Roc"
level: "Creature 9"
size: "Gargantuan"
trait_01: "Animal"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +21"
abilityMods: [8, 2, 5, -4, 1, 0]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +20; __Ref__: +17; __Will__: +16"
hp: 180
health:
  - name: "HP"
    desc: "180"
abilities_mid:
  - name: "Wing Rebuff"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature moves from beyond the reach of the roc's wing to within the reach of the roc's wing"
  - name: "Effect"
    desc: "The roc makes a wing Strike against the triggering creature. If the roc Pushes the creature, it disrupts the triggering [[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]] action."
speed: "20 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+12 piercing"
  - name: "Melee"
    desc: "⬻ talon +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+12 slashing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ wing +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 30 feet]]) __Damage__ 2d6+10 bludgeoning plus Improved Push 10 feet"
abilities_bot:
  - name: "Carry"
    desc: "A roc can [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]] at half Speed while it has a creature grabbed or restrained in either or both of its talons, carrying that creature along with it."
  - name: "Flying Strafe"
    desc: "⬺ The roc [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] up to its Speed and makes two talon Strikes at any point during that movement. Each Strike must target a different creature. Each attack takes the normal multiple attack penalty."
  - name: "Snack"
    desc: "A roc gains a +2 circumstance bonus to hit with its beak Strike if the target is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] in its talon. Roc's Riches While most treasure a roc may possess is incidental—the remains of prey haphazardly scattered in or around the nest—roc feathers, especially white or gold ones, are highly prized in certain markets. Even more valuable are roc eggs, especially to some [[srd/pf2e/compendium/gm/creature-families/giant|giants]] who enjoy their unique flavor."
sourcebook: "_Monster Core_, page 294."
```

```encounter-table
name: Roc
creatures:
  - 1: Roc
```
