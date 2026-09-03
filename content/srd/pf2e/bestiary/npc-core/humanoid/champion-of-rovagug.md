---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Champion of Rovagug"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Champion of Rovagug"
level: 5
source: "NPC Core"
aon_id: "creature-3613"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3613"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Champion of Rovagug"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Unholy"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +13, Deception +10, Intimidation +12, Religion +8, Survival +8"
abilityMods: [4, 1, 3, 0, 1, 3]
abilities_top:
  - name: "Items"
    desc: "Greataxe, Half Plate, Javelin (3)"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +12; __Ref__: +8; __Will__: +10"
hp: 70
health:
  - name: "HP"
    desc: "70"
abilities_mid:
  - name: "Champion's Aura"
    desc: "(aura, divine) 15 feet. Any follower of Rovagug in the aura knows the champion is a champion of Rovagug. Enemies in the aura take a –1 circumstance penalty to saves against fear, and an enemy that ends its turn in the aura can't reduce the value of its frightened condition below 1. The aura can be suppressed or resumed with a single action, which has the concentrate trait, and ends if the champion falls unconscious."
  - name: "Destructive Vengeance"
    desc: "⬲ (divine)"
  - name: "Trigger"
    desc: "An enemy in the champion's aura damages the champion"
  - name: "Effect"
    desc: "The champion increases the amount of damage they take by 2d6 and deals 2d6 spirit damage to the triggering enemy. In addition, until the end of the champion's next turn, the champion's Strikes against the triggering creature deals 2 extra spirit damage."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _fearsome greataxe_ +13 (Magical, Sweep) __Damage__ 1d12+8 slashing"
  - name: "Melee"
    desc: "⬻ gauntlet +13 (Agile, Free-Hand) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ javelin +10 (thrown 30 feet) __Damage__ 1d6+8 piercing"
abilities_bot:
  - name: "Champion Devotion Spells"
    desc: "DC 20, 1 Focus Point - __3rd__ Touch of the Void"
  - name: "Axe Swipe"
    desc: "⬺ The champion makes a melee Strike with a +1 circumstance bonus to the attack roll and compares the roll to the AC of up to two foes that are in reach and adjacent to each other. The champion rolls damage only once and applies it to each creature they hit. This counts as two attacks toward their multiple attack penalty."
  - name: "Fearsome Armament"
    desc: "The champion grants their greataxe the _fearsome_ rune while they wield it. Other Grim Champions The most sinister champions of unholy gods are devoted to desecration or iniquity. This champion serves Rovagug, but Lamashtu, Urgathoa, and demon lords have similar champions. If you switch their deity, change their favored weapon (see the Deity table). If it's a one-handed weapon, reduce the champion's AC by 2, give them a steel shield, and replace Axe Swipe with Defensive Advance, a 2-action activity that lets the champion Raise their Shield, Stride, and make a melee Strike."
sourcebook: "_NPC Core_, page 156."
```

```encounter-table
name: Champion of Rovagug
creatures:
  - 1: Champion of Rovagug
```
