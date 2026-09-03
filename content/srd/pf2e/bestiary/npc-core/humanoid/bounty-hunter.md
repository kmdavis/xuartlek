---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bounty Hunter"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Bounty Hunter"
level: 4
source: "NPC Core"
aon_id: "creature-3515"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3515"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Bounty Hunter"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +9"
abilityMods: [3, 4, 1, 0, 3, 0]
abilities_top:
  - name: "Items"
    desc: "Crossbow (10 bolts), Falchion, simple manacles, studded leather"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +12; __Will__: +11"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ falchion +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d10+6 slashing"
  - name: "Ranged"
    desc: "⬻ crossbow +14 (range increment 120 feet, reload 1) __Damage__ 1d8+3 piercing"
abilities_bot:
  - name: "Hunt Prey"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) The bounty hunter designates a single creature they can see and hear, or one they're [[srd/pf2e/compendium/rules-elements/actions/player-core#Track|Tracking]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Gather Information|Gathering Information]] about, as their prey. The bounty hunter gains a +2 circumstance bonus to Perception checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] the prey, to [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] checks to Track the prey, and to [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] checks to Gather Information about the prey. This effect lasts until they use Hunt Prey again."
  - name: "Running Reload"
    desc: "⬻ The bounty hunter Stride, Steps, or [[srd/pf2e/compendium/rules-elements/actions/player-core#Sneak|Sneaks]], and then Interacts to reload."
  - name: "Precision Edge"
    desc: "The first time the bounty hunter hits their hunted prey in a round, they deal an additional 1d8 precision damage."
  - name: "Posse's Edge"
    desc: "The bounty hunter and their allies gain a +1 circumstance bonus on initiative rolls if the opposing side includes their hunted prey."
sourcebook: "_NPC Core_, page 82."
```

```encounter-table
name: Bounty Hunter
creatures:
  - 1: Bounty Hunter
```
