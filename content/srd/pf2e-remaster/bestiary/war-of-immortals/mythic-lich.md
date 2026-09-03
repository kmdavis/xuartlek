---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mythic Lich"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/mythic
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Mythic Lich"
level: 12
source: "War of Immortals"
aon_id: "creature-3402"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3402"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "WoI"
name: "Mythic Lich"
level: "Creature 12"
size: "Medium"
trait_01: "Mythic"
trait_02: "Rare"
trait_03: "Undead"
trait_04: "Unholy"
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
    desc: "_invisibility potion_, __scroll of teleport__, _greater staff of fire_"
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +17; __Ref__: +21; __Will__: +23 mythic resilience (Ref and Will)"
hp: 190
health:
  - name: "HP"
    desc: "190 (rejuvenation, void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious; __Resistances__ cold 10, physical 10 (except magical bludgeoning)"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 60 feet, DC 29 **Counterspell ⬲ :"
  - name: "Trigger"
    desc: "A creature casts a spell the lich has prepared**"
  - name: "Effect"
    desc: "The lich expends a prepared spell to counter the triggering creature's casting of that same spell. The lich loses their spell slot as if they had cast the triggering spell. The lich then attempts to counteract the triggering spell."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hand +24 (Finesse, Magical) __Damage__ 4d8 void plus siphon life"
abilities_bot:
  - name: "Mythic Power"
    desc: "3 Mythic Points _Recharge Spell_ ⬻ (concentrate)"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "The mythic lich regains one spell._Remove a Condition_ ⬻ (concentrate)"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "The mythic lich ends one condition affecting it."
  - name: "Drain Soul Cage"
    desc: "⭓"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The lich taps into their _soul cage's_ power to cast any arcane spell up to 6th rank, even if the spell being cast is not one of the lich's prepared spells. The lich's _soul cage_ doesn't need to be present for the lich to use this ability."
  - name: "Siphon Life"
    desc: "A lich's form draws forth life from those who come into contact with it. When the lich damages a living creature with an unarmed attack, the lich gains 5 temporary Hit Points and the creature must succeed at a DC 34 Fortitude save or become drained 1. If the lich is grabbed or restrained at the start of its turn, each creature grabbing or restraining it must succeed at a Fortitude save or become drained 1. If the lich siphons a creature's life again, the drained value increase by 1, to a maximum of drained 4."
  - name: "Steady Spellcasting"
    desc: "If a reaction would disrupt the lich's spellcasting action, the lich attempts a DC 15 flat check. On a success, the action isn't disrupted. Mythic Soul Cages Though a standard _soul cage_ appears in _Monster Core_, a truly powerful mythic lich is likely to have a _soul cage_ that is much more spectacular and unusual in nature. The mightiest mythic lich might bind a fearsome and nearly immortal creature to serve as its _soul cage_, or a majestic fortress, or even an entire island."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 36, attack +26 - __Cantrips (6th)__ Detect Magic, Frostbite, Message, Shield, Telekinetic Hand - __1st__ Enfeeble (×2), Fleet Step, Sure Strike - __2nd__ Blur, False Vitality, Resist Energy, See the Unseen - __3rd__ Blindness, Force Barrage, Locate, Vampiric Feast - __4th__ Dispel Magic, Fire Shield, Fly, Translocate - __5th__ Howling Blizzard (×2), Toxic Cloud, Wall of Ice - __6th__ Chain Lightning, Dominate, Vampiric Exsanguination"
sourcebook: "_War of Immortals_, page 172."
```

```encounter-table
name: Mythic Lich
creatures:
  - 1: Mythic Lich
```
