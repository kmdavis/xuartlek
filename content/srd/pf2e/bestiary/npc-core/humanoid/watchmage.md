---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Watchmage"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Watchmage"
level: 5
source: "NPC Core"
aon_id: "creature-3559"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3559"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Watchmage"
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
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +9, [[srd/pf2e/compendium/rules-elements/skills/lore|Legal Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +11"
abilityMods: [1, 4, 2, 4, 1, 0]
abilities_top:
  - name: "Arcane Watch"
    desc: "The watchmage can either [[srd/pf2e/compendium/rules-elements/actions/player-core#Investigate|Investigate]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Search|Search]] while using the [[srd/pf2e/compendium/rules-elements/actions/player-core#Detect Magic|Detect Magic]] exploration activity."
  - name: "Items"
    desc: "Leather Armor, Shortbow (20 arrows), spellbook (contains all prepared spells plus [[srd/pf2e/compendium/spells/rank-3/earthbind|_earthbind_]], [[srd/pf2e/compendium/spells/rank-2/revealing-light|_revealing light_]], [[srd/pf2e/compendium/spells/rank-1/sleep|_sleep_]], and [[srd/pf2e/compendium/spells/rank-1/tailwind|_tailwind_]])"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +12; __Will__: +14"
hp: 70
health:
  - name: "HP"
    desc: "70"
abilities_mid:
  - name: "Counter Escape"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]])"
  - name: "Trigger"
    desc: "A creature Casts a Spell with the [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]] trait or as a reaction"
  - name: "Effect"
    desc: "The watchmage expends a spell slot of the same rank or higher as the trigger creature's spell and attempts to counteract the triggering spell (counteract modifier +11)."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d6+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ shortbow +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 60 feet) __Damage__ 1d6+4 piercing plus 1d6 force"
abilities_bot:
  - name: "Eldritch Arms"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) In a brief ritual that takes 10 minutes, the watchmage chooses a single weapon or unarmed attack through which they can focus their magic. Strikes the watchmage makes with that weapon are magical and deal 1d6 additional force damage."
  - name: "Spellbound Strike"
    desc: "⬽"
  - name: "Requirements"
    desc: "The watchmage is wielding the weapon chosen with Eldritch Arms"
  - name: "Effect"
    desc: "The watchmage Casts a Spell that takes 1 or 2 actions to cast, imbuing that spell into the weapon. The watchmage Strikes with the required weapon. This counts as two attacks for the watchmage's multiple attack penalty. On a hit, the target is also affected by the spell, though the target gets any normal defenses allowed by the spell. If the spell is targeted, it targets the creature that was hit and no one else. If the spell is an area, the target must be in the area. A burst is centered on a corner of the target's square if the target is Medium or smaller, or the corner of a square closest to the creature's center if it's Large or larger. A cone or line emits from a square of the watchmage's choice adjacent to the target."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 20, attack +12 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/ignition|Ignition]], [[srd/pf2e/compendium/spells/cantrips/read-aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/tangle-vine|Tangle Vine]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/command|Command]], [[srd/pf2e/compendium/spells/rank-1/force-barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-1/sure-strike|Sure Strike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/haste|Haste]], [[srd/pf2e/compendium/spells/rank-3/slow|Slow]]"
sourcebook: "_NPC Core_, page 115."
```

```encounter-table
name: Watchmage
creatures:
  - 1: Watchmage
```
