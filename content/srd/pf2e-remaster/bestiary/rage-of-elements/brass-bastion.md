---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Brass Bastion"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Brass Bastion"
level: 14
source: "Rage of Elements"
aon_id: "creature-2631"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2631"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Brass Bastion"
level: "Creature 14"
size: "Huge"
trait_01: "Construct"
trait_02: "Fire"
trait_03: "Mindless"
trait_04: "Rare"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +30"
abilityMods: [8, 0, 7, -5, 0, -5]
abilities_top:
  - name: "Items"
    desc: "_+2 striking falchion_"
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +27; __Ref__: +22; __Will__: +20"
hp: 205
health:
  - name: "HP"
    desc: "205; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, fire, healing, mental, nonlethal attacks, paralyzed, poison, sickened, unconscious, vitality, void; __Resistances__ physical 15 (except adamantine), spells 15 (except water)"
abilities_mid:
  - name: "Molten Demise"
    desc: "(arcane, fire) When a brass bastion is destroyed, its body explodes in a flurry of elemental flame and superheated brass, dealing 4d6 piercing damage and 4d6 fire damage to creatures in a 20-foot emanation (DC 34 basic Reflex save)."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _falchion_ +28 (Forceful, Magical, reach 15 feet, Sweep) __Damage__ 2d10+12 slashing plus 1d10 fire"
  - name: "Melee"
    desc: "⬻ fist +26 (Agile, Magical, reach 15 feet) __Damage__ 2d6+12 bludgeoning plus 1d10 fire"
abilities_bot:
  - name: "Breathe Smoke"
    desc: "⬺ (Arcane, Fire) The brass bastion exhales superheated smoke and cinders in a 10-foot radius centered on a corner of its space. The smoke persists for 1 round. Any creature in the area (or that later enters the area) takes 15d6 fire damage (DC 34 basic Reflex save); on a critical failure, the creature catches fire, taking 2d6 persistent fire damage as well. All creatures in the smoke become concealed, and all creatures outside the smoke become concealed to creatures within it. The brass bastion can't Breathe Smoke again for 1d4 rounds."
  - name: "Heat Weapon"
    desc: "Metal weapons wielded by a brass bastion superheat, dealing 1d10 additional fire damage (included in its statistics). Brass Scraps On the Plane of Fire, destroyed brass bastions are sold as scrap to enterprising ifrits, who reforge the remains into new brass bastions. Many ifrits pay more for the remains of a brass bastion crafted by their rivals yet react violently when offered brass bastion remains they originally created. Thus, identifying a brass bastion's original crafter is a valued skill. Few non-ifrits dare trade in brass bastion scraps, save in extralegal markets."
sourcebook: "_Rage of Elements_, page 126."
```

```encounter-table
name: Brass Bastion
creatures:
  - 1: Brass Bastion
```
