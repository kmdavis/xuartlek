---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Jailer"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Jailer"
level: 3
source: "NPC Core"
aon_id: "creature-3555"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3555"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Jailer"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; (10 to find concealed objects)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +11, Diplomacy +5, Intimidation +7"
abilityMods: [4, 3, 1, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Club, Crossbow (20 bolts), keyring, simple manacles, Signal Whistle, Studded Leather Armor"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +10; __Will__: +7"
hp: 45
health:
  - name: "HP"
    desc: "45"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ club +11 __Damage__ 1d6+8 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +11 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +10 (range increment 120 feet, reload 1) __Damage__ 1d8+4 piercing"
  - name: "Ranged"
    desc: "⬻ club +10 (thrown 10 feet) __Damage__ 1d6+8 bludgeoning"
abilities_bot:
  - name: "Efficient Capture"
    desc: "⬽ (Attack, Manipulate)"
  - name: "Requirements"
    desc: "The jailer has manacles in hand and is adjacent to a creature"
  - name: "Effect"
    desc: "The jailer attempts to bind the creature's wrists or ankles with the manacles. If the jailer succeeds at an attack roll with a +9 modifier against the target's AC, they apply the manacles."
  - name: "Intimidating Strike"
    desc: "⬺ (Emotion, Fear, Mental) The jailer makes a melee Strike. If it hits and deals damage, the target is frightened 1, or frightened 2 on a critical hit."
  - name: "Subdue Prisoners"
    desc: "The jailer doesn't take the normal penalty for making a nonlethal attack when attacking with their club."
sourcebook: "_NPC Core_, page 112."
```

```encounter-table
name: Jailer
creatures:
  - 1: Jailer
```
