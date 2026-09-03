---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wooly Wrangler"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Wooly Wrangler"
level: 8
source: "NPC Core"
aon_id: "creature-3477"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3477"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Wooly Wrangler"
level: "Creature 8"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +14, Intimidation +14, Mountain Lore +18, Nature +16, Survival +18"
abilityMods: [6, 3, 4, 0, 2, 2]
abilities_top:
  - name: "In Balance"
    desc: "Whenever the woolly wrangler rolls a success on a Recall Knowledge check using Nature or Mountain Lore, they get a critical success instead."
  - name: "Items"
    desc: "animal treats, _+1 striking greatclub_, Leather Armor, Whip"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +19; __Ref__: +12; __Will__: +16"
hp: 125
health:
  - name: "HP"
    desc: "125; __Resistances__ cold 10"
abilities_mid:
  - name: "Uneven Footing"
    desc: "(aura) 10 feet. While the woolly wrangler is mounted on a Huge or Gargantuan creature, the ground near the mount shakes and buckles. Squares in the aura are difficult terrain for Medium or smaller creatures."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greatclub_ +20 (Backswing, Magical, Shove) __Damage__ 2d10+12 bludgeoning"
  - name: "Melee"
    desc: "⬻ whip +19 (Disarm, Nonlethal, Reach, Trip) __Damage__ 1d4+12 slashing"
  - name: "Melee"
    desc: "⬻ fist +19 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+12 bludgeoning"
abilities_bot:
  - name: "Wrangling Whip"
    desc: "⬺ The woolly wrangler makes a whip Strike. On a hit, the woolly wrangler can either knock the target prone or pull it up to 5 feet. If the creature ends this movement adjacent to the wrangler's mount, the mount can make a melee unarmed Strike against the creature as a free action."
sourcebook: "_NPC Core_, page 57."
```

```encounter-table
name: Wooly Wrangler
creatures:
  - 1: Wooly Wrangler
```
