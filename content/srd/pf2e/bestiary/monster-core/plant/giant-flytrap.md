---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Flytrap"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/huge
statblock: inline
name: "Giant Flytrap"
level: 10
source: "Monster Core"
aon_id: "creature-3000"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3000"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Flytrap"
level: "Creature 10"
size: "Huge"
trait_01: "Mindless"
trait_02: "Plant"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; tremorsense (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +21"
abilityMods: [7, 5, 5, -5, 3, -2]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +17; __Will__: +15"
hp: 185
health:
  - name: "HP"
    desc: "185; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] 10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10 **Quick Capture ⬲"
abilities_mid:
  - name: "Trigger"
    desc: "A creature hits or touches the flytrap**"
  - name: "Effect"
    desc: "The flytrap makes a leaf Strike against the triggering creature. If it hits, the creature is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] in that leaf."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ leaf +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+7 piercing plus 2d6 acid and Improved Grab"
abilities_bot:
  - name: "Focused Assault"
    desc: "⬺ The flytrap attacks a single target with all four of its leaves. The flytrap makes one leaf Strike. On a success, the flytrap deals the damage from one leaf Strike plus an additional 1d8 damage for every leaf beyond the first. On a failure, the flytrap deals the damage from one leaf Strike, but it can't use Improved Grab. It deals no damage on a critical failure. This counts toward the flytrap's multiple attack penalty as a number of attacks equal to the number of leaves the flytrap has."
  - name: "Hungry Flurry"
    desc: "⬺ The flytrap makes four leaf Strikes at a –2 penalty, each against a different target. These attacks count toward the flytrap's multiple attack penalty, but the multiple attack penalty doesn't increase until after it makes all its attacks."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Large, 2d8+3 bludgeoning plus 2d6 acid, Rupture 17"
sourcebook: "_Monster Core_, page 154."
```

```encounter-table
name: Giant Flytrap
creatures:
  - 1: Giant Flytrap
```
