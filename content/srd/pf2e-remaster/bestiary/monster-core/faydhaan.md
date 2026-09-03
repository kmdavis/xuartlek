---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Faydhaan"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/genie
  - pf2e/creature/trait/water
  - pf2e/creature/trait/large
statblock: inline
name: "Faydhaan"
level: 9
source: "Monster Core"
aon_id: "creature-3005"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3005"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Faydhaan"
level: "Creature 9"
size: "Large"
trait_01: "Elemental"
trait_02: "Genie"
trait_03: "Water"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; (18 to Sense Motive) darkvision, wavesense (imprecise) 60 feet"
languages: "Common, Muan, Petran, Pyric, Sussuran, Talican, Thalassic; _truespeech_"
skills:
  - name: "Skills"
    desc: "Athletics +19, Crafting +16, Deception +18, Diplomacy +20, Nature +18, Performance +20, Society +16, Stealth +18"
abilityMods: [4, 5, 2, 1, 3, 5]
abilities_top:
  - name: "Items"
    desc: "_+1 striking trident_"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +17; __Ref__: +18; __Will__: +18"
hp: 145
health:
  - name: "HP"
    desc: "145; __Resistances__ fire 10"
abilities_mid:
  - name: "Turbulent Seas"
    desc: "(aura, water) 40 feet. Water in the aura that is also in the same body of water as the faydhaan is difficult terrain for Swimmingcreatures. Creatures with the water trait are immune."
speed: "25 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _trident_ +20 (Magical, reach 10 feet) __Damage__ 2d8+10 piercing"
  - name: "Melee"
    desc: "⬻ fist +20 (Agile, Magical, Nonlethal, reach 10 feet) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _trident_ +21 (Magical, thrown 20 feet) __Damage__ 2d8+10 piercing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Arcane, Concentrate, Polymorph) The faydhaan transforms into a Small or Medium water elemental, aquatic animal, or humanoid. This doesn't affect their statistics, but it could change the damage type of their Strikes."
  - name: "Gift of Hospitality"
    desc: "⬽ (Arcane, Emotion, Mental) The faydhaan gives another willing creature a magical gift or an agreeable conversation. The creature gains a +2 status bonus to Society and Diplomacy checks. A creature can't have more than one gift at a time, and a faydhaan can't grant more than one gift at a time. The gift ends if the target acts hostile, or if the faydhaan renounces the recipient (a single action)."
  - name: "Skewer"
    desc: "⬻ The faydhaan makes a trident Strike, dealing an extra 2d6 persistent bleed damage on a hit (4d6 on a critical hit). Faydhaan Shuyookhs Faydhaan shuyookhs grant wishes in ways that please the most people possible. They add the following innate spells: __7th__ _hydraulic torrent_, _planar palace_, _summon elemental_; __5th__ _howling blizzard_ (at will), _illusory creature_ (×2), _mirage_, _truespeech_ (at will); __4th__ _invisibility_ (×2), _vapor form_; __2nd__ _create water_ (at will), _invisibility_ (at will), _see the unseen_."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 24 - __Cantrips (5th)__ Detect Magic - __2nd__ Create Water (at will), Invisibility (×2), Water Breathing - __4th__ Hydraulic Push (at will) - __5th__ Control Water (at will), Hydraulic Torrent, Truespeech (at will) - __7th__ Interplanar Teleport (to Astral Plane; Elemental Planes; or the Universe only) - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core_, page 158."
```

```encounter-table
name: Faydhaan
creatures:
  - 1: Faydhaan
```
