---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Big Boss Goblin"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/goblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Big Boss Goblin"
level: 6
source: "NPC Core"
aon_id: "creature-3643"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3643"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Big Boss Goblin"
level: "Creature 6"
size: "Small"
trait_01: "Goblin"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Goblin|Goblin]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +13, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [3, 1, 3, 1, 1, 3]
abilities_top:
  - name: "Items"
    desc: "battered crown (or other symbol of authority), Hide Armor, _+1 [[srd/pf2e/compendium/equipment/weapons/polearm/horsechopper|horsechopper]]_, Shortbow (20 arrows)"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +17; __Ref__: +11; __Will__: +14"
hp: 100
health:
  - name: "HP"
    desc: "100"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲ __Not Me!__ ⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]])"
  - name: "Trigger"
    desc: "The big boss goblin is targeted with an attack, and a [[srd/pf2e/compendium/rules-elements/traits/player-core/goblin|goblin]] is adjacent to them"
  - name: "Effect"
    desc: "The big boss goblin yanks the goblin in front of the attack to face the consequences in their stead. The big boss goblin gains a +2 circumstance bonus to their AC against the triggering attack. If it hits, the big boss goblin takes half damage, and the other goblin takes the remaining half."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _horsechopper_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 1d8+5 slashing"
  - name: "Melee"
    desc: "⬻ jaws +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d6+5 piercing"
  - name: "Ranged"
    desc: "⬻ shortbow +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 1d10]], range increment 60 feet, reload 0) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "No Fight Fair"
    desc: "A big boss goblin fights dirty, slashing at a foe's hamstrings. Whenever the big boss goblin hits an [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] foe, the creature takes a –5-foot status penalty to its speed (–10-foot on a critical hit) until the creature regains any amount of Hit Points. As with all penalties to Speed, this can't reduce a creature's Speed below 5 feet. __Stab it! Stab it! Stab it!__ ⬻ The big boss goblin picks a target they can see within 30 feet and orders any allied goblins to attack. A single [[srd/pf2e/compendium/rules-elements/traits/player-core/goblin|goblin]] with a lower level than the big boss goblin that is adjacent to the target can immediately use their reaction to Strike the target. In addition, until the start of the big boss goblin's next turn, their attacks against that target deal 1 additional damage dice as the big boss goblin leads them."
sourcebook: "_NPC Core_, page 188."
```

```encounter-table
name: Big Boss Goblin
creatures:
  - 1: Big Boss Goblin
```
