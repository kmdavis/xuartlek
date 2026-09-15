---
noteType: pf2eMonster
aliases: "Chronicler"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Chronicler"
level: 3
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3470"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Chronicler"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +10, [[srd/pf2e/compendium/rules-elements/skills/Lore|Scribing Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +9, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +7, [[srd/pf2e/compendium/rules-elements/skills/Lore|Lore]] +10"
abilityMods: [2, 2, 1, 3, 4, 0]
abilities_top:
  - name: "Items"
    desc: "Crossbow (20 bolts), Dagger, journal, Leather Armor, [[srd/pf2e/compendium/equipment/adventuring-gear/Map|maps]], [[srd/pf2e/compendium/spells/rank-2/Acid Grip|_scroll of acid grip_]], [[srd/pf2e/compendium/spells/rank-1/Heal|_scroll of heal_]], Staff"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +9; __Will__: +10"
hp: 45
health:
  - name: "HP"
    desc: "45"
abilities_mid:
  - name: "Live to Tell the Tale"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The chronicler would gain the [[srd/pf2e/compendium/rules-elements/Conditions#Dying|dying]] condition"
  - name: "Effect"
    desc: "The chronicler instead falls [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]] for 1d4 hours or until they regain 1 Hit Point."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+5 piercing"
  - name: "Melee"
    desc: "⬻ staff +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand d8]]) __Damage__ 1d4+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +7 (range increment 120 feet, reload 1) __Damage__ 1d8+3 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+5 piercing"
abilities_bot:
  - name: "Scroll Mastery"
    desc: "The chronicler can activate any scroll of a 2nd-rank spell or lower, regardless of its magical tradition."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 20, attack +12 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/Know the Way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Sigil|Sigil]], [[srd/pf2e/compendium/spells/cantrips/Tangle Vine|Tangle Vine]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Fleet Step|Fleet Step]], [[srd/pf2e/compendium/spells/rank-1/Tailwind|Tailwind]], [[srd/pf2e/compendium/spells/rank-1/Vanishing Tracks|Vanishing Tracks]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Entangling Flora|Entangling Flora]], [[srd/pf2e/compendium/spells/rank-2/Floating Flame|Floating Flame]]"
sourcebook: "_NPC Core_, page 54."
```

```encounter-table
name: Chronicler
creatures:
  - 1: Chronicler
```
