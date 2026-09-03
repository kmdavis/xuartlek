---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lich"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Lich"
level: 12
source: "Monster Core"
aon_id: "creature-3082"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3082"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lich"
level: "Creature 12"
size: "Medium"
trait_01: "Rare"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision"
languages: "Aklo, Chthonian, Common, Diabolic, Draconic, Elven, Necril, Sakvroth"
skills:
  - name: "Skills"
    desc: "Arcana +28, Crafting +24, Deception +17, Diplomacy +19, Religion +22, Stealth +20"
abilityMods: [0, 4, 0, 6, 4, 3]
abilities_top:
  - name: "Items"
    desc: "_invisibility potion_, _scroll of teleport_, _greater staff of fire_"
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +17; __Ref__: +21; __Will__: +23 +1 status to all saves vs. vitality"
hp: 190
health:
  - name: "HP"
    desc: "190 (void healing, rejuvenation); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious; __Resistances__ cold 10, physical 10 (except magical bludgeoning)"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 60 feet, DC 29"
  - name: "Counterspell"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature casts a spell the lich has prepared"
  - name: "Effect"
    desc: "The lich expends a prepared spell to counter the triggering creature's casting of that same spell. The lich loses their spell slot as if they had cast the triggering spell. The lich then attempts to counteract the triggering spell."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hand +24 (Finesse, Magical) __Damage__ 4d8 void plus siphon life"
abilities_bot:
  - name: "Drain Soul Cage"
    desc: "⭓ 6th rank"
  - name: "Siphon Life"
    desc: "DC 34"
  - name: "Steady Spellcasting"
    desc: "If a reaction would disrupt the lich's spellcasting action, the lich attempts a DC 15 flat check. On a success, the action isn't disrupted."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 36, attack +26 - __Cantrips (6th)__ Detect Magic, Frostbite, Message, Shield, Telekinetic Hand - __1st__ Enfeeble (×2), Fleet Step, Sure Strike - __2nd__ Blur, False Vitality, Resist Energy, See the Unseen - __3rd__ Blindness, Force Barrage, Locate, Vampiric Feast - __4th__ Dispel Magic, Fire Shield, Fly, Translocate - __5th__ Howling Blizzard (×2), Toxic Cloud, Wall of Ice - __6th__ Chain Lightning, Dominate, Vampiric Exsanguination"
sourcebook: "_Monster Core_, page 219."
```

```encounter-table
name: Lich
creatures:
  - 1: Lich
```
