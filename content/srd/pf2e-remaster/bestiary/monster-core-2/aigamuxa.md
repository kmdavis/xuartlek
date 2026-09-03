---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Aigamuxa"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Aigamuxa"
level: 8
source: "Monster Core 2"
aon_id: "creature-4023"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4023"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Aigamuxa"
level: "Creature 8"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; scent (imprecise) 30 feet"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +18, Intimidation +16, Stealth +14"
abilityMods: [6, 4, 6, -2, 3, 0]
abilities_top:
  - name: "Limited Vision"
    desc: "An aigamuxa's eyes are located on the bottom of their feet, making it difficult for them to see. An aigamuxa is typically blind. If they Seek, they can see normally until the end of their turn."
  - name: "Weak Feet"
    desc: "If an aigamuxa takes damage from Striding or Stepping into hazardous terrain or a square with similar grounded hazards (such as caltrops), they can't Seek until the end of their next turn."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +19; __Ref__: +16; __Will__: +13"
hp: 140
health:
  - name: "HP"
    desc: "140"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +20 (Agile, reach 10 feet) __Damage__ 2d8+9 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ jaws +20 __Damage__ 2d12+9 piercing"
abilities_bot:
  - name: "Burrowed Ambush"
    desc: "⬺"
  - name: "Requirements"
    desc: "The aigamuxa is Hiding in dirt, sand, or another soft surface"
  - name: "Effect"
    desc: "The aigamuxa makes a claw Strike against a creature within reach. On a hit, the aigamuxa can attempt to Grab the creature as a free action. Whether or not they hit, the aigamuxa then Strides. If they have a creature grabbed or restrained, the creature moves with the aigamuxa."
  - name: "Burrowing Concealment"
    desc: "⬺"
  - name: "Requirements"
    desc: "The aigamuxa is standing on dirt, sand, or another soft surface"
  - name: "Effect"
    desc: "The aigamuxa digs into the surface and Hides. They leave their feet partially exposed, allowing them to see out from the surface. The aigamuxa can hold their breath for up to 10 minutes while hiding in this way."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Small, 2d12+4 bludgeoning, Rupture 22"
  - name: "Toss Up and Gulp Down"
    desc: "⬻"
  - name: "Requirements"
    desc: "A Small or smaller creature is grabbed or restrained in the aigamuxa's claw"
  - name: "Effect"
    desc: "The aigamuxa tosses the creature into the air and distends their jaw to catch it in their mouth. The target is grabbed in the aigamuxa's jaws, and the aigamuxa attempts to Swallow it Whole. If the aigamuxa fails the Athletics check, the target misses the aigamuxa's mouth and falls 30 feet instead of being grabbed. The First Aigamuxas Stories say aigamuxas were once giants who entered into a wager with Lamashtu, claiming they could stand on their hands longer than any other creature. Lamashtu produced a simple chimpanzee, pointed to its feet and called them hands. The giants couldn't hold their positions and fell. Lamashtu moved their eyes to their feet and told them, “If you wish to boast of your ability, let this be your blessing.”"
sourcebook: "_Monster Core 2_, page 21."
```

```encounter-table
name: Aigamuxa
creatures:
  - 1: Aigamuxa
```
