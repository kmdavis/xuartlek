---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Monster Hunter"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Monster Hunter"
level: 6
source: "NPC Core"
aon_id: "creature-3516"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3516"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Monster Hunter"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Monster Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11"
abilityMods: [4, 3, 3, 1, 1, 1]
abilities_top:
  - name: "Favored Game"
    desc: "A monster hunter specializes in bringing down certain non-humanoid creatures. These favored game are typically [[srd/pf2e/compendium/rules-elements/traits/player-core/animal|animals]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/beast|beasts]], but an individual might hunt dragons, [[srd/pf2e/compendium/rules-elements/traits/player-core/plant|plants]], or more specialized creatures like [[srd/pf2e/bestiary/monster-core/animal/tiger|tigers]] or [[srd/pf2e/bestiary/monster-core/beast/manticore|manticores]]."
  - name: "Items"
    desc: "Composite Longbow (20 arrows), _+1 [[srd/pf2e/compendium/equipment/weapons/axe/greataxe|greataxe]]_, Hide Armor"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +15; __Ref__: +11; __Will__: +13"
hp: 105
health:
  - name: "HP"
    desc: "105"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greataxe_ +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d12+8 slashing plus primal fear"
  - name: "Ranged"
    desc: "⬻ composite longbow +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 100 feet, reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/volley|volley 30 feet]]) __Damage__ 1d8+6 piercing plus primal fear"
abilities_bot:
  - name: "Hunter's Onslaught"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Requirements"
    desc: "The monster hunter isn't [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]]"
  - name: "Effect"
    desc: "The monster hunter leads an attack against their monstrous foe. The monster hunter chooses an enemy they can see that qualifies as their favored game. The monster hunter becomes fascinated by that creature and gains 10 temporary Hit Points that last as long as the onslaught does. During the onslaught, the hunter gains a +8 status bonus to damage rolls against the designated enemy, and allies in a 30- foot aura around the hunter gain half that bonus. The onslaught lasts for 1 minute or until either the monster hunter or the designated creature falls [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]."
  - name: "Primal Fear"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) When the monster hunter hits a creature that qualifies as their favored game, that creature is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 1]] (or frightened 2 on a critical hit)."
  - name: "Sudden Charge"
    desc: "⬺ The monster hunter Strides twice and makes a melee Strike. How To Hunt A Monster Monster hunters fight in different ways. You can replace Sudden Charge with one of the following."
  - name: "Mighty Swing"
    desc: "⬺ The monster hunter makes a melee Strike that deals an additional 1d12 damage. This counts as two attacks when calculating their multiple attack penalty."
  - name: "Far Swing"
    desc: "⬻ The monster hunter makes a Strike with a melee weapon, increasing their [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach]] by 5 feet for that Strike."
  - name: "Brutish Maneuvers"
    desc: "The monster hunter can [[srd/pf2e/compendium/rules-elements/actions/player-core#Reposition|Reposition]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Shove|Shove]], or [[srd/pf2e/compendium/rules-elements/actions/player-core#Trip|Trip]] an enemy up to two sizes larger than them, and can use these actions while wielding a two-handed weapon."
  - name: "Big Game Hunter"
    desc: "The monster hunter gains a +1 circumstance bonus to AC against attacks made by creatures that are Large or larger. Additionally, whenever the monster hunter deals damage to a creature that is Large or larger, they gain 5 temporary Hit Points that last until the start of their next turn."
sourcebook: "_NPC Core_, page 83."
```

```encounter-table
name: Monster Hunter
creatures:
  - 1: Monster Hunter
```
