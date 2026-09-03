---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Aphorite Sharpshooter"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/nephilim
  - pf2e/creature/trait/medium
statblock: inline
name: "Aphorite Sharpshooter"
level: 4
source: "Monster Core 2"
aon_id: "creature-4513"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4513"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Aphorite Sharpshooter"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Nephilim"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "Common, Utopian"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Athletics +8, Deception +10, Diplomacy +10, Engineering Lore +12, Intimidation +10"
abilityMods: [2, 4, 2, 1, 0, 2]
abilities_top:
  - name: "Items"
    desc: "Breastplate, Crossbow (50 bolts), outrageous hat, Shortsword"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +10; __Ref__: +12; __Will__: +8"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +14 (Agile, Finesse, versatile S) __Damage__ 1d6+8 piercing"
  - name: "Ranged"
    desc: "⬻ crossbow +14 (range increment 60, reload 1) __Damage__ 1d8+6 piercing"
abilities_bot:
  - name: "Calculated Reload"
    desc: "When the sharpshooter reloads their crossbow, they also calculate the best angle to their target, increasing the damage die from 1d8 to 1d10 and gaining a +2 circumstance bonus to their damage roll for their next crossbow Strike, as long as it occurs before the end of their next turn."
  - name: "Crystalline Dust"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The sharpshooter becomes concealed for 4 rounds, though they can't use the concealment to Hide or Sneak, as normal for concealment where their position is obvious."
  - name: "Hurtful Critique"
    desc: "⬻ (Auditory, Emotion, Linguistic, Mental) The sharpshooter makes witty but disparaging comments about the fighting style of a target within 30 feet, expressing sympathy over every missed blow and providing sarcastic advice on how to improve. The target must succeed at a DC 18 Will save or take a –1 circumstance penalty to attack rolls (–2 on a critical failure) for 1 minute or until it makes a successful Strike against the sharpshooter. A creature that critically succeeds or who Strikes the sharpshooter after failing is immune to that sharpshooter's Hurtful Critique for 1 hour. Aphorite Gear Due to their propensity for tinkering, many aphorite soldiers and mercenaries carry odd or improbable weapons— such as crossbows with precision sights, exquisitely balanced blades, or partitioned quivers with arrows for every occasion. Outsiders often express skepticism about these weapons, but no one can deny their effectiveness."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 18 - __1st__ Sure Strike"
sourcebook: "_Monster Core 2_, page 255."
```

```encounter-table
name: Aphorite Sharpshooter
creatures:
  - 1: Aphorite Sharpshooter
```
