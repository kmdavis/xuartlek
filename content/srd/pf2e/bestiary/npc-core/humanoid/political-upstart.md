---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Political Upstart"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Political Upstart"
level: 0
source: "NPC Core"
aon_id: "creature-3505"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3505"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Political Upstart"
level: "Creature 0"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; (11 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +8, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +10, [[srd/pf2e/compendium/rules-elements/skills/lore|Legal Lore]] +11, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +10, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +11"
abilityMods: [0, 1, 0, 2, 2, 3]
abilities_top:
  - name: "Rhetoric Specialist"
    desc: "For social encounters involving debate and legal logic, the political upstart is a 3rd-level challenge."
  - name: "Items"
    desc: "long coat (functions as [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]]), political pamphlets, soapbox, Writing Set"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +4; __Ref__: +7; __Will__: +10"
hp: 15
health:
  - name: "HP"
    desc: "15"
abilities_mid:
  - name: "Retort"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature fails a Charisma-based skill check against the political upstart"
  - name: "Effect"
    desc: "The political upstart targets the creature with Fiery Rhetoric."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4 bludgeoning"
abilities_bot:
  - name: "Fiery Rhetoric"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The upstart rattles off talking points at an enemy within 30 feet. The target takes a –2 status penalty to Perception and Will saves for 1 minute."
  - name: "Fascinating Speech"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The political upstart begins a rousing speech which they can Sustain up to 1 minute. Any creature within 30 feet that can hear the speech, must attempt a DC 17 Will save."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] with the upstart for 1 round."
  - name: "Critical Failure"
    desc: "The creature is fascinated with the upstart as long as the speech lasts."
sourcebook: "_NPC Core_, page 76."
```

```encounter-table
name: Political Upstart
creatures:
  - 1: Political Upstart
```
