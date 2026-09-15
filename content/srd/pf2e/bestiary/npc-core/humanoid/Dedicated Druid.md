---
noteType: pf2eMonster
aliases: "Dedicated Druid"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Dedicated Druid"
level: 7
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3583"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Dedicated Druid"
level: "Creature 7"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "+15; lifesense (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Wildsong|Wildsong]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +14, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +12, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +17, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +15, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +13, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +17"
abilityMods: [4, 2, 1, 1, 4, 1]
abilities_top:
  - name: "Plant Empathy"
    desc: "The dedicated druid can ask questions of, receive answers from, and use the [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] skill with [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|plants]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/Fungus|fungus]]."
  - name: "Items"
    desc: "Hide Armor, [[srd/pf2e/compendium/spells/rank-2/Revealing Light|_scroll of revealing light_]] (2), _+1 [[srd/pf2e/compendium/equipment/weapons/spear/Spear|spear]]_, Wooden Shield (Hardness 3, HP 12, BT 6)"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +12; __Ref__: +13; __Will__: +15"
hp: 100
health:
  - name: "HP"
    desc: "100"
abilities_mid:
  - name: "Shield Block"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _spear_ +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 1d6+8 piercing"
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _spear_ +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d6+8 piercing"
abilities_bot:
  - name: "Nature's Patient Healing"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]])"
  - name: "Requirement"
    desc: "The dedicated druid is in a natural environment"
  - name: "Effect"
    desc: "The dedicated druid camouflages themself to blend in with the surrounding area, sprouting leaves or covering themself with scree. They gain [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealment]] until the end of their next turn, they can [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]] with a +4 circumstance bonus, and they recover 4d8 Hit Points. If the druid moves or otherwise leaves their space, these benefits end."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 25, attack +17 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/Electric Arc|Electric Arc]], [[srd/pf2e/compendium/spells/cantrips/Ignition|Ignition]], [[srd/pf2e/compendium/spells/cantrips/Know the Way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/Tangle Vine|Tangle Vine]], [[srd/pf2e/compendium/spells/cantrips/Vitality Lash|Vitality Lash]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Air Bubble|Air Bubble]], [[srd/pf2e/compendium/spells/rank-1/Gentle Landing|Gentle Landing]], [[srd/pf2e/compendium/spells/rank-1/Gust of Wind|Gust of Wind]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Entangling Flora|Entangling Flora]], [[srd/pf2e/compendium/spells/rank-2/Mist|Mist]], [[srd/pf2e/compendium/spells/rank-2/One with Plants|One with Plants]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Earthbind|Earthbind]], [[srd/pf2e/compendium/spells/rank-3/Fireball|Fireball]], [[srd/pf2e/compendium/spells/rank-3/Wall of Thorns|Wall of Thorns]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]], [[srd/pf2e/compendium/spells/rank-3/Lightning Bolt|Lightning Bolt]] __Druid Order Spells 1 Focus Point,__ DC 25 - __4th__ [[srd/pf2e/compendium/spells/focus/Cornucopia|Cornucopia]]"
sourcebook: "_NPC Core_, page 134."
```

```encounter-table
name: Dedicated Druid
creatures:
  - 1: Dedicated Druid
```
