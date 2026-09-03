---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Demolitionist"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Demolitionist"
level: 4
source: "NPC Core"
aon_id: "creature-3461"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3461"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Demolitionist"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +12, [[srd/pf2e/compendium/rules-elements/skills/lore|Explosive Lore]] +14, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +10, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +11"
abilityMods: [1, 3, 3, 4, 0, 0]
abilities_top:
  - name: "Items"
    desc: "bag of explosives, Leather Armor, Light Mace"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +11; __Ref__: +13; __Will__: +6"
hp: 60
health:
  - name: "HP"
    desc: "60; __Resistances__ fire 5"
abilities_mid:
  - name: "Explosive Demise"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]) When the demolitionist is reduced to 0 Hit Points while they have any explosives still in their bag, the remaining explosives detonate, unleashing an explosion of fire upon all creatures in a 30-foot emanation. Each creature in the area takes 3d6 fire damage with a DC 19 Reflex save."
  - name: "Replenish Explosives"
    desc: "The demolitionist can replenish their stock of explosives with 4 hours of downtime."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ light mace +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]]) __Damage__ 1d4+7 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+7 bludgeoning"
abilities_bot:
  - name: "Plant Mine"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The demolitionist plants a mine in an adjacent square. If a creature moves onto a space with a mine, the mine explodes. This deals 3d8 fire damage to the creature with a DC 21 basic Reflex save. The demolitionist can use 2 actions to Plant a Mine to hide the mine, granting it a [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] DC of 21. Creatures that didn't see the mine as it was planted must actively search for it (using the [[srd/pf2e/compendium/rules-elements/actions/player-core#Search|Search]] activity while exploring or the [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] action in an encounter)."
  - name: "Toss Dynamite"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The demolitionist quickly throws a stick of dynamite up to 20 feet away that explodes in 5-foot burst. Creatures within the burst take 4d4 fire damage with a DC 21 basic Reflex save."
  - name: "Wall Charge"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) the demolitionist plants a powerful wall charge on a flat surface such as a door or wall. Once the charge is planted, it explodes after 1 minute, dealing 60 fire damage to the surface and ignoring up to 15 of the surface's Hardness. The explosive also deals 5d6 fire damage to creatures within 30 feet of the explosive with a basic Reflex save DC 25."
sourcebook: "_NPC Core_, page 45."
```

```encounter-table
name: Demolitionist
creatures:
  - 1: Demolitionist
```
