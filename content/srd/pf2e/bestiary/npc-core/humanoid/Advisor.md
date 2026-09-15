---
noteType: pf2eMonster
aliases: "Advisor"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Advisor"
level: 5
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3420"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Advisor"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "+14"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +14, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +14, [[srd/pf2e/compendium/rules-elements/skills/Lore|Legal Lore]] +12, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +10, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +12, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +12"
abilityMods: [0, 2, -1, 3, 3, 5]
abilities_top:
  - name: "Placate"
    desc: "An advisor is well versed in soothing agitated nobles. Their calming voice gives them a +2 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] and [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] checks when dealing with members of the nobility."
  - name: "Items"
    desc: "Dagger (2), [[srd/pf2e/compendium/equipment/adventuring-gear/Clothing|fine clothes]], _[[srd/pf2e/compendium/equipment/consumables/Healing Potion|minor healing potion]]_, [[srd/pf2e/compendium/equipment/adventuring-gear/Musical Instrument|small harp]], Whip"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +8; __Ref__: +11; __Will__: +14"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ whip +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|Trip]]) __Damage__ 1d4+4 slashing"
  - name: "Melee"
    desc: "⬻ fist +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Bard Composition Spells"
    desc: "DC 22, 1 Focus Point - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Rallying Anthem|Rallying Anthem]], [[srd/pf2e/compendium/spells/cantrips/Courageous Anthem|Courageous Anthem]], [[srd/pf2e/compendium/spells/cantrips/Uplifting Overture|Uplifting Overture]] - __3rd__ [[srd/pf2e/compendium/spells/focus/Counter Performance|Counter Performance]]"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 22, attack +14 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/Shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/Void Warp|Void Warp]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Command|Command]], [[srd/pf2e/compendium/spells/rank-1/Force Barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-1/Protection|Protection]], [[srd/pf2e/compendium/spells/rank-1/Soothe|Soothe]] (3 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Augury|Augury]], [[srd/pf2e/compendium/spells/rank-2/Cleanse Affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-1/Soothe|Soothe]], [[srd/pf2e/compendium/spells/rank-2/Stupefy|Stupefy]] (3 slots) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Mind Reading|Mind Reading]], [[srd/pf2e/compendium/spells/rank-1/Soothe|Soothe]], [[srd/pf2e/compendium/spells/rank-3/Ring of Truth|Ring of Truth]] (2 slots)"
sourcebook: "_NPC Core_, page 14."
```

```encounter-table
name: Advisor
creatures:
  - 1: Advisor
```
