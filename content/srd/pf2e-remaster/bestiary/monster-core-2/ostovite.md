---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ostovite"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/small
statblock: inline
name: "Ostovite"
level: 1
source: "Monster Core 2"
aon_id: "creature-4502"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4502"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ostovite"
level: "Creature 1"
size: "Small"
trait_01: "Fiend"
trait_02: "Unholy"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; darkvision"
languages: "Chthonian"
skills:
  - name: "Skills"
    desc: "Crafting +4, Stealth +7"
abilityMods: [0, 4, 3, -4, 1, 0]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +9; __Will__: +4"
hp: 30
health:
  - name: "HP"
    desc: "30; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poisoned, sickened, unconscious"
abilities_mid:
  - name: "Bone Chariot"
    desc: "Ostovites build and inhabit moving shells of bone. The ostovite's base statistics, particularly its immunities, assume the ostovite is safely inside its bone chariot. The bone chariot is destroyed when the ostovite is reduced to less than half its Hit Points or immediately after it takes damage from a critical hit. Damage that can specifically affect the ostovite controlling the chariot even while it's inside doesn't destroy the bone chariot, and it bypasses the ostovite's immunities. Without the bone chariot, the ostovite loses its immunities and bone spike Strike, and it's reduced to Tiny size. It also gains weakness 5 to mental and physical damage. Building a new bone chariot requires the skeleton of a Small or larger creature and 10 minutes. An ostovite in a bone chariot is normally Small, though larger bone chariots are possible, especially when ostovites work together."
  - name: "Scuttle Away"
    desc: "⬲"
  - name: "Trigger"
    desc: "The ostovite's bone chariot is destroyed"
  - name: "Effect"
    desc: "The ostovite within Steps or Strides."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +9 (Finesse) __Damage__ 1d4 piercing plus 1d4 acid"
  - name: "Melee"
    desc: "⬻ bone spike +9 (Finesse) __Damage__ 1d12 piercing plus 1d4 persistent bleed Ostovite Lairs Ostovites are most often found on battlefields, scavenging for food and bones, regardless of the plane. If one of the vermin finds a suitable location and can bring others along with it, a colony might form."
sourcebook: "_Monster Core 2_, page 245."
```

```encounter-table
name: Ostovite
creatures:
  - 1: Ostovite
```
