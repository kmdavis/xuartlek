---
noteType: pf2eMonster
aliases: "Fiend Caller"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Fiend Caller"
level: 3
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3609"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Fiend Caller"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Rare"
trait_04: "Unholy"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], Daemonic, [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], Requian"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +15, [[srd/pf2e/compendium/rules-elements/skills/Lore|Fiend Lore]] +18, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +10, [[srd/pf2e/compendium/rules-elements/skills/Lore|Legal Lore]] +18, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +16, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +13, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +12"
abilityMods: [2, 2, 0, 4, 1, 3]
abilities_top:
  - name: "Legal Specialist"
    desc: "For encounters involving contracts and negotiations, the fiend caller is an 8th-level challenge."
  - name: "Items"
    desc: "Dagger, ritual materials, Chalk, ink, parchment, quill, vial of blood)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +9; __Will__: +8"
hp: 35
health:
  - name: "HP"
    desc: "35"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+6 piercing plus 1d4 persistent bleed"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+6 piercing plus 1d4 persistent bleed"
abilities_bot:
  - name: "Fiendish Contract"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Downtime|Downtime]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) The fiend caller spends 1 day of downtime setting up a bargain between a mortal creature and a [[srd/pf2e/compendium/rules-elements/traits/player-core/Fiend|fiend]] the fiend caller knows well. The fiend caller attempts a [[srd/pf2e/compendium/rules-elements/skills/Lore|Legal Lore]] check against the higher of the fiend's Will DC or [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] DC."
  - name: "Success"
    desc: "The mortal party receives one favor from the fiend, or the fiend becomes the mortal's minion for 1d4 days if they're on the same plane. Alternatively, if the GM allows the option, the mortal can receive a bargained contract of the fiend's level or lower."
  - name: "Failure"
    desc: "The fiend caller fails to strike the bargain."
  - name: "Critical Failure"
    desc: "The process fails, and the magical backlash makes the fiend caller [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained 2]]."
  - name: "Fiendish Ritualist"
    desc: "A fiend caller can cast [[srd/pf2e/compendium/spells/rituals/Binding Circle|_binding circle_]] and [[srd/pf2e/compendium/spells/rituals/Commune|_commune_]] to contact [[srd/pf2e/compendium/rules-elements/traits/player-core/Fiend|fiends]] even though the rituals are beyond the normal rank the fiend caller could cast. Furthermore, they can use [[srd/pf2e/compendium/rules-elements/skills/Lore|Legal Lore]] for the primary check when they do so instead of the listed skill."
  - name: "Planar Communique"
    desc: "A fiend caller can cast [[srd/pf2e/compendium/spells/rank-5/Sending|_sending_]] at will as an occult innate spell, but only to target a [[srd/pf2e/compendium/rules-elements/traits/player-core/Fiend|fiend]] they know well. The fiend can be on any plane. Keeping Enemies Close Heroes may have an easier time dealing with a fiend caller peacefully than they would another villain. Fiend callers are willing to work with just about anyone as long as they receive adequate compensation and may even be helpful in stopping more dangerous fiends. But they are opportunistic above all else. Once the transaction is over, they aren't likely to stick around as a friend, and if a better deal comes along, they might void a prior contract."
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 20, attack +12 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Sigil|Sigil]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]], [[srd/pf2e/compendium/spells/cantrips/Void Warp|Void Warp]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Command|Command]], [[srd/pf2e/compendium/spells/rank-1/Fear|Fear]], [[srd/pf2e/compendium/spells/rank-1/Force Barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-1/Grim Tendrils|Grim Tendrils]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Calm|Calm]], [[srd/pf2e/compendium/spells/rank-2/Paranoia|Paranoia]], [[srd/pf2e/compendium/spells/rank-2/Spiritual Armament|Spiritual Armament]]"
  - name: "Rituals"
    desc: "DC 20 - __6th__ [[srd/pf2e/compendium/spells/rituals/Binding Circle|Binding Circle]], Commune"
sourcebook: "_NPC Core_, page 153."
```

```encounter-table
name: Fiend Caller
creatures:
  - 1: Fiend Caller
```
