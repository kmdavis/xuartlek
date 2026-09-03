---
obsidianUIMode: preview
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
aon_id: "creature-3609"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3609"
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
    desc: "Perception +8"
languages: "Chthonian, Common, Daemonic, Diabolic, Requian"
skills:
  - name: "Skills"
    desc: "Deception +10, Diplomacy +15, Fiend Lore +18, Intimidation +10, Legal Lore +18, Occultism +16, Religion +13, Society +12"
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
    desc: "⬻ dagger +9 (Agile, Finesse, versatile S) __Damage__ 1d4+6 piercing plus 1d4 persistent bleed"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +9 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+6 piercing plus 1d4 persistent bleed"
abilities_bot:
  - name: "Fiendish Contract"
    desc: "(Downtime, Occult) The fiend caller spends 1 day of downtime setting up a bargain between a mortal creature and a fiend the fiend caller knows well. The fiend caller attempts a Legal Lore check against the higher of the fiend's Will DC or Diplomacy DC."
  - name: "Success"
    desc: "The mortal party receives one favor from the fiend, or the fiend becomes the mortal's minion for 1d4 days if they're on the same plane. Alternatively, if the GM allows the option, the mortal can receive a bargained contract of the fiend's level or lower."
  - name: "Failure"
    desc: "The fiend caller fails to strike the bargain."
  - name: "Critical Failure"
    desc: "The process fails, and the magical backlash makes the fiend caller drained 2."
  - name: "Fiendish Ritualist"
    desc: "A fiend caller can cast _binding circle_ and _commune_ to contact fiends even though the rituals are beyond the normal rank the fiend caller could cast. Furthermore, they can use Legal Lore for the primary check when they do so instead of the listed skill."
  - name: "Planar Communique"
    desc: "A fiend caller can cast _sending_ at will as an occult innate spell, but only to target a fiend they know well. The fiend can be on any plane. Keeping Enemies Close Heroes may have an easier time dealing with a fiend caller peacefully than they would another villain. Fiend callers are willing to work with just about anyone as long as they receive adequate compensation and may even be helpful in stopping more dangerous fiends. But they are opportunistic above all else. Once the transaction is over, they aren't likely to stick around as a friend, and if a better deal comes along, they might void a prior contract."
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 20, attack +12 - __Cantrips (2nd)__ Detect Magic, Message, Sigil, Telekinetic Hand, Void Warp - __1st__ Command, Fear, Force Barrage, Grim Tendrils - __2nd__ Calm, Paranoia, Spiritual Armament"
  - name: "Rituals"
    desc: "DC 20 - __6th__ Binding Circle, Commune"
sourcebook: "_NPC Core_, page 153."
```

```encounter-table
name: Fiend Caller
creatures:
  - 1: Fiend Caller
```
