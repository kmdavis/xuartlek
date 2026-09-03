---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Greater Hell Hound"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Greater Hell Hound"
level: 9
source: "Monster Core"
aon_id: "creature-3048"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3048"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Greater Hell Hound"
level: "Creature 9"
size: "Large"
trait_01: "Beast"
trait_02: "Fiend"
trait_03: "Fire"
trait_04: "Unholy"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision, scent (imprecise) 120 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +18, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +20"
abilityMods: [6, 5, 5, -2, 4, -2]
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +21; __Ref__: +19; __Will__: +16"
hp: 150
health:
  - name: "HP"
    desc: "150; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10"
abilities_mid:
  - name: "Hellish Revenge"
    desc: "⬲"
  - name: "Trigger"
    desc: "The greater hell hound is critically hit by any Strike"
  - name: "Effect"
    desc: "The greater hell hound's Hellfire Breath recharges. They can immediately use it as part of this reaction."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d8+9 piercing plus 2d6 fire"
abilities_bot:
  - name: "Hellfire Breath"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) The hell hound breathes flames that deal 10d6 fire damage to all creatures in a 15-foot cone (DC 28 basic Reflex save.) The hell hound can't use Hellfire Breath again for 1d4 rounds. If the greater hell hound would take fire damage or be targeted by a [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] effect, their Hellfire Breath recharges."
  - name: "Pack Attack"
    desc: "The greater hell hound's Strikes deal 1d8 extra damage to creatures within the reach of at least two of their allies. Hell Hound Minions Outside of [[srd/pf2e/compendium/gm/planes#Hell|Hell]], hell hounds are sometimes found in the service of fire-loving monsters such as [[srd/pf2e/bestiary/monster-core/giant/fire-giant|fire giants]] or [[srd/pf2e/bestiary/monster-core/elemental/ifrit|ifrit]], as well as mortals who seek to tame some of the raw power of Hell. In Cheliax, Hellknights occasionally call upon hell hounds to track down fugitives and traitors."
sourcebook: "_Monster Core_, page 194."
```

```encounter-table
name: Greater Hell Hound
creatures:
  - 1: Greater Hell Hound
```
