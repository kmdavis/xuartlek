---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sniper"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Sniper"
level: 5
source: "NPC Core"
aon_id: "creature-3525"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3525"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Sniper"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11"
abilityMods: [2, 4, 1, 1, 4, 0]
abilities_top:
  - name: "Silencer"
    desc: "A silencer is an uncommon item worth 1 sp. It has light Bulk and can be attached to a firearm in 1 minute; the sniper typically already has one attached before going into combat. The first time a shot is fired through it, the silencer is consumed and reduces the report to a quiet noise. A silencer doesn't work on [[srd/pf2e/compendium/rules-elements/traits/npc-core/scatter|scatter]] firearms."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/firearm/arquebus|Arquebus]] (20 cartridges), Dagger, [[srd/pf2e/compendium/equipment/consumables/silencer|Silencer]] (4)"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +10; __Ref__: +15; __Will__: +11"
hp: 65
health:
  - name: "HP"
    desc: "65"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S +15]]) __Damage__ 1d4+8 piercing"
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed +15]]) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ arquebus +15 (range 150 feet, [[srd/pf2e/compendium/rules-elements/traits/npc-core/concussive|Concussive]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d12]], [[srd/pf2e/compendium/rules-elements/traits/npc-core/kickback|Kickback]], reload 1) __Damage__ 1d8+6 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S +15]]) __Damage__ 1d4+8 piercing"
abilities_bot:
  - name: "Concussive Shot"
    desc: "⬺ The sniper makes an arquebus Strike against a creature within the weapon's first range increment. On a success, the creature must succeed at a DC 21 Fortitude save or be [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 1]] (stunned 2 on a critical failure)."
  - name: "Full Bore"
    desc: "⬺ The sniper makes an arquebus Strike against two creatures that are adjacent to each other. The attack ignores any lesser cover one target provides the other. Roll damage once, and apply it to each creature the sniper hits. This counts as two attacks when determining the sniper's multiple attack penalty."
  - name: "Sniper's Edge"
    desc: "The sniper's ranged Strikes deal 2d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Surprise Attack"
    desc: "All enemy creatures that have not yet acted in combat are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the sniper. Outfitting A Sniper The weapons and armor of a sniper vary depending on how they wish to get the job done. Though this one uses an [[srd/pf2e/compendium/equipment/weapons/firearm/arquebus-weapon-518|arquebus]], many snipers choose to use [[srd/pf2e/compendium/equipment/weapons/bow/longbow|longbows]] if gunpowder isn't an option or if they prefer more subtle means of killing. Snipers usually forgo wearing the colors of their company in favor of hues that best match their surroundings. They usually only carry a small insignia for identification purposes, and their position is usually on a need-to-know basis."
sourcebook: "_NPC Core_, page 90."
```

```encounter-table
name: Sniper
creatures:
  - 1: Sniper
```
