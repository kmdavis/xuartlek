---
noteType: pf2eMonster
aliases: "Shae"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/medium
statblock: inline
name: "Shae"
level: 4
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4542"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Shae"
level: "Creature 4"
size: "Medium"
trait_01: "Shadow"
modifier: 10
perception:
  - name: "Perception"
    desc: "+10; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]], Shae, [[srd/pf2e/compendium/rules-elements/Languages#Sussuran|Sussuran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +9, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +11, [[srd/pf2e/compendium/rules-elements/skills/Lore|Netherworld Lore]] +11, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +13"
abilityMods: [3, 5, 1, 3, 2, 3]
abilities_top:
  - name: "Shadow Shift"
    desc: "Being made partially of shadow themselves, shae are [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] in [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Perception and Detection#Dim Light|dim light]] or [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Perception and Detection#Darkness|darkness]] even to creatures that can see clearly in those light levels."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/knife/Dagger|Dagger]] (5)"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +11; __Will__: +10"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ precision; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]] 5"
abilities_mid:
  - name: "Counterattack"
    desc: "⬲"
  - name: "Trigger"
    desc: "The shae is targeted by an attack from an adjacent creature that misses due to the shae being [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]]"
  - name: "Requirements"
    desc: "The shae is aware of the attack"
  - name: "Effect"
    desc: "The shae makes a melee Strike against the attacker."
  - name: "Slip"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature moves adjacent to the shae"
  - name: "Effect"
    desc: "The shae teleports to an unoccupied space adjacent to another creature they can see within 30 feet."
speed: "25 feet, fly 35 feet; swift steps, tenebral form"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+5 piercing and 1d6 cold"
  - name: "Ranged"
    desc: "⬻ dagger +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+5 piercing and 1d6 cold"
abilities_bot:
  - name: "Bide"
    desc: "⬺ The shae prepares to take action against their foes, watching their opponent and waiting for the right opportunity to respond. The shae gains a second reaction until the start of their next turn, though they still can't use more than one reaction on the same triggering action."
  - name: "Swift Steps"
    desc: "The shae's movement doesn't trigger reactions."
  - name: "Tenebral Form"
    desc: "The shae can [[srd/pf2e/compendium/spells/rank-4/Fly|_Fly_]] at full Speed in vapor form. Children Of Shadow Though rare, shae occasionally engage in relationships with mortals, resulting in children born as fetchlings. Though shae maintain a cool superiority over their mortal children, fetchlings who join a shae's cult are placed in positions of authority over other mortals and receive blatantly preferential treatment."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 21 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Void Warp|Void Warp]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Vapor Form|Vapor Form]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]] (self only, to [[srd/pf2e/compendium/gm/Planes#The Netherworld|Netherworld]] or [[srd/pf2e/compendium/gm/Planes#The Universe|Universe]] only)"
sourcebook: "_Monster Core 2_, page 284."
```

```encounter-table
name: Shae
creatures:
  - 1: Shae
```
