---
obsidianUIMode: preview
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
aon_id: "creature-3590"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3590"
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
    desc: "Perception +10"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +8, [[srd/pf2e/compendium/rules-elements/skills/lore|Astronomy Lore]] +12, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +8"
abilityMods: [0, 1, 2, 4, 3, 0]
abilities_top:
  - name: "Living Sextant"
    desc: "If the astronomer is able to see the night sky, they can [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Direction|Sense Direction]] using [[srd/pf2e/compendium/rules-elements/skills/lore|Astronomy Lore]]."
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
    desc: "A creature within 30 feet Casts a Spell or uses an ability with the [[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|fortune]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/misfortune|misfortune]] trait"
  - name: "Effect"
    desc: "The astronomer's rejection of such fantasy becomes manifest. The astronomer attempts to counteract the triggering effect with a counteract modifier of +9 and a counteract rank of 1."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ staff +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d8]]) __Damage__ 1d4+4 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 17, attack +9 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/read-aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/sigil|Sigil]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-projectile|Telekinetic Projectile]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/alarm|Alarm]], [[srd/pf2e/compendium/spells/rank-1/gentle-landing|Gentle Landing]], [[srd/pf2e/compendium/spells/rank-1/phantasmal-minion|Phantasmal Minion]], [[srd/pf2e/compendium/spells/rank-1/sleep|Sleep]]"
sourcebook: "_NPC Core_, page 139."
```

```encounter-table
name: Astronomer
creatures:
  - 1: Astronomer
```
