---
noteType: pf2eMonster
aliases: "Bone Mother"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/ratfolk
  - pf2e/creature/trait/small
statblock: inline
name: "Bone Mother"
level: 6
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3669"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Bone Mother"
level: "Creature 6"
size: "Small"
trait_01: "Humanoid"
trait_02: "Ratfolk"
modifier: 13
perception:
  - name: "Perception"
    desc: "+13; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], Requian, [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]], [[srd/pf2e/compendium/rules-elements/Languages#Ysoki|Ysoki]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +14, [[srd/pf2e/compendium/rules-elements/skills/Lore|Fortune-Telling Lore]] +16, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +13, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +16, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +14, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +13, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +12"
abilityMods: [0, 3, 0, 2, 3, 4]
abilities_top:
  - name: "Items"
    desc: "bones for fortune telling, _+1 [[srd/pf2e/compendium/equipment/weapons/knife/Dagger|dagger]]_"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +13; __Will__: +15"
hp: 80
health:
  - name: "HP"
    desc: "80"
abilities_mid:
  - name: "Rattling Bones"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]])"
  - name: "Trigger"
    desc: "The bone mother or another ratfolk in their square takes damage from a melee Strike"
  - name: "Effect"
    desc: "Spirits from the bones emerge to deal 2d6 spirit damage to the attacker with a DC 24 basic Will save."
speed: "25 feet; swarming"
attacks:
  - name: "Melee"
    desc: "⬻ _dagger_ +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+6 piercing plus 1d10 spirit"
  - name: "Melee"
    desc: "⬻ jaws +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]]) __Damage__ 1d4+6 piercing plus 1d10 spirit"
  - name: "Ranged"
    desc: "⬻ _dagger_ +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+6 piercing plus 1d10 spirit"
abilities_bot:
  - name: "Swarming"
    desc: "A ysoki can end their movement in the same square as an ally that also has this ability. Only two such creatures can share the same space."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 24, attack +16 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Projectile|Telekinetic Projectile]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Bless|Bless]], [[srd/pf2e/compendium/spells/rank-1/Command|Command]], [[srd/pf2e/compendium/spells/rank-1/Mindlink|Mindlink]], [[srd/pf2e/compendium/spells/rank-1/Sanctuary|Sanctuary]] (4 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Augury|Augury]], [[srd/pf2e/compendium/spells/rank-2/Cleanse Affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-2/Translate|Translate]] (4 slots) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Enthrall|Enthrall]], [[srd/pf2e/compendium/spells/rank-3/Haste|Haste]], [[srd/pf2e/compendium/spells/rank-3/Paralyze|Paralyze]], [[srd/pf2e/compendium/spells/rank-3/Ring of Truth|Ring of Truth]] (4 slots)"
sourcebook: "_NPC Core_, page 211."
```

```encounter-table
name: Bone Mother
creatures:
  - 1: Bone Mother
```
