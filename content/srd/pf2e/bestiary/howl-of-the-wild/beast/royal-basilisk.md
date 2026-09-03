---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Royal Basilisk"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Royal Basilisk"
level: 13
source: "Howl of the Wild"
aon_id: "creature-3255"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3255"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Royal Basilisk"
level: "Creature 13"
size: "Huge"
trait_01: "Beast"
trait_02: "Rare"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; darkvision, scent (imprecise) 120 feet, tremorsense (precise) 60 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +24, Athletics +27, Stealth +24, Survival +25"
abilityMods: [8, 5, 7, -3, 6, 2]
abilities_top:
  - name: "Items"
    desc: "iron crown"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +26; __Ref__: +22; __Will__: +23"
hp: 290
health:
  - name: "HP"
    desc: "290; __Immunities__ poison; __Resistances__ acid 15"
abilities_mid:
  - name: "Crowned Royalty"
    desc: "The royal basilisk's crown is firmly attached to its head but can be Disarmed as though it were a held item. Without a crown, the royal basilisk's mastery over poison is weakened enough that it loses its miasmatic shroud. The royal basilisk can equip a crown within its tail's reach as an Interact action. A royal basilisk's crown is normally made of iron and enables the basilisk to use miasmatic shroud, but crowns made of other, more exotic materials might confer different abilities."
  - name: "Miasmatic Shroud"
    desc: "(aura, poison) 15 feet. The poison in the breath of the royal basilisk makes the air around it a haze, concealing it from all creatures outside the aura, but it cannot use this concealment to Hide or Sneak. When a creature ends its turn within the aura, it is exposed to royal basilisk venom."
speed: "30 feet, climb 30 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +27 (reach 10 feet) __Damage__ 4d10+11 piercing plus Improved Grab and royal basilisk venom"
  - name: "Melee"
    desc: "⬻ tail +27 (Agile, reach 15 feet) __Damage__ 4d8+11 bludgeoning"
  - name: "Ranged"
    desc: "⬻ spit +24 (Poison, range 120 feet) __Damage__ 5d10 poison plus royal basilisk venom"
abilities_bot:
  - name: "Greater Constrict"
    desc: "⬻ 4d8+3 bludgeoning, DC 32"
  - name: "Royal Basilisk Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 36"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d10 poison and clumsy 2 (1 round)"
  - name: "Stage 2"
    desc: "3d10 poison and clumsy 3 (1 round)"
  - name: "Stage 3"
    desc: "4d10 poison, clumsy 3, and slowed 1 (1 round)"
  - name: "Stone-Hewing Spit"
    desc: "⬺ (Acid) The royal basilisk spits its poison with immense force, dealing 5d10 acid and 5d8 piercing damage (DC 32 basic Reflex save) to creatures in a 240-foot line and exposing each creature that took damage to royal basilisk venom. The line penetrates barriers with Hardness of less than 20, ignoring any bonuses they'd provide from cover. The royal basilisk can't use Stone-Hewing Spit again for 1d4 rounds."
  - name: "Swallow Whole"
    desc: "⬻ Large, 5d10 acid damage, Rupture 30"
  - name: "Wrap in Coils"
    desc: "⬻"
  - name: "Requirements"
    desc: "A Large or smaller creature is grabbed or restrained in the royal basilisk's jaws"
  - name: "Effect"
    desc: "The royal basilisk moves the creature into its coils, freeing its jaws to make attacks, then uses Greater Constrict against the creature. The royal basilisk's coils can hold as many creatures as will fit in its space."
sourcebook: "_Howl of the Wild_, page 127."
```

```encounter-table
name: Royal Basilisk
creatures:
  - 1: Royal Basilisk
```
