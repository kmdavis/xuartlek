---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Horned Dragon"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/large
statblock: inline
name: "Young Horned Dragon"
level: 8
source: "Monster Core"
aon_id: "creature-2947"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2947"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Young Horned Dragon"
level: "Creature 8"
size: "Large"
trait_01: "Amphibious"
trait_02: "Dragon"
trait_03: "Primal"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Arcana +16, Athletics +17, Deception +14, Diplomacy +16, Forest Lore +14, Intimidation +16, Nature +14, Occultism +17, Society +14, Stealth +15"
abilityMods: [5, 1, 3, 2, 2, 4]
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +16; __Ref__: +16; __Will__: +17"
hp: 135
health:
  - name: "HP"
    desc: "135; __Immunities__ paralyzed, poison, sleep"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 90 feet, DC 24"
  - name: "Twisting Tail"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the dragon's tail uses a move action or leaves a square during a move action it's using"
  - name: "Effect"
    desc: "The dragon makes a tail Strike at the creature with a –2 penalty. If the Strike hits, the dragon disrupts the creature's action."
speed: "30 feet, fly 120 feet, swim 30 feet; forest passage"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 (Magical, Poison, reach 10 feet) __Damage__ 2d10+8 piercing plus 2d4 poison"
  - name: "Melee"
    desc: "⬻ claw +20 (Agile, Magical) __Damage__ 2d8+8 slashing"
  - name: "Melee"
    desc: "⬻ tail +18 (Magical, reach 15 feet) __Damage__ 2d8+7 bludgeoning"
  - name: "Melee"
    desc: "⬻ horn +18 (Magical, reach 10 feet) __Damage__ 1d12+7 piercing"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one horn Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Poison Breath whenever they score a critical hit with a Strike."
  - name: "Forest Passage"
    desc: "The horned dragon ignores any difficult terrain caused by plants, such as bushes, vines, and undergrowth. Even plants manipulated by magic don't impede their progress."
  - name: "Impaling Charge"
    desc: "⬺"
  - name: "Requirements"
    desc: "The dragon doesn't have a creature impaled on their horn"
  - name: "Effect"
    desc: "The dragon attempts to gore a foe. They Stride, then attempt a horn Strike. On a hit, the target becomes impaled on the dragon's horn. The creature is grabbed while on the horn (and can attempt to Escape as normal). The dragon doesn't need to use additional actions to keep the impaled creature grabbed. If the dragon moves, they bring the grabbed creature along with them."
  - name: "Poison Breath"
    desc: "⬺ (Primal, Poison) The dragon breathes a toxic cloud that deals 9d6 poison damage in a 40-foot cone (DC 25 basic Fortitude save). They can't use Poison Breath again for 1d4 rounds."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 26 - __1st__ Charm - __2nd__ Entangling Flora"
sourcebook: "_Monster Core_, page 119."
```

```encounter-table
name: Young Horned Dragon
creatures:
  - 1: Young Horned Dragon
```
