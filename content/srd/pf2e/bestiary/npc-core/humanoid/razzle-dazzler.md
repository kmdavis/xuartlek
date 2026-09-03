---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Razzle Dazzler"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/gnome
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Razzle Dazzler"
level: 5
source: "NPC Core"
aon_id: "creature-3638"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3638"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Razzle Dazzler"
level: "Creature 5"
size: "Small"
trait_01: "Gnome"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision"
languages: "Common, Elven, Fey, Gnomish"
skills:
  - name: "Skills"
    desc: "Arcana +10, Deception +14, Diplomacy +14, Intimidation +12, Performance +14, Thievery +12"
abilityMods: [1, 3, 1, 2, 1, 4]
abilities_top:
  - name: "Items"
    desc: "Dagger, Dueling Cape, Hand Crossbow (20 bolts)"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +9; __Ref__: +12; __Will__: +15"
hp: 78
health:
  - name: "HP"
    desc: "78"
abilities_mid:
  - name: "Daunting Charisma"
    desc: "⭓"
  - name: "Trigger"
    desc: "The razzle dazzler rolls initiative using Deception or Performance"
  - name: "Effect"
    desc: "The razzle dazzler can attempt to Demoralize one creature they can see."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +13 (Agile, Finesse, versatile S) __Damage__ 1d4+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +13 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +13 (range increment 60 feet, reload 1) __Damage__ 1d6+2 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +13 (Agile, Finesse, thrown 10 feet) __Damage__ 1d4+3 piercing"
abilities_bot:
  - name: "Dazzling Duplicate"
    desc: "⬻ (Arcane, Concentrate, Illusion, Manipulate) The razzle dazzler creates an illusory duplicate of themself in their space that lasts for 1 round. A creature who attacks the razzle dazzler must first attempt a DC 11 flat check. On a failure, the attack misses the razzle dazzler and destroys the illusion instead, ending this effect."
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 22, attack +15 - __Cantrips (3rd)__ Figment, Light, Prestidigitation, Telekinetic Hand, Telekinetic Projectile - __1st__ Dizzying Colors, Illusory Disguise, Illusory Object, Ventriloquism (4 slots) - __2nd__ Illusory Creature, Illusory Object, Laughing Fit, Revealing Light (4 slots) - __3rd__ Enthrall, Hypnotize, Illusory Disguise (3 slots)"
sourcebook: "_NPC Core_, page 183."
```

```encounter-table
name: Razzle Dazzler
creatures:
  - 1: Razzle Dazzler
```
