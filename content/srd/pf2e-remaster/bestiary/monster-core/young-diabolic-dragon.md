---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Diabolic Dragon"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Young Diabolic Dragon"
level: 11
source: "Monster Core"
aon_id: "creature-2938"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2938"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Young Diabolic Dragon"
level: "Creature 11"
size: "Large"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Unholy"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; greater darkvision, scent (imprecise) 60 feet, smoke vision"
languages: "Common, Diabolic, Draconic, Pyric"
skills:
  - name: "Skills"
    desc: "Acrobatics +20, Athletics +24, Deception +20, Diplomacy +22, Hell Lore +19, Intimidation +20, Legal Lore +21, Religion +21, Society +19, Thievery +20"
abilityMods: [7, 3, 6, 2, 4, 3]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +23; __Ref__: +20; __Will__: +21 +2 status to all saves vs. divine"
hp: 215
health:
  - name: "HP"
    desc: "215; __Immunities__ fire, paralyzed, sleep; __Weaknesses__ holy 10"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 90 feet, DC 28"
  - name: "Hell's Sting"
    desc: "⬲ (divine, mental, unholy)"
  - name: "Trigger"
    desc: "The dragon is critically hit with a melee attack"
  - name: "Effect"
    desc: "The dragon channels the rancor of Hell back through the body of their foe, overwhelming it with an infernal assault on the mind. The triggering creature takes 6d6 mental damage with a DC 30 basic Will save. Holy creatures use an outcome one degree of success worse than they roll on their saving throw."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "50 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +24 (Fire, Magical, reach 10 feet, Unholy) __Damage__ 2d12+10 piercing plus 2d6 fire"
  - name: "Melee"
    desc: "⬻ claws +24 (Agile, Fire, Magical, Unholy) __Damage__ 2d8+10 piercing plus 2d6 fire and Grab"
  - name: "Melee"
    desc: "⬻ tail +22 (Fire, reach 15 feet, Magical, Unholy) __Damage__ 2d8+10 bludgeoning plus 2d6 fire and Knockdown"
abilities_bot:
  - name: "Diabolic Fire"
    desc: "Any fire damage that a diabolic dragon deals, including fire damage from spells, is imbued with the unholy power of Hell to scorch the spirit as well. A creature takes spirit damage instead of fire damage if that would be more detrimental to the creature (as determined by the GM). A diabolic dragon is immune to the diabolic fire of other diabolic dragons, the fire from _divine immolation_, and similar effects."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Hellfire Breath whenever they score a critical hit with a Strike."
  - name: "Hellfire Breath"
    desc: "⬺ (Divine, Fire, Unholy) The dragon unleashes a blast of infernal fire that deals 12d6 fire damage in a 40-foot cone (DC 30 basic Reflex save). The dragon can't use Hellfire Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 28, attack +20 - __Cantrips (6th)__ Ignition - __5th__ Divine Immolation, Wall of Fire"
sourcebook: "_Monster Core_, page 112."
```

```encounter-table
name: Young Diabolic Dragon
creatures:
  - 1: Young Diabolic Dragon
```
