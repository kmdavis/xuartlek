---
obsidianUIMode: preview
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
aon_id: "creature-3141"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3141"
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
    desc: "Perception +11; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +11, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +10, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +12, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +7"
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
    desc: "The lawbringer has a [[srd/pf2e/compendium/spells/rank-1/heal|_heal_]] spell prepared"
  - name: "Effect"
    desc: "Before the ally falls [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] or dies, the lawbringer Strides toward them and casts a 2-action _heal_ spell targeting the ally. The ally remains standing."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greatsword +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 1d12+7 slashing"
  - name: "Ranged"
    desc: "⬻ crossbow +11 (range increment 120 feet, reload 1) __Damage__ 1d8+3 piercing"
abilities_bot:
  - name: "Channel Smite"
    desc: "⬺"
  - name: "Requirements"
    desc: "The lawbringer has a [[srd/pf2e/compendium/spells/rank-1/heal|_heal_]] or [[srd/pf2e/compendium/spells/rank-1/harm|_harm_]] spell prepared"
  - name: "Effect"
    desc: "The lawbringer makes a melee Strike and expends a _harm_ or _heal_ spell. On a hit, they cast the 1-action version of the spell to damage the target. The target automatically gets a failure on its save (or a critical failure if the lawbringer's Strike was a critical hit). The spell doesn't have the [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]] trait when cast this way."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 20, attack +12 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/divine-lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/forbidding-ward|Forbidding Ward]], [[srd/pf2e/compendium/spells/cantrips/guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/light|Light]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/harm|Harm]], [[srd/pf2e/compendium/spells/rank-1/heal|Heal]], [[srd/pf2e/compendium/spells/rank-1/sure-strike|Sure Strike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/enlarge|Enlarge]], [[srd/pf2e/compendium/spells/rank-1/harm|Harm]], [[srd/pf2e/compendium/spells/rank-1/heal|Heal]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/blindness|Blindness]], [[srd/pf2e/compendium/spells/rank-3/haste|Haste]] __Domain Spells 1 Focus Point,__ DC 20 - __3rd__ [[srd/pf2e/compendium/spells/focus/athletic-rush|Athletic Rush]]"
sourcebook: "_Monster Core_, page 267."
```

```encounter-table
name: Lawbringer Warpriest
creatures:
  - 1: Lawbringer Warpriest
```
