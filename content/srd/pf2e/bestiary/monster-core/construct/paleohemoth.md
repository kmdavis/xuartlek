---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Paleohemoth"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Paleohemoth"
level: 12
source: "Monster Core"
aon_id: "creature-3133"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3133"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Paleohemoth"
level: "Creature 12"
size: "Huge"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Rare"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20"
abilityMods: [7, 2, 6, -5, 0, -5]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +26; __Ref__: +20; __Will__: +18"
hp: 195
health:
  - name: "HP"
    desc: "195; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Resistances__ physical 10 (except adamantine or bludgeoning), spells 10 (except cold, earth, or water); __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|earth]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]] 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 2d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+13 piercing plus fossilization"
abilities_bot:
  - name: "Fossilization"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]]) The first time each round a creature takes damage from the paleohemoth's jaws, the target must attempt a DC 32 Fortitude save. If it fails and has not already been [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] by this ability, it becomes slowed 1 for 1 minute. If the creature was already slowed by this ability, a failed save causes it to be [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrified]] permanently."
  - name: "Reassemble"
    desc: "⬻ The paleohemoth reorganizes its bones, increasing its [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach]] to 25 feet and reducing its Speed to 15 feet. It can revert to its original form by taking this action again. Dragon Bones Many crafters attempt to infuse elemental magic into paleohemoths. The greatest successes have occurred when most of the bones originated from [[srd/pf2e/compendium/gm/creature-families/dragon|dragons]]. Specially created paleohemoths gain the following ability, with a damage type determined by the source of the bones."
  - name: "Energy Blast"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]]) The paleohemoth blasts magical energy from one of the skulls that make up its body. Each creature in a 30-foot cone takes 10d6 damage with a DC 32 basic Reflex save. The paleohemoth can't use Energy Blast again for 1d4 rounds."
sourcebook: "_Monster Core_, page 260."
```

```encounter-table
name: Paleohemoth
creatures:
  - 1: Paleohemoth
```
