---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dybbuk"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Dybbuk"
level: 15
source: "Monster Core"
aon_id: "creature-2967"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2967"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dybbuk"
level: "Creature 15"
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Spirit"
trait_03: "Uncommon"
trait_04: "Undead"
trait_05: "Unholy"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; darkvision"
languages: "Aklo, Chthonian, Common; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +28, Deception +31, Diplomacy +27, Intimidation +29, Stealth +28"
abilityMods: [-5, 7, 0, 1, 6, 8]
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +21; __Ref__: +28; __Will__: +29"
hp: 175
health:
  - name: "HP"
    desc: "175 (void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, precision, unconscious; __Resistances__ all damage 10 (except force, _ghost touch_, spirit, or vitality; double resistance vs. non-magical)"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, divine, emotion, fear, mental 30 feet, DC 33)"
speed: "fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ghostly hand +28 (Agile, Finesse, Magical, Unholy) __Damage__ 3d10+14 void plus 2d6 spirit"
abilities_bot:
  - name: "Malevolent Possession"
    desc: "⬺ (Incapacitation, Mental, Occult, Possession) The dybbuk attempts to possess an adjacent corporeal creature. This has the same effect as the _possession_ spell (DC 34) with an unlimited duration, except since the dybbuk doesn't have a physical body, they aren't unconscious, and aren't paralyzed when the effect ends, though they take 5d6 spirit damage if the body is knocked unconscious or killed. If the dybbuk took control of the target with Malevolent Possession, when the dybbuk departs, the target has only incoherent memories of the interval it was possessed. Cruel Puppet Masters Dybbuks revel in tricking mortals and using their telekinetic abilities to sow fear in the hearts of those around them. They create chaos in the households of their victims using their innate magical abilities. Victims possessed by dybbuks are often controlled indefinitely, until the dybbuk becomes bored with them or until some brave soul finds a way to release the victim from their torment."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 36, attack +30 - __Cantrips (6th)__ Telekinetic Projectile - __3rd__ Fear (at will) - __4th__ Rewrite Memory - __5th__ Chilling Darkness (×2), Fear - __6th__ Dominate, Never Mind, Telekinetic Maneuver (at will)"
sourcebook: "_Monster Core_, page 136."
```

```encounter-table
name: Dybbuk
creatures:
  - 1: Dybbuk
```
