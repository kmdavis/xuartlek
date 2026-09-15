---
noteType: pf2eMonster
aliases: "Troubadour"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Troubadour"
level: 3
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3575"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Troubadour"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "+9"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +9, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +9, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +13, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +7, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +7, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/Lore|Storytelling Lore]] +9"
abilityMods: [0, 3, 0, 2, 1, 4]
abilities_top:
  - name: "Bardic Lore"
    desc: "The troubadour can [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] on any subject with a +7 modifier."
  - name: "Items"
    desc: "Leather Armor, [[srd/pf2e/compendium/equipment/adventuring-gear/Musical Instrument|lute]], poetry book, Rapier"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +11; __Will__: +9"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ rapier +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly 1d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]]) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Bard Composition Spells"
    desc: "DC 20, 2 Focus Points - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Courageous Anthem|Courageous Anthem]] - __2nd__ [[srd/pf2e/compendium/spells/focus/Counter Performance|Counter Performance]], [[srd/pf2e/compendium/spells/focus/Lingering Composition|Lingering Composition]]"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 20, attack +12 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]], [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|Illusory Disguise]], [[srd/pf2e/compendium/spells/rank-1/Soothe|Soothe]], [[srd/pf2e/compendium/spells/rank-1/Ventriloquism|Ventriloquism]] (3 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Calm|Calm]], [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]], [[srd/pf2e/compendium/spells/rank-2/Embed Message|Embed Message]] (2 slots)"
sourcebook: "_NPC Core_, page 127."
```

```encounter-table
name: Troubadour
creatures:
  - 1: Troubadour
```
