---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Chameleon"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Giant Chameleon"
level: 3
source: "Monster Core 2"
aon_id: "creature-4467"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4467"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Chameleon"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10"
abilityMods: [5, 3, 1, -4, 3, -2]
abilities_top:
  - name: "Camouflage"
    desc: "The giant chameleon can change its coloration to match its surroundings. It doesn't need cover to attempt to [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]] with a [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] check."
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +12; __Will__: +8"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "30 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d10+7 piercing"
  - name: "Melee"
    desc: "⬻ tongue +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ tongue grab"
abilities_bot:
  - name: "Tongue Grab"
    desc: "If the giant chameleon hits a creature with a tongue Strike, that creature becomes [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] by the giant chameleon. The target isn't [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]], but it can't move beyond the reach of the giant chameleon's tongue. A creature can sever the tongue with a Strike against AC 15 that deals at least 4 slashing damage. Though this doesn't deal any damage to the giant chameleon, it prevents it from using its tongue Strike until it regrows its tongue, which takes a week."
sourcebook: "_Monster Core 2_, page 216."
```

```encounter-table
name: Giant Chameleon
creatures:
  - 1: Giant Chameleon
```
