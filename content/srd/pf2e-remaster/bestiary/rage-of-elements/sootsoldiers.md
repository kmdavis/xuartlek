---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sootsoldiers"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Sootsoldiers"
level: 10
source: "Rage of Elements"
aon_id: "creature-2639"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2639"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Sootsoldiers"
level: "Creature 10"
size: "Gargantuan"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: "Troop"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision, smoke vision"
languages: "Pyric"
skills:
  - name: "Skills"
    desc: "Acrobatics +21, Athletics +21, Nature +18, Plane of Fire Lore +18, Warfare Lore +18"
abilityMods: [7, 5, 6, 2, 4, 0]
abilities_top:
  - name: "Smoke Vision"
    desc: "Sootsoldiers ignore the concealed condition from smoke."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +20; __Ref__: +21; __Will__: +18"
hp: 165
health:
  - name: "HP"
    desc: "165 (16 squares); __Immunities__ bleed, fire, paralyzed, poison, sleep; __Weaknesses__ area damage 10, cold 10, splash damage 10"
abilities_mid:
  - name: "Ashen Smoke"
    desc: "When the sootsoldiers are reduced by an HP Threshold or are reduced to 0 HP, the destroyed soldiers crumble to a cloud of ash-laden smoke in 20-foot burst centered on the sootsoldiers. All creatures within the cloud are concealed, and all creatures outside it are concealed to those inside. The smoke lasts for 1 minute or until dispersed by a strong wind."
  - name: "Troop Defenses"
    desc: ""
speed: "40 feet; troop movement"
abilities_bot:
  - name: "Incinerating Grasp"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The sootsoldiers reach to constrain each enemy in a 5-foot emanation in their fiery clutches (DC 26 basic Reflex save). The damage and additional effects depend on the number of actions. ⬻ 2d8 fire damage ⬺ 3d8+7 fire damage plus grabbed ⬽ 4d8+7 fire damage plus grabbed"
  - name: "Seething Flash"
    desc: "⬺ (Fire, Primal) The sootsoldiers reignite and rush across the battlefield, Forming Up and Striding twice. At the end of this movement, a wave of flame and heat pours off the sootsoldiers, dealing 4d8 fire damage to other creatures in a 10-foot emanation, with a DC 29 basic Reflex save. A creature that critically fails its save is also knocked prone. The Radiant Host Sootsoldiers who serve the other Lord of Fire, the Lambent King Atreia, are covered in glowing embers instead of black char. In place of ashen smoke's normal effects, any creature in the area must attempt a DC 29 Reflex save. On a failure, for 1 minute that creature is dazzled and its invisibility is negated."
sourcebook: "_Rage of Elements_, page 133."
```

```encounter-table
name: Sootsoldiers
creatures:
  - 1: Sootsoldiers
```
