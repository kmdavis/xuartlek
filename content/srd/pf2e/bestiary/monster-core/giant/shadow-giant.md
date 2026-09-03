---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Shadow Giant"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/large
statblock: inline
name: "Shadow Giant"
level: 13
source: "Monster Core"
aon_id: "creature-3016"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3016"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Shadow Giant"
level: "Creature 13"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Shadow"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]], [[srd/pf2e/compendium/rules-elements/languages#Shadowtongue|Shadowtongue]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +24, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +21"
abilityMods: [8, 2, 5, 0, 1, 3]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/resilient-major|resilient]] [[srd/pf2e/compendium/equipment/armor#Breastplate|breastplate]]_, _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/flail/spiked-chain|spiked chain]]_"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +25; __Ref__: +20; __Will__: +23"
hp: 275
health:
  - name: "HP"
    desc: "275"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _spiked chain_ +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 3d8+18 slashing plus pall of shadow"
  - name: "Melee"
    desc: "⬻ fist +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d8+18 bludgeoning plus pall of shadow"
abilities_bot:
  - name: "Pall of Shadow"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shadow|Shadow]]) When a shadow giant hits with a melee attack, the target must succeed at a DC 30 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] and take a –1 status penalty to Perception checks involving sight as long as they remain drained. On a critical failure, this condition doesn't heal naturally and can be removed only with magic."
  - name: "Shadow Chain"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shadow|Shadow]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|Teleportation]]) Shadows extend the giant's chain as they make a spiked chain Strike, increasing their reach to 60 feet for that Strike. If this hits, the target must succeed at a DC 33 Will save or be teleported to an empty space within the shadow giant's normal reach."
  - name: "Shadowcloak"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shadow|Shadow]]) The shadow giant gains the effect of the [[srd/pf2e/compendium/spells/rank-2/blur|_blur_]] spell for 1 minute or until it is exposed to direct sunlight, whichever comes first."
sourcebook: "_Monster Core_, page 168."
```

```encounter-table
name: Shadow Giant
creatures:
  - 1: Shadow Giant
```
