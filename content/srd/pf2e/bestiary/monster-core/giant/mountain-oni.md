---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mountain Oni"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/oni
  - pf2e/creature/trait/large
statblock: inline
name: "Mountain Oni"
level: 8
source: "Monster Core"
aon_id: "creature-3121"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3121"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Mountain Oni"
level: "Creature 8"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Oni"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +18, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +18, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +17"
abilityMods: [6, 3, 4, 0, 3, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/club/tetsubo|tetsubo]]_"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +18; __Ref__: +15; __Will__: +14"
hp: 165
health:
  - name: "HP"
    desc: "165; __Weaknesses__ bean panic, [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]] 10"
abilities_mid:
  - name: "Bean Panic"
    desc: "Oni are curiously afraid of beans, especially as the seasons begin to change. If a creature Interacts to throw a handful of beans at the oni, the oni becomes frightened 2. While frightened this way, their weakness to spirit damage is increased by 5. The oni then becomes immune to bean panic for 24 hours."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _tetsubo_ +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core-2/razing|Razing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 2d10+9 bludgeoning"
  - name: "Melee"
    desc: "⬻ jaws +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+9 piercing plus 1d6 persistent bleed"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The mountain oni can take on the appearance of any Medium or Large [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]] creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Thundering Iron"
    desc: "⬺ The oni lifts their tetsubo and brings it down in a deafening peal. They make a tetsubo Strike. On a success, the target takes an additional 1d10 sonic damage. Each creature in a 10-foot emanation around the target, other than the oni, take this damage as well and is pushed 5 feet away from the target. Tetsubo A mountain oni wields a [[srd/pf2e/compendium/equipment/weapons/club/tetsubo|tetsubo]], which appears in _Lost Omens Tian Xia Character Guide_. This [[srd/pf2e/compendium/rules-elements/traits/player-core/uncommon|uncommon]] martial weapon costs 3 gp, deals 1d10 bludgeoning damage, has 3 Bulk, and require two hands to use. Tetsubo are in the club weapon group and have the [[srd/pf2e/compendium/rules-elements/traits/treasure-vault-remastered/razing|razing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shove|shove]], and [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|sweep]] traits. The razing trait means that whenever the weapon damages an object, the object takes an amount of additional damage equal to double the number of weapon damage dice."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 25 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (at will; self only)"
sourcebook: "_Monster Core_, page 252."
```

```encounter-table
name: Mountain Oni
creatures:
  - 1: Mountain Oni
```
