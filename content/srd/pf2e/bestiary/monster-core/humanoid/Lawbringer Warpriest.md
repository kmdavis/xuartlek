---
noteType: pf2eMonster
aliases: "Lawbringer Warpriest"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/nephilim
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Lawbringer Warpriest"
level: 5
source: "Monster Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3141"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lawbringer Warpriest"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Nephilim"
trait_04: "Uncommon"
modifier: 11
perception:
  - name: "Perception"
    desc: "+11; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +11, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +10, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +12, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +7"
abilityMods: [4, 1, 3, 0, 3, 2]
abilities_top:
  - name: "Items"
    desc: "Crossbow (10 bolts), Greatsword, Half Plate"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +8; __Will__: +12"
hp: 64
health:
  - name: "HP"
    desc: "64"
abilities_mid:
  - name: "Responsive Recovery"
    desc: "⬲"
  - name: "Trigger"
    desc: "One of the lawbringer's allies is reduced to 0 Hit Points"
  - name: "Requirements"
    desc: "The lawbringer has a [[srd/pf2e/compendium/spells/rank-1/Heal|_heal_]] spell prepared"
  - name: "Effect"
    desc: "Before the ally falls [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]] or dies, the lawbringer Strides toward them and casts a 2-action _heal_ spell targeting the ally. The ally remains standing."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greatsword +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 1d12+7 slashing"
  - name: "Ranged"
    desc: "⬻ crossbow +11 (range increment 120 feet, reload 1) __Damage__ 1d8+3 piercing"
abilities_bot:
  - name: "Channel Smite"
    desc: "⬺"
  - name: "Requirements"
    desc: "The lawbringer has a [[srd/pf2e/compendium/spells/rank-1/Heal|_heal_]] or [[srd/pf2e/compendium/spells/rank-1/Harm|_harm_]] spell prepared"
  - name: "Effect"
    desc: "The lawbringer makes a melee Strike and expends a _harm_ or _heal_ spell. On a hit, they cast the 1-action version of the spell to damage the target. The target automatically gets a failure on its save (or a critical failure if the lawbringer's Strike was a critical hit). The spell doesn't have the [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|manipulate]] trait when cast this way."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 20, attack +12 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Divine Lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/Forbidding Ward|Forbidding Ward]], [[srd/pf2e/compendium/spells/cantrips/Guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Harm|Harm]], [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]], [[srd/pf2e/compendium/spells/rank-1/Sure Strike|Sure Strike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Enlarge|Enlarge]], [[srd/pf2e/compendium/spells/rank-1/Harm|Harm]], [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Blindness|Blindness]], [[srd/pf2e/compendium/spells/rank-3/Haste|Haste]] __Domain Spells 1 Focus Point,__ DC 20 - __3rd__ [[srd/pf2e/compendium/spells/focus/Athletic Rush|Athletic Rush]]"
sourcebook: "_Monster Core_, page 267."
```

```encounter-table
name: Lawbringer Warpriest
creatures:
  - 1: Lawbringer Warpriest
```
