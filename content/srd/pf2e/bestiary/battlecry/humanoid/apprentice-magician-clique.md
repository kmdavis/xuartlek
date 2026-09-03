---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Apprentice Magician Clique"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Apprentice Magician Clique"
level: 5
source: "Battlecry!"
aon_id: "creature-3900"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3900"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Apprentice Magician Clique"
level: "Creature 5"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12"
languages: "Common, Draconic"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Arcana +13, Diplomacy +10, Deception +10, Thievery +12"
abilityMods: [0, 4, 1, 5, 1, 2]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +12; __Will__: +15"
hp: 75
health:
  - name: "HP"
    desc: "75 (4 segments); __Weaknesses__ area damage 4, splash damage 4"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Barrage of Force"
    desc: "⬺ (Arcane, Force) The apprentice magicians launch shards of pure magic at all creatures in a 10-foot burst within 120 feet. This barrage deals 5d4 force damage (DC 19 basic Reflex save). When the clique is reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Clique Spellcasting"
    desc: "When the apprentice magician clique Casts a Spell, its members pool their arcane power into the spell. A creature who critically fails their save against the spell or whom the clique hits with a critical spell attack is also stupefied 1 for 1 minute."
  - name: "Sparking Wands"
    desc: "(Arcane, Electricity)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The apprentice magicians wave wands that shoot out minor bolts of electricity at short range. Each enemy in a 5-foot emanation must attempt a DC 19 basic Reflex save. The damage dealt depends on the number of actions. ⬻ 1d8 electricity damage ⬺ 2d8+3 electricity damage ⬽ 2d8+7 electricity damage"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 22, attack +15 - __Cantrips (3rd)__ Electric Arc, Ignition, Light, Prestidigitation, Telekinetic Projectile - __1st__ Dizzying Colors, Hydraulic Push, Sleep - __2nd__ Blazing Bolt, Entangling Flora, Laughing Fit - __3rd__ Fireball, Wall of Wind"
sourcebook: "_Battlecry!_, page 173."
```

```encounter-table
name: Apprentice Magician Clique
creatures:
  - 1: Apprentice Magician Clique
```
