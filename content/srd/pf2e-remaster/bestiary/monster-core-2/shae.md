---
obsidianUIMode: preview
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
aon_id: "creature-4542"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4542"
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
    desc: "Perception +10; darkvision"
languages: "Aklo, Common, Sakvroth, Shae, Sussuran"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Deception +9, Occultism +11, Netherworld Lore +11, Stealth +13"
abilityMods: [3, 5, 1, 3, 2, 3]
abilities_top:
  - name: "Shadow Shift"
    desc: "Being made partially of shadow themselves, shae are concealed in dim light or darkness even to creatures that can see clearly in those light levels."
  - name: "Items"
    desc: "Dagger (5)"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +11; __Will__: +10"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ precision; __Resistances__ cold 5, void 5"
abilities_mid:
  - name: "Counterattack"
    desc: "⬲"
  - name: "Trigger"
    desc: "The shae is targeted by an attack from an adjacent creature that misses due to the shae being concealed"
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
    desc: "⬻ dagger +13 (Agile, finesse, versatile S) __Damage__ 1d4+5 piercing and 1d6 cold"
  - name: "Ranged"
    desc: "⬻ dagger +13 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+5 piercing and 1d6 cold"
abilities_bot:
  - name: "Bide"
    desc: "⬺ The shae prepares to take action against their foes, watching their opponent and waiting for the right opportunity to respond. The shae gains a second reaction until the start of their next turn, though they still can't use more than one reaction on the same triggering action."
  - name: "Swift Steps"
    desc: "The shae's movement doesn't trigger reactions."
  - name: "Tenebral Form"
    desc: "The shae can _Fly_ at full Speed in vapor form. Children Of Shadow Though rare, shae occasionally engage in relationships with mortals, resulting in children born as fetchlings. Though shae maintain a cool superiority over their mortal children, fetchlings who join a shae's cult are placed in positions of authority over other mortals and receive blatantly preferential treatment."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 21 - __Cantrips (2nd)__ Detect Magic, Void Warp - __4th__ Vapor Form (at will) - __7th__ Interplanar Teleport (self only, to Netherworld or Universe only)"
sourcebook: "_Monster Core 2_, page 284."
```

```encounter-table
name: Shae
creatures:
  - 1: Shae
```
