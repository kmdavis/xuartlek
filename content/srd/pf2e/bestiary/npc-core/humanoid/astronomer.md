---
noteType: pf2eMonster
aliases: "Astronomer"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Astronomer"
level: 2
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3590"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Astronomer"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "+10"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +8, [[srd/pf2e/compendium/rules-elements/skills/Lore|Astronomy Lore]] +12, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +8"
abilityMods: [0, 1, 2, 4, 3, 0]
abilities_top:
  - name: "Living Sextant"
    desc: "If the astronomer is able to see the night sky, they can [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Direction|Sense Direction]] using [[srd/pf2e/compendium/rules-elements/skills/Lore|Astronomy Lore]]."
  - name: "Items"
    desc: "Astrolabe, spellbook, Staff"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +5; __Will__: +9"
hp: 23
health:
  - name: "HP"
    desc: "23"
abilities_mid:
  - name: "Reject Myth"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 30 feet Casts a Spell or uses an ability with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Fortune|fortune]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Misfortune|misfortune]] trait"
  - name: "Effect"
    desc: "The astronomer's rejection of such fantasy becomes manifest. The astronomer attempts to counteract the triggering effect with a counteract modifier of +9 and a counteract rank of 1."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ staff +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand d8]]) __Damage__ 1d4+4 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 17, attack +9 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/Sigil|Sigil]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Projectile|Telekinetic Projectile]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Alarm|Alarm]], [[srd/pf2e/compendium/spells/rank-1/Gentle Landing|Gentle Landing]], [[srd/pf2e/compendium/spells/rank-1/Phantasmal Minion|Phantasmal Minion]], [[srd/pf2e/compendium/spells/rank-1/Sleep|Sleep]]"
sourcebook: "_NPC Core_, page 139."
```

```encounter-table
name: Astronomer
creatures:
  - 1: Astronomer
```
