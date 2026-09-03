---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wealthy Vigilante"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Wealthy Vigilante"
level: 8
source: "NPC Core"
aon_id: "creature-3619"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3619"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Wealthy Vigilante"
level: "Creature 8"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +16, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +17, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17"
abilityMods: [4, 2, 1, 3, 1, 3]
abilities_top:
  - name: "Custom Gear"
    desc: "The wealthy vigilante's support team has spent years tailoring and tuning the vigilante's equipment. Anyone but the vigilante attempting to use the items takes the same drawbacks they would if they were [[srd/pf2e/books/player-core/chapter-6-equipment/shoddy-items|shoddy items]]. These peculiarities make the items have no value if sold."
  - name: "Talisman Prepper"
    desc: "The vigilante goes on patrol with six talismans of 6th level or lower. The typical set includes a [[srd/pf2e/compendium/equipment/consumables/fear-gem|_fear gem_]] and [[srd/pf2e/compendium/equipment/consumables/emerald-grasshopper-greater|_emerald grasshopper_]] affixed, with a [[srd/pf2e/compendium/equipment/consumables/dragon-turtle-scale-greater|_dragon turtle scale_]], [[srd/pf2e/compendium/equipment/consumables/effervescent-ampoule|_effervescent ampoule_]], [[srd/pf2e/compendium/equipment/consumables/feather-step-stone|_feather step stone_]], and [[srd/pf2e/compendium/equipment/consumables/iron-cube|_iron cube_]] in storage."
  - name: "Items"
    desc: "_crimefighting pouches_ (function as [[srd/pf2e/compendium/equipment/worn-items/sleeves-of-storage-greater|_sleeves of storage_]]), _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/firearm/flintlock-musket-weapon-521|flintlock musket]]_ (10 rounds), [[srd/pf2e/compendium/equipment/worn-items/lifting-belt|_lifting belt_]], _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/sword/longsword|longsword]]_, [[srd/pf2e/compendium/equipment/consumables/healing-potion-major|_moderate healing potion_]], Studded Leather Armor"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +12; __Ref__: +17; __Will__: +15"
hp: 120
health:
  - name: "HP"
    desc: "120"
abilities_mid:
  - name: "Quick Replace"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]])"
  - name: "Trigger"
    desc: "The wealthy vigilante Activates one of their affixed talismans"
  - name: "Requirements"
    desc: "The wealthy vigilante has a hand free"
  - name: "Effect"
    desc: "As soon as one of their talismans burns out, the wealthy vigilante pulls another from their _crimefighting pouches_ and deftly [[srd/pf2e/compendium/rules-elements/actions/gm-core-co-tak#Affix a Talisman|Affixes]] it to replace the used talisman."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longsword_ +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 2d8+10 slashing"
  - name: "Melee"
    desc: "⬻ fist +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _flintlock musket_ +17 ([[srd/pf2e/compendium/rules-elements/traits/npc-core/concussive|Concussive]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 70 feet, reload 1) __Damage__ 2d6+6 piercing"
abilities_bot:
  - name: "Calculated Strike"
    desc: "⬺ The wealthy vigilante makes a melee Strike. If the Strike hits, the vigilante can then [[srd/pf2e/compendium/rules-elements/actions/player-core#Shove|Shove]] the target. This Shove uses the same multiple attack penalty as the Strike and doesn't count toward the vigilante's multiple attack penalty, but the vigilante must Stride after the pushed creature. If the Strike misses, the vigilante can Step up to three times, each of which must take it further from the target. The vigilante can [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]] if, after the Steps, they have cover or [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealment]] from the target. Vigilante's Arsenal A wealthy vigilante's threat (and flexibility) as a combatant comes from their ability to use the right gear at the right time. A canny vigilante enters combat with the best consumables readied and talismans affixed for the type of encounter to come, along with a plan for what to use next. As a GM, you can swap out the wealthy vigilante's talismans over multiple engagements to make them appear much more threatening than they are. Keep the PCs guessing!"
sourcebook: "_NPC Core_, page 160."
```

```encounter-table
name: Wealthy Vigilante
creatures:
  - 1: Wealthy Vigilante
```
