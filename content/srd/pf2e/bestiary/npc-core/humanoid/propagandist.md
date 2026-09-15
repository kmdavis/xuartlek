---
noteType: pf2eMonster
aliases: "Propagandist"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Propagandist"
level: 3
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3610"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Propagandist"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "+10; (12 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +11, [[srd/pf2e/compendium/rules-elements/skills/Lore|Legal Lore]] +8, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +10, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +10"
abilityMods: [0, 2, 1, 1, 3, 4]
abilities_top:
  - name: "Nuanced Spin"
    desc: "The propagandist phrases everything loosely and vaguely enough that, though it's always misleading, none of it is false. The propagandist can use [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] instead of [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Create a Diversion|Create a Diversion]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Feint|Feint]], and instead of [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Coerce|Coerce]]. A creature attempting to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]] against the propagandist gets a result one degree of success worse than they rolled."
  - name: "Items"
    desc: "Dagger (3), [[srd/pf2e/compendium/equipment/adventuring-gear/Musical Instrument|lute]], Shortsword, Writing Set"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +9; __Will__: +12"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d6+4 piercing"
  - name: "Melee"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+4 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Bard Composition Spells"
    desc: "DC 21, 2 Focus Points - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Courageous Anthem|Courageous Anthem]], [[srd/pf2e/compendium/spells/cantrips/Rallying Anthem|Rallying Anthem]] - __2nd__ [[srd/pf2e/compendium/spells/focus/Hymn of Healing|Hymn of Healing]], [[srd/pf2e/compendium/spells/focus/Lingering Composition|Lingering Composition]]"
  - name: "No Hard Feelings"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotional]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) The propagandist offers amnesty and other benefits to all who choose to join them. All enemies who can hear the propagandist must attempt a DC 19 Will save. If any of the propagandist's allies is currently benefiting from one of the propagandist's bard composition spells, any enemy who is aware of that takes a –2 circumstance penalty to the save."
  - name: "Critical Success"
    desc: "The creature sees through the propagandist's pitch and is temporarily immune for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature's conviction stumbles. Until the end of its next turn, the creature must succeed at a DC 5 flat check to target the propagandist with a hostile action."
  - name: "Critical Failure"
    desc: "The creature finds the propagandist's offer too good to pass up, switching sides in the combat and instantly gaining any benefits the propagandist is currently granting their allies. At the end of each of its turns, the creature can attempt another DC 19 Will save to snap out of it and rejoin their allies."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 21, attack +13 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Bullhorn|Bullhorn]], [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Haunting Hymn|Haunting Hymn]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Summon Instrument|Summon Instrument]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Concordant Choir|Concordant Choir]], [[srd/pf2e/compendium/spells/rank-1/Fear|Fear]], [[srd/pf2e/compendium/spells/rank-1/Sanctuary|Sanctuary]] (3 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Blistering Invective|Blistering Invective]], [[srd/pf2e/compendium/spells/rank-2/Paranoia|Paranoia]] (2 slots)"
sourcebook: "_NPC Core_, page 154."
```

```encounter-table
name: Propagandist
creatures:
  - 1: Propagandist
```
