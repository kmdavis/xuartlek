---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dero Magister"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/dero
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/small
statblock: inline
name: "Dero Magister"
level: 5
source: "Monster Core"
aon_id: "creature-2904"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2904"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dero Magister"
level: "Creature 5"
size: "Small"
trait_01: "Dero"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "Aklo, Sakvroth"
skills:
  - name: "Skills"
    desc: "Crafting +12, Medicine +10, Occultism +12, Stealth +11"
abilityMods: [1, 4, 2, 3, -1, 5]
abilities_top:
  - name: "Items"
    desc: "cytillesh toolkit (see sidebar), Staff"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +10; __Ref__: +13; __Will__: +10"
hp: 65
health:
  - name: "HP"
    desc: "65; __Immunities__ confused"
abilities_mid:
  - name: "Vulnerable to Sunlight"
    desc: "A dero magister takes 10 damage for every hour they're exposed to sunlight."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +10 (two-hand 1d8) __Damage__ 1d4+3 bludgeoning"
abilities_bot:
  - name: "Cytillesh Stare"
    desc: "⬻ (Concentrate, Incapacitation, Mental, Visual)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The magister focuses their gaze on a creature they can see within 30 feet. The target is dazzled for 1 round and must succeed at a DC 24 Will saving throw or be confused for 1 round."
  - name: "Dero Medicine"
    desc: "⬻ (Healing, Manipulate)"
  - name: "Requirements"
    desc: "The dero is wearing a cytillesh toolkit and has a hand free"
  - name: "Effect"
    desc: "The dero excises damaged flesh and crudely stitches wounds shut, healing themself or an ally in reach for 2d8+10 Hit Points. For 1 hour, the target has slashing weakness 2 and is immune to Dero Medicine."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 24 - __Cantrips (3rd)__ Daze, Light, Read Aura - __2nd__ Darkness, Revealing Light - __4th__ Nightmare, Rewrite Memory"
  - name: "Occult Spontaneous Spells"
    desc: "DC 24 - __Cantrips (3rd)__ Detect Magic, Forbidding Ward, Light, Message, Void Warp - __1st__ Force Barrage, Grim Tendrils, Phantom Pain, Soothe (4 slots) - __2nd__ Laughing Fit, Paranoia, Stupefy, Telekinetic Maneuver (4 slots) - __3rd__ Blindness, Levitate, Vampiric Feast (3 slots)"
sourcebook: "_Monster Core_, page 85."
```

```encounter-table
name: Dero Magister
creatures:
  - 1: Dero Magister
```
