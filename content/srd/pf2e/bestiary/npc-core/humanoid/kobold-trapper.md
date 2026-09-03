---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kobold Trapper"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kobold
  - pf2e/creature/trait/small
statblock: inline
name: "Kobold Trapper"
level: 2
source: "NPC Core"
aon_id: "creature-3654"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3654"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Kobold Trapper"
level: "Creature 2"
size: "Small"
trait_01: "Humanoid"
trait_02: "Kobold"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; (9 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] for [[srd/pf2e/compendium/rules-elements/traits/player-core/trap|traps]]) darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +7"
abilityMods: [1, 3, 1, 3, 2, 0]
abilities_top:
  - name: "Booby-Trapped"
    desc: "A kobold trapper protects items in their backpack with a booby trap. This booby trap requires a successful DC 18 Perception check to notice, and two successful DC 15 [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] checks to disable. Accessing the backpack without disabling the trap destroys its contents, and splinters explode in a 10-foot burst centered on the backpack, dealing 3d6 piercing damage (DC 15 basic Reflex save)."
  - name: "Items"
    desc: "Backpack, Crossbow (20 bolts), formula book (containing formulas for three 1st- or 2nd-level [[srd/pf2e/compendium/rules-elements/traits/player-core-2/snare|snares]]), Leather Armor, [[srd/pf2e/compendium/equipment/weapons/hammer/light-hammer|Light Hammer]]"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +5; __Ref__: +11; __Will__: +8 +1 circumstance to all defenses vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/trap|traps]]"
hp: 32
health:
  - name: "HP"
    desc: "32"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ light hammer +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d6+1 bludgeoning"
  - name: "Melee"
    desc: "⬻ claw +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+1 slashing"
  - name: "Ranged"
    desc: "⬻ crossbow +9 (range increment 120 feet, reload 1) __Damage__ 1d8 piercing"
  - name: "Ranged"
    desc: "⬻ light hammer +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d6+1 bludgeoning"
abilities_bot:
  - name: "Construct Trap"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The kobold trapper creates a rudimentary trap on a surface in an adjacent square. The trap activates the next time a creature moves adjacent to it. The creature takes 2d6 bludgeoning, piercing, or slashing damage (determined by the trapper when the trap is constructed) with a DC 18 basic Reflex save. On a failure, the creature also takes a –5 status penalty to all Speeds for 1 minute. The trap is destroyed when activated or after 8 hours, whichever comes first. A trapper typically carries enough raw materials to make six traps each day."
sourcebook: "_NPC Core_, page 198."
```

```encounter-table
name: Kobold Trapper
creatures:
  - 1: Kobold Trapper
```
