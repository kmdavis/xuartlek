---
noteType: pf2eMonster
aliases: "Hryngar Bombardier"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/dwarf
  - pf2e/creature/trait/hryngar
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/duergar
statblock: inline
name: "Hryngar Bombardier"
level: 1
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3062"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hryngar Bombardier"
level: "Creature 1"
size: "Medium"
trait_01: "Dwarf"
trait_02: "Hryngar"
trait_03: "Humanoid"
trait_04: "Duergar"
modifier: 4
perception:
  - name: "Perception"
    desc: "+4; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Dwarven|Dwarven]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +6, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +6, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +6, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +4"
abilityMods: [1, 3, 2, 3, 1, -1]
abilities_top:
  - name: "Alchemical Grenades"
    desc: "A hryngar bombardier carries 6 alchemical grenades that deal either acid, cold, or fire damage plus 1 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent damage]] and 1 [[srd/pf2e/compendium/rules-elements/traits/gm-core/Splash|splash]] damage of the same type (typically two of each). The bombardier replenishes these grenades each day using easily collected materials."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/Alchemist's Toolkit|Alchemist's Toolkit]], studded leather, warhammer"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +7; __Ref__: +8; __Will__: +4 +2 status to all saves vs. magic"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Light Blindness"
    desc: ""
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ warhammer +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Shove|Shove]]) __Damage__ 1d8+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ alchemical grenade +8 (range increment 20 feet, [[srd/pf2e/compendium/rules-elements/traits/gm-core/Splash|Splash]]) __Damage__ 1d6 acid, cold, or fire plus 1 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent damage]] and 1 [[srd/pf2e/compendium/rules-elements/traits/gm-core/Splash|splash]] damage of the same type"
abilities_bot:
  - name: "Quick Bombardier"
    desc: "⬻ The hryngar bombardier draws an alchemical grenade with an Interact action and throws it as a ranged Strike."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Sigil|Sigil]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Blood Vendetta|Blood Vendetta]], [[srd/pf2e/compendium/spells/rank-2/Paranoia|Paranoia]]"
sourcebook: "_Monster Core_, page 202."
```

```encounter-table
name: Hryngar Bombardier
creatures:
  - 1: Hryngar Bombardier
```
