---
noteType: pf2eMonster
aliases: "Tree Singer"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Tree Singer"
level: 13
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3585"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tree Singer"
level: "Creature 13"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 22
perception:
  - name: "Perception"
    desc: "+22"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Wildsong|Wildsong]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +25, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +23, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +26, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +27, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +22"
abilityMods: [4, 3, 1, 2, 3, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/Resilient|resilient]] [[srd/pf2e/compendium/equipment/Armor#Leather Armor|leather armor]]_, _+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/spear/Longspear|longspear]]_, _+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/bow/Composite Longbow|composite longbow]]_"
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +23; __Ref__: +21; __Will__: +25"
hp: 220
health:
  - name: "HP"
    desc: "220"
abilities_mid:
  - name: "Bloodthirsty Plants"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]])"
  - name: "Trigger"
    desc: "An enemy in the tree singer's Verdant Aria aura (see below) attacks one of the tree singer's allies"
  - name: "Effect"
    desc: "Vines and branches to lash out at the attacker, dealing 3d6 piercing damage."
  - name: "Plant Empathy"
    desc: "The tree singer can ask questions of, receive answers from, and use the [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] skill with [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|plants]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/Fungus|fungus]]."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longspear_ +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d8+10 piercing plus 2d10 sonic"
  - name: "Melee"
    desc: "⬻ fist +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning plus 2d10 sonic"
  - name: "Ranged"
    desc: "⬻ _composite longbow_ +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], range increment 100 feet, reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/Volley|volley 30 feet]]) __Damage__ 2d8+8 piercing plus 1d10 sonic"
abilities_bot:
  - name: "Druid Order Spells"
    desc: "DC 33, 1 Focus Point - __7th__ [[srd/pf2e/compendium/spells/focus/Cornucopia|Cornucopia]]"
  - name: "Verdant Aria"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|Aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|Plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Wood|Wood]]) The tree singer raises their voice in a haunting melody, creating an aura in a 30-foot emanation. Plants in the aura seem to come to life, swaying and rustling in response to the music. The tree singer's allies in the aura gain a +2 status bonus to AC and saving throws as the foliage around them shields and defends them from harm. The aura lasts until the end of the tree singer's next turn but can be Sustained. It can be Sustained even if the tree singer is [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|polymorphed]]. The effect ends early if the tree singer stops singing."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 33, attack +25 - __Cantrips (7th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/Stabilize|Stabilize]], [[srd/pf2e/compendium/spells/cantrips/Tangle Vine|Tangle Vine]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Gentle Landing|Gentle Landing]] (×2), [[srd/pf2e/compendium/spells/rank-1/Ventriloquism|Ventriloquism]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Entangling Flora|Entangling Flora]], [[srd/pf2e/compendium/spells/rank-2/One with Plants|One with Plants]] (×2) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Earthbind|Earthbind]] (×2), [[srd/pf2e/compendium/spells/rank-3/Slow|Slow]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/Oaken Resilience|Oaken Resilience]], [[srd/pf2e/compendium/spells/rank-2/Resist Energy|Resist Energy]], [[srd/pf2e/compendium/spells/rank-4/Vapor Form|Vapor Form]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Elemental Form|Elemental Form]] (wood only), [[srd/pf2e/compendium/spells/rank-5/Nature's Pathway|Nature's Pathway]], [[srd/pf2e/compendium/spells/rank-5/Plant Form|Plant Form]] - __6th__ [[srd/pf2e/compendium/spells/rank-5/Plant Form|Plant Form]], [[srd/pf2e/compendium/spells/rank-6/Tangling Creepers|Tangling Creepers]], [[srd/pf2e/compendium/spells/rank-3/Wall of Thorns|Wall of Thorns]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/Regenerate|Regenerate]], [[srd/pf2e/compendium/spells/rank-6/Tree of Seasons|Tree of Seasons]]"
sourcebook: "_NPC Core_, page 135."
```

```encounter-table
name: Tree Singer
creatures:
  - 1: Tree Singer
```
