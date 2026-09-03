---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tengu Sneak"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tengu
  - pf2e/creature/trait/medium
statblock: inline
name: "Tengu Sneak"
level: 2
source: "Monster Core"
aon_id: "creature-3214"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3214"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Tengu Sneak"
level: "Creature 2"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Tengu"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Tengu; plus two others"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +5, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +8"
abilityMods: [2, 4, 1, 1, 0, 1]
abilities_top:
  - name: "Items"
    desc: "Shortbow (30 arrows), tengu feather fan, Wakizashi"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +7; __Ref__: +10; __Will__: +4"
hp: 27
health:
  - name: "HP"
    desc: "27"
abilities_mid:
  - name: "Eat Fortune"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core-2/tengu|tengu]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "A creature within 60 feet uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|fortune]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/misfortune|misfortune]] effect"
  - name: "Effect"
    desc: "The tengu negates the attempt to manipulate fate and fortune. Eat Fortune gains the opposing trait, and the triggering effect is disrupted."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ wakizashi +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 1d4+2 slashing"
  - name: "Melee"
    desc: "⬻ beak +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+2 piercing"
  - name: "Ranged"
    desc: "⬻ shortbow +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], range increment 60 feet, reload 0) __Damage__ 1d6 piercing"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The tengu deals an additional 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Surprise Attacker"
    desc: "On the first round of combat, creatures that haven't acted yet are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the tengu."
  - name: "Feather Fan Dustup"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]])"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Effect"
    desc: "The tengu waves their feather fan, summoning a small magical breeze that kicks up dust in a 5-foot burst centered on a corner of their space, which lasts for 1d4 rounds. All creatures within that area are [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]], and all other creatures are concealed to them."
sourcebook: "_Monster Core_, page 325."
```

```encounter-table
name: Tengu Sneak
creatures:
  - 1: Tengu Sneak
```
