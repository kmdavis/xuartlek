---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Horned Dragon"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Horned Dragon"
level: 12
source: "Monster Core"
aon_id: "creature-2948"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2948"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Adult Horned Dragon"
level: "Creature 12"
size: "Huge"
trait_01: "Amphibious"
trait_02: "Dragon"
trait_03: "Primal"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic, Elven, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +19, Arcana +22, Athletics +24, Deception +19, Diplomacy +23, Forest Lore +22, Intimidation +23, Nature +20, Occultism +24, Society +22, Stealth +21"
abilityMods: [6, 3, 3, 4, 4, 5]
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +20; __Ref__: +22; __Will__: +23 +1 status to all saves vs. primal"
hp: 215
health:
  - name: "HP"
    desc: "215; __Immunities__ paralyzed, poison, sleep Frightful Presence (aura, emotion, fear, mental) 90 feet, DC 31"
abilities_mid:
  - name: "Twisting Tail"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the dragon's tail uses a move action or leaves a square during a move action it's using"
  - name: "Effect"
    desc: "The dragon makes a tail Strike at the creature with a –2 penalty. If the Strike hits, the dragon disrupts the creature's action."
speed: "40 feet, fly 160 feet, swim 40 feet; forest passage, trackless journey"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +26 (Magical, Poison, reach 15 feet) __Damage__ 3d10+12 piercing plus 3d4 poison"
  - name: "Melee"
    desc: "⬻ claw +26 (Agile, Magical, reach 10 feet) __Damage__ 3d8+12 slashing"
  - name: "Melee"
    desc: "⬻ tail +24 (Magical, reach 20 feet) __Damage__ 3d8+10 bludgeoning"
  - name: "Melee"
    desc: "⬻ horn +24 (Magical, reach 15 feet) __Damage__ 2d8+10 piercing"
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
    desc: "⬺ (Primal, Poison) The dragon breathes a toxic cloud that deals 13d6 poison damage in a 50-foot cone (DC 31 basic Fortitude save). They can't use Poison Breath again for 1d4 rounds."
  - name: "Trackless Journey"
    desc: "The horned dragon always gains the benefits of Cover Tracks in natural surroundings, even while moving at full speed."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 32 - __2nd__ Charm (at will), Entangling Flora (×2) - __4th__ Suggestion"
sourcebook: "_Monster Core_, page 120."
```

```encounter-table
name: Adult Horned Dragon
creatures:
  - 1: Adult Horned Dragon
```
